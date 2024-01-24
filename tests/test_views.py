from django.test import TestCase
from restaurant.models import Menu


class MenuViewTest(TestCase):
    totalItems = 3

    def setUp(self):
        for i in range(self.totalItems):
            Menu.objects.create(title=f"item{i}", price=i*2, inventory=i*20)

    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(len(items), self.totalItems)
