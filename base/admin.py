from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

# Register your models here.

from .models import Project, Tag, Bio, SoftSkill, Skill


class BioAdmin(TranslationAdmin):
    model = Bio


class ProjectAdmin(TranslationAdmin):
    model = Project


class SoftSkillAdmin(TranslationAdmin):
    model = SoftSkill


class TagAdmin(TranslationAdmin):
    model = Tag


class SkillAdmin(TranslationAdmin):
    model = Skill


admin.site.register(Bio, BioAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(SoftSkill, SoftSkillAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Skill, SkillAdmin)
