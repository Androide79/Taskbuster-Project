# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from . import models
 
 
class TestProfileModel(TestCase):
 
    def test_profile_creation(self):
        User = get_user_model()
        # New user created
        user = User.objects.create(
            username="taskbuster", password="django-tutorial")
        # Check that a Profile instance has been crated
        self.assertIsInstance(user.profile, models.Profile)
        # Call the save method of the user to activate the signal
        # again, and check that it doesn't try to create another
        # profile instace
        user.save()
        self.assertIsInstance(user.profile, models.Profile)

class TestProjectModel(TestCase):
 
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(
            username="taskbuster", password="django-tutorial")
        self.profile = self.user.profile
 
    def tearDown(self):
        self.user.delete()
 
    def test_validation_color(self):
        # This first project uses the default value, #fff
        project = models.Project(
            user=self.profile,
            name="TaskManager"
            )
        self.assertTrue(project.color == "#fff")
        # Validation shouldn't rise an Error
        project.full_clean()
 
        # Good color inputs (without Errors):
        for color in ["#1cA", "#1256aB"]:
            project.color = color
            project.full_clean()
 
        # Bad color inputs:
        for color in ["1cA", "1256aB", "#1", "#12", "#1234",
                      "#12345", "#1234567"]:
            with self.assertRaises(
                    ValidationError,
                    msg="%s didn't raise a ValidationError" % color):
                project.color = color
                project.full_clean()