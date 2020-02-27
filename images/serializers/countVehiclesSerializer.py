from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
# models
from images.models import Historic_Vehicles_detected
#utils
from utils.S3.save_file import create as save_file
from utils.S3.save_file import delete as delete_file
from utils.S3.rekognition import count_labels

class CountVehiclesSerializer(serializers.ModelSerializer):
	device_id = serializers.CharField()
	image = serializers.FileField(required=True)
	
	def create(self, validated_data):
		image = validated_data.get('image')
		device = validated_data.get('device_id')
		url = save_file( device , image )
		awsRekognition = count_labels( device , image.name )

		#assign data to object
		validated_data['image'] = url
		validated_data['awsRekognition_response'] = awsRekognition[0]
		validated_data['vehicles_detected'] = awsRekognition[1]

		#save data in model's object
		instance = Historic_Vehicles_detected(**validated_data)
		instance.save()
		return instance

	def to_representation(self, instance):
		#breakpoint()
		ret = SerializerResponseSerializer(instance)
		return ret.data

	class Meta:
		model = Historic_Vehicles_detected
		fields = (
				'pk', 
				'image',
				'device_id'
				)

class SerializerResponseSerializer(serializers.ModelSerializer):#
	"""serializer que muestra las imagenes"""
	device_id = serializers.CharField()
	time = serializers.models.DateTimeField()
	image = serializers.URLField(required=False)
	vehicles_detected = serializers.IntegerField()

	class Meta:
		model = Historic_Vehicles_detected
		fields = (
				'pk',
				'device_id',
				'image',
				'vehicles_detected'
				)