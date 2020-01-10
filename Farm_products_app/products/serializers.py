from django.contrib.auth.models import User
from rest_framework import serializers
from products.models import Product


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")


class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ("user", "id", "p_name", "p_category",
                  "p_price", "p_price_unit", "p_description", "p_image",
                  "date_created", "date_updated")
