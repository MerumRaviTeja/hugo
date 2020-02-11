from rest_framework import serializers
from attedance.db.models.library import Attendance, Employee

"""
    The ModelSerializer class provides a shortcut that lets you automatically
    create a Serializer class with fields that correspond to the Model fields.

"""


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ["id", "employee", "check_in", "check_out","ip_address", "in_field", "check_in_image","check_out_image", "created", "updated"]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "user", "full_name", "designation","phone_number","alternative_phone_number","email","id_number","dob","joining_date","is_active","created", "updated"]


