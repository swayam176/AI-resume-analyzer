from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Student
from .forms import StudentForm


@login_required(login_url="login")
def student_list(request):
    students = Student.objects.all().order_by("student_id")

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )


@login_required(login_url="login")
def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            messages.success(request, "Student Added Successfully.")

            return redirect("student_list")

    else:

        form = StudentForm()

    return render(
        request,
        "students/add_student.html",
        {"form": form}
    )


@login_required(login_url="login")
def edit_student(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():

            form.save()

            messages.success(request, "Student Updated Successfully.")

            return redirect("student_list")

    else:

        form = StudentForm(instance=student)

    return render(
        request,
        "students/edit_student.html",
        {
            "form": form,
            "student": student
        }
    )


@login_required(login_url="login")
def delete_student(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":

        student.delete()

        messages.success(request, "Student Deleted Successfully.")

        return redirect("student_list")

    return render(
        request,
        "students/delete_student.html",
        {"student": student}
    )


@login_required(login_url="login")
def student_detail(request, pk):

    student = get_object_or_404(Student, pk=pk)

    return render(
        request,
        "students/student_detail.html",
        {"student": student}
    )