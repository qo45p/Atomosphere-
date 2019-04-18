from django.shortcuts import render,redirect

def questions(request):
	if 'userSessionID' not in request.session:
		return redirect("https://www.atmoscareplus.com/");
	return render(request,'questions.html',{})
