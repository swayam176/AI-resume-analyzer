from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Faculty
from .forms import FacultyForm


@login_required(login_url="login")
def faculty_list(request):

    faculty = Faculty.objects.all()

    return render(
        request,
        "faculty/faculty_list.html",
        {"faculty": faculty}
    )


@login_required(login_url="login")
def add_faculty(request):

    if request.method == "POST":

        form = FacultyForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Faculty Added Successfully."
            )

            return redirect("faculty_list")

    else:

        form = FacultyForm()

    return render(
        request,
        "faculty/add_faculty.html",
        {"form": form}
    )


@login_required(login_url="login")
def edit_faculty(request, pk):

    faculty = get_object_or_404(Faculty, pk=pk)

    if request.method == "POST":

        form = FacultyForm(
            request.POST,
            request.FILES,
            instance=faculty
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Faculty Updated Successfully."
            )

            return redirect("faculty_list")

    else:

        form = FacultyForm(instance=faculty)

    return render(
        request,
        "faculty/edit_faculty.html",
        {
            "form": form,
            "faculty": faculty
        }
    )


@login_required(login_url="login")
def delete_faculty(request, pk):

    faculty = get_object_or_404(Faculty, pk=pk)

    if request.method == "POST":

        faculty.delete()

        messages.success(
            request,
            "Faculty Deleted Successfully."
        )

        return redirect("faculty_list")

    return render(
        request,
        "faculty/delete_faculty.html",
        {"faculty": faculty}
    )


@login_required(login_url="login")
def faculty_detail(request, pk):

    faculty = get_object_or_404(Faculty, pk=pk)

    return render(
        request,
        "faculty/faculty_detail.html",
        {"faculty": faculty}
    )