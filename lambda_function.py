import boto3
from PIL import Image
import io
from urllib.parse import unquote_plus

s3 = boto3.client('s3')

DESTINATION_BUCKET = 'thanvi-navoditha-final'  # your destination bucket

def lambda_handler(event, context):
    # Get the uploaded file's bucket and filename from the trigger event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    file_key = unquote_plus(event['Records'][0]['s3']['object']['key'])

    # Download the original image into memory
    response = s3.get_object(Bucket=source_bucket, Key=file_key)
    image_content = response['Body'].read()

    # Open it with Pillow and resize it (max width 800px, keeps aspect ratio)
    image = Image.open(io.BytesIO(image_content))
    image.thumbnail((800, 800))

    # Save the resized image into memory
    buffer = io.BytesIO()
    image_format = image.format if image.format else 'JPEG'
    image.save(buffer, format=image_format, quality=70)
    buffer.seek(0)

    # Upload the processed image to the destination bucket
    output_key = f"processed-{file_key}"
    s3.put_object(
        Bucket=DESTINATION_BUCKET,
        Key=output_key,
        Body=buffer,
        ContentType=response.get('ContentType', 'image/jpeg')
    )

    print(f"Processed {file_key} and saved as {output_key}")
    return {"statusCode": 200, "body": f"Processed {file_key}"}
