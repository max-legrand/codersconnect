from django.shortcuts import redirect, render
from .decorators import is_org, is_user
from . import forms
from . import models
from users import models as usermodel
# Create your views here.
# def is_organization(func):
#     def wrapper(request):
#         user = request.user
#         if user.organization:
#             func(request)
#         else:
#             return render(request, "home")
@is_org
def delete_post(request):
    if request.method == "POST":
        print(request.POST)
        try:
            post = models.Postings.objects.get(id=request.POST["postnum"])
            cnct = models.Connection.objects.all().filter(post=post)
            for c in cnct:
                c.delete()
            post.delete()
        except Exception:
            pass
        return redirect("/posts/manage_post")


def view_listings(request, location=None, techstack=None):
    if request.method == "POST":
        pass
    else:
        posts = models.Postings.objects.all().filter(status=True)
    #print(posts[0].techstack[0:15])
    #print(type(posts[0].techstack))
    return render(request, "posts/view_all.html", {"posts": posts})


def filter_list(request):
    if request.method == "POST":
        print(request.POST)
        if len(request.POST.getlist("location[]")) == 0 and len(request.POST.getlist("techstack[]")) == 0:
            return redirect("/posts/view_listings")
        else:
            locationList = request.POST.getlist("location[]")
            techList = request.POST.getlist("techstack[]")
            queryset = models.Postings.objects.all().filter(status=True)
            resultset = []
            for location in locationList:
                resultset += queryset.filter(location__icontains=location)
            for techstack in techList:
                resultset += queryset.filter(techstack__icontains=techstack)
            return render(request, "posts/view_all.html", {"posts":resultset})
    else:
        return redirect("/posts/view_listings")
    

def view_post(request, num):
    if request.method == "POST":
        pass
    else:
        post = models.Postings.objects.get(id=num)
        contact = usermodel.Organization.objects.get(id=post.organization_id)
    return render(request, "posts/view_post.html", {"post":post, "contact": contact, "skillslist": post.techstack.split(', ')})

@is_org
def edit_post(request, num):
    if request.method == "POST":
        print("POST")
        print(request.POST)
        form = forms.CreatePost(data=request.POST)
        if form.is_valid():
            post = models.Postings.objects.get(id=num)
            post.title = form.cleaned_data["title"]
            post.description = form.cleaned_data["description"]
            post.location = form.cleaned_data["location"]
            post.techstack = form.cleaned_data["techstack"]
            post.save()
            print("SAVED")
            return redirect("/posts/manage_post")
    else:
        print(num)
        try:
            post = models.Postings.objects.get(id=num)
        except Exception as e:
            print("EMPTY")
            return redirect("/posts/manage_post")
        if post.organization_id != request.user.organization.id:
            print("not mine")
            return redirect("/posts/manage_post")
        form = forms.CreatePost(instance=post)
    return render(request, "posts/edits_post.html", {"form":form,"number":num})


@is_org
def manage_posts(request):
    print("enter")
    entries = models.Postings.objects.all().filter(organization_id=request.user.organization.id)
    print(entries)
    return render(request, "posts/manage_posts.html", {"entries": entries})

@is_org
def create_post(request):
    # user = request.user
    # if user.organization:
    #     return render(request, "posts/create_post.html")
    # else:
    #     return render(request, "home")
    if request.method == "POST":
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            print ("POST")
            post = form.save(commit=False)
            print(post.title)
            user = request.user.organization
            post.techstack = post.techstack.replace("'", "").replace("[","").replace("]","")

            print(request.user.username)
            print(request.user.organization.organization_name)
            post.organization = user
            print(post)
            post.save()
            return redirect('home')
    #      # form = UserCreationForm(request.POST)
    #     # form2 = forms.CreateOrg(request.POST)
    #     # if form.is_valid() and form2.is_valid():
    #     #     user = form.save(commit=False)
    #     #     orgform = form2.save(commit=False)
    #     #     user.save()
    #     #     orgform.user = user
    #     #     orgform.save()
    #     #     login(request, user)
    #     #     return redirect('home')
    else:
        form = forms.CreatePost()
    return render(request, "posts/create_post.html", {"form": form})

@is_user
def apply(request):
    if request.method == "POST":
        try:
            num = int(request.POST['num'])
            post = models.Postings.objects.get(id=num)
            post.applicants+=1
            post.save()
            cnct = models.Connection(post=post, accept_user=request.user.extendeduser, status=0)
            cnct.save()
        except Exception as e:
            print(e)
            pass
        pass
    else:
        pass
    return redirect('/posts/view_jobs')

@is_user
def view_jobs(request):
    if request.method == "GET":
        user = request.user
        jobs = models.Connection.objects.all().filter(accept_user=user.extendeduser, accepted=False)
        #filterd_list = jobs.filter(user__exact=user.extendeduser)
    else:
        return redirect('home')
        pass
    return render(request, 'posts/view_jobs.html', {"user": user, "jobs": jobs})

@is_user
def withdraw(request):
    if request.method == "POST":
        num = int(request.POST['num'])
        cnct = models.Connection.objects.get(id=num)
        cnct.post.applicants-=1
        cnct.post.save()
        cnct.delete()
    else:
        return redirect('home')
    return redirect('/posts/view_jobs')

@is_user
def statusChange(request):
    if request.method == "POST":
        num = int(request.POST['num'])
        cnct = models.Connection.objects.get(id=num)
        if request.POST['status'] == 'accept':
            cnct.accepted = True
            cnct.save()
        elif request.POST['status'] == 'reject':
            cnct.post.applicants -= 1
            cnct.post.save()
            cnct.delete()
        else:
            pass
    else:
        pass
    return redirect('/posts/view_jobs')
@is_org
def view_applicants(request,num):
    if request.method == "GET":
        post = models.Postings.objects.get(id=num)
        applicants = models.Connection.objects.all().filter(post=post, status=0)
        try:
            return render(request, 'posts/view_applicants.html', {"applicants": applicants, "post": post})
        except Exception as e:
            print(e)
            return redirect('/posts/manage_post')
    else:
        return redirect('home')
@is_org
def status_applicant(request):
    if request.method == "POST":
        id = int(request.POST['num'])
        status = request.POST['status']
        cnct = models.Connection.objects.get(id=id)
        if status == 'accept':
            cnct.status = 2
            cnct.post.applicants-=1
            cnct.post.save()
            cnct.save()
        elif status == 'reject':
            cnct.status = 1
            cnct.post.applicants -= 1
            cnct.post.save()
            cnct.save()
        else:
            pass
    else:
        return redirect('home')
    applicants = models.Connection.objects.all().filter(post=cnct.post, status=0)
    return render(request, 'posts/view_applicants.html', {'applicants': applicants, 'post': cnct.post})

@is_user
def view_jobs_accepted(request):
    if request.method == "GET":
        user = request.user.extendeduser
        try:
            jobs_accepted = models.Connection.objects.all().filter(accept_user=user, accepted=True)
            return render(request, 'posts/view_jobs_accepted.html', {'jobs': jobs_accepted})
        except Exception as e:
            print(e)
            return redirect('home')
    else:
        return redirect('home')

@is_org
def view_connections(request):
    if request.method == "GET":
        org = request.user.organization
        posts = models.Postings.objects.all().filter(organization=org)
        connections = []
        allCnct = models.Connection.objects.all()
        for post in posts:
            connections+= allCnct.filter(post=post, accepted=True)

        return render(request, 'posts/view_connections.html', {'connections': connections})
    else:
        return redirect('home')

@is_org
def status_connection(request):
    if request.method == "POST":
        id = int(request.POST['num'])
        status = request.POST['status']
        cnct = models.Connection.objects.get(id=id)
        if status == 'delete':
            cnct.delete()
        else:
            pass
    else:
        return redirect('home')
    return redirect('/posts/view_connections')

@is_org
def close_listing(request):
    if request.method == "POST":
        id = request.POST['num']
        post = models.Postings.objects.get(id=id)
        post.status = False
        post.save()
    return redirect('/posts/manage_post')

@is_org
def open_listing(request):
    if request.method == "POST":
        id = request.POST['num']
        post = models.Postings.objects.get(id=id)
        post.status = True
        post.save()
    return redirect('/posts/manage_post')