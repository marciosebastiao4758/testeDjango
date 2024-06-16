from django.urls import path
from .views import index, post_detail

urlpatterns = [    
    path("", index, name="index"),
     path("post_detail/<int:id>/", post_detail, name="post_detail"),
]
