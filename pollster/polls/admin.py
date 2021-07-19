from django.contrib import admin
from django.db import models

from .models import Question, Choice

admin.site.site_header = "DONT TOUCH IT HARD..."
admin.site.site_title = "DONT TOUCH IT HARD... Area"
admin.site.index_title = "Welcome my lish"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin (admin.ModelAdmin):
    fieldsets = [(None,{'fields':['question_text']}),
                ('Date Information',{'fields': ['pub_date'],'classes':
                ['collapse']}),]
    inlines = [ChoiceInLine]

admin.site.register(Question,QuestionAdmin)
 #admin.site.register(Question)
#admin.site.register(Choice)
