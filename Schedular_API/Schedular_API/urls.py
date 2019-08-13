# *****************************************************************************
# scheduler_api/urls.py
# *****************************************************************************

from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from rest_framework.routers import SimpleRouter, DefaultRouter

from app import views

# *****************************************************************************
# urlpatterns
# *****************************************************************************

router = SimpleRouter()
router.register(r'calendars', views.InterviewCalendarViewSet)
router.register(r'interviews', views.InterviewViewSet)
router.register('interviewer', views.InterviewerView)
router.register('candidate', views.CandidateView)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^matching_slots/$', views.RedistributeView.as_view(),name='interview'),

    # url(r'^admin/', include(admin.site.urls)),
]
