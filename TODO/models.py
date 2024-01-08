from django.db import models
from django.conf import settings
from authors.models import User


class Project(models.Model):
    project_name = models.CharField(max_length=64, unique = True);    
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL);
    uls_repo = models.URLField(blank = True, unique = False, null = True);

    def __str__(self):
        return self.project_name

class TODO(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE);
    text_todo = models.TextField();
    date_create = models.DateTimeField(auto_now_add=True);
    date_update = models.DateTimeField(auto_now=True);
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE);
    active = models.BooleanField(default=True);


    