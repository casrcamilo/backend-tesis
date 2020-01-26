import boto3
import requests
import time
from io import BytesIO
from utils.S3.save_file import create as save_file
from django.conf import settings

from PIL import Image, ImageDraw

def detect_labels(photo, url):
    bucket='tesis-files'
    client=boto3.client('rekognition')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    responseImg = requests.get(url)
    im = Image.open(BytesIO(responseImg.content))
    imgWidth,imgHeight  = im.size  

    for label in response['Labels']:
        if (label['Name'] == 'Car' or label['Name'] == 'Motorcycle' or label['Name'] == 'Truck'  or label['Name'] == 'Bus'  or label['Name'] == 'Taxi' or label['Name'] == 'Boat'):
            for i in range(0, len(label['Instances'])):
                draw = ImageDraw.Draw(im)
                box=label['Instances'][i]['BoundingBox']
                left = imgWidth * box['Left']
                top = imgHeight * box['Top']
                width = imgWidth * box['Width']
                height = imgHeight * box['Height']
                points = (
                            (left,top),
                            (left + width, top),
                            (left + width, top + height),
                            (left , top + height),
                            (left, top)
                )
                draw.line(points, fill='#00d400', width=2)

    imageName = time.asctime( time.localtime(time.time()) )
    buffer = BytesIO()
    im.save(buffer, "JPEG")
    buffer.seek(0)
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket='tesis-files',
        Key=str('%s.jpeg' % imageName),
        Body=buffer,
        ContentType='image/jpeg',
        ACL= 'public-read'
    )
    return str("https://%s.s3.amazonaws.com/%s.jpeg" % ('tesis-files', imageName)).replace(' ','+')