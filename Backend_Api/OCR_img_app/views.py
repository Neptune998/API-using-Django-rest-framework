from django.shortcuts import render
from google.cloud import vision
from rest_framework.views import APIView
from OCR_img_app.serializers import ImageSerializer
import io

# API view for images
# http://127.0.0.1:8000/image/
class ImageView(APIView):

    def get(self, request):
        """Detects text in the file."""
        client = vision.ImageAnnotatorClient()
        file_name="..../image.jpg"
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        #texts = Image.objects.all()
        serializer = ImageSerializer(texts, many=True)

        return render(request=request,
                      template_name='image.html',
                      context={'details': serializer.data})





