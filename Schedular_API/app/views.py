# *****************************************************************************
# companies/views.py
# *****************************************************************************

from django.shortcuts import get_object_or_404
from django.shortcuts import render, HttpResponse
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json
from .serializers import InterviewerSerializer, CandidateSerializer
from .models import (
    InterviewCalendar,
    Interview, Interviewer, Candidate
)

from .serializers import (
    InterviewCalendarSerializer,
    InterviewSerializer
)


class InterviewerView(viewsets.ModelViewSet):
    queryset = Interviewer.objects.all()
    serializer_class = InterviewerSerializer

class CandidateView(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class RedistributeView(APIView):
    """
    A view that returns the count of active candidates & interviewers
    if no of interviewers more than the candidates then redistribute the Interview
    then return the updated slots in JSON.
    """
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        interviewers = Interviewer.objects.values_list('interviewer_name').distinct()
        candidates = Candidate.objects.values_list('candidate_name').distinct()
        time_slot = Interviewer.objects.values_list('interview_date_and_time').intersection(Candidate.objects.values_list('candidate_date_and_time'))
        data = {'candidates': candidates, 'interviewers': interviewers, 'matching_time_slot': list(time_slot)}
        content = {'interviews': data}
        return Response(content)
        # pickup_records = json.dumps(content, indent=4)
        # return HttpResponse(pickup_records, content_type="application/json")



# *****************************************************************************
# InterviewCalendarViewSet
# *****************************************************************************

class InterviewCalendarViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):

    """
    a ViewSet to list and retrieve InterviewCalendars

    """

    serializer_class = InterviewCalendarSerializer
    queryset = InterviewCalendar.objects.all()

    def get_serializer_context(self):

        """
        adds start and end dates to generate available interview times

        """

        start_date = self.request.query_params.get('startDate', None)
        end_date = self.request.query_params.get('endDate', None)

        return {
            'start_date': start_date,
            'end_date': end_date,
        }

# *****************************************************************************
# InterviewViewSet
# *****************************************************************************

class InterviewViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):

    """
    a ViewSet to list Interviews

    """

    serializer_class = InterviewSerializer
    queryset = Interview.objects.all()

    def perform_create(self, serializer):

        """
        add application to serializer for save

        """

        return serializer.save()
