from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    content_object = GenericForeignKey()


class Tags(models.Models):
    label = models.CharField(max_length = 255)
    models.true = models.DateTimeField(auto_now=true, auto_now_add=true)
    
        
class TagedItem(models.Model):
    name = models.ForeignKeyField('Tag', on_delete=models.CASCADE)
    objectId = models.foreignKeyField('Product', on_delete=models.CASCADE)
    objectType = models.foreignKeyField('')