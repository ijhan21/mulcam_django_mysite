from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.http import HttpResponse
from ..models import Question, Answer, Comment
from ..forms import QuestionForm, AnswerForm, CommentForm
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def answer_create(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            # return redirect("pybo:detail", pk=pk)
            return redirect('{}#answer_{}'.format(resolve_url(
                'pybo:detail', pk=answer.question.id
            )
            , answer.id))
    else:
        form = AnswerForm()
    context = {'question':question, 'form':form}    
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user !=answer.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', pk=answer.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            # return redirect('pybo:detail', pk=answer.question.id)
            return redirect('{}#answer_{}'.format(resolve_url(
                'pybo:detail', pk=answer.question.id
            )
            , answer.id))
    else:
        form = QuestionForm(instance=answer)
    context = {'answer':answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('pybo:detail', pk=answer.question.id)
    answer.delete()
    return redirect('pybo:detail',pk=answer.question.id)
