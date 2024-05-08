from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


from mptt import models as mptt_models

class Category(models.Model):
    name = models.CharField(max_length=255)
    serial = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Blog post model.
    """

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)  # Optional, for automatic slug generation
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=10, choices=options, default="draft")
    tags = TaggableManager()
    image = models.ImageField(upload_to='post_images/', blank=True)  # Add the ImageField
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')

    def get_absolute_url(self):
        return reverse("post_single", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Optional, for automatic slug generation
        super().save(*args, **kwargs)
        
    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
