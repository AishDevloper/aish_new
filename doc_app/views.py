from django.shortcuts import render

# Create your views here.
def ShowView(request):
    template_name = 'doc_app/thank.html'
    return render(request, template_name, {})