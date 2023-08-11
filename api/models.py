from django.db import models


# Create your models here.
class Company(models.Model):
    TYPE = (
        ("IT", "IT"),
        ("Non IT", "Non IT"),
    )

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    about = models.TextField()
    type = models.CharField(max_length=50, choices=TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    TYPE = (
        ("Manager", "Manager"),
        ("Developer", "Developer"),
        ("Project Leader", "Project Leader"),
    )
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    about = models.TextField(max_length=500)
    position = models.CharField(max_length=50, choices=TYPE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
