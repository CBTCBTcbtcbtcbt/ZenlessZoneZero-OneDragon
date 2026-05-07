# `launcher/`

这里是命令行启动入口。

## 文件树

```text
launcher/
├─ cli.py
└─ README.md
```

## `cli.py`

这个文件做的事情很少：

1. 解析命令行参数。
2. 支持 `--version`。
3. 延迟导入真正的 app。
4. 在依赖缺失时给出明确提示。

### 代码段 1: 参数解析

```python
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Taygedo auto battle minimal demo")
    parser.add_argument("--version", action="store_true", help="Print demo version and exit")
    return parser
```

这段只定义两个动作：

1. 创建 `ArgumentParser`。
2. 定义 `--version`。

### 代码段 2: `main()`

```python
def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
```

这里先拿到命令行参数。
如果用户只想看版本，就不会继续初始化完整运行环境。

### 代码段 3: `--version`

```python
if args.version:
    print("taygedo-toolkit demo v0.1.0")
    return
```

这使得版本查询不依赖游戏环境，也不依赖 OCR 模型。

### 代码段 4: 延迟导入 app

```python
try:
    from one_dragon.utils.log_utils import log
    from taygedo_toolkit.app.demo_app import TaygedoDemoApp
except ModuleNotFoundError as exc:
    ...
```

这段是为了避免一上来就因依赖缺失崩掉。
只有真正启动 demo 时才需要导入 `app`。

### 代码段 5: 启动 app

```python
app = TaygedoDemoApp()
log.info("Launching taygedo-toolkit demo")
app.run()
```

这里把控制权交给 `TaygedoDemoApp`。
后续所有生命周期都在 app / context 里处理。

## `run_demo.py`

这个文件是 IDE 友好启动器，不是核心逻辑。

### 代码段 1: 设置 `PYTHONPATH`

```python
env["PYTHONPATH"] = os.pathsep.join(extra_paths + ...)
```

目的很简单：

1. 让 `src/one_dragon` 能被找到。
2. 让 `taygedo-toolkit/src` 能被找到。

### 代码段 2: 转发命令行参数

```python
cmd = [sys.executable, "-m", "taygedo_toolkit.launcher.cli", *sys.argv[1:]]
```

它把当前命令行参数原样转给真正的入口。
所以 `python taygedo-toolkit/run_demo.py --version` 也能工作。
