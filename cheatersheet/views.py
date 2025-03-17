from django.http import HttpResponse
from django.template import loader

from cheatersheet.models import Course, Case, DataBlock, Student
from cheatersheet.forms import CaseDataBlockForm

def home(request):
    template = loader.get_template("home.html")
    context = {"courses": Course.objects.all()}
    return HttpResponse(template.render(context, request))

def course(request, course_id):
    template = loader.get_template("course.html")
    course = Course.objects.get(pk=course_id)
    context = { "cases": Case.objects.all(), "students": Student.objects.all(), "course": course }
    return HttpResponse(template.render(context, request))

def case(request, case_id):
    template = loader.get_template("case.html")
    case = Case.objects.get(pk=case_id)
    data_blocks = DataBlock.objects.all().filter(case=case)
    context = { "case": case, "form": CaseDataBlockForm(instance=case), "data_blocks": data_blocks }
    return HttpResponse(template.render(context, request))

def save_case_data_block(request, case_id):
    case = Case.objects.get(pk=case_id)
    template = loader.get_template("case.html")
    data_blocks = DataBlock.objects.all().filter(case=case)
    context = { "case": case, "form": CaseDataBlockForm(instance=case), "data_blocks": data_blocks }

    if request.method == 'POST':
        form = CaseDataBlockForm(request.POST, instance=case)
        if form.data["data_type"] == 0:
            data = { "text": form.data["data"] }
        else:
            data = { "code": form.data["data"] }
        new_data_block = DataBlock(
            key=form.data["key"],
            case=case,
            data_type=form.data["data_type"],
            data=data)
        new_data_block.save()
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))