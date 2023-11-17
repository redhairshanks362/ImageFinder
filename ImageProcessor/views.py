import os

from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
import boto3
from PIL import Image, ImageDraw, ImageFont


class AWSImageProcessing(APIView):
    '''
    def post(self, request, image=None, draw=None, *args, **kwargs):
        client = boto3.client('rekognition', region_name='ap-south-1', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

        #photo will be passed from post request
        photo = request.FILES('photo')
        with open(photo, 'rb') as image_file:
            source_bytes = image_file.read()

        detect_objects = client.detect_labels(Image={'Bytes': source_bytes})

        # image = Image.open(photo)
        #
        # # Create a drawing object
        # draw = ImageDraw.Draw(image)

        for label in detect_objects['Labels']:
            print(label["Name"])
            print("Confidence:", label["Confidence"])

            for instances in label['Instances']:
                if 'BoundingBox' in instances:

                    box = instances["BoundingBox"]

                    left = image.width * box['Left']
                    top = image.height * box['Top']
                    width = image.width * box['Width']
                    height = image.height * box['Height']

                    points = (
                        (left,top),
                        (left + width, top),
                        (left + width, top + height),
                        (left, top + height),
                        (left, top)
                    )

                    draw.line(points, width=5, fill="#69f5d9")

                    shape = [(left -2, top - 35), (width + 2 + left, top)]
                    draw.rectangle(shape, fill = "#69f5d9")

                    font = ImageFont.truetype("arial.ttf", 30)

                    draw.text((left + 10, top - 30), label["Name"], font=font, fill='#000000')
                    image.save("output.jpg")

                    return Response(status=status.HTTP_200_OK)
                    '''
    def post(self, request, *args, **kwargs):
        # Get the image from the request
        source_bytes = request.FILES['photo'].read()

        #photo = '/home/kidastudios/Downloads/440px-Maniac_UK_premiere_(Theroux).jpg'
        #photo = '/home/kidastudios/Downloads/microsoft_logo_02-666x666.png'
        #photo = '/home/kidastudios/Downloads/istockphoto-466754640-2048x2048.jpg'

        output_folder = '/home/kidastudios/Downloads/'

        # image = Image.open(photo)
        # draw = ImageDraw.Draw(image)


        # Read the image bytes
        # with open(photo, 'rb') as image_file:
        #     source_bytes = image_file.read()

        # Create a Rekognition client
        access_key_id = os.environ.get('access_key_id')
        secret_access_key = os.environ.get('secret_access_key')
        client = boto3.client('rekognition', region_name='ap-south-1', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

        # Detect labels in the image
        detect_objects = client.detect_labels(Image={'Bytes': source_bytes})
        labels = []
        # Print the labels and confidence scores
        for label in detect_objects['Labels']:
            print(label["Name"])
            print("Confidence:", label["Confidence"])
            label_name = label["Name"]
            confidence = label["Confidence"]
            labels.append({"name": label_name, "confidence": confidence})

            #This below part is not working need to fix
            # for instances in label['Instances']:
            #     if 'BoundingBox' in instances:
            #
            #         box = instances["BoundingBox"]
            #
            #         left = image.width * box['Left']
            #         top = image.height * box['Top']
            #         width = image.width * box['Width']
            #         height = image.height * box['Height']
            #
            #         points = (
            #             (left,top),
            #             (left + width, top),
            #             (left + width, top + height),
            #             (left, top + height),
            #             (left, top)
            #         )
            #
            #         draw.line(points, width=5, fill="#69f5d9")
            #
            #         shape = [(left -2, top - 35), (width + 2 + left, top)]
            #         draw.rectangle(shape, fill = "#69f5d9")
            #
            #         font = ImageFont.truetype("arial.ttf", 30)
            #
            #         draw.text((left + 10, top - 30), label["Name"], font=font, fill='#000000')
            #         output_path = os.path.join(output_folder, "output.jpg")
            #
            #         image.save(output_path)

        return Response({"labels": labels},status=status.HTTP_200_OK)






