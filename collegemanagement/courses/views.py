from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Course
from .forms import CourseForm


@login_required(login_url="login")
def course_list(request):

    courses = Course.objects.all()

    return render(
        request,
        "courses/course_list.html",
        {"courses": courses}
    )


@login_required(login_url="login")
def add_course(request):

    if request.method == "POST":

        form = CourseForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Course Added Successfully."
            )

            return redirect("course_list")

    else:

        form = CourseForm()

    return render(
        request,
        "courses/add_course.html",
        {"form": form}
    )


@login_required(login_url="login")
def edit_course(request, pk):

    course = get_object_or_404(Course, pk=pk)

    if request.method == "POST":

        form = CourseForm(
            request.POST,
            instance=course
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Course Updated Successfully."
            )

            return redirect("course_list")

    else:

        form = CourseForm(instance=course)

    return render(
        request,
        "courses/edit_course.html",
        {
            "form": form,
            "course": course
        }
    )


@login_required(login_url="login")
def delete_course(request, pk):

    course = get_object_or_404(Course, pk=pk)

    if request.method == "POST":

        course.delete()

        messages.success(
            request,
            "Course Deleted Successfully."
        )

        return redirect("course_list")

    return render(
        request,
        "courses/delete_course.html",
        {"course": course}
    )


@login_required(login_url="login")
def course_detail(request, pk):

    course = get_object_or_404(Course, pk=pk)

    return render(
        request,
        "courses/course_detail.html",
        {"course": course}
    )