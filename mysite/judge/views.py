from django.shortcuts import get_object_or_404, render
from .models import Problems, Solutions, TestCases


def prob_list(request):
    problem = Problems.objects.all()
    context = {
        'prob_list': problem
    }
    return render(request, "judge/prob_list.html", context)

def submit_list(request,problemss_code):
    problem =  get_object_or_404(Problems, pk=problemss_code)
    context = {
        'submit_list': problem
    }
    return render(request, "judge/submit_list.html", {'problem': problem})
