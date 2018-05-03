from datetime import datetime
from random import choice, randint
import time
import random
from faker import Factory
from django.core.management.base import BaseCommand

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from mainapp.models import Question, Profile, Comment, Tag


class Command(BaseCommand):
    faker = Factory.create()

    def create_fake_data(self):

        for i in range(1, 50):
            u = User(username='user_' + str(i),
                     email='email_' + str(i) + '@email.com',
                     password=make_password('qwerty123'),
                     first_name=self.faker.first_name(),
                     last_name=self.faker.last_name())
            u.save()
            p = Profile(user=u,
                        avatar="cookie.png",
                        rating=random.choice(range(1, 99)))
            p.save()

            year = random.choice(range(1950, 2001))
            month = random.choice(range(1, 13))
            day = random.choice(range(1, 29))
            post_time = random.seed(time.time())

            q = Question(author=u,
                         title=self.faker.sentence(nb_words=randint(4, 6), variable_nb_words=True),
                         text=self.faker.paragraph(nb_sentences=randint(4, 13), variable_nb_sentences=True),
                         likes=random.choice(range(-50, 172)),
                         date=(datetime(year, month, day, post_time)))
            q.save()
            for j in range(4):
                ans = Comment(author=u,
                              question=q,
                              text=self.faker.paragraph(nb_sentences=randint(2, 10), variable_nb_sentences=True),
                              likes=random.choice(range(-32, 172)))
                ans.save()

    def create_tags(self):
        tags = [
            'JavaScript', 'Java', 'C#', 'PHP', 'Android', 'JQuery', 'Python',
            'HTML', 'CSS', 'C++', 'iOS', 'MySQL', 'Objective-C',
            'SQL', '.net', 'RUBY', 'Swift', 'Vue', '1C'
        ]
        for tag in tags:
            if len(Tag.objects.filter(text=tag)) == 0:
                t = Tag()
                t.text = tag
                t.save()

        tags = Tag.objects.all()
        questions = Question.objects.all()
        for question in questions:
            for i in range(0, 4):
                t = choice(tags)

                if t not in question.tags.all():
                    question.tags.add(t)
            self.stdout.write('tagged question [%d]' % question.id)

    def handle(self, *args, **options):
        self.create_fake_data()
        self.create_tags()
