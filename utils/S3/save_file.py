import boto3
import uuid
# Django
from django.conf import settings

def create(image):
    file_name = create_name_file(image.name)	
    s3_resource = boto3.resource('s3')
    object_s3 = s3_resource.Object('tesis-files', file_name)
    object_s3.put(Body=image,ACL= 'public-read')
    url = str("https://%s.s3.amazonaws.com/%s" % ('tesis-files', file_name)).replace(' ','+')
    return(url, file_name)

def create_name_file(file_name):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])	
    return (random_file_name)

def delete(name_old):
    s3_resource = boto3.resource('s3')
    s3_resource.Object('tesis-files', name_old).delete()