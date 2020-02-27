from django.urls import path, include
#Django Resteframework
from rest_framework.routers import DefaultRouter 
from images.views import Images, CountVehicles

router = DefaultRouter(trailing_slash=False)
router.register(r'images',Images,basename="_images")
router.register(r'count_vehicles', CountVehicles, basename="count_vehicles")

urlpatterns = [
    path('',include(router.urls)),
]