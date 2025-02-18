import os
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PDFUploadSerializer
from .utils import process_pdf

class PDFUploadView(APIView):
    def post(self, request, format=None):

        serializer = PDFUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            pdf_file = serializer.data['pdf_file']
            pdf_file = pdf_file.replace('/media', '').replace('\\', '/')
            pdf_path = settings.MEDIA_ROOT + pdf_file
            print(pdf_path)
            process_pdf(pdf_path)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)