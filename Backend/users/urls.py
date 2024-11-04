from django.urls import path
from .views import CreateUserView, CreateVendorView, UserDetailView, VendorDetailView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='user-register'),
    path('register/vendor/', CreateVendorView.as_view(), name='vendor-register'),
    path('profile/', UserDetailView.as_view(), name='user-profile'),
    path('profile/vendor/', VendorDetailView.as_view(), name='vendor-profile'),
]