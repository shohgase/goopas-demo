from django_celery_results.models import TaskResult
from django.utils.functional import cached_property

class PlayerTaskResult(TaskResult):

    @cached_property
    def display_state(self):
        return self.status