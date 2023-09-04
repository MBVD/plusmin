from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from .views import *

urlpatterns =[
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('Fsite/images/favicon.ico'))),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('problems/', problems, name='problems'),
    path('problem/<int:problem_id>/', problem, name='problem'),
    path('news/', news, name='news'),
    path('news/<int:news_id>/', news_with_id, name='news_with_id'),
    path('rating/', rating, name='rating'),
    path('contests/', contests, name="contests"),
    path('contests/<int:contest_id>', contest, name="contest"),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('user/<str:username>', change_form, name='user_profile'),  # /<int:user_id>
    path('registration_for_the_contest/<int:contest_id>/<str:username>', registration_for_contest, name="registration_for_contest"),
    path('find_information', render_find_info, name="find_information"),
    path('contest/<int:contest_id>/problem/<int:problem_id>/', problem_in_contest, name='problem_in_contest'),
    # path('update_contest/<int: contest_id>', update_contest, ) # для отправки js запроса на изменение статуса контеста
    path('contest_checking/<int:contest_id>', checking_contest_solutions, name="contest_checking"),
    path('download_history_tests/', download_history_tests, name="download_history_tests"),
]

