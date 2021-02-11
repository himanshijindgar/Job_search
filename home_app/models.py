from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Post(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    date_posted = models.DateTimeField(default=timezone.now)
    contact_no = models.PositiveIntegerField(validators=[MaxValueValidator(999999999)])
    def __str__(self):
        return self.category
