from django.urls import path

from tasks.views import TaskComplete, TaskListCreate, TaskRetrieveUpdateDelete


urlpatterns = [
    path("", TaskListCreate.as_view(), name="task-list-create"),
    path("<int:pk>/", TaskRetrieveUpdateDelete.as_view(), name="task-retrieve-update-delete"),
    path("<int:pk>/complete", TaskComplete.as_view(), name="task-set-as-complete")
]
