from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def home(request):
    my_data = {"name": "John Doe"}
    return Response(my_data, status=status.HTTP_200_OK)
