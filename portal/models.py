from django.db import models
from django.utils.text import slugify

class Author(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='author_picture/', blank=True, default='')

    def __str__(self):
        return self.name

        
class Article(models.Model):
    category = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    firstParagraph = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    slug_category  = models.CharField(max_length=255, editable=False, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug_category = slugify(self.category)
        
        super(Article, self).save(*args, **kwargs)
