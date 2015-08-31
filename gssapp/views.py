from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from gssapp.models import Msg
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.

def index(request):
	if request.method == 'GET':
		a = Msg.objects.all().order_by('date').reverse()
		context ={'msgs':a}
		return render(request,'gssapp/index.html',context)
	elif request.method == 'POST':
		t = request.POST.get("msg", "")
		a = Msg(text=t,date=timezone.now())
		a.save()
		return redirect('/')

# Create your views here.
