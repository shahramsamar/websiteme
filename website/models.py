from django.db import models

# Create your models here.
class BasicInformationModel(models.Model):
        about = models.TextField()
        age = models.PositiveIntegerField()
        email = models.EmailField()
        phone_number = models.CharField(max_length=255)
        address = models.CharField(max_length=255)
        language = models.CharField(max_length=255)
        
class Contact(models.Model):
        name = models.CharField(max_length=255)
        email = models.EmailField()
        subject = models.CharField(max_length=255)
        message = models.TextField()
        create_date = models.DateTimeField(auto_now_add =True)
        updated_date = models.DateTimeField(auto_now=True)
        
        class Meta :
                ordering = ['create_date']
        
        def __str__(self):
                return self.name