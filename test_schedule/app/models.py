from django.db import models
from django.utils import timezone

class Interviewer(models.Model):
    interviewer_name = models.CharField(max_length=50, null=False, blank=False)
    interview_date_and_time = models.DateTimeField(default=timezone.now,auto_now_add=False, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'interviewer'

    def __str__(self):
        return self.interview_date_and_time

class Candidate(models.Model):
    candidate_name = models.CharField(max_length=50, null=False, blank=False)
    candidate_date_and_time = models.DateTimeField(default=timezone.now,auto_now_add=False, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'candidate'

    def __str__(self):
        return self.candidate_date_and_time
