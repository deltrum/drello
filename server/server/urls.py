from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/api/', include('todos.urls')),
    path('users/api/', include('users.urls')),
]
