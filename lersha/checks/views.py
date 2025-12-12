from django.shortcuts import render
from django.http.response import HttpResponse

def chapa(request):
    return render(request, 'checks/check.html')

posts = 0
returns = 0
def chapa_callback_url_reciever(request):
    global posts
    if request.method == 'POST':
        posts = request
    return HttpResponse(posts)

def chapa_return_reciever(request):
    global returns
    if request.method == 'POST':
        returns = request
    return HttpResponse(returns)