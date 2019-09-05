from django.db import models

class Contractor(models.Model):
    name = models.CharField(null=False, max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(null=False, max_length=255)
    zip = models.CharField(null=False, max_length=255)
    category = models.CharField(null=False, max_length=255)
    logo = models.CharField(null=False, max_length=255)
    example_project_1 = models.CharField(max_length=255)
    example_project_2 = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.name, self.email, self.phone_number, self.zip, self.category, self.logo)

class User(models.Model):
    full_name = models.CharField(null=False, max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(null=False, max_length=255)
    zip = models.CharField(null=False, max_length=255)

    def __str__(self):
        return "{} - {}".format(self.full_name, self.email, self.phone_number, self.zip)
