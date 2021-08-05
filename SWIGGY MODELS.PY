from django.db import models
class user(models.Model):
    Name=models.CharField(max_length=200)
    place=models.CharField(max_length=100)
    def __str__(self):
        return self.Name
class product(models.Model):
    price=models.ForeignKey(user,on_delete=models.CASCADE)
    quality=models.CharField(max_length=500)
    rating=models.CharField(max_length=500)
    def __str__(self):
        return self.price
class login(models.Model):
    username=models.CharField(max_length=500)
    password=models.CharField(max_length=500)
    def __str__(self):
        return self.username
class order(models.Model):
    Name = models.CharField(max_length=500)
    Address = models.CharField(max_length=500)
    MobileNumber = models.CharField(max_length=500)
    EmailID = models.CharField(max_length=500)
    OrderedDate = models.CharField(max_length=500)
    item = models.CharField(max_length=500)
    price = models.CharField(max_length=500)
    def __str__(self):
        return self.Name

