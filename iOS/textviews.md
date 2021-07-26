### UILabel vs UITextField vs UITextView

---

**UILabel**

읽기 전용 텍스트

- 기본 설정은 1줄이지만 lines 속성을 통해 여러줄로 사용 가능

**UITextField**

텍스트 편집 가능한 객체

- 클릭하면 입력, 수정 가능
- 한줄로만 작성가능

**UITextView**

여러가지 방식으로 사용가능한 Text 객체

여러줄의 읽기전용 텍스트, 텍스트 편집 가능한 객체 등

- UITextView를 터치하면 키보드가 등장하며, 편집 가능
- Behavior 속성의 Edit table을 해제하면 편집 불가능하게 설정 가능
- 텍스트가 길어질 경우 자동스크롤 기능 제공