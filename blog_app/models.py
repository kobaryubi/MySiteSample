from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from CommonClasses.FieldCommonConsts import *

class Category(models.Model):
    name = models.CharField(
        max_length=FieldCommonConsts.NORMAL_LENGTH
    )

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(
        max_length=FieldCommonConsts.NORMAL_LENGTH
    )
    text = models.TextField()
    categories = models.ManyToManyField(Category)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="create_blogs")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="update_blogs")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_app:blog_detail", kwargs={'pk': self.pk})
