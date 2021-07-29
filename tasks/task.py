from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time

@shared_task(bind=True)
def pi(self, x1):
    A=x1
    pi=0
    for L in range(1,A):
        if L%2==0:
            B=-1
        else:
            B=1
        pi+=(4/(2*L-1))*B
    return pi