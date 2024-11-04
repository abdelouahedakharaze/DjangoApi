from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, VendorSerializer, UserUpdateSerializer, VendorUpdateSerializer

User = get_user_model()

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class CreateVendorView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.AllowAny]

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class VendorDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.filter(user_type='VENDOR')
    serializer_class = VendorUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        if request.user.user_type != 'VENDOR':
            return Response({"detail": "You do not have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)