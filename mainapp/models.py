from django.db import models


class Tag(models.Model):
    text = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.text


# class User(models.Model):
#     name = models.CharField(default='', max_length=100)
#
#     def __str__(self):
#         return self.name


class Questions(models.Model):
    # author = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(verbose_name="Your comment")
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
