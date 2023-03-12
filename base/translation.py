from modeltranslation.translator import register, TranslationOptions
from .models import Bio, Project, SoftSkill, Tag, Skill


@register(Bio)
class BioTranslationOptions(TranslationOptions):
    fields = ('body', 'resume', 'softSkill', 'skill',)


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'projectResume', 'body', 'tags',)


@register(SoftSkill)
class SoftSkillTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('name',)
