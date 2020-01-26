from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
# models
from images.models import Historico_Imagenes
#utils
from utils.S3.save_file import create as save_file
from utils.S3.save_file import delete as delete_file
from utils.S3.rekognition import detect_labels

# Update images
class imagesSerializer(serializers.ModelSerializer):
    """serializer que sube imagenes a s3"""
    imagen_sin_analizar = serializers.FileField()
    imagen_analizada = serializers.CharField(required=False)

    def create(self, validated_data):
        #breakpoint()

        url = save_file(validated_data.get('imagen_sin_analizar'))
        validated_data['imagen_sin_analizar'] = url[0]
        validated_data['imagen_analizada']  = detect_labels(url[1], url[0])
        #breakpoint()
        image = Historico_Imagenes(**validated_data)
        image.save()
        return image

    def to_representation(self, instance):
        ret = ImagePutSerializer(instance)
        return ret.data

    class Meta:
        model = Historico_Imagenes
        fields = (
                'pk',
                'imagen_sin_analizar',
                'imagen_analizada'
                )
        read_only_fields = (
                'imagen_analizada',
        )

class ImagePutSerializer(serializers.ModelSerializer):#
    """serializer que muestra las imagenes"""
    imagen_sin_analizar = serializers.URLField(required=False)
    imagen_analizada = serializers.URLField(required=False)

    class Meta:
        model = Historico_Imagenes
        fields = (
                'pk',
                'imagen_sin_analizar',
                'imagen_analizada'
                )
        read_only_fields = (
                'imagen_analizada',
        )

class UpdateImagesSerializer(serializers.ModelSerializer):

    cajas_teoricas = serializers.IntegerField()
    cajas_practicas = serializers.IntegerField()
    porcentaje = serializers.IntegerField()
    imagen_sin_analizar = serializers.URLField(required=False)
    imagen_analizada = serializers.URLField(required=False)

    class Meta:
        model = Historico_Imagenes
        fields = (
                'pk',
                'imagen_sin_analizar',
                'imagen_analizada',
                'cajas_teoricas',
                'cajas_practicas',
                'porcentaje'
                )
