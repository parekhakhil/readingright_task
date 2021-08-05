from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# Create your models here.

class Grocery(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('bought', 'Bought'),
        ('not_available', 'Not Available'),
    )

    product = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=200)
    status = models.CharField(max_length=200,choices=STATUS)
    date = models.DateField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product

    def get_absolute_url(self):
        return reverse('grocery-detail', kwargs={'pk': self.pk})
