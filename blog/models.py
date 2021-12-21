from enum import auto
from django.db import models
from django.db.models.fields import DateField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #ediiteed
    image = models.ImageField(upload_to ='post_image',blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # editted
    # likes=models.ManyToManyField(User,related_name='blog_posts')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

        img = Image.open(self.image.path)
        if img.height <300 or img.width < 300 :
            size = (700, 700)
            img.thumbnail(size)
            img.save(self.image.path)


#editted

# class Comment(models.Model):
# 	post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
# 	name = models.CharField(max_length=255)
# 	content = models.TextField()

   
    

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	name = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
	body = models.CharField(max_length=255)
    

class Like(models.Model):
	user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
	

