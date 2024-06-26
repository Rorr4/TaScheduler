from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.
class UserTable(models.Model):
    # Fields
    firstName = models.CharField(max_length=30, blank=True, null=True)
    lastName = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, unique=False, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    userType = models.CharField(max_length=20, blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)


class CourseTable(models.Model):
    # Fields
    courseName = models.CharField(max_length=30)
    time = models.CharField(max_length=30, blank=True, null=True)


class UserCourseJoinTable(models.Model):
    # Relationship Fields
    courseId = models.ForeignKey(
        CourseTable,
        on_delete=models.CASCADE,
    )
    userId = models.ForeignKey(
        UserTable,
        on_delete=models.CASCADE,
    )


class SectionTable(models.Model):
    # Fields
    name = models.CharField(max_length=30)
    time = models.CharField(max_length=30, blank=True, null=True)

    courseId = models.ForeignKey(
        CourseTable,
        on_delete=models.CASCADE,
    )

class LabTable(models.Model):
    # Fields
    sectionNumber = models.CharField(max_length=30)
    time = models.CharField(max_length=30, blank=True, null=True)
    section = models.ForeignKey(SectionTable, on_delete=models.CASCADE)


class UserSectionJoinTable(models.Model):
    # Relationship Fields
    sectionId = models.ForeignKey(
        SectionTable,
        on_delete=models.CASCADE,
    )
    userId = models.ForeignKey(
        UserTable,
        on_delete=models.CASCADE,
    )


class UserLabJoinTable(models.Model):
    # Relationship Fields
    labId = models.ForeignKey(
        LabTable,
        on_delete=models.CASCADE,
    )
    userId = models.ForeignKey(
        UserTable,
        on_delete=models.CASCADE,
    )