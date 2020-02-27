# django 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404 as _get_object_or_404
# python
from datetime import timedelta
#import jwt
# restframework
from rest_framework import viewsets,mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination, BasePagination
from rest_framework.decorators import action
from rest_framework.settings import api_settings

#from apps.users.permissions.auth import IsAdminOrOwner
# models
from images.models import Historico_Imagenes, Historic_Vehicles_detected
#from apps.users.models import User_Course, User
#from apps.dailyActivities.models import Daily_Activities
#serializers
from images.serializers import imagesSerializer, countVehiclesSerializer
#from apps.users.serializers.appSerializers import dailyActivitiesSerializer

class LargeResultsSetPagination(PageNumberPagination, BasePagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000

class Images(viewsets.GenericViewSet,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin
            ):

    permission_classes = (AllowAny,)
    pagination_class = LargeResultsSetPagination
    #filter_backends = [DjangoFilterBackend]   
    queryset = Historico_Imagenes.objects.all()
    serializer_class = imagesSerializer.imagesSerializer

    @action(detail=True, methods=['PATCH'])
    def upload(self,request, *args, **kwargs):
        """
        Determine the courses of the user
        """
        #breakpoint()
        instance = self.get_object()
        serializer = imagesSerializer.UpdateImagesSerializer(data=request.data)
        serializer.is_valid()
        serializer.update(instance, serializer.data)
        return Response(serializer.data)  


class CountVehicles(viewsets.GenericViewSet,
                    mixins.CreateModelMixin):
    permission_classes = (AllowAny,)
    pagination_class = LargeResultsSetPagination
    serializer_class = countVehiclesSerializer.CountVehiclesSerializer
    queryset = Historic_Vehicles_detected.objects.all()
