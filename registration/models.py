from django.db import models

class Student(models.Model): 
    student_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=50, blank=True)
    program = models.CharField(max_length=100)
    year_level = models.IntegerField() 
    email = models.EmailField() 
    status = models.CharField(max_length=20, default='Active')


    def __str__(self): 
        return self.student_name 
