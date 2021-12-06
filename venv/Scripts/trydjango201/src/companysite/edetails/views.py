from django.shortcuts import render
from .forms import EmployeeForm
from .models import dept,employee
from django.shortcuts import render
# Create your views here.

def emp_create(request):
    obj = EmployeeForm()
    template_name = "edetails/employee_create.html"
    context = {"form": obj}
    if request.method == "POST":
        qs = EmployeeForm(request.POST)
        if qs.is_valid():
            qs.save()
            qs = EmployeeForm()
            return render(request, template_name, context)
        #employee.objects.create(request.cleaned_data())
    return render(request,template_name,context)

