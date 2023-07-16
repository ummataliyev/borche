from django.db import models
from django.utils import timezone
from django.db.models.query import QuerySet


class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status='PB')


class Product(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=False)
    image = models.ImageField(upload_to="media")
    publish_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.Draft
        )
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-publish_time"]

    def __str__(self) -> str:
        return self.title


class GetInTouch(models.Model):
    fullname = models.CharField(max_length=255, null=True, blank=False)
    number = models.CharField(max_length=20, null=True, blank=False)

    def __str__(self):
        return self.fullname
