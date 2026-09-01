from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    cgpa = models.FloatField(default=0.0)
    skills = models.TextField(blank=True)
    placed = models.BooleanField(default=False)

    def  __str__(self):
        return self.name


class Company(models.Model):

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default="")
    role = models.CharField(max_length=100)
    package = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Placement(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    job_role = models.CharField(
        max_length=100
    )

    package = models.CharField(
        max_length=50
    )

    placement_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.name} - {self.company.name}"