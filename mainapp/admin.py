from django.contrib import admin
from mainapp.models import Question, Comment, Tag, Profile

admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Profile)
