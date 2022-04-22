from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_birth = models.DateTimeField()
    field = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(default='static/user/images/default_image.jpg', upload_to='profile_images')

    def age(self):
        return relativedelta(timezone.now().date(), self.date_birth).years

    def save(self, *args, **kwargs):
        data = super().save(*args, **kwargs)
        send_mail(
            subject="Profile",
            message="asdasdf",
            from_email="artshesblbulyan@gmail.com",
            recipient_list=[self.user.email],
        )

    def __str__(self):
        return f"{self.user.username}"
