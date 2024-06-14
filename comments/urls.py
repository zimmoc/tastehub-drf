from django.urls import path
from comments.views import CommentDetail, CommentList

urlpatterns = [
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>', CommentDetail.as_view()),
]