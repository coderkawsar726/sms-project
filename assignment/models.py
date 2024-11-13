from django.db import models
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget

# Create your models here.
  
# Book List Model 
class BookList(models.Model):
    CLASS_CHOICES = [
        ('1', 'Class 1'),
        ('2', 'Class 2'),
        ('3', 'Class 3'),
        ('4', 'Class 4'),
        ('5', 'Class 5'),
        ('0', 'Add this book as new book '),
    ]
    bookname = models.CharField(max_length=100)
    classfor = models.CharField(max_length=20, choices=CLASS_CHOICES)
    subjectcode = models.IntegerField()


    def __str__(self):
        return self.bookname


class Assignment(models.Model):
    CLASS_CHOICES = [
        ('1', 'Class 1'),
        ('2', 'Class 2'),
        ('3', 'Class 3'),
        ('4', 'Class 4'),
        ('5', 'Class 5'),
    ]
    stclass = models.CharField(max_length=10, choices=CLASS_CHOICES)
    subject = models.ForeignKey(BookList, on_delete=models.CASCADE, related_name='subjectid')
    assignment = RichTextField()
    publishdate = models.DateTimeField(auto_now_add=True)
    activation = models.CharField(default='1', max_length=1)

    class Meta:
        ordering= ['-publishdate']

    def __str__(self):
        return self.stclass
  

