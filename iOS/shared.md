# shared

Swift를 사용하여 iOS 개발을 하면서 `Class명.shared.메서드` 방식으로 많이 사용하길래 무엇인지 궁금해서 찾아보았다.


## Singleton Pattern

Singleton Pattern은 디자인 패턴의 일부로,

**인스턴스를 하나만 생성하여 생성된 인스턴스를 어디서든 참조할 수 있도록 하는 패턴**이다. 

동시성(Concurreny)문제를 고려하여(Thread-Safe 하게 작성하여) multi-thread에서 사용해도 문제가 없도록 설계해야한다.

### 사용이유

- 하나의 인스턴스를 메모리에 등록하여 여러 스레드가 동시에 해당 인스턴스를 공유하기 때문에 요청이 많은 곳에서 사용하면 효율을 높일 수 있다.

### in Code

```swift
/// in Referenced Class
class AuthManager {
	static let shared = AuthManager()
	public func registerNewUser(email: String, password: String) {
		// Create New User, Insert account to database
	}
}

/// Client
AuthManager.shared.registerNewUser(email: email, password: password) {
	// Something
}
```

위 코드 처럼 인스턴스화시킨 `shared` 변수를 가져야 사용하면 된다.