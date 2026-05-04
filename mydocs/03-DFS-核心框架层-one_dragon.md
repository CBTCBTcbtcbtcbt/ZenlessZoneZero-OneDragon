# 03 DFS-核心框架层-one_dragon

> 说明：本卷采用“目录前序 DFS + 同级字典序”，核心脚本逐文件讲解。

## 目录：`src/one_dragon/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

### 目录：`src/one_dragon/base/`
说明：通用基础能力层：配置、控制器、操作框架、识别框架等。

#### 目录：`src/one_dragon/base/conditional_operation/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/one_dragon/base/conditional_operation/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/conditional_operation/atomic_op.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicOp
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/conditional_operation/execution_info.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ExecutionInfo
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, one_dragon.base.conditional_operation.state_cal_tree
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/conditional_operation/loader.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: MergedConfigDumper, ConditionalOperatorLoader；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.operation_def, one_dragon.base.conditional_operation.scene, one_dragon.base.conditional_operation.state_handler, one_dragon.utils；外部库: yaml
- 使用的外部库：yaml
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/conditional_operation/operation_def.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: OperationDef
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/one_dragon/base/conditional_operation/operation_executor.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: OperationExecutor
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, one_dragon.utils, one_dragon.utils.log_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/one_dragon/base/conditional_operation/operator.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ConditionalOperator
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, one_dragon.base.conditional_operation.execution_info, one_dragon.base.conditional_operation.loader, one_dragon.base.conditional_operation.operation_def
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/conditional_operation/scene.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: Scene
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, one_dragon.base.conditional_operation.execution_info, one_dragon.base.conditional_operation.operation_def, one_dragon.base.conditional_operation.state_handler
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/conditional_operation/state_cal_tree.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: StateCalNodeType, StateCalOpType, StateCalNode；函数: construct_state_cal_tree
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.state_recorder, one_dragon.utils.log_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/conditional_operation/state_handler.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: StateHandler
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, one_dragon.base.conditional_operation.execution_info, one_dragon.base.conditional_operation.operation_def, one_dragon.base.conditional_operation.state_cal_tree
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/conditional_operation/state_record_service.py`
- 脚本职责：服务脚本：提供跨流程复用的能力（下载、数据、调度、推送等）。
- 关键类/函数：类: StateRecordService
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.operator, one_dragon.base.conditional_operation.state_recorder, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/conditional_operation/state_recorder.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: StateRecord, StateRecorder
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/one_dragon/base/config/`
说明：配置层：将参数与策略从代码中解耦。

##### 脚本：`src/one_dragon/base/config/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/config/basic_game_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: TypeInputWay, ScreenSizeEnum, FullScreenEnum, MonitorEnum, BasicGameConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.config.yaml_config, one_dragon_qt.widgets.setting_card.yaml_config_adapter
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/one_dragon/base/config/basic_model_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: BasicModelConfig；函数: get_ocr_opts
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.config.yaml_config, one_dragon.base.matcher.ocr.onnx_ocr_matcher, one_dragon.base.web.common_downloader
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/one_dragon/base/config/config_item.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: ConfigItem；函数: get_config_item_from_enum
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/one_dragon/base/config/custom_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: UILanguageEnum, ThemeEnum, ThemeColorModeEnum, BackgroundTypeEnum, CustomConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.config.yaml_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/one_dragon/base/config/game_account_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: GamePlatformEnum, GameLanguageEnum, GameRegionEnum, GameAccountConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.config.yaml_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/one_dragon/base/config/json_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: JsonConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.json_operator, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/one_dragon/base/config/json_operator.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: JsonOperator
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.log_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/config/notify_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: NotifyLevel, NotifyConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.yaml_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/one_dragon/base/config/one_dragon_app_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: OneDragonAppConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.yaml_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/one_dragon/base/config/one_dragon_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: RunInOneDragonApp, OneDragonInstance, AfterDoneOpEnum, InstanceRun, OneDragonConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.config.yaml_config, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/one_dragon/base/config/yaml_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: YamlConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.yaml_operator, one_dragon.utils, one_dragon_qt.widgets.setting_card.yaml_config_adapter
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/one_dragon/base/config/yaml_operator.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: YamlOperator；函数: get_temp_config_path, read_cache_or_load
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.log_utils；外部库: yaml
- 使用的外部库：yaml
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/one_dragon/base/controller/`
说明：输入与窗口控制层：执行真实点击/按键/截图。

##### 目录：`src/one_dragon/base/controller/pc_button/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/one_dragon/base/controller/pc_button/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/controller/pc_button/backend_keyboard_mouse_contoller.py`
- 脚本职责：控制脚本：封装键鼠/手柄/窗口/截图等系统交互能力。
- 关键类/函数：类: KEYBDINPUT, HARDWAREINPUT；函数: send_key, send_text, find_window, attach_to_window_thread, detach_from_window_thread, main
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/controller/pc_button/ds4_button_controller.py`
- 脚本职责：控制脚本：封装键鼠/手柄/窗口/截图等系统交互能力。
- 关键类/函数：类: Ds4ButtonEnum, Ds4ButtonController
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.controller.pc_button, one_dragon.base.controller.pc_button.pc_button_controller；外部库: vgamepad
- 使用的外部库：vgamepad
- 新手理解要点：这层直接和系统输入交互，问题常见于权限、窗口焦点、分辨率。

###### 脚本：`src/one_dragon/base/controller/pc_button/keyboard_mouse_controller.py`
- 脚本职责：控制脚本：封装键鼠/手柄/窗口/截图等系统交互能力。
- 关键类/函数：类: KeyboardMouseController
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.controller.pc_button, one_dragon.base.controller.pc_button.pc_button_controller；外部库: pynput
- 使用的外部库：pynput
- 新手理解要点：这层直接和系统输入交互，问题常见于权限、窗口焦点、分辨率。

###### 脚本：`src/one_dragon/base/controller/pc_button/pc_button_controller.py`
- 脚本职责：控制脚本：封装键鼠/手柄/窗口/截图等系统交互能力。
- 关键类/函数：类: PcButtonController
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：这层直接和系统输入交互，问题常见于权限、窗口焦点、分辨率。

###### 脚本：`src/one_dragon/base/controller/pc_button/pc_button_listener.py`
- 脚本职责：控制脚本：封装键鼠/手柄/窗口/截图等系统交互能力。
- 关键类/函数：类: PcButtonListener
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils；外部库: pynput
- 使用的外部库：pynput
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/controller/pc_button/pc_button_utils.py`
- 脚本职责：控制脚本：封装键鼠/手柄/窗口/截图等系统交互能力。
- 关键类/函数：函数: is_mouse_button, is_xbox_button, is_ds4_button, get_button, get_mouse_button, get_keyboard_button, is_vgamepad_installed
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: pynput, vgamepad
- 使用的外部库：pynput, vgamepad
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/controller/pc_button/xbox_button_controller.py`
- 脚本职责：控制脚本：封装键鼠/手柄/窗口/截图等系统交互能力。
- 关键类/函数：类: XboxButtonEnum, XboxButtonController
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.controller.pc_button, one_dragon.base.controller.pc_button.pc_button_controller；外部库: vgamepad
- 使用的外部库：vgamepad
- 新手理解要点：这层直接和系统输入交互，问题常见于权限、窗口焦点、分辨率。

##### 脚本：`src/one_dragon/base/controller/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/controller/controller_base.py`
- 脚本职责：控制脚本：封装键鼠/手柄/窗口/截图等系统交互能力。
- 关键类/函数：类: ScreenshotWithTime, ControllerBase
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：这层直接和系统输入交互，问题常见于权限、窗口焦点、分辨率。

##### 脚本：`src/one_dragon/base/controller/pc_clipboard.py`
- 脚本职责：控制脚本：封装键鼠/手柄/窗口/截图等系统交互能力。
- 关键类/函数：类: PcClipboard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.log_utils；外部库: pynput, pywintypes, win32clipboard, win32con
- 使用的外部库：pynput, pywintypes, win32clipboard, win32con
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/controller/pc_controller_base.py`
- 脚本职责：控制脚本：封装键鼠/手柄/窗口/截图等系统交互能力。
- 关键类/函数：类: PcControllerBase；函数: win_click, win_scroll, get_mouse_sensitivity, drag_mouse, get_current_mouse_pos
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.controller.controller_base, one_dragon.base.controller.pc_button, one_dragon.base.controller.pc_button.ds4_button_controller, one_dragon.base.controller.pc_button.keyboard_mouse_controller；外部库: PIL, cv2, mss, numpy
- 使用的外部库：PIL, cv2, mss, numpy, pyautogui, pynput
- 新手理解要点：这层直接和系统输入交互，问题常见于权限、窗口焦点、分辨率。

##### 脚本：`src/one_dragon/base/controller/pc_game_window.py`
- 脚本职责：控制脚本：封装键鼠/手柄/窗口/截图等系统交互能力。
- 关键类/函数：类: PcGameWindow
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.utils.log_utils；外部库: pyautogui, pygetwindow, win32ui
- 使用的外部库：pyautogui, pygetwindow, win32ui
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/one_dragon/base/cv_process/`
说明：图像流水线层：按步骤执行 CV 处理。

##### 目录：`src/one_dragon/base/cv_process/steps/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/one_dragon/base/cv_process/steps/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: 
- 使用的外部库：
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_contour_properties.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvContourPropertiesStep
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_crop_by_area.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvStepCropByArea
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_crop_by_template.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvStepCropByTemplate
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step, one_dragon.utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_crop_to_annulus.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvStepCropToAnnulus
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_dilate.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvDilateStep
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_erode.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvErodeStep
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_filter_by_arc_length.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvStepFilterByArcLength
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_filter_by_area.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvStepFilterByArea
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_filter_by_aspect_ratio.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvStepFilterByAspectRatio
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_filter_by_centroid_distance.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvStepFilterByCentroidDistance
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2, numpy, scipy
- 使用的外部库：cv2, numpy, scipy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_filter_by_hsv.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvStepFilterByHSV
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step, one_dragon.utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_filter_by_radius.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvStepFilterByRadius
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_filter_by_rgb.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvStepFilterByRGB
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step, one_dragon.utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_find_contours.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvFindContoursStep
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_grayscale.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvStepGrayscale
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_histogram_equalization.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvStepHistogramEqualization
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_match_shapes.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvMatchShapesStep
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_morphology_ex.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvMorphologyExStep
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_ocr.py`
- 脚本职责：识别脚本：负责 OCR、目标检测或模板匹配能力封装。
- 关键类/函数：类: CvStepOcr
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：这层是“看懂画面”的关键，模型文件、阈值、输入尺寸很重要。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_template_matching.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvTemplateMatchingStep
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step, one_dragon_qt.logic.image_analysis_logic；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/cv_process/steps/step_threshold.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvStepThreshold
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/cv_process/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/cv_process/cv_code_generator.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvCodeGenerator
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step, one_dragon.base.cv_process.steps；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/cv_process/cv_pipeline.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvPipeline
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_service, one_dragon.base.cv_process.cv_step；外部库: numpy
- 使用的外部库：numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/cv_process/cv_service.py`
- 脚本职责：服务脚本：提供跨流程复用的能力（下载、数据、调度、推送等）。
- 关键类/函数：类: CvService
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_pipeline, one_dragon.base.cv_process.cv_step, one_dragon.base.cv_process.steps, one_dragon.base.operation.one_dragon_context；外部库: cv2, numpy, yaml
- 使用的外部库：cv2, numpy, yaml
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/cv_process/cv_step.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CvPipelineContext, CvStep
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_service, one_dragon.base.matcher.match_result, one_dragon.utils；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/one_dragon/base/geometry/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/one_dragon/base/geometry/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/geometry/point.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: Point
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/geometry/rectangle.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: Rect
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/one_dragon/base/matcher/`
说明：匹配层：模板/OCR 等识别统一接口。

##### 目录：`src/one_dragon/base/matcher/ocr/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/one_dragon/base/matcher/ocr/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/matcher/ocr/ocr_match_result.py`
- 脚本职责：识别脚本：负责 OCR、目标检测或模板匹配能力封装。
- 关键类/函数：类: OcrMatchResult
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.matcher.match_result
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：这层是“看懂画面”的关键，模型文件、阈值、输入尺寸很重要。

###### 脚本：`src/one_dragon/base/matcher/ocr/ocr_matcher.py`
- 脚本职责：识别脚本：负责 OCR、目标检测或模板匹配能力封装。
- 关键类/函数：类: OcrMatcher
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.matcher.match_result, one_dragon.base.matcher.ocr.ocr_match_result；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：这层是“看懂画面”的关键，模型文件、阈值、输入尺寸很重要。

###### 脚本：`src/one_dragon/base/matcher/ocr/ocr_service.py`
- 脚本职责：识别脚本：负责 OCR、目标检测或模板匹配能力封装。
- 关键类/函数：类: OcrCacheEntry, OcrService
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.rectangle, one_dragon.base.matcher.match_result, one_dragon.base.matcher.ocr.ocr_match_result, one_dragon.base.matcher.ocr.ocr_matcher；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：这层是“看懂画面”的关键，模型文件、阈值、输入尺寸很重要。

###### 脚本：`src/one_dragon/base/matcher/ocr/ocr_utils.py`
- 脚本职责：识别脚本：负责 OCR、目标检测或模板匹配能力封装。
- 关键类/函数：函数: merge_ocr_result_to_single_line, merge_ocr_result_to_multiple_line, match_word_list_by_priority
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.matcher.match_result, one_dragon.utils, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：这层是“看懂画面”的关键，模型文件、阈值、输入尺寸很重要。

###### 脚本：`src/one_dragon/base/matcher/ocr/onnx_ocr_matcher.py`
- 脚本职责：识别脚本：负责 OCR、目标检测或模板匹配能力封装。
- 关键类/函数：类: OnnxOcrParam, OnnxOcrMatcher；函数: get_ocr_model_dir, get_ocr_download_url_github, get_ocr_download_url_gitee, get_ocr_download_url, get_final_file_list, __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.matcher.match_result, one_dragon.base.matcher.ocr, one_dragon.base.matcher.ocr.ocr_match_result, one_dragon.base.matcher.ocr.ocr_matcher；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：这层是“看懂画面”的关键，模型文件、阈值、输入尺寸很重要。

##### 脚本：`src/one_dragon/base/matcher/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/matcher/match_result.py`
- 脚本职责：识别脚本：负责 OCR、目标检测或模板匹配能力封装。
- 关键类/函数：类: MatchResult, MatchResultList
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/matcher/template_matcher.py`
- 脚本职责：识别脚本：负责 OCR、目标检测或模板匹配能力封装。
- 关键类/函数：类: TemplateMatcher
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.matcher.match_result, one_dragon.base.screen.template_info, one_dragon.base.screen.template_loader, one_dragon.utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/one_dragon/base/operation/`
说明：步骤节点层：封装可调度的自动化动作。

##### 目录：`src/one_dragon/base/operation/application/`
说明：应用编排层：按可运行功能组织业务入口。

###### 脚本：`src/one_dragon/base/operation/application/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/one_dragon/base/operation/application/application_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: ApplicationConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.yaml_operator, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

###### 脚本：`src/one_dragon/base/operation/application/application_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/one_dragon/base/operation/application/application_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: ApplicationFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

###### 脚本：`src/one_dragon/base/operation/application/application_group_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: ApplicationGroupConfigItem, ApplicationGroupConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.yaml_operator, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

###### 脚本：`src/one_dragon/base/operation/application/application_group_manager.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: ApplicationGroupManager
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.one_dragon_app_config, one_dragon.base.operation.application.application_const, one_dragon.base.operation.application.application_group_config, one_dragon.base.operation.one_dragon_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/one_dragon/base/operation/application/application_run_context.py`
- 脚本职责：上下文脚本：集中管理共享状态、服务对象与运行期资源。
- 关键类/函数：类: ApplicationRunContextStateEnum, ApplicationRunContextStateEventEnum, ApplicationRunContext
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config, one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它看作“共享工具箱”，很多模块都从这里拿公共能力。

###### 脚本：`src/one_dragon/base/operation/application/group_application.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: GroupApplication
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_group_config, one_dragon.base.operation.application_base, one_dragon.base.operation.one_dragon_context, one_dragon.base.operation.operation
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/one_dragon/base/operation/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/one_dragon/base/operation/application_base.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: ApplicationEventId, Application
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record, one_dragon.base.operation.one_dragon_context, one_dragon.base.operation.operation, one_dragon.base.operation.operation_base
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/one_dragon/base/operation/application_run_record.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: AppRunRecordPeriod, AppRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.yaml_config, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/one_dragon/base/operation/context_event_bus.py`
- 脚本职责：上下文脚本：集中管理共享状态、服务对象与运行期资源。
- 关键类/函数：类: ContextEventItem, ContextEventBus
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它看作“共享工具箱”，很多模块都从这里拿公共能力。

##### 脚本：`src/one_dragon/base/operation/context_lazy_signal.py`
- 脚本职责：上下文脚本：集中管理共享状态、服务对象与运行期资源。
- 关键类/函数：类: ContextLazySignal
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它看作“共享工具箱”，很多模块都从这里拿公共能力。

##### 脚本：`src/one_dragon/base/operation/one_dragon_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: OneDragonApp
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.game_account_config, one_dragon.base.config.one_dragon_config, one_dragon.base.controller.controller_base, one_dragon.base.operation.application
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/one_dragon/base/operation/one_dragon_context.py`
- 脚本职责：上下文脚本：集中管理共享状态、服务对象与运行期资源。
- 关键类/函数：类: ContextKeyboardEventEnum, ContextInstanceEventEnum, OneDragonContext
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.operation_executor, one_dragon.base.conditional_operation.operator, one_dragon.base.conditional_operation.state_record_service, one_dragon.base.config.custom_config；外部库: pynput
- 使用的外部库：pynput
- 新手理解要点：把它看作“共享工具箱”，很多模块都从这里拿公共能力。

##### 脚本：`src/one_dragon/base/operation/one_dragon_env_context.py`
- 脚本职责：上下文脚本：集中管理共享状态、服务对象与运行期资源。
- 关键类/函数：类: OneDragonEnvContext
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.envs.download_service, one_dragon.envs.env_config, one_dragon.envs.ghproxy_service, one_dragon.envs.git_service
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它看作“共享工具箱”，很多模块都从这里拿公共能力。

##### 脚本：`src/one_dragon/base/operation/operation.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: NodeStateProxy, Operation
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.matcher.match_result, one_dragon.base.matcher.ocr, one_dragon.base.operation.application.application_run_context；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/one_dragon/base/operation/operation_base.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: OperationResult, OperationBase
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/one_dragon/base/operation/operation_edge.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: OperationEdge, OperationEdgeDesc；函数: node_from
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_node
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/one_dragon/base/operation/operation_node.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: OperationNode；函数: operation_node
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_base, one_dragon.base.operation.operation_round_result
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/one_dragon/base/operation/operation_notify.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: NotifyTiming, NodeNotifyDesc；函数: _get_app_info, _get_notify_level, send_application_notify, node_notify, send_node_notify
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.notify_config, one_dragon.base.operation.application_base, one_dragon.base.operation.operation, one_dragon.base.operation.operation_node
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/one_dragon/base/operation/operation_round_result.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: OperationRoundResultEnum, OperationRoundResult
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 目录：`src/one_dragon/base/push/`
说明：通知层：多渠道推送实现。

##### 目录：`src/one_dragon/base/push/channel/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/one_dragon/base/push/channel/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/ai_botk.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AiBotK
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/bark.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: Bark
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/chronocat.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: Chronocat
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/dingding.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: DingDingBot
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/discord.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: Discord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/fake.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: FakePushChannel
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/feishu.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: FeiShu；函数: gen_sign
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/gotify.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: Gotify
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/i_got.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: IGot
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/ntfy.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: Ntfy
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/one_bot.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: OneBot
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/push_deer.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: PushDeer
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/push_me.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: PushMe
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/push_plus.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: PushPlus
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/q_msg.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: QMsg
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/server_chan.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ServerChan
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/smtp.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: Smtp
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/synology_chat.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: SynologyChat
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/telegram.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: Telegram
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/we_plus_bot.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: WePlusBot
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/webhook.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: Webhook
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/work_weixin_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: WorkWeixinApp
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

###### 脚本：`src/one_dragon/base/push/channel/work_weixin_bot.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: WorkWeixinBot
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config, one_dragon.utils.log_utils；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/one_dragon/base/push/channel/wx_pusher.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: WxPusher
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel, one_dragon.base.push.push_channel_config；外部库: cv2, requests
- 使用的外部库：cv2, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/push/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/push/curl_generator.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CurlGenerator
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/push/push_channel.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: PushChannel
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.push.push_channel_config；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/push/push_channel_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: FieldTypeEnum, PushChannelConfigField
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/one_dragon/base/push/push_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: PushProxy, PushConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.config.yaml_config, one_dragon.base.push.push_channel_config, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/one_dragon/base/push/push_email_services.py`
- 脚本职责：服务脚本：提供跨流程复用的能力（下载、数据、调度、推送等）。
- 关键类/函数：类: PushEmailServices
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/push/push_service.py`
- 脚本职责：服务脚本：提供跨流程复用的能力（下载、数据、调度、推送等）。
- 关键类/函数：类: PushService
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_context, one_dragon.base.push.channel.ai_botk, one_dragon.base.push.channel.bark, one_dragon.base.push.channel.chronocat；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/one_dragon/base/screen/`
说明：屏幕语义层：定义界面区域与导航信息。

##### 脚本：`src/one_dragon/base/screen/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/screen/screen_area.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ScreenArea
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle；外部库: numpy
- 使用的外部库：numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/screen/screen_info.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ScreenInfo
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.yaml_operator, one_dragon.base.geometry.rectangle, one_dragon.base.screen.screen_area, one_dragon.utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/screen/screen_loader.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ScreenRouteNode, ScreenRoute, ScreenContext
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.screen.screen_area, one_dragon.base.screen.screen_info, one_dragon.utils, one_dragon.utils.log_utils；外部库: yaml
- 使用的外部库：yaml
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/screen/screen_utils.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: OcrClickResultEnum, FindAreaResultEnum；函数: find_area, find_area_in_screen, find_and_click_area, get_match_screen_name, get_match_screen_name_from_last, is_target_screen, find_by_ocr
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.one_dragon_context, one_dragon.base.screen.screen_area, one_dragon.base.screen.screen_info；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/screen/template_info.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: TemplateShapeEnum, TemplateInfo；函数: get_template_root_dir_path, get_template_sub_dir_path, get_template_dir_path, is_template_existed, get_template_raw_path, get_template_mask_path, get_template_config_path, is_template_config_existed
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.config.yaml_operator, one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/screen/template_loader.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: TemplateLoader
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.screen.template_info, one_dragon.utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/one_dragon/base/web/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/one_dragon/base/web/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/web/common_downloader.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CommonDownloaderParam, CommonDownloader
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils, one_dragon.utils.log_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon/base/web/zip_downloader.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ZipDownloader
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.web.common_downloader, one_dragon.utils, one_dragon.utils.log_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/base/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/one_dragon/devtools/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

#### 脚本：`src/one_dragon/devtools/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/devtools/compile_po.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：函数: compile_lang, compile_po_files
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils；外部库: polib
- 使用的外部库：polib
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/devtools/python_launcher.py`
- 脚本职责：启动入口脚本：负责参数解析、上下文创建和运行模式切换。
- 关键类/函数：函数: print_message, verify_working_directory, configure_environment, execute_python_script, fetch_latest_code, run_python
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context；外部库: colorama
- 使用的外部库：colorama
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/one_dragon/envs/`
说明：环境层：管理 Python、Git、下载源与代理。

#### 脚本：`src/one_dragon/envs/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/envs/download_service.py`
- 脚本职责：服务脚本：提供跨流程复用的能力（下载、数据、调度、推送等）。
- 关键类/函数：类: DownloadService
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.envs.env_config, one_dragon.envs.project_config, one_dragon.utils, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/envs/env_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: ProxyTypeEnum, RepositoryTypeEnum, RegionEnum, PipSourceEnum, GitRemoteEnum, GitBranchEnum
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.config.yaml_config, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

#### 脚本：`src/one_dragon/envs/ghproxy_service.py`
- 脚本职责：服务脚本：提供跨流程复用的能力（下载、数据、调度、推送等）。
- 关键类/函数：类: GhProxyService；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.envs.env_config, one_dragon.utils.log_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/envs/git_service.py`
- 脚本职责：服务脚本：提供跨流程复用的能力（下载、数据、调度、推送等）。
- 关键类/函数：类: GitLog, GitService；函数: __fetch_latest_code
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.envs.env_config, one_dragon.envs.project_config, one_dragon.utils, one_dragon.utils.i18_utils；外部库: packaging, pygit2
- 使用的外部库：packaging, pygit2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/envs/project_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: ProjectConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.yaml_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

#### 脚本：`src/one_dragon/envs/python_service.py`
- 脚本职责：服务脚本：提供跨流程复用的能力（下载、数据、调度、推送等）。
- 关键类/函数：类: PythonService
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.envs.download_service, one_dragon.envs.env_config, one_dragon.envs.project_config, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/one_dragon/launcher/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

#### 脚本：`src/one_dragon/launcher/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/launcher/application_launcher.py`
- 脚本职责：启动入口脚本：负责参数解析、上下文创建和运行模式切换。
- 关键类/函数：类: ApplicationLauncher
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.one_dragon_context, one_dragon.launcher.launcher_base, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/launcher/exe_launcher.py`
- 脚本职责：启动入口脚本：负责参数解析、上下文创建和运行模式切换。
- 关键类/函数：类: ExeLauncher
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.launcher.launcher_base；外部库: pyuac
- 使用的外部库：pyuac
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/launcher/launcher_base.py`
- 脚本职责：启动入口脚本：负责参数解析、上下文创建和运行模式切换。
- 关键类/函数：类: LauncherBase
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/one_dragon/thread/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

#### 脚本：`src/one_dragon/thread/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/thread/atomic_bool.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBool
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/thread/atomic_int.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicInt
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/one_dragon/utils/`
说明：通用工具层：日志、字符串、文件、线程等。

#### 脚本：`src/one_dragon/utils/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/utils/app_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：函数: start_one_dragon, get_launcher_version
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/utils/cal_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：函数: distance_between, get_angle_by_pts, calculate_direction_angle, angle_delta, angle_add, in_rect, calculate_overlap_area, cal_overlap_percent
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/utils/cmd_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：函数: run_command, shutdown_sys, cancel_shutdown_sys
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils, one_dragon.utils.log_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/utils/cv2_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：函数: read_image, save_image, get_image_file_type, show_image, image_rotate, mark_area_as_color, match_template, concat_vertically
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.rectangle, one_dragon.base.matcher.match_result；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/utils/debug_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：函数: get_debug_dir_path, get_debug_image_dir_path, get_debug_image_path, get_debug_image, copy_image_to_clipboard, save_debug_image
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils, one_dragon.utils.log_utils；外部库: PIL, cv2, win32clipboard, win32con
- 使用的外部库：PIL, cv2, win32clipboard, win32con
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/utils/file_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：函数: unzip_file
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/utils/http_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：类: DownloadCancelledError；函数: download_file
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils, one_dragon.utils.log_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/utils/i18_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：函数: detect_language, detect_and_set_default_language, get_translations, gt, coalesce_gt, update_default_lang, get_default_lang
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/utils/log_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：函数: get_logger, set_log_level, mask_text
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/utils/mini_map_angle_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：函数: generate_polar_remap_maps, create_angular_histogram_from_peaks, peak_confidence, convolve, normalize_angle, calculate, calculate_sector_angle
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: cv2, numpy, scipy
- 使用的外部库：cv2, numpy, scipy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/utils/mini_map_angle_visualizer.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：函数: setup_chinese_font, get_title, visualize_calculate, _draw_angle_on_minimap, visualize_calculate_sector_angle, _draw_sector_on_minimap
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils, one_dragon.utils.mini_map_angle_utils, one_dragon.utils.mini_map_angle_visualizer；外部库: cv2, matplotlib, numpy
- 使用的外部库：cv2, matplotlib, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/utils/os_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：函数: join_dir_path_with_mk, get_path_under_work_dir, run_in_exe, get_work_dir, get_env, get_env_def, now_timestamp_str, get_dt
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/utils/str_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：函数: find, find_by_lcs, longest_common_subsequence_length, get_positive_digits, get_positive_float, remove_not_digit, find_best_match_by_lcs, find_best_match_by_difflib
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/utils/thread_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：函数: handle_future_result
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.log_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/utils/yolo_config_utils.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：函数: get_model_category_dir, get_model_dir, get_available_models, is_model_existed
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

### 目录：`src/one_dragon/yolo/`
说明：YOLO 模型封装层：检测与分类能力。

#### 脚本：`src/one_dragon/yolo/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/yolo/detect_utils.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: DetectContext, DetectClass, DetectObjectResult, DetectFrameResult；函数: nms, multiclass_nms, compute_iou, xywh2xyxy, draw_detections, draw_text, draw_masks
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/yolo/log_utils.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：函数: get_logger
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/yolo/onnx_model_loader.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: OnnxModelLoader
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.yolo.log_utils；外部库: onnxruntime
- 使用的外部库：onnxruntime
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/yolo/onnx_utils.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：函数: scale_input_image_u
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon/yolo/yolo_utils.py`
- 脚本职责：识别脚本：负责 OCR、目标检测或模板匹配能力封装。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：这层是“看懂画面”的关键，模型文件、阈值、输入尺寸很重要。

#### 脚本：`src/one_dragon/yolo/yolov8_onnx_cls.py`
- 脚本职责：识别脚本：负责 OCR、目标检测或模板匹配能力封装。
- 关键类/函数：类: RunContext, ClassificationResult, Yolov8Classifier
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.yolo, one_dragon.yolo.onnx_model_loader；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：这层是“看懂画面”的关键，模型文件、阈值、输入尺寸很重要。

#### 脚本：`src/one_dragon/yolo/yolov8_onnx_det.py`
- 脚本职责：识别脚本：负责 OCR、目标检测或模板匹配能力封装。
- 关键类/函数：类: Yolov8Detector
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.yolo, one_dragon.yolo.detect_utils, one_dragon.yolo.onnx_model_loader；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：这层是“看懂画面”的关键，模型文件、阈值、输入尺寸很重要。

### 脚本：`src/one_dragon/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`src/one_dragon/version.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。
