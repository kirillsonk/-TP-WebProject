from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    text = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.text


class Like(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.count


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    text = models.TextField(max_length=5000)
    date = models.DateTimeField()
    likes = models.IntegerField(Like, default=0)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Your comment")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    likes = models.IntegerField(Like, default=0)

    def __str__(self):
        return self.text


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to='')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
