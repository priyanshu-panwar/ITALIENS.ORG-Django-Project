from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = TaggableManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

class Social(models.Model):
	github = models.URLField(null=True, blank=True)
	weibo = models.URLField(null=True, blank=True)
	twitter = models.URLField(null=True, blank=True)
	facebook = models.URLField(null=True, blank=True)
	google = models.URLField(null=True, blank=True)
	instagram = models.URLField(null=True, blank=True)

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	created = models.DateTimeField(default=timezone.now)
	Parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.body
