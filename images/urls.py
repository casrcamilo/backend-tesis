from django.urls import path, include
#Django Resteframework
from rest_framework.routers import DefaultRouter 
from images.views import Images

router = DefaultRouter(trailing_slash=False)
router.register(r'images',Images,basename="_images")

urlpatterns = [
    path('',include(router.urls)),
]