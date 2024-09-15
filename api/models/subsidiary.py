from django.db import models

from api.models import school

class Subsidiary(models.Model):
    School = models.ForeignKey(school.School, related_name='branches', on_delete=models.CASCADE, null=False)
    subsidiary_name = models.CharField(max_length=100, null=False)
    subsidiary_slogan = models.CharField(max_length=100)
    subsidiary_address = models.CharField(max_length=100, null=False)
    subsidiary_city = models.CharField(max_length=100)
    subsidiary_state = models.CharField(max_length=100)
    subsidiary_zip = models.IntegerField()
    subsidiary_phone = models.CharField(max_length=100)
    subsidiary_email = models.EmailField(null=False)
    subsidiary_photo_logo = models.ImageField(upload_to='media/', default="media/no_img.jpg", null=True)
    
    def __string__(self):
        return self.subsidiary_name