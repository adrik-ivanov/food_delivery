from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('category', CategoryViewSet)
router.register('', RestaurantViewSet)

urlpatterns = router.urls

urlpatterns += [

]
