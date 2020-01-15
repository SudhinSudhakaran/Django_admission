from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
        path('', TemplateView.as_view(template_name='index.html'), name='home'),
        path('faculty-login', TemplateView.as_view(template_name='login.html'), name='login_form'),
        path('faculty-home', TemplateView.as_view(template_name='faculty-home.html'), name='faculty_home'),
        path('faculty-student_leave', TemplateView.as_view(template_name='faculty_student_leave.html'), name='faculty_student_leave'),
        path('faculty-assessment', TemplateView.as_view(template_name='faculty_assessment.html'), name='faculty_assessment'),
        path('faculty-attendence', TemplateView.as_view(template_name='faculty_attendence.html'), name='faculty_attendence'),
        #path('faculty-profile', TemplateView.as_view(template_name='faculty_profile.html'), name='faculty_profile'),
        #path('faculty-profile-edit', TemplateView.as_view(template_name='faculty_profile_edit.html'), name='faculty_profile_edit'),
        path('faculty-leave-forwarded', TemplateView.as_view(template_name='faculty_leave_forwarded.html'), name='faculty_leave_forwarded'),
        path('faculty-leave-rejected', TemplateView.as_view(template_name='faculty_leave_rejected.html'), name='faculty_leave_rejected'),
        path('faculity-home-batch', TemplateView.as_view(template_name='faculity_home_batch.html'), name='faculity_home_batch'),
        path('faculty-student-add', TemplateView.as_view(template_name='faculty_student_add.html'), name='faculty_student_add'),
        #path('faculty_student_details', TemplateView.as_view(template_name='faculty_student_details.html'), name='faculty_student_details'),

        path('login',views.login, name='login'),
        path('logout',views.flogout, name='logout'),
        path('faculty-profile',views.faculty_profile, name='faculty_profile'),
        path('faculty-profile-edit',views.faculty_profile_edit, name='faculty_profile_edit'),
        path('faculty-profile-update',views.faculty_profile_update, name='faculty_profile_update'),
        path('faculty-student-table',views.faculty_student_table, name='faculty_student_table'),
        path('student-profile',views.studentprofile, name='student_profile'),
        path('faculty_new_student',views.faculty_new_student, name='faculty_new_student'),

]