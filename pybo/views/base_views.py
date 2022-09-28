from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models import Question, Answer, Comment
from ..forms import QuestionForm, AnswerForm, CommentForm
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
# Create your views here.
def index(request):
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw','')
    so = request.GET.get('so','recent')

    #정렬
    # """
    if so == 'recommend':
        question_list=Question.objects.annotate(
            num_voter=Count('voter')
        ).order_by('-num_voter','-create_date')
    elif so == 'popular':
        question_list=Question.objects.annotate(
            num_answer=Count('answer')
        ).order_by('-num_answer','-create_date')
    else:
        question_list= Question.objects.order_by('-create_date')
    # """

    # question_list = Question.objects.order_by('-create_date') # 앞에 - 때문에 역순 정렬
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        )#.distinct() #distinct 안해도 중복 안됨!!!
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    # context = {'question_list':question_list}
    context = {'question_list':page_obj, 'page':page, 'kw': kw}
    # return HttpResponse("hello")
    return render(request, 'pybo/question_list.html', context)

def detail(request, pk):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=pk)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)