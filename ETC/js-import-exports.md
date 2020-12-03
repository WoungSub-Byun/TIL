# export error

---

javascript에서는 파일의 모듈화를 위해 import, export 기능을 제공한다.

### Commonjs

```javascript
const module1 = require('[모듈이름 / 현재위치에서의 파일 상대경로]')

module.exports = [내보낼 파일]
```

### ES6

> **import**

```javascript
import name form "module-name";
import * as name from "module-name";
import { member } from "module-name";
import { member as alias } from "module-name";
import { member1, member2 } from "module-name";
import { member1, member2 as alias2, [...] } from "module-name";
import defaultMember, { member [, [...]] } from "module-name";
import defaultMember, * as alias from "module-name";
import defaultMember from "module-name";
import "module-name";
```

> **exports**

```javascript
export { name1, name2, ..., nameN };
export { variable1 as name1, variable2 as name2, ..., nameN };
export let name1, name2, ..., nameN; // 또는 var
export let name1 = ..., name2 = ..., ..., nameN; // 또는 var, const
export expression; export dafault expression;
export default function (...) { ... } // 또는 class, function*
export default function name1(...) { ... } // 또는 class, function*
export { name1 as default, ... };
export * from ...;
export { name1, name2, ..., nameN } from ...;
export { import1 as name1, import2 as name2, ..., nameN } from ...;

```

- Named exports

```javascript
export { myFunction };
export const foo = Math.sqrt(2);
```

Named exports는 여러값을 export 하는데 유용합니다. export 된 이름을 사용하여 import 하여 사용할 수 있습니다.

- Default exports

```javascript
export default myFunctionOrClass; // 여기에는 세미콜론이 없습니다.
```

모듈 당 딱 한 개의 default export만 있어야 합니다. default export로 객체, 함수 클래스 등이 될 수 있습니다.

가장 간단하게 export 할 수 있으며, 딱 한개만 default export를 할 수 있기 때문에, "메인" 이라고 할 수 있는 것을 default export 하는 것이 좋습니다.
