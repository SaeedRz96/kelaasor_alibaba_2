from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from bus_app.models import Sale
from rest_framework.generics import ListAPIView
from bus_app.serializers import SaleSerializer
from rest_framework.permissions import IsAuthenticated


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
        