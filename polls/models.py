from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    question_image1 = models.ImageField(default=None, max_length=200)
    question_image2 = models.ImageField(default=None, max_length=200)
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(default="0", max_length=2)
    votes = models.IntegerField(default=0)
    image = models.ImageField(default=None, max_length=200)
    def __str__(self):
        return self.choice_text

class IndirizzoIP(models.Model):
    IndirizzoIP_text = models.CharField(max_length=200)
    date = models.DateTimeField('date')
    def __str__(self):
        return self.IndirizzoIP

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now