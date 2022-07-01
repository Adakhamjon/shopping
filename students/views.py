from django.shortcuts import render,redirect
from django.urls import reverse
from .models import *

def index(request):
	students = Student.objects.all()
	context = {
	"students":students
	}
	return render(request,"simpleforms/students_list.html",context)

def create(request):
	if request.method=="POST":
		name = request.POST.get("name",None)
		stage_id = request.POST.get("stage_id",None)

		stage=Stage.objects.get(id=stage_id)

		group_id = request.POST.get("group_id",None)
		group = Group.objects.get(id=group_id)

		course_id = request.POST.get("course_id",None)
		course = Course.objects.get(id=course_id)

		faculty_id = request.POST.get("faculty_id",None)
		faculty = Faculty.objects.get(id=faculty_id)

		student = Student()
		student.name = name
		student.stage = stage
		student.group = group
		student.course = course
		student.faculty = faculty
		student.save()

		return redirect(reverse("student-list"))
	stages = Stage.objects.all()
	groups = Group.objects.all()
	courses = Course.objects.all()
	faculties = Faculty.objects.all()
	context = {
	"stages":stages,
	"groups":groups,
	"courses":courses,
	"faculties":faculties
	}


	return render(request,"simpleforms/add_student.html",context)


def update(request,pk):
	students = Student.objects.filter(id=pk)
	if not students.exists():
		return redirect(reverse("student-list"))
	else:
		students = students.first()

	if request.method=="POST":
		name = request.POST.get("name",None)
		stage_id = request.POST.get("stage_id",None)

		stage=Stage.objects.get(id=stage_id)

		group_id = request.POST.get("group_id",None)
		group = Group.objects.get(id=group_id)

		course_id = request.POST.get("course_id",None)
		course = Course.objects.get(id=course_id)

		faculty_id = request.POST.get("faculty_id",None)
		faculty = Faculty.objects.get(id=faculty_id)

		students.name = name
		students.stage = stage
		students.group = group
		students.course = course
		students.faculty = faculty
		students.save()
	stages = Stage.objects.all()
	groups = Group.objects.all()
	courses = Course.objects.all()
	faculties = Faculty.objects.all()
	context = {
	"stages":stages,
	"groups":groups,
	"courses":courses,
	"faculties":faculties,
	"students":students
	}
	return render(request,"simpleforms/update_student.html",context)


def delete(request,pk):
	try:
		student = Student.objects.get(id=pk)
		student.delete()
	except Student.DoesNotExist:
		pass
	return redirect(reverse("student-list"))