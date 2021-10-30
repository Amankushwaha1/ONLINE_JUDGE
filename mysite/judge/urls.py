from django.urls import path
from .views import prob_list
from  .views import submit_list

urlpatterns = [
    path('', prob_list),
    path('char<problemss_code>/', submit_list)
]
