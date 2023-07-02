from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name = models.CharField(max_length=20, unique=True)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name
     
class Doctors(models.Model):
    doc_name = models.CharField(max_length=30)
    doc_spec = models.CharField(max_length=30)
    doc_dep = models.ForeignKey(Department, on_delete=models.CASCADE)
    doc_images = models.ImageField(upload_to="doctors")

    def __str__(self):
        return self.doc_name

class Booking(models.Model):
    patient_name = models.CharField(max_length=20)
    patient_phone = models.CharField(max_length=10)
    patient_email = models.EmailField()
    doctor = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    appointment_date = models.DateField()
    booked_on = models.DateField(auto_now =True)

    def __str__(self):
        return self.p_name
    

class User(AbstractUser):
    name = models.CharField(max-max_length=20)
    