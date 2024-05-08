from django.db import models
from PIL import Image

# Create your models here.
class WebInfo(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    designation = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True, verbose_name='Image')
    bio = models.CharField(max_length=50, blank=True)
    

    def __str__(self):
        return self.name + " - " + self.bio