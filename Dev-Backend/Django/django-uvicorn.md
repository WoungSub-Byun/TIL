# django runserver 문제

django 프로젝트를 실행 할때에는 기본적으로 `manage.py`를 기반으로하는

```bash
$ python manage.py runserver
```

위 명령어로 실행합니다.

하지만 실제 배포를할 때에는 대부분 WAS + wsgi를 섞는 방식으로 서버를 실행시킵니다.

이 이유에 대해 알아보던 중 본 포스트에서 runserver에 대해 잘 설명하는 포스팅이 있어 공유하려고 합니다.

(https://twowix.me/85)

글의 내용을 요약해보자면

1. `python manage.py runserver` 실행
2. manage.py
   - Import Error
   - `execute_from_command_line(sys.argv)`
3. `execute_from_command_line(argv)`
   - `utility = ManagementUtility(argv)`
   - `utility.execute()`
4. `ManagementUtility`
   - `__init__()` : argv 세팅
   - `execute()`
     - `subcommand = self.args` or `subcommand = help`
   - CommandParser : 두번째 인자값, 즉 옵션 체크
   - `fetch_command(subcommand).run_from_argv(self.argv)`
5. run_from_args
   - 정적파일 체크
   - DB 체크
   - 로깅 설정
   - `runserver` 실행
6. `django/core/management/commands/runserver.py`
   - `inner_run`
     - 서버 종료 커맨드 셋팅
     - 마이그레이션 체크
     - 서버 실행 및 셋팅 띄우기
     - `run()`
   - `run`
     - `django.core.servers.basehttp`: python 기본 http server 열기

위와 같은 과정으로 runserver 가 실행되게 되는 것입니다.

여기서 어떤 부분 때문에 runserver를 실 서비스 배포시에 사용하지 않는가 라고 한다면 맨 마지막에 실행되는 `django.core.servers.basehttp` 를 사용해 서버를 열기 때문이라고 생각합니다.

해당 모듈을 잘 보면 위의 주석 처리된곳에
`This is a simple server for use in testing or debugging Django apps. it hasn't been reviewed for security issues. DON'T USE IT FOR PRODUCTION USE!` 라고 쓰여있습니다.

간단하게 해석하면

`이 서버는 간단한 테스트나 디버깅용으로 사용되는것이니, 절대 배포용으로 사용하지 말아라!`

라고 볼 수 있습니다.

이 모듈을 더 잘 보면 https를 사용하게 되면 예외처리 하는 단계도 존재합니다.
이만큼 서버의 보안문제가 있다고 판단할 수 있습니다.

이와 같은 이유때문에 실제 배포시에는 gunicorn, uvicorn 과 같은 WAS를 같이 사용합니다.
정확한 사용방법은 다른 곳을 찾아보시는게 좋고
간단한 실행명령어 정도만 기록하도록 하겠습니다.

```bash
gunicorn [asgi.py 들어있는 폴더 이름].asgi:application --bind [IP]:[PORT] -k uvicorn.workers.UvicornWorker
```

위의 명령어는 uvicorn을 사용하여 비동기처리가 가능하게끔 서버를 실행하는 명령어입니다.
