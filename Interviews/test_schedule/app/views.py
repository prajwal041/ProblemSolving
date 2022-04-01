from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import Interviewer, Candidate
from .serializers import InterviewerSerializer, CandidateSerializer
import json

class InterviewerView(viewsets.ModelViewSet):
    queryset = Interviewer.objects.all()
    serializer_class = InterviewerSerializer

class CandidateView(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

def schedule_by_FCFS(I,C):
    r = []

    for i in range(len(I)):
        b = []
        for j in range(len(C)):
            try:
                if C[i][1]==I[j][1]:
                    b.append(I[i][0])
                    r.append([C[i][0],b,C[i][1]])
                    break
            except:
                if I[i][1]==C[j][1]:
                    b.append(I[i][0])
                    if len(r[j][1])<=2:
                        r[j][1] = r[j][1] + b
                        break
    return r

class RedistributeView(APIView):
    """
    A view that returns the count of active candidates & interviewers
    if no of interviewers more than the candidates then redistribute the Interview
    then return the updated slots in JSON.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        I = []
        for i, j in Interviewer.objects.values_list('interviewer_name', 'interview_date_and_time').distinct():
            I.append([i, str(j)])

        C = []
        for i, j in Candidate.objects.values_list('candidate_name', 'candidate_date_and_time').distinct():
            C.append([i, str(j)])

        r = schedule_by_FCFS(I, C)
        # r = [['Prajwal Shetty', ['Saravaran', 'Abraham'], '2019-08-05 11:00:00+00:00'], ['Keerthan', ['Sara'], '2019-08-05 11:00:00+00:00']]
        d = []
        for i in range(len(r)):
            data = {'candidate': r[i][0], 'interviewer': r[i][1], 'interview_scheduled': r[i][2]}
            d.append(data)
        content = {'interviews': d}
        # return Response(content)
        pickup_records = json.dumps(content, indent=4)
        return HttpResponse(pickup_records, content_type="application/json")

