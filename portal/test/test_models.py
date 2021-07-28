from django.test import TestCase
from ..models import *


class ModelBase(TestCase):

    def setUp(self):

        self.author = Author.objects.create(
            name='Lorem Ipsum'
        )

        self.article = Article.objects.create(
            category='Lorem Ipsum',
            author=self.author,
            title='Lorem Ipsum mussun',
            summary='Lorem Ipsum',
            firstParagraph='Lorem Ipsum',
            body='Lorem Ipsum',
        )

class AuthorModelTest(ModelBase):

    def test_model_creation(self):
        """ model was created ? """

        self.assertEquals(self.author.name,'Lorem Ipsum')    
        self.assertEquals(self.author.picture, '')    

    def test_article_creation(self):
        """ model was created ? """

        self.assertEquals(self.article.category,'Lorem Ipsum')    
        self.assertEquals(self.article.author, self.author)   
        self.assertEquals(self.article.title,'Lorem Ipsum mussun')  
        self.assertEquals(self.article.summary,'Lorem Ipsum')  
        self.assertEquals(self.article.firstParagraph,'Lorem Ipsum')  
        self.assertEquals(self.article.body,'Lorem Ipsum')  
        self.assertEquals(self.article.slug_category,'lorem-ipsum')  