from django.contrib import admin
from .models import Question
# Register your models here.
# admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Question, QuestionAdmin)