# Create your views here.

from django.http import HttpResponseRedirect,HttpResponse  
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.models import *



def homeController(request):					#MainPage for the Lab.. Uploads of the files. 
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
		    pass
	    	
	    else:
		return HttpResponse('No Actions')
		
	return render_to_response('home/homePage.html',{"myUploads":myUploads},context_instance=RequestContext(request))


def downloads(request):
	reports = uploadFiles.objects.all()
	return render_to_response('home/downloads.html',{"reports": reports},context_instance=RequestContext(request))









