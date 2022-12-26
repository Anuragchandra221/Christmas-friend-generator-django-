from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import *

class FriendSerializer(ModelSerializer):
     class Meta:
        model = Friends
        fields = ['name']