from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "У вас нет прав!"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False
