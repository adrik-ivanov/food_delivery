from django.urls import path, include
from . import views

# Create your views here.
urlpatterns = [
    # path('signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/', include('allauth.urls')),
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
]
