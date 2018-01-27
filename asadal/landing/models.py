# -*- coding:utf8 -*-


from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    content = models.TextField(null=True)
