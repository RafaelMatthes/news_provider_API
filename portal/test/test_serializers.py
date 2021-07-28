from .test_models import ModelBase

class AuthorSerializerTestCase(ModelBase):
       
    def test_author_serializer(self):
        data = self.AuthorSerializer.data

        self.assertEquals(set(data.keys()),set(['id','name', 'picture']))

class ArticleSerializerTestCase(ModelBase):
 
    def test_article_serializer(self):
        data = self.ArticleSerializer.data

        self.assertEquals(set(data.keys()),set(['id','category', 'author', 'title', 'summary', 'firstParagraph', 'body']))

    def test_article_by_category_serializer(self):
        data = self.getArticlesByCategorySerializer.data

        self.assertEquals(set(data.keys()),set(['id', 'author', 'category', 'title', 'summary']))

    def test_article_by_id_serializer(self):
        data = self.getArticlesByIdSerializer.data

        self.assertEquals(set(data.keys()),set(['id', 'author', 'category', 'title', 'summary', 'firstParagraph', 'body']))
    
    def test_article_by_id_anonymous_serializer(self):
        data = self.getArticlesByIdAnonymousSerializer.data

        self.assertEquals(set(data.keys()),set(['id', 'author', 'category', 'title', 'summary', 'firstParagraph']))

class UserSerializerTestCase(ModelBase):

    def test_user_serializer(self):
        data = self.UserSerializer.data

        self.assertEquals(set(data.keys()),set(['id', 'username', 'email']))