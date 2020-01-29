from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=250)
    amount = models.IntegerField()
    purpose = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField('Email Address', blank=True)

    def __str__(self):
        return self.name + "    :    " +self.email