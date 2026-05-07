# `taygedo_toolkit`

这是 demo 的主包。

## 文件树

```text
taygedo_toolkit/
├─ app/
├─ config/
├─ context/
├─ controller/
├─ launcher/
└─ service/
```

## 分层职责

1. `launcher`
   - 命令行入口。
   - 负责把程序跑起来。

2. `app`
   - 生命周期。
   - 负责 init / run / shutdown。

3. `context`
   - 依赖组装。
   - 负责把配置、控制器、识别服务、战斗服务串起来。

4. `controller`
   - 输入输出。
   - 负责窗口激活、截图、鼠标键盘输出。

5. `service`
   - 核心逻辑。
   - 负责红光识别、OCR 探测、自动战斗循环。

6. `config`
   - 参数定义和默认值。

## 依赖方向

只允许单向依赖：

```text
launcher -> app -> context -> service -> controller -> one_dragon base
```

不要反向让底层模块依赖上层模块，否则后续扩展会变乱。

## 你应该优先看哪里

1. `launcher/README.md`
2. `app/README.md`
3. `context/README.md`
4. `service/README.md`
5. `controller/README.md`
6. `config/README.md`
