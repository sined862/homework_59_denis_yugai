﻿from django.urls import path
from issuetracker.views.base import IndexView
from issuetracker.views.issues import IssueView, IssueAddView, IssueUpdateView, IssueDelView, IssueDelConfirmView
from issuetracker.views.projects import ProjectsView, ProjectView, ProjectAddView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/<int:pk>', IssueView.as_view(), name='issue'),
    path('issue_add/', IssueAddView.as_view(), name='issue_add'),
    path('issue_update/<int:pk>', IssueUpdateView.as_view(), name='issue_update'),
    path('issue_del/<int:pk>', IssueDelView.as_view(), name='issue_del'),
    path('issue_del_confirm/<int:pk>', IssueDelConfirmView.as_view(), name='del_confirm'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('project/<int:pk>', ProjectView.as_view(), name='project'),
    path('project_add/', ProjectAddView.as_view(), name='project_add')
]