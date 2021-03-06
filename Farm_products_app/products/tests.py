import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from products.models import Product
from products.serializers import ProductSerializer


class ProductListCreateAPIViewTestCase(APITestCase):
    url = reverse("products:list")

    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_product(self):
        response = self.client.post(self.url, {"p_name": "Good fertilizers", "p_category": "Fertilizers", 
                                               "p_price": "300", "p_price_unit": "per kg", 
                                               "p_description": "Description"})
        self.assertEqual(201, response.status_code)

    def test_user_products(self):
        """
        Test to verify user products list
        """
        Product.objects.create(user=self.user, p_name="APk fertilizers!")
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == Product.objects.count())


class ProductDetailAPIViewTestCase(APITestCase):

    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.product = Product.objects.create(user=self.user, name="Call Mom!")
        self.url = reverse("products:detail", kwargs={"pk": self.product.pk})
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_product_object_bundle(self):
        """
        Test to verify product object bundle
        """
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

        product_serializer_data = ProductSerializer(instance=self.product).data
        response_data = json.loads(response.content)
        self.assertEqual(product_serializer_data, response_data)

    def test_product_object_update_authorization(self):
        """
            Test to verify that put call with different user token
        """
        new_user = User.objects.create_user("newuser", "new@user.com", "newpass")
        new_token = Token.objects.create(user=new_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + new_token.key)

        # HTTP PUT
        response = self.client.put(self.url, {"name", "Hacked by new user"})
        self.assertEqual(403, response.status_code)

        # HTTP PATCH
        response = self.client.patch(self.url, {"name", "Hacked by new user"})
        self.assertEqual(403, response.status_code)

    def test_product_object_update(self):
        response = self.client.put(self.url, {"name": "Call Dad!"})
        response_data = json.loads(response.content)
        product = Product.objects.get(id=self.product.id)
        self.assertEqual(response_data.get("name"), product.name)

    def test_product_object_partial_update(self):
        response = self.client.patch(self.url, {"done": True})
        response_data = json.loads(response.content)
        product = Product.objects.get(id=self.product.id)
        self.assertEqual(response_data.get("done"), product.done)

    def test_product_object_delete_authorization(self):
        """
            Test to verify that put call with different user token
        """
        new_user = User.objects.create_user("newuser", "new@user.com", "newpass")
        new_token = Token.objects.create(user=new_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + new_token.key)
        response = self.client.delete(self.url)
        self.assertEqual(403, response.status_code)

    def test_product_object_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(204, response.status_code)
