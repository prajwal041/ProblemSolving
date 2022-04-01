from rest_framework import serializers
from .models import Interviewer, Candidate

# class InterviewSerializer(serializers.HyperlinkedModelSerializer):
# #     class Meta:
# #         model = Interview
# #         fields = '__all__'

class InterviewerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interviewer
        fields = '__all__'

class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'