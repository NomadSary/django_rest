from rest_framework.serializers import ModelSerializer
from django.conf import settings

from .models import User



class UserModelSerializer(ModelSerializer):


    class Meta:
        model = User  
        # fields = '__all__'     
        fields =('username','first_name','last_name','email')