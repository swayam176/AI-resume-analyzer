from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Attendance
from .forms import AttendanceForm


@login_required(login_url="login")
def attendance_list(request):

    attendance = Attendance.objects.select_related("student").all()

    return render(
        request,
        "attendance/attendance_list.html",
        {
            "attendance": attendance
        }
    )


@login_required(login_url="login")
def add_attendance(request):

    if request.method == "POST":

        form = AttendanceForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Attendance Added Successfully."
            )

            return redirect("attendance_list")

    else:

        form = AttendanceForm()

    return render(
        request,
        "attendance/add_attendance.html",
        {
            "form": form
        }
    )


@login_required(login_url="login")
def edit_attendance(request, pk):

    attendance = get_object_or_404(
        Attendance,
        pk=pk
    )

    if request.method == "POST":

        form = AttendanceForm(
            request.POST,
            instance=attendance
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Attendance Updated Successfully."
            )

            return redirect("attendance_list")

    else:

        form = AttendanceForm(
            instance=attendance
        )

    return render(
        request,
        "attendance/edit_attendance.html",
        {
            "form": form,
            "attendance": attendance
        }
    )


@login_required(login_url="login")
def delete_attendance(request, pk):

    attendance = get_object_or_404(
        Attendance,
        pk=pk
    )

    if request.method == "POST":

        attendance.delete()

        messages.success(
            request,
            "Attendance Deleted Successfully."
        )

        return redirect("attendance_list")

    return render(
        request,
        "attendance/delete_attendance.html",
        {
            "attendance": attendance
        }
    )