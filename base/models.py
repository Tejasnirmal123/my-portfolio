from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    body = RichTextUploadingField()
    slug = models.SlugField(null=True, blank=True)
    created  = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = models.IntegerField(unique=True)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    

class Question(models.Model):

    TYPES = (
        ('backend', 'backend'),
        ('frontend', 'frontend'),
        ('fullstack', 'fullstack'),
    )

    answer = models.CharField(max_length=200, choices=TYPES)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.answer


