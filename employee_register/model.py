from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=100, unique=True)
    mobile = models.CharField(max_length=100, unique=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class Product(models.Model):
    web_id = models.CharField(
        max_length=50,
        unique=True,
    )
    slug = models.SlugField(
        max_length=255,
    )
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField(blank=True)
    is_active = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name