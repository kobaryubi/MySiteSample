from django.conf import settings
from django.db import models
from django.utils import timezone

from CommonClasses.FileUtils import *

class Favorites(models.Model):
    class Meta:
        db_table = 'favorite'

    title = models.CharField(max_length=2**8)
    comment = models.TextField()
    photo = models.ImageField(blank=True, null=True,
        upload_to=FileUtils.get_favs_share_app_image_path)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    created_at = models.DateTimeField(default=timezone.now)