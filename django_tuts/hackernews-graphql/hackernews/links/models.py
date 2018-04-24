from django.db import models
from uuid import uuid4
# Create your models here.
class Link(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	#name = models.CharField(max_length=200)
	description = models.CharField(max_length=200, blank=True)
	notes = models.TextField('Notes', blank=True)
	url = models.URLField('URL', unique=True)
	# Todos
	#created_at = models.DateTimeField(auto_now_add=True)
	#last_modified = models.DateTimeField(auto_now=True)
	#tag = models.ManyToManyField(Tag)
