import boto3
import os
from PIL import Image, ImageOps
from io import BytesIO

s3 = boto3.client('s3')
size = int(os.environ['THUMBNAIL_SIZE'])


def s3_thumbnail_generator(event, context):
    print(event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    if not key.endswith('_thumbnail.png'):

        # Get the image
        image = get_s3_image(bucket, key)
        # Resize the image
        thumbnail = image_to_thumbnail(image)
        # Get the new filename
        thumbnail_key = new_filename(key)
        # Upload the file
        url = upload_to_s3(bucket, thumbnail_key, thumbnail)
        return url


def get_s3_image(bucket, key):
    response = s3.get_object(Bucket=bucket, Key=key)
    image_content = response['Body'].read()

    file = BytesIO(image_content)
    img = Image.open(file)

    return img


def image_to_thumbnail(image):
    return ImageOps.fit(image, (size, size), Image.ANTIALIAS)


def new_filename(key):
    key_split = key.rsplit('.', 1)
    print(key_split)
    return key_split[0].replace("original/", "thumb/") + "_thumbnail.png"


def upload_to_s3(bucket, key, image):
    # We're saving the image into a cStringIO object to avoid writing to disk
    out_thumbnail = BytesIO()
    # You must specify the file type because there is no file name to discern it from
    image.save(out_thumbnail, 'PNG')
    out_thumbnail.seek(0)

    response = s3.put_object(
        ACL='public-read',
        Body=out_thumbnail,
        Bucket=bucket,
        ContentType='image/png',
        Key=key
    )
    print(response)

    url = '{}/{}/{}'.format(s3.meta.endpoint_url, bucket, key)
    print(url)
    return url
