from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save

 
class Profile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=255)
	interests = models.TextField()
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
 
	class Meta:
		ordering = ['-created']
 
	def __unicode__(self):
		return u'%s' % self.user.username
 
	def get_absolute_url(self):
 		return reverse('app.views.profile', args=[self.user.username])

def create_profile(sender, instance, created, **kwargs):  
	if created:  
		profile, created = Profile.objects.get_or_create(user=instance)


class Event(models.Model):
	title = models.CharField(max_length=255)
	interests1 = models.TextField()
	interests2 = models.TextField()
	description = models.CharField(max_length=255)
	when = models.DateTimeField(auto_now_add=True)
 
	class Meta:
		ordering = ['-when']
 
	def __unicode__(self):
		return u'%s' % self.title



