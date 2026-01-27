from rest_framework import permissions

# 1️⃣ Только авторизованные пользователи могут видеть список
class IsAuthenticatedUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # True если пользователь авторизован
        return request.user and request.user.is_authenticated

# 2️⃣ Только админ может делать всё
class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

# 3️⃣ Пользователь может изменять только свои объекты
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Изменять объект может только владелец
        return obj.owner == request.user

# 4️⃣ Пользователь может редактировать объект только если суперюзер или владелец
class IsAdminOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        # Проверка глобально — все могут смотреть (GET), изменять только авторизованные
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Суперюзер или владелец может редактировать
        if request.user.is_superuser:
            return True
        return obj.owner == request.user
