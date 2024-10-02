# signing/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Document, Signature
from .serializers import DocumentSerializer, SignatureSerializer

class DocumentUploadView(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class SignatureCreateView(generics.CreateAPIView):
    queryset = Signature.objects.all()
    serializer_class = SignatureSerializer

    def post(self, request, *args, **kwargs):
        document_id = request.data.get('document')
        if not Document.objects.filter(id=document_id).exists():
            return Response({"error": "Document does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().post(request, *args, **kwargs)
