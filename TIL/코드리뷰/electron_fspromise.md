[[0-코드리뷰 MOC.md]] · #code-review <!-- moc-nav -->

# 일렉트론 start or Build error Issue!

일렉트론 프로젝트의 `Auto- Builder` 문제를 해결하는 과정에서 다음과 같은 문제가 발생했다.

```
Cannot find module fs/promises

/Users/abhimatta/Documents/abhishek/accura-electron-dev/node_modules/builder-util/out/fs.js
/Users/abhimatta/Documents/abhishek/accura-electron-dev/node_modules/builder-util/out/util.js
/Users/abhimatta/Documents/abhishek/accura-electron-dev/node_modules/electron-builder/out/cli/cli.js
/Users/abhimatta/Documents/abhishek/accura-electron-dev/node_modules/electron-builder/cli.js at Function.Module._resolveFilename (internal/modules/cjs/loader.js:797:15) at Function.Module._load (internal/modules/cjs/loader.js:690:27) at Module.require (internal/modules/cjs/loader.js:852:19) at require (internal/modules/cjs/helpers.js:74:18) at Object. (/Users/abhimatta/Documents/abhishek/accura-electron-dev/node_modules/builder-util/src/fs.ts:4:1) at Module._compile (internal/modules/cjs/loader.js:959:30) at Object.Module._extensions..js (internal/modules/cjs/loader.js:995:10) at Module.load (internal/modules/cjs/loader.js:815:32) at Function.Module._load (internal/modules/cjs/loader.js:727:14) at Module.require (internal/modules/cjs/loader.js:852:19) at require (internal/modules/cjs/helpers.js:74:18) at Object. (/Users/abhimatta/Documents/abhishek/accura-electron-dev/node_modules/builder-util/src/util.ts:24:1) at Module._compile (internal/modules/cjs/loader.js:959:30) at Object.Module._extensions..js (internal/modules/cjs/loader.js:995:10) at Module.load (internal/modules/cjs/loader.js:815:32) at Function.Module._load (internal/modules/cjs/loader.js:727:14)
Package.json configurations
```

## Cause

```
const {app, BrowserWindow, Menu} = require('electron');

const log = require('electron-log');

const {autoUpdater} = require("electron-updater");
```
원인은 `const {autoUpdater} = require("electron-updater");` 모듈의 내부의 `fs/promises` 의 버전 문제 였다.

**Error Log 가 말하는 것은 `fs/promises` 모듈을 찾을 수 없다는 것이다.**

GitHub `electron-builder` 공식 문서에서는 Node.js 가 가지는 `node_module`의 버전 문제임을 알렸다.


## Solve

많은 개발자들이 문제 해결에 다양한 방법을 제안하고있다.

1. Node version 14 이상으로 변경
2. electron-builder 22.10.5.ver 이하로 변경
3. npm install 다시할것

**나는 공식 문서에 따라 다음과 같은 방식을 따르기로 했다.**

`해당 프로젝트  > node_modules > electron-updater > out > AppUpdater.js`

const promises_1 = require("fs/promises"); 에서 

🔻

const promises_1 = require("fs").promises;

으로 변경 해줄 것.




## Reference
- [Github issu](https://github.com/electron-userland/electron-builder/issues/5978)