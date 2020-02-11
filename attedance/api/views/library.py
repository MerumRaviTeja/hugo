from ..serializers.library import EmployeeSerializer, AttendanceSerializer
from ...db.models.library import Attendance, Employee
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeeList(APIView):
    """
    A view for viewing and posting catalog.
    """

    def get(self, request):
        """
        Return a list of all catalogs.
        """
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a catalog.
        """
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    """
    Retrieve, update or delete a catalog
    """

    def get_object(self, pk):
        """
        Return catalog object if pk value present.
        """
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return catalog.
        """
        employee = self.get_object(pk)

        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update catalog.
        """
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete catalog.
        """
        employee = self.get_object(pk)
        employee.delete()
        return Response(
            {"message": "Delete Success"}, status=status.HTTP_204_NO_CONTENT
        )


class AttendanceList(APIView):
    """
    A view for viewing and posting catalog.
    """

    def get(self, request):
        """
        Return a list of all catalogs.
        """
        queryset = Attendance.objects.all()
        serializer = AttendanceSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a catalog.
        """
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttendanceDetail(APIView):
    """
    Retrieve, update or delete a catalog
    """

    def get_object(self, pk):
        """
        Return catalog object if pk value present.
        """
        try:
            return Attendance.objects.get(pk=pk)
        except Attendance.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return catalog.
        """
        attendance = self.get_object(pk)

        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update catalog.
        """
        attendance = self.get_object(pk)
        serializer = AttendanceSerializer(attendance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete catalog.
        """
        attendance = self.get_object(pk)
        attendance.delete()
        return Response(
            {"message": "Delete Success"}, status=status.HTTP_204_NO_CONTENT
        )