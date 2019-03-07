from django.urls import path
from . import views
from .views import (IssueCreateView, IssueDetailView,
                    IssueListView, IssueUpdateView,
                    IssueDeleteView, CommentUpdateView, CommentDeleteView,
                    UserIssueListView)

app_name = 'girlapp'

urlpatterns = [
    path('', views.index, name='girlapp-home'),
    path('home/', IssueListView.as_view(), name='girlapp-index'),
    path('user/<str:username>/', UserIssueListView.as_view(), name='user-issues'),
    # path('<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('create_new/', IssueCreateView.as_view(), name='issue-create'),
    path('<int:pk>/update/', IssueUpdateView.as_view(), name='issue-update'),
   # path('<int:pk>/comment/', CommentCreateView.as_view(),
    #     name='question-comment'),
    path('<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    # path('<int:pk>/delete_comment/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('<int:pk>/delete/', IssueDeleteView.as_view(), name='issue-delete'),
    # path('<int:pk>/comment/', Comm.as_view(), name='question-comment'),


   # path('create_new/', views.create_quiz, name='question-create'),
    path('(?P<issue_id>[0-9]+)/', views.detail, name='issue-detail'),
   # path('(?P<quiz_id>[0-9]+)/comment/', views.detail, name='question-comment'),
   # path('(?P<quiz_id>[0-9]+)/delete/', views.delete, name='question-delete'),
]