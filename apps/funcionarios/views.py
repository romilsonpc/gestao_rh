from django.http import HttpResponse
from django.shortcuts import render


def home(requests):
    return HttpResponse('Ola')