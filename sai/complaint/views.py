from django.shortcuts import render,redirect
from .models import Complaints,Poll,Lecturer
from complaint.forms import RegistrationForm,Complaintform
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import get_object_or_404
# Create your views here.
@login_required
def view_home(request):
	c=Complaints.objects.all().order_by('-created_date')
	args={'c':c}
	return render(request,'complaint/home.html',args)

@login_required
def view_poll(request):
    c=Poll.objects.all().order_by('-created_date')
    lts = Lecturer.objects.all().distinct()
    args={'c':c,'lts':lts}
    return render(request,'complaint/add_poll.html',args)

@login_required
def give_poll(request,pk=None):
	c = get_object_or_404(Poll,pk=pk)
	return render(request,'complaint/give_poll.html',{'c':c})


@login_required
def cont(request):
	return render(request,'complaint/cont.html')

@login_required
def status(request):
    c=Poll.objects.all()
    lect = Lecturer.objects.all()
    count=0
    for x in lect:
        count = count + x.votes
    args={'c':c,'count':count,'lect':lect}
    return render(request,'complaint/poll_status.html',args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = RegistrationForm()


    return render(request,'complaint/register.html',{'form':form})

@login_required
def update_vote(request,pk=None):
    Lecturer.objects.filter(pk=pk).update(votes=F('votes')+1)
    return redirect('/add_poll/')

class HomeView(TemplateView):
	template_name = 'complaint/complaint.html'
	def get(self,request):
		comp=Complaintform()
		args={'comp':comp}
		return render(request,self.template_name,args)
	def post(self,request):
		comp=Complaintform
		if request.method== 'POST':
			comp=Complaintform(request.POST)
			if comp.is_valid():
				post=comp.save(commit=False)
				post.user = request.user
				post.save()
				title = comp.cleaned_data['title']
				description = comp.cleaned_data['description']
				category= comp.cleaned_data['category']
				comp=Complaintform(request.GET)
				return redirect('/home/')
		return render(request,self.template_name,{'title':title,'comp':comp,'description':description,'category':category})
# class pollview(TemplateView):
#     template_name = 'complaint/add_poll.html'

#     def get(self, request):
#         survey = PollForm
#         args = {'survey':survey}
#         return render(request, self.template_name,args)

#     def post(self,r
