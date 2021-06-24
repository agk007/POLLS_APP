from django.db import models
from django.forms import forms
# Create your models here.
import datetime
from django.utils import timezone


class Tag(models.Model):
    name=models.CharField(max_length=250,null=True)
    class Meta:
        pass
    def __str__(self):
        return self.name

class Question(models.Model):
   question_text = models.CharField(max_length=200)
   tags= models.ManyToManyField(Tag)
   pub_date = models.DateTimeField('date published')

   class Meta:
       pass

   def __str__(self):
       return self.question_text

   def was_published_recently(self):
       now = timezone.now()
       return now - datetime.timedelta(days=1) <= self.pub_date <= now

   was_published_recently.admin_order_field = 'pub_date'
   was_published_recently.boolean = True
   was_published_recently.short_description = 'Published recently?'

   @classmethod
   def is_valid(cls):
       pass


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING,)
    class Meta:
        pass


    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
ch=Choice()


