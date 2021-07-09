# goopas-demo

```
1, docker-compose up -d --build
2-1, docker-compose exec ap bash
2-2, python manage.py makemigrations &&  python manage.py migrate
2-3, python manage.py runserver 0.0.0.0:8000
3-1, docker-compose exec celery bash
3-2, celery -A app worker -l info
```

これで

```
localhost:8000
```

開けばDBの `django_celery_results_taskresult` のテーブルにばんばん値が入ってくると思います。
