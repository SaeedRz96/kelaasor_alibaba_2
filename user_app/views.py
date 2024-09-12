from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from bus_app.models import Sale
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView
from bus_app.serializers import SaleSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer
from .models import Wallet
from rest_framework.views import APIView
import random
from rest_framework.response import Response
from django.core.cache import cache
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class Login(TokenObtainPairView):
    pass


class GetOTP(APIView):
    def post(self,request):
        phone_number = request.data.get("phone")
        otp = random.randint(1000,9999)
        cache.set(phone_number,otp, timeout=180)
        # SMS TO USER
        return Response("Your Code for Is :{}".format(otp))


class OTPLogin(APIView):
    def post(self, request):
        input_otp = request.data.get("input_otp")
        phone_number = request.data.get("phone_number")
        otp_valid = cache.get(phone_number)
        if not otp_valid:
            return Response("No otp!")
        if otp_valid == input_otp:
            cache.delete(phone_number)
            user = User.objects.get(username=phone_number)
            refresh_token = RefreshToken.for_user(user)
            access_token = AccessToken.for_user(user)
            return Response(
                {
                    "refresh_token" : str(refresh_token),
                    "access_token" : str(access_token)
                }
            )
            
        else:
            return Response("OTP is incorrect")
        


class Refresh(TokenRefreshView):
    pass


class MySale(ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Sale.objects.filter(user=self.request.user)


class DeleteSale(DestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            return super().perform_destroy(instance)


class CreateSale(CreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        sale = serializer.save(user = self.request.user)
        return sale


class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    
    # def perform_create(self, serializer):
    #     user = serializer.save()
    #     Wallet.objects.create(user=user)