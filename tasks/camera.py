from pprint import pformat
from app import settings
from celery.events.snapshot import Polaroid
from celery.utils.imports import symbol_by_name

class DumpCam(Polaroid):
    clear_after = True  # clear after flush (incl, state.event_count).

    def django_setup(self):
        import django
        django.setup()

    def install(self):
        super(DumpCam, self).install()
        self.django_setup()

    @property
    def TaskResult(self):
        return symbol_by_name('tasks.models.PlayerTaskResult')

    def _store_result(self, task=None, ctype='application/json',cenc='utf-8'):
        return self.TaskResult.objects.store_result(ctype, cenc, task.id, result=task.result, status=task.state)

    def on_shutter(self, state):
        if not state.event_count:
            # No new events since last snapshot.
            return
        print('Workers: {0}'.format(pformat(state.workers, indent=4)))
        print('Tasks: {0}'.format(pformat(state.tasks, indent=4)))
        print('Total: {0.event_count} events, {0.task_count} tasks'.format(
            state))
        def _handle_tasks():
            for i, uuid_task in enumerate(state.tasks.items()):
                _, task = uuid_task
                # 設定に含めたタスクだけを対象にする
                if task.name not in settings.MONITORED_TASKS:
                    continue
                self._store_result(task)
        _handle_tasks()

        # celery -A app events -l info --camera tasks.camera.DumpCam --frequency=2.0