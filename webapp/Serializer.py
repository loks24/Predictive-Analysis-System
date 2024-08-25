from rest_framework import serializers
from . models import GetTagCode

class TagCodeSerializer(serializers.ModelSerializer):
   
 
    class Meta:
        model=GetTagCode
        fields=['TagCode']