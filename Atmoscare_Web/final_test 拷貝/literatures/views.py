from django.shortcuts import render,redirect

def literatures(request):
	if 'userSessionID' not in request.session:
		return redirect("http://www.atmoscareplus.com/");
	return render(request,'literatures.html',{})
