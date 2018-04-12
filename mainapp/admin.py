from django.contrib import admin
from mainapp.models import Questions, Comment, Tag


class QuestionInLine(admin.StackedInline):
    model = Comment
    extra = 1


class QuestionsAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'date', 'tags']
    inlines = [QuestionInLine]


admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
