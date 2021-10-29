from django.db.models import fields
from rest_framework import serializers
from . models import Advisor_details, User,Book_call

class Advisor_details_serializers(serializers.ModelSerializer):
    class Meta:
        model=Advisor_details
        fields=["id","Advisor_name","Advisor_Photo_URL"]
        
class User_serializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","Name","Email","Password"]
        
class Book_call_serializers(serializers.ModelSerializer):
    class Meta:
        model=Book_call
        fields=["id","time","advisor_id","user_id"]
    