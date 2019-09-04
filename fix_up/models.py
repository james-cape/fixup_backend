from django.db import models

class Contractors(models.Model):
    name = models.CharField(null=False, max_length=255)
    email = models.CharField(null=False, max_length=255)
    phone_number = models.CharField(null=False, max_length=255)
    zip = models.CharField(null=False, max_length=255)
    specialty = models.CharField(null=False, max_length=255)
    logo = models.CharField(null=False, max_length=255)
    example_project_1 = models.CharField(max_length=255)
    example_project_2 = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.name, self.email, self.phone_number, self.zip, self.specialty, self.logo)
