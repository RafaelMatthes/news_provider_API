from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='author_picture/', blank=True, default='')

    def __str__(self):
        return self.name

        
class Article(models.Model):
    category = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    firstParagraph = models.CharField(max_length=255)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.tittle

