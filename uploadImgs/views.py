from .models import Pictures
from .serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class upload_images(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        # converts querydict to original dict
        images = dict((request.data).lists())['picture']
        print(images)
        for image in images:
            print(image.name.split('.'))
            print(id(image))
            serializer = ImageSerializer(data={'picture': image})
            if serializer.is_valid():
                 Pictures.objects.create(picture=image)
            else:
                 return Response({'error': 'Failed to load images'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Images uploaded successfully'}, status=status.HTTP_200_OK)