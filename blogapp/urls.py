from django.urls import path
from . import views

urlpatterns=[
    path('<int:blog_id>',views.detail,name='detail'),
    path('new/', views.new,name='new'),
    path('create/', views.create,name="create"),
    path('delete/<int:blog_id>', views.delete,name="delete"),
    path('search/',views.search,name="search"),
    path('update/<int:blog_id>', views.update, name="update"),

]   