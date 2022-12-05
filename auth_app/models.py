from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SecretUser(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    picked_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="picked_user")
    hobby = models.TextField(null=True,max_length=300)
    fav_food = models.TextField(null=True, max_length=100)
    hap_moment = models.TextField(null=True, max_length=300)
    fun_moment = models.TextField(null=True, max_length=300)
    child_dream = models.TextField(null=True, max_length=300)
    job_desc = models.TextField(null=True, max_length=300)
    teen_photo = models.ImageField(null=True, upload_to="images")
