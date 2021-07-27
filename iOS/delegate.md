# Delegate
---

직역하면, '대리자', '대리인', '위임하다' 라는 뜻이다.

swift에서도 이와 비슷한 의미로 사용되는데, 실제 코드로 보면서 이해해보자

```swift
import UIkit

class ViewController: UIViewController{
    @IBOutlet weak var enteredLabel: UILabel!
    @IBOutlet weak var textField: UITextField!

    @IBAction func buttonClicked(_ sender: Any) {
        enteredLabel.text = textField.text
    }
}
```

위의 코드는 button을 누르게 되면 textField에 입력한 데이터가 label에 표시되게 하는 코드이다.

swift를 처음 맛보게 될 때 대부분 @IBOutlet으로 storyboard에 있는 ui와 소통한다.

이렇게 직접 IBOutlet으로 연결하여 메서드를 구현하는 것 외의 방법 중 하나가 delegate 패턴이다.

delegate 패턴에는 세 가지 개념이 존재한다.

- Receiver: 수신자
- Delegate: 대리자
- Send (Delegate ← Receiver)

Delegate는 Reciever로부터 Receiver자신의 객체를 전달 받고, 이를 이용한 행동(ex: 메소드 호출)을 취했을 때 수신자는 그 결과를 받게 된다.

```swift
// protocol로 delegate가 사용할 메소드 등록
protocol TapDelegate: class {
    func helloWorld()
}

class Receiver: TapDelegate {
    let button = Delegate()
    
    init() {
        button.delegate = self // delegate에게 자신의 객체를 전달
    }
    
    func helloWorld() {
        print("Hello World")
    }
}

class Delegate {
    weak var delegate: TapDelegate?
    
    func didTapButton() {
        delegate?.helloWorld() // delegate에 등록된 receiver 객체를 사용하여 메소드 사용
    }
}
```

**왜 사용하는가?**

첫번째로 소개했던 @IBOutlet의 경우 직접 UI의 요소를 연결하고 하나하나씩 Action을 만들어야하지만, delegate를 사용하면 여러 요소가 비슷한 Action을 취할 경우, 만들어놓은 delegate에 자신의 객체를 전달하여 delegate에서 구현된 행동을 취하면 되기때문에 코드의 재사용성이 높아진다.

viewcontroller에서 delegate를 사용하기 위해서는 각요소의 delegate 프로토콜을 상속 받아 사용하거나 아래 코드 처럼 extension으로 기존의 프로토콜을 확장시켜 사용한다.

실제 코드)

```swift


import UIKit

class HomeViewController: UIViewController {
    
    /// Receiver
    private let tableView: UITableView = {
        let tableView = UITableView()
        return tableView
    }()
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.addSubview(tableView)
        // 위에서 선언한 tableView객체를 delegate에게 보낸다.
        tableView.delegate = self
        tableView.dataSource = self
    }
    
    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        tableView.frame = view.bounds
    }

}

/// Delegate
// 이렇게 extension으로 protocol을 확장하고 메서드를 구현하여 사용하기도 한다.
extension HomeViewController: UITableViewDelegate, UITableViewDataSource {
    func numberOfSections(in tableView: UITableView) -> Int {
        return 0
    }
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 0
    }
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        return UITableViewCell()
    }
}
```