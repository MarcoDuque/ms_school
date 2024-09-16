from django.db import models

class School(models.Model):
    school_name = models.CharField(max_length=100, null=False)
    school_slogan = models.CharField(max_length=100)
    school_address = models.CharField(max_length=100, null=False)
    school_city = models.CharField(max_length=100)
    school_state = models.CharField(max_length=100)
    school_zip = models.IntegerField()
    school_phone = models.CharField(max_length=100)
    school_email = models.EmailField(null=False)
    school_photo_logo = models.ImageField(upload_to='media/', default="media/no_img.jpg", null=True)
    school_users_admin = models.IntegerField()
    school_users_operators = models.IntegerField()
    school_subsidiaries = models.BooleanField(default=False)
    
    def __string__(self):
        return self.school_name