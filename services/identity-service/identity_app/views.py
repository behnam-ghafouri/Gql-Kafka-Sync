from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Company

def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return JsonResponse({
        "id": company.id,
        "name": company.name,
        "domain": company.domain, # Add this line
    })