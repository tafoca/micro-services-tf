# signing/serializers.py

from rest_framework import serializers
from .models import Document, Signature

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'file', 'created_at']

class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = ['id', 'document', 'signature_image', 'created_at']
