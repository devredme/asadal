# -*- coding:utf8 -*-


from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    content = models.TextField(null=True)


class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)