from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

r= Reporter()
r.first_name ='Sam'
r.last_name = 'arsh'
r.email ='abc@gmail.com'
print(r)