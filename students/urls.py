from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('student-home', TemplateView.as_view(template_name='student_home.html'), name='student_home'),
    path('student_assessment', TemplateView.as_view(template_name='student_assessment.html'), name='student_assessment'),
    path('student_attendence', TemplateView.as_view(template_name='student_attendence.html'), name='student_attendence'),
    path('student-leave-management', TemplateView.as_view(template_name='student-leave-management.html'), name='student-leave-management'),
    #path('student-applied-leave', TemplateView.as_view(template_name='student-applied-leave.html'), name='student-applied-leave'),
    #path('student-profile', TemplateView.as_view(template_name='student-profile.html'), name='student-profile'),
    #path('student_profile_edit', TemplateView.as_view(template_name='student_profile_edit.html'), name='student_profile_edit'),

    path('student-profile-view',views.student_profile_view, name='student_profile_view'),
    path('student-profile-edit',views.student_profile_edit, name='student_profile_edit'),
    path('student-profile-update',views.student_profile_update, name='student_profile_update'),
    path('student-new-leaves',views.student_new_leave, name='student_new_leave'),
    path('student-applied-leave',views.student_leave_table, name='student-applied-leave'),

]