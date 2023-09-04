from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'time_update', 'is_published', 'tag_list')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'time_update')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_name', 'title', 'author', 'source', 'time_update', 'is_published', 'rate', 'tag_list', 'show_solution')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'rate')
    list_editable = ('is_published', 'show_solution')
    list_filter = ('is_published', 'time_create', 'time_update', 'rate')

    def subject_name(self, obj):
        if obj.subject:
            return obj.subject.name
        else:
            return None

    subject_name.short_description = 'Предмет'
    subject_name.admin_order_field = 'subject__name'

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


class UserProfileAdmin(UserAdmin):
    add_form = RegisterUserForm
    model = UserProfile
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birth_date', 'phone_number', 'avatar', 'about_me', 'status', 'rate', 'country')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email',)}),
    )
    list_display = ['email', 'username', 'avatar', 'phone_number']

class ContestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'started_at', 'completed_at', 'is_published', 'finished', 'tag_list')
    list_display_links = ('id', 'name')
    list_editable = ('is_published', 'finished')
    list_filter = ('is_published', 'created_at', 'started_at', 'started_at')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['id', 'time_update', 'is_published', 'author', 'source', 'subject']


class MaterialSubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class UserSolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'contest', 'problem', 'mark')
    list_display_links = ('id', 'user', 'contest', 'problem')
    list_filter = ('user', 'date', 'contest', 'problem', 'mark')


class HistoryProblemAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'time_create', 'time_update', 'is_published', 'show_solution')
    list_editable = ('is_published', 'show_solution')


class HistoryTestProblemAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'time_create', 'time_update', 'is_published', 'show_solution')
    list_editable = ('is_published', 'show_solution')


admin.site.register(HistoryProblem, HistoryProblemAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Contest, ContestAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserSolution, UserSolutionAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(MaterialSubject, MaterialSubjectAdmin)
admin.site.register(HistoryTestProblem, HistoryTestProblemAdmin)
