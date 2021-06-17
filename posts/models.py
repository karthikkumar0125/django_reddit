from django.db import models

# Create your models here.


class post(models.Model):
    #user=models.ForeignKey(user)
    post_name=models.CharField(max_length=100)
    post_data=models.TextField()
    create_time=models.DateTimeField(auto_now_add=True)
    votes=models.IntegerField(null=True, default=0)
    #community=models.ForeignKey(community)


class comments(models.Model):
    #user=models.ForeignKey(user)
    comment_data=models.CharField(max_length=255)
    create_time=models.DateTimeField(auto_now_add=True)
    votes=models.IntegerField(null=True, default=0)
    post=models.ForeignKey(post, on_delete=models.CASCADE)

