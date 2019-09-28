from django.db import models


class Book(models.Model):
    isbn = models.CharField(max_length=200, primary_key=True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.CharField(max_length=200)
    borrowed_by_who = models.CharField(max_length=200)
    borrowed_till = models.DateField(null=True)
    # Field is_borrowed is not displayed, but keeps boolean value True/False if book is borrowed/not borrowed
    is_borrowed = models.BooleanField()
