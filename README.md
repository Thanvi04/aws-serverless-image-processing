
# AWS Serverless Image Processing

## Overview

AWS Serverless Image Processing is a cloud-based project that automates image resizing and compression using AWS Lambda, Amazon S3, and Python.

When an image is uploaded to the source S3 bucket, an event triggers an AWS Lambda function. The function retrieves the image, resizes it to fit within 800 × 800 pixels while maintaining its aspect ratio, compresses it, and uploads the processed image to a destination S3 bucket.

## Objectives

- Automate image processing using AWS services.
- Resize images while maintaining their aspect ratio.
- Compress images to reduce file size.
- Store processed images in a destination S3 bucket.
- Implement an event-driven serverless workflow.

## Technologies Used

- AWS Lambda
- Amazon S3
- Python
- Boto3
- Pillow (PIL)

## How It Works

1. Image is uploaded to the source S3 bucket.
2. An S3 event triggers the Lambda function.
3. The function retrieves the image using Boto3.
4. Pillow resizes the image to fit within 800 × 800 pixels.
5. The image is compressed using a quality setting of 70.
6. The processed image is uploaded to the destination S3 bucket with the prefix `processed-`.

## Architecture

    User Uploads Image
            |
            v
    Source S3 Bucket
            |
            v
    S3 Event Notification
            |
            v
    AWS Lambda Function
            |
            v
    Resize and Compress Image
            |
            v
    Destination S3 Bucket

## Key Features

- Automatic image processing
- Image resizing with aspect ratio preservation
- Image compression
- Cloud-based image storage
- Event-driven serverless execution

## Setup and Configuration

### Prerequisites

- An AWS account
- An Amazon S3 source bucket
- An Amazon S3 destination bucket
- An AWS Lambda function
- Appropriate IAM permissions

### Install Dependencies

```bash
pip install boto3 Pillow
```

### Deployment Steps

1. Create the source and destination S3 buckets.
2. Create an AWS Lambda function using a compatible Python runtime.
3. Add the project code and package Pillow and its dependencies.
4. Configure IAM permissions for S3 access and CloudWatch logging.
5. Configure an S3 event notification to invoke the Lambda function when an image is uploaded.
6. Upload a test image and verify that the processed image appears in the destination bucket.

## Example

Original image: `photo.jpg`

Processed image: `processed-photo.jpg`

The processed image fits within 800 × 800 pixels while maintaining its aspect ratio.

## Applications

- Image optimization for websites
- Automated media processing
- Cloud-based image transformation
- Serverless application development

## Future Enhancements

- Generate thumbnails in multiple sizes.
- Support batch image processing.
- Improve error handling.
- Configure bucket names through environment variables.
- Add monitoring using Amazon CloudWatch.

## Author

Thanvi Rai N

GitHub: [Thanvi04](https://github.com/Thanvi04)

