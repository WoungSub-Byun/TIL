# DB Connection pool

SQLAlchemy와 같은 ORM에 대해서 공부하던 중 'Pool 관리'라는 단어가 나와 찾아본 내용입니다.

ORM Session이 DB에 연결한 후 작업이 끝나면 연결을 종료하는 것이 아니라 만들어 놓은 connection pool을 사용하고 다시 반환하는 방식....?

**DB에 처음 접속하는 과정(getConnection())에서 부하가 걸리게 되는데 이를 막기 위해서 여러개의 연결을 해놓은 후 하나씩 사용하면 되는 것이다.**

하지만 Pool을 너무 많이 해놓으면 메모리의 소모가 크고 너무 적게 해놓으면 Pool을 만든 근본적인 이유가 사라질 뿐더러 대기 시간이 길어진다. 따라서 적당한 크기로 Connection Pool을 관리해야한다.

Python에서 주로 사용하는 `SQLAlchemy`에서는 `QueuePool을` 기본값으로 사용한다.

기본 인자는 `pool_size` 와 `max_overflow` 이고 이것을 기반으로 connection pool 개수를 관리한다.

더 자세한 내용은 아래의 포스트를 확인해보자

[SQLAlchemy의 연결 풀링 이해하기](https://spoqa.github.io/2018/01/17/connection-pool-of-sqlalchemy.html)
