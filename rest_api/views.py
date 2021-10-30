from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from . models import Advisor_details,User,Book_call
from . serializers import Advisor_details_serializers,User_serializers,Book_call_serializers
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAdminUser,IsAuthenticated              
from rest_api import serializers
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
import datetime

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
        
#   api for adding advisors with POST request      
@api_view(["POST"])
def Admin(request):
        serializer=Advisor_details_serializers(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
        else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

# api for fetching advisor details with GET request
@api_view(["GET"])
def fetch_advisor(request,user_id):
        try:
                verify=User.objects.get(id=user_id)         
                data_fetch=Advisor_details.objects.all()
                serializer=Advisor_details_serializers(data_fetch,many=True)
                # tm=Book_call.objects.get(id=6)
                # print((str(tm.time)))
                return Response(serializer.data)
                # return Response(status=status.HTTP_200_OK)
        except:
                return  Response({"message":"user doesnot exist"},status=status.HTTP_400_BAD_REQUEST)
        
# api for login as a user with POST request
@api_view(["POST"])
def login(request):
        email=request.data["Email"]
        password=request.data["Password"] 
        
        try:
                verify=User.objects.get(Email=email,Password=password)
                serializer=User_serializers(data=request.data)
                return Response(data=serializer.data["id"])
               
        except:        
                if email=="" or password=="":
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                        return Response(status=status.HTTP_401_UNAUTHORIZED)
                
                
#  api for booking call with the POST request               
@api_view(["POST"])
def book_call(request,user_id,advisor_id):
        from django.utils.dateparse import parse_datetime
        import dateutil.parser
        try:
                verify_user=User.objects.get(id=user_id)
                verify_advisor=Advisor_details.objects.get(id=advisor_id)
                booking_time=parse_datetime(request.data["time"])
                # booking_time=(request.data["time"])
                Book_call.objects.create(time=booking_time,advisor_id=verify_advisor,user_id=verify_user)
                return Response(status=status.HTTP_200_OK)
        except:
                return Response(data={"msg":"either passed user_id or advisor_id is invalid"},status=status.HTTP_400_BAD_REQUEST)

# api for fetching all the booked calls with GET request
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
                
        
        
        
                
                
                
                
        
        
        
        