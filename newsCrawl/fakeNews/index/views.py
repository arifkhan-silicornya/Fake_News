from django.shortcuts import render

# Create your views here.
def index(request):
    data = {'d' : "Copy a NEWS and paste it."}
    return render(request,'index.html',data)