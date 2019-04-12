from rest_framework import serializers

from OCR_img_app.models import Image


# serializers for image model
class ImageSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(max_length=50)
    DOB = serializers.DateField()

    class Meta:
        model = Image
        fields = ['Name', 'DOB']



