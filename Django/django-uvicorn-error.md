# django runserver 문제

django 프로젝트를 실행 할때에는 기본적으로 `manage.py`를 기반으로하는

```bash
$ python manage.py runserver
```

위 명령어로 실행합니다.

하지만 실제 배포를할 때에는 대부분 WAS + wsgi를 섞는 방식으로 서버를 실행시킵니다.

이 이유에 대해 알아보던 중 본 포스트에서 runserver에 대해 잘 설명하는 포스팅이 있어 공유하려고 합니다.

(https://twowix.me/85)

암튼 보안관련 이슈와 테스팅이나 디버깅할 때만 사용하길 바란다
