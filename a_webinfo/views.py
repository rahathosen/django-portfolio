from django.shortcuts import render

def about_view(request):
    title = "About"
    return render(request,'about.html',{'title': title,})

