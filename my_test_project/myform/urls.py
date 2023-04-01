from django.urls import path

from myform.views import my_view

urlpatterns = [
    # path('test', post_list, name='posts'),
    path('test', my_view, name='posts'),
    # path('chk111111/', admin.site.urls),
]
