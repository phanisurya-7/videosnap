from django.utils.http import MAX_URL_LENGTH
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=500)
    city = models.TextField()
    state = models.TextField()
    district = models.TextField()
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)


    def __str__(self):
        return self.user.username


class Projects(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.user.username

class Education(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()   
    
    
    def __str__(self):
        return self.user.username

class Experience(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    
    
    def __str__(self):
        return self.user.username

class Certifications(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100)
    certification = models.CharField(max_length=100)
    date = models.DateField()
    
    
    
    def __str__(self):
        return self.user.username

class Contact(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    

    def __str__(self):
        return self.user.username


class Achievements(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100)
    achievement = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.user.username
        


    


    

