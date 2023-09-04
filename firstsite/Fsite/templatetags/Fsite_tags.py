from django_jinja import library
from datetime import datetime
import random

@library.global_function
def is_one(n):
    return n == 1

@library.global_function
def format_datetime(argument):
    return datetime.strftime(argument, "%Y-%m-%d %H:%M")
    
@library.global_function
def format_json_datetime(s):
    return format_datetime(datetime.strptime(s ,'%Y-%m-%dT%H:%M:%S.%fz'))

@library.global_function
def shuffle(s):
    return random.shuffle(s)

