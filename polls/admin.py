from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Question title', {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes':['collapse']})
    ]

    inlines = [ChoiceInline]
    # list_display 변수명은 고정입니다. (소괄호는 생략되어도 무방)
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']
    search_fields = ['question_text']


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
