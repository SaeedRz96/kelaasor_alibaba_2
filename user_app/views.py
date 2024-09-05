from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from bus_app.models import Sale
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView
from bus_app.serializers import SaleSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer
from .models import Wallet


class Login(TokenObtainPairView):
    pass


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