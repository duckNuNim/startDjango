"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('books/',views.BookListView.as_view(), name='books'),
    path('book/<int:pk>',views.BookDetailView.as_view(),name='book-detail'),
    path('authors/',views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',views.AuthorDetailView.as_view(),name='author-detail'),
    path('add/bmi/',views.addbmi, name='addBmi'),
    path('add/addConbmi/',views.addConbmi,name = 'addCon'),
    # path('add/bmiResult/',views.bmiResult, name='bmiResult'),
    path('bmis/',views.BmiListView.as_view(), name='bmis'),
    path('bmi/<int:pk>',views.BmiDetailView.as_view(),name='bmi-detail'),
]