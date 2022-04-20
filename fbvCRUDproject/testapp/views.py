from django.shortcuts import render,redirect
from testapp.models import Student
from testapp.forms import StudentForm

# Create your views here.

def retrieve_view(request):
    stud_list=Student.objects.all()
    my_dict={'stud_list' : stud_list}
    return render(request,'testapp/retrieve.html',context=my_dict)

def create_view(request):
    form=StudentForm()
    if request.method=='POST':
        form1=StudentForm(request.POST)
        if form1.is_valid():
            form1.save()
            print('added to database..')
            return redirect('/retrieve')
    return render(request,'testapp/create.html',{'form' : form})

def delete_view(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/retrieve')


def update_view(request,id):
    student=Student.objects.get(id=id)
    if request.method=='POST':
        form1=StudentForm(request.POST,instance=student)
        if form1.is_valid():
            form1.save()
            print('added to database..')
            return redirect('/retrieve')
    return render(request,'testapp/update.html',{'student' : student})
