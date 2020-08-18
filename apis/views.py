from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def base_view(request):
    return render(request, 'base.html', {})