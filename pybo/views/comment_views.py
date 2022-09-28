from django.shortcuts import render, get_object_or_404, redirect,resolve_url
from django.http import HttpResponse
from ..models import Question, Answer, Comment
from ..forms import QuestionForm, AnswerForm, CommentForm
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            # return redirect('pybo:detail', pk = question.id)
            return redirect('{}#comment_{}'.format(resolve_url(
                'pybo:detail', pk=comment.question.id
            )
            , comment.id))
    else:
        form = CommentForm()
    context = {'form':form}
    return render(request, 'pybo/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user !=comment.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', pk=comment.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            # return redirect('pybo:detail', pk=comment.question.id)
            return redirect('{}#comment_{}'.format(resolve_url(
                'pybo:detail', pk=comment.question.id
            )
            , comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'comment':comment, 'form': form}
    return render(request, 'pybo/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('pybo:detail', pk=comment.question.id)
    comment.delete()
    return redirect('pybo:detail',pk=comment.question.id)

# 답변 댓글
@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            # return redirect('pybo:detail', pk = answer.question.id)
            return redirect('{}#comment_{}'.format(resolve_url(
                'pybo:detail', pk=comment.answer.id
            )
            , comment.id))
    else:
        form = CommentForm()
    context = {'form':form}
    return render(request, 'pybo/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user !=comment.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', pk=comment.answer.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            # return redirect('pybo:detail', pk=comment.answer.question.id)
            return redirect('{}#comment_{}'.format(resolve_url(
                'pybo:detail', pk=comment.answer.id
            )
            , comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'comment':comment, 'form': form}
    return render(request, 'pybo/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('pybo:detail', pk=comment.answer.question.id)
    comment.delete()
    return redirect('pybo:detail',pk=comment.answer.question.id)