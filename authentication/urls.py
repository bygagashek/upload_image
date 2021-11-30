from django.urls import path
from authentication.views import RegisterView, LogoutView, GetCurrentUserView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('current-user/', GetCurrentUserView.as_view(), name='get_current_user'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
]