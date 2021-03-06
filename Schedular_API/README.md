# Scheduler System

## Introduction

An interview calendar contains one or more interview slot objects which define what times are available to book,
as well as the maximum number of candidates that can be booked in each slot. A calendar can also contain interview
conflicts. Interview conflicts specify a date and time range during which no interviews can be booked.

An interview can only start on the hour.

## Getting the Application Running

The scheduler is a Dockerized Django REST application. You'll need to make sure that Python and Docker are installed on
your system and correctly configured in order to run the application. The files in this package should be set up
such that once Docker is configured, you can simply run `docker-compose up --build` to rebuild and run the
application. Depending on your environment, you might need to run `docker-compose` as an administrator in order for
the container to start correctly.

If you don't already have Docker on your machine, Docker provides an [installation guide](https://docs.docker.com/engine/installation/).

If you're running Windows or MacOS X, you'll need to use `docker-machine` to set up a virtual environment that your containers can run in.

### Setting up a Superuser

Once the Docker container is up, you'll probably want to add a superuser to the application, so that you can access the
Django admin console and add calendars, interview slots, and conflicts to the database.

Make sure you made all the migrations & migrate to the database.

`sudo docker-compose run web python manage.py makemigrations app`

`sudo docker-compose run web python manage.py migrate`

To do this, first run `sudo docker-compose run web python manage.py createsuperuser` from the root of the project to get a root shell on the Docker machine.
Then it will prompt the superuser credentails.

You'll be prompted to create a username, provide an email address, and set up a password. You can choose whatever is convenient for you.

After you create the superuser, if you navigate to the `/admin` path in the application, you should be able to log in as the superuser
you created and add items to the database through Django's GUI. This will help you test your implementation.

To test application `sudo docker-compose run web python manage.py test` added few sample test cases.

## Class Documentation

There are four major important classes in this project:
`InterviewSlot`, `InterviewCalender`, `Interview`, and `InterviewConflict`.

### InterviewSlot

`InterviewSlot` represents a repeating block of available time for an interview. An interview
slot is not associated with any particular date--it is an availability from a start time of day
to an end time of day, paired with flags which indicate what day of the week it is.

Additionally, a single `InterviewSlot` may accommodate multiple concurrent `Interview`s on the same
date.

`InterviewSlot` has the following fields:

`calendar` is the `InterviewCalendar` that this `InterviewSlot` is valid on.

`start_time` is the time of day on which this `InterviewSlot` begins.
`end_time` is the time of day on which this `InterviewSlot` ends.

`monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, `sunday` are boolean flags
which represent whether this `InterviewSlot` is valid on the corresponding day of the week.

`max_spots` is the maximum number of concurrent `Interview`s that can be scheduled in this
`InterviewSlot`.

`InterviewSlot` also has two methods on it:

`InterviewSlot.local_tz()` returns the local timezone for the calendar that the `InterviewSlot`
is on.

`InterviewSlot.is_available(interview_date)` accepts a `date` as an argument, and determines
whether or not the `InterviewSlot` is currently available to be scheduled on that date.

### InterviewCalendar

An `InterviewCalendar` represents a calendar on which `Interviews` may be scheduled.
`InterviewCalendar` has the following fields:

`description` is a human-readable descripton of the `InterviewCalendar`

`timezone` is the local timezone of the calendar, which may be different from the timezone in
which it is viewed.

`InterviewCalendar` displays interview calender also has a `__str__` method for stringifying itself, which you do not need to
worry about.

### Interview

The `Interview` represents a scheduled candidate interview. It has the following fields:

`calendar` is the calendar this `Interview` appears on.

`created` is a datetime representing when the `Interview` object was created.

`start_time` is the start time of the `Interview`.

`end_time` is the end time of the `Interview`.

`candidate` is the list of available candidates enrolled  for interview.

`interviewer` is also a list of available candidates enrolled for interview process. 


### InterviewConflict

An `InterviewConflict` represents a block of time during which no interviews may be scheduled.
`InterviewConflict`s have the following fields:

`calendar` is the calendar this `InterviewConflict` appears on.

`start_time` is a datetime value that specifies the date and time at which the conflict begins.

`end_time` is a datetime value that specifies the date and time at which the conflict ends.

An `InterviewSlot` is considered to be unavailable during an `InterviewConflict` if they overlap at
all, no matter how much or how little time the overlap encompasses.

## Handling Erroneous request
This System is capable of many user erroneous requests,

`interview duration` should be 1 hour(endtime - starttime)

`end_time` should lesser than or equal to `start_time`

You can't book the already assigned slots.
You can only book in the designated slots of days which you created in `InterviewCalender`

## APIs
This is an alpha version of scheduling APIs
Endpoints:

`calendars` will display the list of calender events

`interviews` will display the set of assigned interviews

`interviewer` interviewer can book the slots independently

`candidate` similarly candidates can book the slots independently

`matching_slots` displays the matching slots between interviewer & candidates.