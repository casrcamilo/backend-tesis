import boto3
import uuid
# Django
from django.conf import settings

s3_resource = boto3.resource('s3')

def create_example(image):
    file_name = create_name_file(image.name)	
    object_s3 = s3_resource.Object('tesis-images', file_name)
    object_s3.put(Body=image,ACL= 'public-read')
    url = str("https://%s.s3.amazonaws.com/%s" % ('tesis-images', file_name)).replace(' ','+')
    return(url, file_name)

def create( device, image ):
    object_s3 = s3_resource.Object('tesis-images', device+'/'+image.name)
    object_s3.put(Body=image,ACL= 'public-read')
    url = str("https://%s.s3.amazonaws.com/%s" % ('tesis-images', device+'/'+image.name)).replace(' ','+')
    return(url)

def create_name_file(file_name):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])	
    return (random_file_name)

def delete(name_old):
    s3_resource = boto3.resource('s3')
    s3_resource.Object('tesis-images', name_old).delete()