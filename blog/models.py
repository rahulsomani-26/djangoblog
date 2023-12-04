from django.db import models

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    date_created = models.DateField(auto_created=True,auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return f'{self.title}'
    
 