from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SoftSkill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    projectResume = models.CharField(null=True, blank=True, max_length=1000)
    body = RichTextUploadingField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if self.slug is None:
            slug = slugify(self.title)

            has_slug = Project.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Project.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={id: self.id})


class Bio(models.Model):
    body = RichTextField(null=True, blank=True)
    resume = models.FileField(null=True, blank=True, upload_to="media")
    softSkill = models.ManyToManyField(SoftSkill, null=True, blank=True)
    skill = models.ManyToManyField(Skill, null=True, blank=True)



