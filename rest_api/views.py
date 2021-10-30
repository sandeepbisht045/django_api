from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.serializers import Serializer
from . models import Advisor_details,User,Book_call
from . serializers import Advisor_details_serializers,User_serializers,Book_call_serializers
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAdminUser,IsAuthenticated              
# from rest_api import serializers
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.validators import URLValidator
validate=URLValidator()
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Landing Page
def homepage(request):
        return render(request,"index.html")


# API FOR SIGNUP AS A USER WITH POST REQUEST
@api_view(["POST"])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def users(request):
        serializer=User_serializers(data=request.data)
        if serializer.is_valid():
                user= serializer.save()
                refresh = RefreshToken.for_user(user)
        #        str(refresh.access_token)          
                res = {"JWT Authentication Token": str(refresh),
                        "User id":serializer.data["id"]}
                return Response(res)    
        else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
#   API FOR ADDING ADVISORS WITH POST REQUEST      
@api_view(["POST"])
def Admin(request):
        url=request.data["Advisor_Photo_URL"]
        try:
                validate(url)
        except:
                return Response({"msg":"image url is invalid"},status=status.HTTP_400_BAD_REQUEST)
        serializer=Advisor_details_serializers(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
        else:
                return Response(status=status.HTTP_400_BAD_REQUEST)


# API FOR FETCHING ADVISOR DETAILS WITH GET REQUEST
@api_view(["GET"])
def fetch_advisor(request,user_id):
        try:
                verify=User.objects.get(id=user_id)         
                data_fetch=Advisor_details.objects.all()
                serializer=Advisor_details_serializers(data_fetch,many=True)
                return Response(serializer.data)
        except:
                return  Response({"message":"user doesnot exist"},status=status.HTTP_400_BAD_REQUEST)
       
        
# API FOR LOGIN AS A USER WITH POST REQUEST
@api_view(["POST"])
def login(request):
        email=request.data["Email"]
        password=request.data["Password"] 
        
        try:
                verify=User.objects.get(Email=email,Password=password)
                return Response({"User_Id":verify.id})
               
        except:        
                if email=="" or password=="":
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                        return Response(status=status.HTTP_401_UNAUTHORIZED)
     
                
#  API FOR BOOKING CALL WITH THE POST REQUEST                               
@api_view(["POST"])
def book_call(request,user_id,advisor_id):
        try:
                verify_user=User.objects.get(id=user_id)
                verify_advisor=Advisor_details.objects.get(id=advisor_id)     
                timing=request.data["time"]
                serializer=Book_call_serializers(data={"time":timing,"advisor_id":advisor_id,"user_id":user_id})
                if serializer.is_valid():
                        serializer.save()
                        return Response(status=status.HTTP_200_OK)
        except:
                return Response(data={"msg":"either passed user_id or advisor_id is invalid"},status=status.HTTP_400_BAD_REQUEST)


# API FOR FETCHING ALL THE BOOKED CALLS WITH GET REQUEST
@api_view()
def booking_fetch(request,user_id):
        try:
                lst=[]
                fetch_booking=Book_call.objects.filter(user_id=user_id)
                print(fetch_booking)
                for i in fetch_booking:
                        dic={"Booking_time":i.time,"Booking_id":i.id}
                
                        fetch_advisor=Advisor_details.objects.filter(id=i.advisor_id)
                        for i in fetch_advisor:
                                dic.update({"Advisor_Name":i.Advisor_name,"Advisor_id":i.id,"Advisor_Profile_Picture":i.Advisor_Photo_URL})
                                lst.append(dic)
                return Response(lst)
        except:
                return Response({"msg":"user does not exist with this id"})
                
        
        
        
                
                
                
                
        
        
        
        