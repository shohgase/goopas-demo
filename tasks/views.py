# demoapp/views.py
from django.http import HttpResponse
from django_celery_results.models import TaskResult
from .task import hello

def home(request):
    # うざいけど
    for _ in range(100):
        task_id = hello.delay()
        print(task_id)
    # ただここでTaskResultから値を引っ張ってくればいいだけ
    r = list(TaskResult.objects.all().values_list("result", flat=True))
    print(r)
    return HttpResponse("<html><body>Hello</body></html>")