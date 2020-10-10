from django.contrib import admin

# Register your models here.

from .models import Project, Tag, Bio, SoftSkill, Skill

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Bio)
admin.site.register(SoftSkill)
admin.site.register(Skill)
