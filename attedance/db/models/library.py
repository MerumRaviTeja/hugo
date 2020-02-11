from django.db import models
from django.contrib.auth.models import User

from ..mixins import TimeAuditModel


class Employee(TimeAuditModel):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    full_name = models.CharField(max_length=255, blank=False)
    designation = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=10, unique=True, blank=False)
    alternative_phone_number = models.CharField(max_length=10, blank=True, unique=True, null=True)
    email = models.EmailField(unique=True, blank=False)
    id_number = models.CharField(max_length=255, unique=True, blank=False)
    dob = models.DateField(blank=True, null=True)
    joining_date = models.DateField(blank=False)
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        db_table = "employees"

    def __str__(self):
        return f"{self.user.username}"


class Attendance(TimeAuditModel):
    employee = models.ForeignKey(Employee, related_name="attendances", on_delete= models.CASCADE)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=255)
    in_field = models.BooleanField()
    check_in_image = models.ImageField(upload_to=f"employees images")
    check_out_image = models.ImageField(upload_to=f"employees images")

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendances"
        db_table = "attendances"

    def __str__(self):
        return f"{self.employee.full_name}"


