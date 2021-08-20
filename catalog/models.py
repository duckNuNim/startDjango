from django.db import models
from django.urls import reverse
import uuid
import datetime

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the book genere (e.g. Science Fiction)')
    
    def __str__(self):
        return self.name
    
class Language(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the book's Language (e.g. English, French, Japanese etc.)")
    
    def __str__(self):
        return self.name
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.first_name + ', ' +self.last_name

class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000)
    isbn = models.CharField(max_length=13)
    author = models.ForeignKey('Author', on_delete = models.SET_NULL, null = True)
    
    genre = models.ManyToManyField('Genre', help_text='Select a genre for this book')
    language = models.ForeignKey('Language', on_delete = models.SET_NULL, null = True)
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.title
    
class BookInstance(models.Model):
    uniqueid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    due_back = models.DateField( null=True, blank=True)
    imprint = models.CharField(max_length=200)
    status = models.CharField(max_length=1, blank=True, default='m', 
                              choices=(('m', 'Maintenance'),
                                       ('o', 'On Loan'),
                                       ('a', 'Avaialble'),
                                       ('r', 'Reserved')))
    book = models.ForeignKey('Book', on_delete = models.RESTRICT, null=True)
    
    class Meta:
        ordering = ['due_back']
    
    def __str__(self):
        return str(self.uniqueid) + ' ' + self.book.title


class BMI(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    # Bmi = (weight / (height*height)) * 10000
    
    def get_bim(self):
        self.bmi =  (self.weight/(self.height**2))*10000

    def get_absolute_url(self):
        return reverse('bmi-detail', args=[str(self.id)])

    def __str__(self):
        return self.name