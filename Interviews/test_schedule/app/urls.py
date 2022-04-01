from django.urls import path, include
from django.conf.urls import url
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('interviewer', views.InterviewerView)
router.register('candidate', views.CandidateView)
# router.register('scheduled', views.RedistributeView)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^interview/$', views.RedistributeView.as_view(),name='interview'),
]
