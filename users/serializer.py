from .models import User
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= "__all__"
        read_only_fields = ["id", "is_active", "is_staff", "is_superuser", "is_deleted", "date_joined", "last_login", "groups", "user_permissions", "user_permissions"]

