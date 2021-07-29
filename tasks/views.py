from celery import shared_task, states, app
from celery.result import AsyncResult
from .models import PlayerTaskResult
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from .task import pi
import time

class MyTaskListView(ListView):

        template_name = 'task_list.html'

        def get_queryset(self):
            return list(PlayerTaskResult.objects.all())

        def get_context_data(self, **kwargs):
            context_data = super().get_context_data(**kwargs)
            pi.apply_async(args=[1000000], serializer='json')
            return context_data

home = MyTaskListView.as_view()