from . import views
from django.urls import path, include

app_name = 'pybo'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.detail, name='detail'),
    # path('', views.IndexView.as_view(), name = 'index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('answer/create/<int:pk>', views.answer_create, name='answer_create'),
    path('question_create', views.question_create, name='question_create'),
    path('question_modify/<int:question_id>', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer_modify/<int:answer_id>', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    path("comment/create/question/<int:question_id>/", views.comment_create_question, name='comment_create_question'),
    path("comment/modify/question/<int:comment_id>/", views.comment_modify_question, name='comment_modify_question'),
    path("comment/delete/question/<int:comment_id>/", views.comment_delete_question, name='comment_delete_question'),
    path("comment/create/answer/<int:answer_id>/", views.comment_create_answer, name='comment_create_answer'),
    path("comment/modify/answer/<int:comment_id>/", views.comment_modify_answer, name='comment_modify_answer'),
    path("comment/delete/answer/<int:comment_id>/", views.comment_delete_answer, name='comment_delete_answer'),
    path("vote_question/<int:question_id>/", views.vote_question, name='vote_question'),    
    path("vote_answer/<int:answer_id>/", views.vote_answer, name='vote_answer'),    
]
