# signing/models.py
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Signature(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    signature_image = models.ImageField(upload_to='signatures/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Signature for {self.document.title}'
