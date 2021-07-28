from django.test import TestCase
from ..models import *


class ModelBase(TestCase):

    def setUp(self):

        self.author = Author.objects.create(
            name='Lorem Ipsum'
        )

        self.article = Article.objects.create(
            category='Lorem Ipsum',
            author=self.author.id,
            tittle='Lorem Ipsum massun',
            summary='Lorem Ipsum',
            firstParagraph='Lorem Ipsum',
            body='Lorem Ipsum',
        )

