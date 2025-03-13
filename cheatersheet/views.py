from django.http import HttpResponse
from django.template import loader

from cheatersheet.models import Course, Case, Student

def home(request):
    template = loader.get_template("home.html")
    context = {"courses": Course.objects.all()}
    return HttpResponse(template.render(context, request))

def course(request, course_id):
    template = loader.get_template("course.html")
    course = Course.objects.get(pk=course_id)
    context = { "cases": Case.objects.all(), "students": Student.objects.all(), "course": course }
    return HttpResponse(template.render(context, request))