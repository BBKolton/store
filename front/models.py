from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=50)
    published = models.DateField()
    summary = models.CharField(max_length=1000)
    price = models.IntegerField()
    link = models.CharField(max_length=256)
    image = models.CharField(max_length=256)

    def __str__(self):
        return self.title

class Authors(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=30)
    
class BooksAuthors(models.Model):
    book = models.ForeignKey('Books')
    author = models.ForeignKey('Authors')

class Publishers(models.Model):
    name = models.CharField(max_length=100)

class BooksPublishers(models.Model):
    book = models.ForeignKey('Books')
    publisher = models.ForeignKey('Publishers')
    

