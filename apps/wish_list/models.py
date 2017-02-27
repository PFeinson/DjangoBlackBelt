from __future__ import unicode_literals

from django.db import models
from ..loginAndReg.models import User
# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length = 100)
    added_by = models.ForeignKey(User, related_name = "all_items")
    wanted_by = models.ManyToManyField(User, related_name = "wanted_by")
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
