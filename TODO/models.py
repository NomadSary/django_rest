from django.db import models
from django.conf import settings
import datetime 

class Project(models.Model):
    project_name = models.CharField(max_length=64);
    uls_repo = models.URLField(max_length=154, blank = True );
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL);

class TODO(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE);
    text_todo = models.TextField();
    date_create = models.DateTimeField(default = datetime.date.today());
    date_update = models.DateTimeField(blank = True);
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE);
    active = models.BooleanField();


    