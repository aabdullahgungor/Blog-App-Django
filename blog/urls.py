from django.urls import path # we must add this for using "path()" method
from . import views


urlpatterns = [
    path("", views.index),
    path("index", views.index),
    path("blogs", views.blogs),
    path("blog/<int:id>", views.blog_details), # After "blog" comes a variable int value. We named this variable "id". The method will  #wait for the parameter with this name.
    
]
