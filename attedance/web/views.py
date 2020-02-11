from django.shortcuts import render,redirect
from django.core.files import File
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from ..db.models.library import Attendance, Employee
import datetime
import base64


@login_required(login_url='/accounts/login/')
def home(request):
    try:
        details = Employee.objects.get(user_id=request.user)
    except:
        return HttpResponse("Contact HR to fill your details thank you!")
    validating = details.attendances.filter(employee=details).last()
    try:
        if validating.check_in.date() == datetime.date.today() and validating.check_out:

            notify = {"check_in":validating.check_in,"check_out":validating.check_out,"check_in_image":validating.check_in_image}
            return render(request, 'check_out_page.html',{"notify":notify})
        if validating.check_in.date() == datetime.date.today():
            return render(request, 'home.html',{'a': validating})
        return render(request, 'home.html')
    except:
        return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def check_in_page(request):
        employee_instance = Employee.objects.get(user=request.user)
        try:
            str_obj = request.POST.get("imgSrc").partition(",")[2]
            padding = len(str_obj) % 4
            str_obj += "=" * padding
            date_time=str(datetime.datetime.now().strftime("%Y-%m-%d %H:hr %M:min %Ssec"))
            with open(f"{request.user}.png", "wb") as fh:
                fh.write(base64.b64decode(str_obj))


            saving =Attendance.objects.create(employee=employee_instance,check_in=datetime.datetime.now(),ip_address="43.228.93.193",in_field=True,check_in_image="")
            saving.check_in_image.save(f"{request.user}' '{date_time}.png", File(open(f"/hugo/attedance/{request.user}.png", "rb")))

            return redirect(check_out_redirect)
        except:
            return redirect(home)





@login_required(login_url='/accounts/login/')
def check_out_redirect(request):
    try:
        details = Employee.objects.get(user=request.user)
        validating = details.attendances.filter(employee=details).last()
        if validating.check_in.date() == datetime.date.today():
            return render(request, "check_in_redirect.html")
        else:
            return redirect(home)
    except:
        return redirect(home)

@login_required(login_url='/accounts/login/')
def check_out_page(request):
        details = Employee.objects.get(user=request.user)
        saving = details.attendances.filter(employee=details).last()
        return render(request, 'home.html', {'a': saving})

@login_required(login_url='/accounts/login/')
def check_out(request):
        try:
            str_obj = request.POST.get("imgSrc").partition(",")[2]
        except:
            return redirect(home)
        padding = len(str_obj) % 4
        str_obj += "=" * padding
        date_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:hr %M:min %Ssec"))
        with open(f"{request.user}.png", "wb") as fh:
            fh.write(base64.b64decode(str_obj))
        details = Employee.objects.get(user=request.user)

        saving = details.attendances.filter(employee=details).last()
        saving =Attendance.objects.get(id=saving.id)
        saving.check_out = datetime.datetime.now()
        saving.check_out_image.save(f"{request.user}' '{date_time}.png", File(open(f"/hugo/attedance/{request.user}.png", "rb")))
        return render(request, 'check_out_page.html')
