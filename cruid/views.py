from django.shortcuts import render , redirect
from .models import student
from django.views import View 
from .form import AddStudentForm

# Create your views here.

class home(View):
    def get(self, request):
        stu_data = student.objects.all()
        return render(request,'C:/Users/abhishek/Desktop/my/template/parc3.html', {'student':stu_data } )


class Add_Student(View):
    def get(self, request):
        fm = AddStudentForm()
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
          return render(request, 'C:/Users/abhishek/Desktop/my/template/form.html', {'form':fm})

    def post(self, request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
          fm.save()
          return redirect('/')
        else:
          return render(request, 'C:/Users/abhishek/Desktop/my/template/form.html', {'form':fm})
        
class Delete_Student(View):
    def post(self, request):
        uniq_id = request.POST.get('uniq_id')

        studata = student.objects.get(uniq_id=uniq_id)
        studata.delete()

        return redirect('ho')

class editstudent(View):
   def get(self, request):
      stu = student.object.get(roll_no=roll_no)
      fm = AddStudentForm(instance=stu)
      return render(request, 'C:/Users/abhishek/Desktop/my/template/form.html', {'form':fm})

   def post(self, request):
      stu = student.object.get(id=id)
      fm = AddStudentForm(request.POST, instance=stu)
      if fm.is_valid():
         fm.save()
         return redirect('ho')