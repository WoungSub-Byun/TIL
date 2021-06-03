# How to use alembic?

오늘은 python의 데이터베이스 마이그레이션 툴 `alembic` 사용법을 정리해보려합니다.

최근 개발하고 있는 졸업작품에서 FastAPI를 이용한 서버개발을 맡게 되었는데 Django를 쓸 때 기본적으로 `manage.py`에서 제공하는 migration 기능이 유용해서 다른 라이브러리가 없을까 찾던 중 `alembic`이라는 툴을 찾게되어 사용하게 되었습니다.

## 마이그레이션(migration)?

alembic에 대해 알아보기 전 마이그레이션이란 무엇인지 알아봅시다.
직역하면

`migration : 이주, 이전`

정보기술 분야에서는 운영환경을 옮기는 것을 말합니다.

최근 클라우드 서비스를 많이 사용되면서 기존 온프레미스 방식의 IDC환경에서 클라우드 환경으로 마이그레이션하는 것을 자주 볼 수 있습니다. 이에 따라 마이그레이션을 쉽게 할 수 있는 툴들이 많이 등장하고 있습니다.

ex. AWS Storage Gateway, AWS DataSync, AWS Snowcone 등

근데 이런 것들은 인프라 자체를 이전할때 쓰는 것 같은데, alembic은 그럼 뭘까요?

alembic은 **ORM으로 스키마를 사용하여 데이터베이스를 관리할때 사용하는 도구**입니다.

alembic 스크립트에는 `upgrade()`와 `downgrade()` 함수들을 사용하여 변경 사항을 제어하고 변경 히스토리를 저장하여 데이터베이스를 재구성할 수 있습니다.

## 설치

`alembic`은 pip 로 설치할 수 있다.

```bash
pip install alembic
```

## 사용법

### 초기화

```bash
alembic init 폴더명
```

위의 명령어를 실행하면 지정한 폴더명으로 아래와 같은 마이그레이션 관리 폴더가 생성됩니다.

![alembicinit](../Image/alembic-init.png)

### 데이터베이스 연동

위의 명령어를 실행하고 만들어진 `env.py`의
`run_migrations_offline()` 함수의 `url` 변수에 연결할 데이터베이스 URI를 입력합니다.

해당 URI는 alembic.ini 파일에 작성되어있는데 해당 파일에서

```
sqlalchemy.url = drivier://user:password@localhost.dbname
```

위의 변수의 값을 연결할 데이터베이스 URI로 바꾸어 사용하면 됩니다.

- 기본으로 제공하는 `alembic.ini`가 아니어도 dotenv 같은 모듈을 사용하여 env.py에 따로 입력하여 사용해도 됩니다😃

### 마이그레이션

이제 실제 마이그레이션 작업을 해봅시다.

alembic에서는 `revision`명령어를 사용하여 migration script를 작성하고 마이그레이션을 진행할 수 있습니다.

```bash
$ alembic revision -m "[Migration Script]"
Generating /path/to/my_folder/practice/versions/f09152543072_example.py ...  done
```

revision을 생성하면 `versions`폴더 밑에 `{revisioncode}_{migrationscript}.py`로 파일이 생성됩니다.

해당 파일에는
`upgrade(), downgrade()`

두 함수가 있는데, 해당 revision을 실제 데이터베이스에 적용할 때 수행될 작업이 `upgrade()`에 명시됩니다.
`downgrade()`에는 변경사항이 있을 때 있기전 상태가 명시됩니다.

- 첫번째 revision에는 만들어진대로 비워두거나 table drop을 적어주면 됩니다.

이제 정말 실제 데이터베이스에 revision을 적용시켜 봅시다.

```bash
$ alembic upgrade head
```

명령어를 사용하면 가장 최근의 revision을 데이터베이스에 적용합니다.

### 이외 기능들

alembic은 아래 명령어를 사용하여 migration history를 확인할 수 있습니다.

```bash
$ alembic history
```

- downgrade 하는 방법
  downgrade를 수행할 때는 특정 revision번호를 지정하거나 -1, -2 같이 현재상태에서 상대적인 위치의 downgrade를 할 수 있습니다.

```bash
$ alembic downgrade <down_revision 번호>

$ alembic downgrade -1 #가장 최신 버전의 전 단계로 downgrade 수행
```

## 마무리

프로젝트를 하면서 유용하게 사용했던 alembic에 대해서 정리했습니다. python프로젝트가 아니더라도 nodejs, go 등 다양한 언어로 서버를 개발하고, alembic으로 마이그레이션을 수행할 수 있으니 유용하게 사용할 수 있었으면 좋겠습니다. 더 자세한 내용은 참고한 블로그 링크를 공유해둘테니 참고하시면 될 것 같습니다:D

### 참고 링크

- [sqlalchemy와 함께 alembic 사용하기](https://www.hides.kr/1045)
- [alembic을 이용해 DB 마이그레이션 하기](https://codeac.tistory.com/115)
- [Alembic documentation](https://alembic.sqlalchemy.org/en/latest/)
