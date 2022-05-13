from django.urls import path

from todo.views import TaskListView

app_name = 'todo'

urlpatterns = [
    path('test/', view=TaskListView.as_view(), name='test_route'),
]