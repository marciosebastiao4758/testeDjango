from django.urls import path
from .views import index, post_detail, save_form

urlpatterns = [    
    path("", index, name="index"),
     path("post_detail/<int:id>/", post_detail, name="post_detail"),
     path("save_form/", save_form, name="save_form")
]
