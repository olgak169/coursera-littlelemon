from django.test import TestCase
from .models import Menu

# Create your tests here.


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Test item', price=50, inventory=50)
        self.assertEqual(item, 'Test item: 50')

