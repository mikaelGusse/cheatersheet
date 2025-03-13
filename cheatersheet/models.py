from django.conf import settings
from django.core.exceptions import ValidationError, FieldError
from django.db import models
from django.contrib import admin

class Course(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    key = models.CharField(
        max_length=64, unique=True, help_text="Unique alphanumeric course instance id"
    )
    name = models.CharField(max_length=255, help_text="Descriptive course name")
    provider = models.CharField(
        max_length=16,
        help_text="Provider for submission data",
    )
    objects = models.Manager()

class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    key = models.CharField(
        max_length=64, unique=True, help_text="Unique alphanumeric student id"
    )
    name = models.CharField(max_length=255, help_text="Student name")
    student_id = models.CharField(max_length=255, help_text="Student number", default="")
    aplus_id = models.CharField(max_length=255, help_text="A+ user id")
    objects = models.Manager()

class Case(models.Model):
    key = models.CharField(
        max_length=64, unique=True, help_text="Unique alphanumeric case id"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('key', 'name', 'provider', 'created')
    search_fields = ('key', 'name', 'provider')

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('key', 'course', 'created_at')
    search_fields = ('key', 'course')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('key', 'name', 'student_id', 'aplus_id', 'created')
    search_fields = ('key', 'name', 'student_id', 'aplus_id')