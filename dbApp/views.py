from django.shortcuts import render, redirect

from dbApp.forms import StudentForm, Teacherform
from .models import Students, Teachers

# Create your views here.
student_data = Students.objects.all()
teacher_data = Teachers.objects.all()


def homePage(request):
    return render(
        request,
        "pages/homePage.html",
        {"student_data": student_data, "teacher_data": teacher_data},
    )


def createStudent(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("homePage")
    context = {"form": form}
    return render(request, "pages/addStudent.html", context)


def updateStudent(request, pk):
    student = Students.objects.get(unique_id=pk)
    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("homePage")
    context = {"form": form}
    return render(request, "pages/addStudent.html", context)


def deleteStudent(request, pk):
    student = Students.objects.get(unique_id=pk)
    if request.method == "POST":
        student.delete()
        return redirect("homePage")
    context = {"object": student}
    return render(request, "pages/delete-template.html", context)


def viewStudent(request, pk):
    student = Students.objects.get(unique_id=pk)
    context = {"student": student}
    return render(request, "pages/view_student.html", context)


def createTeacher(request):
    form = Teacherform()

    if request.method == "POST":
        form = Teacherform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("homePage")
    context = {"form": form}
    return render(request, "pages/addTeacher.html", context)


def updateTeacher(request, pk):
    teacher = Teachers.objects.get(id=pk)
    form = Teacherform(instance=teacher)

    if request.method == "POST":
        form = Teacherform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homePage")
    context = {"form": form}
    return render(request, "pages/addTeacher.html", context)


def deleteTeacher(request, pk):
    teacher = Teachers.objects.get(id=pk)
    if request.method == "POST":
        teacher.delete()
        return redirect("homePage")
    context = {"object": teacher}
    return render(request, "pages/delete-template.html", context)
