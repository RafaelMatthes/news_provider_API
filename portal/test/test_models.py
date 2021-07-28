from django.test import TestCase
from ..models import *
from ..serializer import *
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


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

        user = get_user_model()
        self.user = user.objects.create(
            username='Test',
            password='123123',
            email='teste@mail.com'
        )
        self.user.is_staff = True
        self.user.save()
        self.token = Token.objects.create(user=self.user)

        self.AuthorSerializer = AuthorSerializer(instance=self.author)
        self.ArticleSerializer = ArticleSerializer(instance=self.article)
        self.getArticlesByCategorySerializer = getArticlesByCategorySerializer(instance=self.article)
        self.getArticlesByIdSerializer = getArticlesByIdSerializer(instance=self.article)
        self.getArticlesByIdAnonymousSerializer = getArticlesByIdAnonymousSerializer(instance=self.article)
        self.UserSerializer = UserSerializer(instance=self.user)

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