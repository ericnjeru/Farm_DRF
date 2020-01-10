from django.contrib import admin
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("user", "id", "p_name", "p_category", "p_price",
                    "p_price_unit", "p_description", "p_image", "date_created", "date_updated")
    list_filter = ("p_price", "date_updated")


admin.site.register(Product, ProductAdmin)

