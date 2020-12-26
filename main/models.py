from django.db import models

class Todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.text)

    class Meta:
        verbose_name_plural = 'Todo'

class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_email = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.user_name)
