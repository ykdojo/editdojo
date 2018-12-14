"""editdojo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import select_languages, signup_flow
from main.views import home

# The following two lines are for CS Dojo's tutorials
from hello.views import my_view, home_view
from todo.views import todo_view, add_todo, delete_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('', home, name='home'),
    path('signup/', signup_flow),
    path('selectLanguages/', select_languages),

    # This one is for YK's hello world app tutorial: https://youtu.be/h7rvyDK70FA
    path('sayHello/', my_view),

    # These are for YK's to-do app tutorial: https://youtu.be/ovql0Ui3n_I
    path('todo/', todo_view),
    path('addTodo/', add_todo),
    path('deleteTodo/<int:todo_id>/', delete_todo),
]