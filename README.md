# AWS Serverless Image Processing

A serverless image processing pipeline built using AWS Lambda, Amazon S3, and Python (Pillow).

## What it does
When an image is uploaded to a source S3 bucket, this Lambda function automatically:
- Downloads the image
- Resizes it to fit within 800x800px (preserving aspect ratio)
- Compresses it
- Uploads the processed image to a destination S3 bucket

## Architecture
