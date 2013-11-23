# Create your views here.

from django.http import HttpResponseRedirect,HttpResponse  
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from labLogin.models import *


def loginUser(request):
	next= request.GET.get('next','')
	if request.method == "POST":
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		
		print username + password
		try:
			admin = User.objects.get(username=username)
		except:
			print "error"
			return render_to_response('login/login.html',{"error":"Please enter valid username and password"},context_instance=RequestContext(request))
		print admin.username
		user =  authenticate(username=username, password=str(password))	#check for authentication
			
      		if user is not None:
		      if user.is_active:
               		login(request, user)
               		return HttpResponseRedirect('/homePage/')
			
		else:
			return render_to_response('login/login.html',{"error":"Please enter valid username and password"},context_instance=RequestContext(request))
	return render_to_response('login/login.html',context_instance=RequestContext(request))



def logoutUser(request):
    # Log users out and re-direct them to the main page.
    logout(request)
    return HttpResponseRedirect('/login/')



@login_required
def labHome(request):					#MainPage for the Lab.. Uploads of the files. 
	
	
	if request.method == "GET":			#if get method used the perform delete operation
		
		if request.GET.get('del','')=='true':
			labToDelete = subLabs.objects.all()
			
			deleteId = request.GET.get('id','')

			print labToDelete
			if labToDelete == 'none':		#Handle the error
				pass			

			for lab in labToDelete:
				if lab.id == int(deleteId):
					lab.delete()
					break
			return HttpResponse("Lab deleted")
	

	labs = subLabs.objects.all()				#get all the labs in '>>labs'
	userDetails = User.objects.get(username=request.user)   #get all the current logged user
	myUploads = uploadFiles.objects.all()

	if request.method =="POST":
	    if request.POST.get('factor','') == "formUpload":		#Upload query
		print request.POST.get('branchValue','')
		if request.FILES:
			print request.FILES['upl']
			up = uploadFiles(upFiles = request.FILES['upl'],upBranch=request.POST.get('branchValue',''))
			up.save()
	    elif request.POST.get('factor','') == "formAddLabs":	#Add labs query
		
		post = request.POST
		sublab = subLabs(labName=post.get('name',''),labType=post.get('type',''),labLocation=post.get('address',''),labContact=post.get('contact',''),labEmail=post.get('email',''),adminUsername=post.get('adminName',''),adminPassword=post.get('adminPass',''))
		sublab.save()
	    elif request.POST.get('factor','') == "formEditAccount":		#Edit accounts query
		user = User.objects.get(username=request.user)
		user.username = request.POST.get('username','')
		user.set_password(request.POST.get('password',''))
		user.first_name = request.POST.get('labName','')
		user.email = request.POST.get('email','')
		user.save()
		
	    else:
		return HttpResponse(' hey ')
		
	return render_to_response('labHome/homePage.html',{"labs" : labs,"userDetails": userDetails,"myUploads":myUploads},context_instance=RequestContext(request))


def downloads(request):
	reports = uploadFiles.objects.all()
	return render_to_response('labHome/downloads.html',{"reports": reports},context_instance=RequestContext(request))




"""
def addLab(request):
	if request.method =="POST":
		post = request.POST
		sublab = subLabs(labName=post.get('name',''),labType=post.get('type',''),labLocation=post.get('address',''),labContact=post.get('contact',''),labEmail=post.get('email',''),adminUsername=post.get('adminName',''),adminPassword=post.get('adminPass',''))
		sublab.save()
	return render_to_response('labHome/addLab.html',context_instance=RequestContext(request))


def upload(request):
	if request.method =="POST":
		if request.FILES:
			print "hai files"
			print request.FILES['upl']
			up = uploadFiles(upFiles = request.FILES['upl'])
			up.save()
		else:
			print "none"

	if request.method == "GET":
		print "get"	
	
	return render_to_response('labHome/uploads.html',context_instance=RequestContext(request))

"""





