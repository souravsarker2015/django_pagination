from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myform.urls')),
    # path('chk111111/', admin.site.urls),
]
