from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=("users"), on_delete=models.CASCADE)
    avatar = models.ImageField(("avatar"), upload_to='profiles', blank=True, null=True)
    bio = models.TextField(("Bio"), blank=True, null=True) #optional
    link = models.URLField(("link"), null=True, blank=True, max_length=200) # optional
    email = models.EmailField(("email"), max_length=254, blank=True, null=True) #optional
    slug = models.SlugField(("slug"))
    
    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.pk})
