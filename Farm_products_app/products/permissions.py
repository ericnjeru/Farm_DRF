from rest_framework.permissions import BasePermission


class UserIsOwnerProduct(BasePermission):

    def has_object_permission(self, request, view, product):
        return request.user.id == product.user.id
