# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TestModel(models.Model):
	first = models.BooleanField()
	last = models.BooleanField()
	