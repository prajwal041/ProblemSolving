from datetime import date, datetime, timedelta

import pytz
import calendar
# import datetime

from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe


class Interviewer(models.Model):
    interviewer_name = models.CharField(max_length=50, null=False, blank=False)
    interview_date_and_time = models.DateTimeField(default=timezone.now,auto_now_add=False, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'interviewer'

    def __str__(self):
        return '{}'.format(self.interviewer_name).format(self.interview_date_and_time)


class Candidate(models.Model):
    candidate_name = models.CharField(max_length=50, null=False, blank=False)
    candidate_date_and_time = models.DateTimeField(default=timezone.now,auto_now_add=False, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'candidate'

    def __str__(self):
        return '{}'.format(self.candidate_name).format(self.candidate_date_and_time)

# *****************************************************************************
# Interview
# *****************************************************************************

class Interview(models.Model):
    """
    represents a scheduled candidate interview

    """

    calendar = models.ForeignKey(
        'app.InterviewCalendar',
        blank=True,
        null=True,
        related_name='interviews',on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    candidate = models.ForeignKey('app.Candidate', blank=True, null=True,related_name='candidate',on_delete=models.CASCADE)
    interviewer = models.ForeignKey('app.Interviewer', blank=True, null=True,related_name='interviewer',on_delete=models.CASCADE)


    def __str__(self):
        return 'Interview at {}'.format(self.start_time)

# *****************************************************************************
# InterviewCalendar
# *****************************************************************************

class InterviewCalendar(models.Model):
    """
    represents an availability calendar for interview scheduling
    """

    description = models.CharField(max_length=512, blank=True, null=True)
    timezone = models.CharField(
        choices=[(zone, zone) for zone in pytz.common_timezones],
        max_length=32,
    )


    def __str__(self):
        return '{}'.format(self.description)

# *****************************************************************************
# InterviewConflict
# *****************************************************************************

class InterviewConflict(models.Model):
    """
    represents a block of time in which interviews cannot be scheduled

    """

    calendar = models.ForeignKey(
        'app.InterviewCalendar',
        related_name='conflicts', on_delete=models.CASCADE
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


# *****************************************************************************
# InterviewSlot
# *****************************************************************************

class InterviewSlot(models.Model):
    """
    represents a block of available weekday time for an interview
    """

    calendar = models.ForeignKey(
        'app.InterviewCalendar',
        related_name='slots',
    on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    monday = models.BooleanField(default=False, verbose_name='Mon')
    tuesday = models.BooleanField(default=False, verbose_name='Tue')
    wednesday = models.BooleanField(default=False, verbose_name='Wed')
    thursday = models.BooleanField(default=False, verbose_name='Thur')
    friday = models.BooleanField(default=False, verbose_name='Fri')
    saturday = models.BooleanField(default=False, verbose_name='Sat')
    sunday = models.BooleanField(default=False, verbose_name='Sun')

    max_spots = models.PositiveIntegerField(default=1)


    @property
    def local_tz(self):

        """
        returns pytz timezone for slot
        """
        return pytz.timezone(self.calendar.timezone)

