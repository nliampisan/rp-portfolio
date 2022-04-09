from django.test import TestCase
from .models import Category
# Create your tests here.


class ModelsTestCase(TestCase):
    def test_doctor(self):
        cat = Category.objects.create(name="test")
        cat.save()
        self.assertTrue(isinstance(cat, Category))
        cat.delete()