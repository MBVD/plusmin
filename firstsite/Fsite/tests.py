from django.test import TestCase

# Create your tests here.

from models import *
contest = Contest.objects.get(pk = 1)
print(contest.is_finished())