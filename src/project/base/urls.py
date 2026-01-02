from django.urls import path
from .views import PendingList, TaskDetail, CreateTask

urlpatterns = [path('', PendingList.as_view(), name='tasks'),
                path('task/<int:pk>', TaskDetail.as_view(), name='task'),
                path('create-task/', CreateTask.as_view(), name='create-task')]