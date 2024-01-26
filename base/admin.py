from django.contrib import admin

# Register your models here.
from .models import Project, Skill, Tag, User, Question, Message


admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(Message)

admin.site.register(User)
admin.site.register(Question)

