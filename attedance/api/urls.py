from django.urls import path
from .views.library import EmployeeList, EmployeeDetail, AttendanceList, AttendanceDetail
# Create your urls here.

urlpatterns = [
    path("employees/", EmployeeList.as_view()),
    path("employees/<int:pk>/", EmployeeDetail.as_view()),
    path("attendances/", AttendanceList.as_view()),
    path("attendances/<int:pk>/", AttendanceDetail.as_view()),
]
