from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


from rest_framework.authtoken.models import Token

class RegView(APIView):

    def get(self, request, *args, **kwargs):
        data = Registartion.objects.all()
        serials = RegisterSerializer(data=data, many=True)  
        return Response({
            'status': status.HTTP_200_OK,
            'data': serials.data
        })

    def post(self, request, *args, **kwargs):
        data_get = request.data
        print(request.data['username'])
        username = request.data['username']
        serials = RegisterSerializer(data=data_get)
        send = {}

        if serials.is_valid():
            user = serials.save()
            date = User.objects.get(username = username)
            token, _ = Token.objects.get_or_create(user=date)
            
            send['token'] = token.key
            state = status.HTTP_201_CREATED
        else:
            state = status.HTTP_400_BAD_REQUEST

        return Response({
            'status': state,
            'data': send
        })


# =======================ITEM RETRIVLA AND DELETE AND UPDATE===================================


class ItemView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    def get(self,request,*args, **kwargs):
        pre_data = ItemModel.objects.all()
        user = ItemSerializer(pre_data,many=True)
        
        return Response({
            'status':status.HTTP_200_OK,
            'data':user.data
        })
        
        
    def post(self,request,*args, **kwargs):
        serial  = ItemSerializer(data=request.data)
        
        if serial.is_valid():
            user = serial.save()
            return Response({
                'status':status.HTTP_201_CREATED,
                'data':serial.data,
            })
        else:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'data':serial.errors
            })
    def put(self,request,id,*args, **kwargs):
        obj = get_object_or_404(ItemModel,id=id)
        serial = ItemSerializer(obj,data = request.data)
        if serial.is_valid():
            user = serial.save()
            send = serial.data
            stat = status.HTTP_202_ACCEPTED
        else:
            send = serial.errors
            stat = status.HTTP_403_FORBIDDEN
        return Response({
            'status':stat,
            'data':send
        })