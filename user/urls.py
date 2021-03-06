from django.urls import path
from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('editprofile', views.user_update, name='editprofile'),
    path('changepassword', views.change_password, name='changepassword'),
    path('comments', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservationdetail/<int:id>', views.reservationdetail, name='reservationdetail'),
    # path('addcomment/<int:id>', views.addcomment, name='addcomment'),

    # ex: /home/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /home/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /home/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]