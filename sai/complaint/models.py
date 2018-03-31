from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm

class Complaints(models.Model):
	CHOICES = (
	        ('cse','CSE-dept'),
	        ('it','It-dept'),
	        ('ece','ECE-dept'),
			('eee','EEE-dept'),
			('mech','MECH-dept'),
			('exam','Examination-branch'),
			('maintenance','MAINTENANCE'),
	    )
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	title = models.CharField(max_length=20)
	category = models.CharField(max_length=20,choices=CHOICES,null=True)
	description = models.TextField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)
	complaintno = models.IntegerField(default=0)

	def __unicode__(self):
		return self.compl


class Lecturer(models.Model):
    pollno = models.CharField(max_length=255,null=True)
    name = models.CharField(max_length=255)
    des = models.TextField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.pollno


class Poll(models.Model):
	lecturer = models.ManyToManyField(Lecturer,related_name='lecturer')
	subject = models.CharField(max_length=100,null=True)
	date = models.DateTimeField(auto_now_add=True)
	created_date = models.DateTimeField(default=timezone.now)
