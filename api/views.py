from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics, mixins
from api.serilizers import *
from rest_framework.authtoken.models import Token
import math
import random
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class SignUp(APIView):
    serializer_class = UserSerilizer
    def post(self,request):
        serilize = self.serializer_class(data=request.POST)
        if serilize.is_valid(raise_exception=True):
            user = serilize.save()
            token = token = Token.objects.create(user=user)
            return JsonResponse({"status":"ok","token":token.key})
        else:
            return JsonResponse({"status":"faild"},status=422)


class CreateLink(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def generate_random_string(self,lenght):
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        OTP = ""
        for i in range(lenght):
            OTP += digits[math.floor(random.random() * 62)]
        return OTP
    
    def post(self,request):
        random_string = self.generate_random_string(9)
        serilize = LinkSerilizer(data={"user":request.user.pk,
        "link":request.POST.get("link",None),
        "random_string":random_string})
        if serilize.is_valid(raise_exception=True):
            link = serilize.save()
            return JsonResponse({"status":"ok","link":link.short_link()})
        else:
            return JsonResponse({"status":"faild"},status=422)


class RedirectToLink(APIView):
    def get(self,request,random_string):
        link = get_object_or_404(Link,random_string=random_string)
        link.visit_count += 1
        link.save()
        return redirect(link.link)
