from django.shortcuts import redirect, render
from .decorators import is_org
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
            post = models.Postings.objects.get(id=request.POST["postnum"][0])
            post.delete()
        except Exception:
            pass
        return redirect("/posts/manage_post")


def view_listings(request, location=None, techstack=None):
    if request.method == "POST":
        pass
    else:
        posts = models.Postings.objects.all()
    print(posts[0].techstack[0:15])
    print(type(posts[0].techstack))
    return render(request, "posts/view_all.html", {"posts": posts})


def filter_list(request):
    if request.method == "POST":
        print(request.POST)
        if request.POST["location"] == "" and request.POST["techstack"] == "":
            return redirect("/posts/view_listings")
        else:
            print(request.POST["location"])
            print(request.POST["techstack"])
            queryset = models.Postings.objects.all()
            queryset = queryset.filter(location__icontains=request.POST["location"])
            queryset = queryset.filter(techstack__icontains=request.POST["techstack"])
            return render(request, "posts/view_all.html", {"posts":queryset})
    else:
        return redirect("/posts/view_listings")
    

def view_post(request, num):
    if request.method == "POST":
        pass
    else:
        post = models.Postings.objects.get(id=num)
        contact = usermodel.Organization.objects.get(id=post.organization_id)
    return render(request, "posts/view_post.html", {"post":post, "contact": contact})

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
