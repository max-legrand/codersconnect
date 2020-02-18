from django.shortcuts import render
from .decorators import is_org

# Create your views here.
# def is_organization(func):
#     def wrapper(request):
#         user = request.user
#         if user.organization:
#             func(request)
#         else:
#             return render(request, "home")


@is_org
def create_post(request):
    # user = request.user
    # if user.organization:
    #     return render(request, "posts/create_post.html")
    # else:
    #     return render(request, "home")
    return render(request, "posts/create_post.html")
