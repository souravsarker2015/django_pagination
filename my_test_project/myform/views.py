from django.core.paginator import InvalidPage
from django.shortcuts import render

# from django.core.paginator import Paginator
# from django.shortcuts import render
#
# from myform.models import Post
#
#
# def post_list(request):
#     post_list = Post.objects.all()
#     paginator = Paginator(post_list, 10)  # 10 posts per page
#     page = request.GET.get('page')
#     posts = paginator.get_page(page)
#     return render(request, 'pagination.html', {'posts': posts})


from django.shortcuts import render

from .models import Post
from .pagination import CustomPaginator


def my_view(request):
    objects = Post.objects.all()
    paginator = CustomPaginator(objects, 1)
    page_number = request.GET.get('page')
    try:
        page = paginator.page(page_number)
    except InvalidPage:
        page = paginator.page(1)
    return render(request, 'pagination.html', {'page': page})
