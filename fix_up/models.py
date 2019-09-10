from django.db import models

class Contractor(models.Model):
    projects = models.ManyToManyField('Project', related_name="project_list", blank=True)
    name = models.CharField(null=False, max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(null=False, max_length=255)
    zip = models.CharField(null=False, max_length=255)
    category = models.CharField(null=False, max_length=255)
    logo = models.TextField(null=False)
    example_project_1 = models.TextField()
    example_project_2 = models.TextField()

    def __str__(self):
        return "{} - {}".format(self.name, self.projects, self.email, self.phone_number, self.zip, self.category, self.logo)

class User(models.Model):
    full_name = models.CharField(null=False, max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(null=False, max_length=255)
    zip = models.CharField(null=False, max_length=255)

    def __str__(self):
        return "{} - {}".format(self.full_name, self.email, self.phone_number, self.zip)

class Project(models.Model):
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    contractors = models.ManyToManyField('Contractor', related_name="contractor_list", blank=True)
    title = models.CharField(null=False, max_length=255)
    description = models.CharField(null=False, max_length=1000)
    category = models.CharField(null=False, max_length=255)
    user_before_picture = models.TextField()
    user_after_picture = models.TextField(null=True)

    def __str__(self):
        return "{} - {}".format(self.user, self.contractors, self.title, self.description, self.category, self.user_before_picture, self.user_after_picture)

class ContractorProject(models.Model):
    project = models.ForeignKey('Project', on_delete=models.PROTECT)
    contractor = models.ForeignKey('Contractor', on_delete=models.PROTECT)
    contractor_choice = models.IntegerField(default=0)
    user_choice = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    contractor_before_picture = models.TextField(default=None, null=True)
    contractor_after_picture = models.TextField(default=None, null=True)
    user_rating = models.IntegerField(default=None, null=True)
    contractor_rating = models.IntegerField(default=None, null=True)

    def __str__(self):
        return "{} - {}".format(self.project, self.contractor, self.contractor_choice, self.user_choice, self.completed, self.contractor_before_picture, self.contractor_after_picture, self.user_rating, self.contractor_rating)
