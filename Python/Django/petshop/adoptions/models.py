from django.db import models, migrations

class Pet(models.Model):
    sex_choice = [('M','Male'),('F', 'Female')]
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=25)
    breed  =models.CharField(max_length=25, blank=True)
    submitter = models.CharField(max_length=100)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=sex_choice, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)


class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name