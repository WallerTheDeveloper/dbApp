from django.db import models
import uuid
# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    card_id = models.IntegerField()
    unique_id = models.UUIDField(
         default=uuid.uuid4, 
         unique=True,
         primary_key=True, 
         editable=False)
    student_image = models.ImageField(null=True, blank=True, default="default_student.jpg")
    class Meta:
        verbose_name_plural = 'Students'

    #Methods
    def __str__(self):
        return f'{self.name} {self.surname}'

class Teachers(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    related_students = models.ManyToManyField(Students)
    age = models.PositiveSmallIntegerField(default=1)
    id = models.UUIDField(
         default=uuid.uuid4, 
         unique=True,
         primary_key=True, 
         editable=False)

    class Meta:
        verbose_name_plural = 'Teachers' 

    #Methods
    def __str__(self):
        return f'{self.name} {self.surname}'