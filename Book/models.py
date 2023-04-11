from django.db import models


class BOOK(models.Model):
    ID = models.TextField(primary_key=True)
    Title = models.TextField()
    Author = models.TextField()
    Publisher = models.TextField()
    Filter_number = models.IntegerField()
    All_filter = models.TextField()
    Y_date = models.IntegerField()


class MARK(models.Model):
    code = models.TextField()
    book = models.ForeignKey('BOOK', on_delete=models.CASCADE)
