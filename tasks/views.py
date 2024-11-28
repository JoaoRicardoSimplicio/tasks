from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, views

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskComplete(views.APIView):

    def post(self, request, pk, format=None):
        """
        Set task as complete
        """
        task = Task.get_or_none(pk=pk)

        if task is not None:
            task.status = "Done"
            task.save()

            return Response(
                TaskSerializer(task).data,
                status=status.HTTP_200_OK
            )

        return Response(status=status.HTTP_404_NOT_FOUND)
