from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    background_image = models.ImageField(default='bg-default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        profile_image = Image.open(self.profile_image.path)
        if profile_image.height > 300 or profile_image.width > 300:
            output_size = (300, 300)
            profile_image.thumbnail(output_size)
            profile_image.save(self.profile_image.path)

        background_image = Image.open(self.background_image.path)
        if background_image.height > 1080 or background_image.width > 1080:
            output_size = (1080, 1080)
            background_image.thumbnail(output_size)
            background_image.save(self.background_image.path)


class Todo(models.Model):

    title = models.CharField(max_length=300)
    important = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('todos-profile')

    def __str__(self):
        return self.title


class Notes(models.Model):

    title = models.CharField(max_length=300)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('todos-profile')

    def __str__(self):
        return self.title


