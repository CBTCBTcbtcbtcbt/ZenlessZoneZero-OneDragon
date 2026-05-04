# 05 DFS-核心业务层-zzz_od

> 说明：本卷采用“目录前序 DFS + 同级字典序”，核心脚本逐文件讲解。

## 目录：`src/zzz_od/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

### 目录：`src/zzz_od/application/`
说明：应用编排层：按可运行功能组织业务入口。

#### 目录：`src/zzz_od/application/battle_assistant/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 目录：`src/zzz_od/application/battle_assistant/auto_battle/`
说明：自动战斗核心层：状态识别、原子动作与策略执行。

###### 脚本：`src/zzz_od/application/battle_assistant/auto_battle/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/battle_assistant/auto_battle/auto_battle_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: AutoBattleApp
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.controller.pc_button, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

###### 脚本：`src/zzz_od/application/battle_assistant/auto_battle/auto_battle_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: AutoBattleAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, zzz_od.application.battle_assistant.auto_battle, zzz_od.application.battle_assistant.auto_battle.auto_battle_app
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

###### 脚本：`src/zzz_od/application/battle_assistant/auto_battle/auto_battle_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 目录：`src/zzz_od/application/battle_assistant/dodge_assitant/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/application/battle_assistant/dodge_assitant/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/battle_assistant/dodge_assitant/dodge_assistant_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: DodgeAssistantApp
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.controller.pc_button, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

###### 脚本：`src/zzz_od/application/battle_assistant/dodge_assitant/dodge_assistant_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/battle_assistant/dodge_assitant/dodge_assistant_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: DodgeAssistantFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, zzz_od.application.battle_assistant.dodge_assitant, zzz_od.application.battle_assistant.dodge_assitant.dodge_assistant_app
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 目录：`src/zzz_od/application/battle_assistant/operation_debug/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/application/battle_assistant/operation_debug/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/battle_assistant/operation_debug/operation_debug_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: OperationDebugApp
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, one_dragon.base.conditional_operation.loader, one_dragon.base.conditional_operation.operation_def, one_dragon.base.controller.pc_button
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/application/battle_assistant/operation_debug/operation_debug_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: OperationDebugAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, zzz_od.application.battle_assistant.operation_debug, zzz_od.application.battle_assistant.operation_debug.operation_debug_app
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

###### 脚本：`src/zzz_od/application/battle_assistant/operation_debug/operation_debug_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/application/battle_assistant/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/battle_assistant/auto_battle_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：函数: get_auto_battle_op_config_list, get_all_auto_battle_op, get_auto_battle_op_by_name, get_auto_battle_config_file_path
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.operator, one_dragon.base.config.config_item, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/zzz_od/application/battle_assistant/battle_assistant_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: BattleAssistantConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.yaml_config, zzz_od.config.game_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/zzz_od/application/battle_assistant/operation_template_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：函数: get_operation_template_config_list
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

#### 目录：`src/zzz_od/application/charge_plan/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/charge_plan/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/charge_plan/charge_plan_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: ChargePlanApp
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_notify
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/charge_plan/charge_plan_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: ChargePlanAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config, one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/charge_plan/charge_plan_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: CardNumEnum, RestoreChargeEnum, ChargePlanItem, ChargePlanConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.config.yaml_config, one_dragon.base.operation.application.application_config, zzz_od.application.charge_plan
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/zzz_od/application/charge_plan/charge_plan_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/charge_plan/charge_plan_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: ChargePlanRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/city_fund/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/city_fund/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/city_fund/city_fund_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: CityFundApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_notify, one_dragon.base.operation.operation_round_result
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/city_fund/city_fund_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: CityFundAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record, zzz_od.application.city_fund
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/city_fund/city_fund_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/city_fund/city_fund_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: CityFundRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/coffee/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/coffee/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/coffee/coffee_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: CoffeeApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.matcher.match_result, one_dragon.base.operation.application, one_dragon.base.operation.operation_edge；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/coffee/coffee_app_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/coffee/coffee_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: CoffeeAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config, one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/coffee/coffee_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: CoffeeChooseWay, CoffeeChallengeWay, CoffeeCardNumEnum, CoffeeConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.operation.application.application_config, one_dragon_qt.widgets.setting_card.yaml_config_adapter
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/zzz_od/application/coffee/coffee_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: CoffeeRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/commission_assistant/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/commission_assistant/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/commission_assistant/commission_assistant_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: CommissionAssistantApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.application, one_dragon.base.operation.context_event_bus, one_dragon.base.operation.one_dragon_context；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/commission_assistant/commission_assistant_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: CommissionAssistantAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config, one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, zzz_od.application.commission_assistant
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/commission_assistant/commission_assistant_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: DialogOptionEnum, StoryMode, CommissionAssistantConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.operation.application.application_config, zzz_od.application.devtools.screenshot_helper
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/zzz_od/application/commission_assistant/commission_assistant_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/devtools/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 目录：`src/zzz_od/application/devtools/large_map_recorder/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/application/devtools/large_map_recorder/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/devtools/large_map_recorder/large_map_downloader.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：函数: get_map_image, get_area_map_image, match_large_map_size
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils；外部库: PIL, cv2, numpy, requests
- 使用的外部库：PIL, cv2, numpy, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/devtools/large_map_recorder/large_map_recorder_utils.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：函数: get_mini_map_circle_mask, get_mini_map_in_circle, merge_large_map, _initialize_large_map, _merge_at_position, _expand_edges_if_needed, get_large_map_display, create_mini_map_snapshot
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.matcher.match_result, one_dragon.utils, zzz_od.application.devtools.large_map_recorder.large_map_recorder_wrapper；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/devtools/large_map_recorder/large_map_recorder_wrapper.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LargeMapSnapshot, MiniMapSnapshot
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, zzz_od.application.world_patrol.world_patrol_area；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/devtools/large_map_recorder/map_icon_utils.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：函数: extract_map_icon, __debug_extract_map_icon
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.screen.template_info, one_dragon.utils, zzz_od.context.zzz_context；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 目录：`src/zzz_od/application/devtools/screenshot_helper/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/application/devtools/screenshot_helper/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/devtools/screenshot_helper/screenshot_helper_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: ScreenshotHelperApp
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.context_event_bus, one_dragon.base.operation.one_dragon_context, one_dragon.base.operation.operation_base
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

###### 脚本：`src/zzz_od/application/devtools/screenshot_helper/screenshot_helper_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: ScreenshotHelperAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config, one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, zzz_od.application.devtools.screenshot_helper
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

###### 脚本：`src/zzz_od/application/devtools/screenshot_helper/screenshot_helper_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: ScreenshotHelperConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

###### 脚本：`src/zzz_od/application/devtools/screenshot_helper/screenshot_helper_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/devtools/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/drive_disc_dismantle/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/drive_disc_dismantle/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/drive_disc_dismantle/drive_disc_dismantle_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: DriveDiscDismantleApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_notify
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/drive_disc_dismantle/drive_disc_dismantle_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: DriveDiscDismantleAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config, one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/drive_disc_dismantle/drive_disc_dismantle_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: DismantleLevelEnum, DriveDiscDismantleConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.config.yaml_config, one_dragon.base.operation.application.application_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/zzz_od/application/drive_disc_dismantle/drive_disc_dismantle_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/drive_disc_dismantle/drive_disc_dismantle_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: DriveDiscDismantleRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/email_app/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/email_app/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/email_app/email_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: EmailApp
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_notify, one_dragon.base.operation.operation_round_result
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/email_app/email_app_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/email_app/email_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: EmailAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record, zzz_od.application.email_app
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/email_app/email_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: EmailRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/engagement_reward/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/engagement_reward/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/engagement_reward/engagement_reward_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: EngagementRewardApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_notify, one_dragon.base.operation.operation_round_result
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/engagement_reward/engagement_reward_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: EngagementRewardAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record, zzz_od.application.engagement_reward
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/engagement_reward/engagement_reward_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/engagement_reward/engagement_reward_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: EngagementRewardRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/game_config_checker/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/game_config_checker/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/game_config_checker/mouse_sensitivity_checker.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: MouseSensitivityChecker；函数: __debug, __debug_turn_dx
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.log_utils；外部库: numpy
- 使用的外部库：numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/game_config_checker/mouse_sensitivity_checker_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/game_config_checker/mouse_sensitivity_checker_factoru.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: MouseSensitivityCheckerFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, zzz_od.application.game_config_checker, zzz_od.application.game_config_checker.mouse_sensitivity_checker
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/game_config_checker/predefined_team_checker.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: TeamWrapper, PredefinedTeamChecker；函数: __debug_update_team_members, __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.base.matcher.match_result, one_dragon.base.operation.operation_edge；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/game_config_checker/predefined_team_checker_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/game_config_checker/predefined_team_checker_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: PredefinedTeamCheckerFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, zzz_od.application.game_config_checker, zzz_od.application.game_config_checker.predefined_team_checker
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

#### 目录：`src/zzz_od/application/hollow_zero/`
说明：空洞玩法层：事件识别、路径与战斗交互。

##### 目录：`src/zzz_od/application/hollow_zero/lost_void/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 目录：`src/zzz_od/application/hollow_zero/lost_void/context/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/context/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/context/lost_void_artifact.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LostVoidArtifact
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/context/lost_void_context.py`
- 脚本职责：上下文脚本：集中管理共享状态、服务对象与运行期资源。
- 关键类/函数：类: LostVoidContext
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.yaml_operator, one_dragon.base.operation.application, one_dragon.base.screen, one_dragon.base.screen.screen_utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：把它看作“共享工具箱”，很多模块都从这里拿公共能力。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/context/lost_void_det_class.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LostVoidDetClass
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/context/lost_void_detector.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LostVoidDetector；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils, one_dragon.yolo, one_dragon.yolo.detect_utils, one_dragon.yolo.yolo_utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/context/lost_void_investigation_strategy.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LostVoidInvestigationStrategy
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 目录：`src/zzz_od/application/hollow_zero/lost_void/operation/`
说明：步骤节点层：封装可调度的自动化动作。

###### 目录：`src/zzz_od/application/hollow_zero/lost_void/operation/interact/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/operation/interact/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/operation/interact/lost_void_artifact_pos.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LostVoidArtifactPos
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.rectangle, zzz_od.application.hollow_zero.lost_void.context.lost_void_artifact
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/operation/interact/lost_void_bangboo_store.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LostVoidBangbooStore；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/operation/interact/lost_void_choose_common.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LostVoidChooseCommon；函数: __debug, __get_get_artifact_pos
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.matcher.match_result, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/operation/interact/lost_void_choose_gear.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LostVoidChooseGear；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.base.matcher.match_result, one_dragon.base.operation.operation_edge；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/operation/interact/lost_void_interact_target_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LostVoidInteractNPC, LostVoidBoss, LostVoidInteractTarget；函数: match_interact_target
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.utils, one_dragon.utils.i18_utils, zzz_od.application.hollow_zero.lost_void.lost_void_challenge_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/operation/interact/lost_void_lottery.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LostVoidLottery；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/operation/interact/lost_void_route_change.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LostVoidRouteChange
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, zzz_od.context.zzz_context, zzz_od.operation.zzz_operation
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/operation/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/operation/lost_void_move_by_det.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: MoveTargetWrapper, LostVoidMoveByDet
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/operation/lost_void_run_level.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LostVoidRunLevel；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.operation, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/operation/update_priority_operation.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: UpdatePriorityOperation；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.log_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/lost_void_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LostVoidApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.matcher.match_result, one_dragon.base.operation.application, one_dragon.base.operation.operation；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/lost_void_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: LostVoidAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.application.application_config, one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/lost_void_challenge_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: LostVoidRegionType, LostVoidPeriodBuffNo, LostVoidBuyOnlyPriority, LostVoidChallengeConfig；函数: get_all_lost_void_challenge_config, get_lost_void_challenge_new_name
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.config.yaml_config, one_dragon.utils, one_dragon.utils.log_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/lost_void_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: LostVoidTaskEnum, LostVoidConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.operation.application.application_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/lost_void_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/hollow_zero/lost_void/lost_void_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LostVoidRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record, one_dragon.utils, zzz_od.application.hollow_zero.lost_void.lost_void_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 目录：`src/zzz_od/application/hollow_zero/withered_domain/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/application/hollow_zero/withered_domain/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/hollow_zero/withered_domain/withered_domain_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: WitheredDomainApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_notify
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

###### 脚本：`src/zzz_od/application/hollow_zero/withered_domain/withered_domain_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: WitheredDomainAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.application.application_config, one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

###### 脚本：`src/zzz_od/application/hollow_zero/withered_domain/withered_domain_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: HollowZeroExtraTask, HollowZeroExtraExitEnum, WitheredDomainConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.operation.application.application_config, one_dragon_qt.widgets.setting_card.yaml_config_adapter, zzz_od.application.hollow_zero.withered_domain
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

###### 脚本：`src/zzz_od/application/hollow_zero/withered_domain/withered_domain_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/hollow_zero/withered_domain/withered_domain_context.py`
- 脚本职责：上下文脚本：集中管理共享状态、服务对象与运行期资源。
- 关键类/函数：类: WitheredDomainContext
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.base.operation.application, one_dragon.utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：把它看作“共享工具箱”，很多模块都从这里拿公共能力。

###### 脚本：`src/zzz_od/application/hollow_zero/withered_domain/withered_domain_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: WitheredDomainRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record, one_dragon.utils, zzz_od.application.hollow_zero.withered_domain, zzz_od.application.hollow_zero.withered_domain.withered_domain_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/hollow_zero/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/life_on_line/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/life_on_line/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/life_on_line/life_on_line_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LifeOnLineApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_notify
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/life_on_line/life_on_line_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: LifeOneLineAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.application.application_config, one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/life_on_line/life_on_line_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: LifeOnLineConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config, one_dragon_qt.widgets.setting_card.yaml_config_adapter
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/zzz_od/application/life_on_line/life_on_line_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/life_on_line/life_on_line_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: LifeOnLineRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record, zzz_od.application.life_on_line.life_on_line_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/notify/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/notify/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/notify/notify_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: NotifyApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, zzz_od.application.notify
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/notify/notify_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: NotifyAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record, zzz_od.application.notify
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/notify/notify_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/notify/notify_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: NotifyRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/notorious_hunt/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/notorious_hunt/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/notorious_hunt/notorious_hunt_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: NotoriousHuntApp
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_notify
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/notorious_hunt/notorious_hunt_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: NotoriousHuntLevelEnum, NotoriousHuntBuffEnum, NotoriousHuntConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.config.yaml_config, one_dragon.base.operation.application.application_config, zzz_od.application.charge_plan.charge_plan_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/zzz_od/application/notorious_hunt/notorious_hunt_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/notorious_hunt/notorious_hunt_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: NotoriousHuntAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config, one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/notorious_hunt/notorious_hunt_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: NotoriousHuntRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/one_dragon_app/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/one_dragon_app/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/one_dragon_app/zzz_one_dragon_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: ZOneDragonApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.one_dragon_app, zzz_od.application.zzz_application, zzz_od.context.zzz_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/one_dragon_app/zzz_one_dragon_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: ZzzOneDragonAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, zzz_od.application.one_dragon_app.zzz_one_dragon_app
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

#### 目录：`src/zzz_od/application/random_play/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/random_play/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/random_play/random_play_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: RandomPlayApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.matcher.match_result, one_dragon.base.operation.application, one_dragon.base.operation.operation_edge；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/random_play/random_play_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: RandomPlayConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/zzz_od/application/random_play/random_play_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/random_play/random_play_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: RandomPlayFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config, one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/random_play/random_play_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: RandomPlayRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/redemption_code/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/redemption_code/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/redemption_code/redemption_code_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: RedemptionCodeApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_notify
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/redemption_code/redemption_code_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/redemption_code/redemption_code_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: RedemptionCodeFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record, zzz_od.application.redemption_code
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/redemption_code/redemption_code_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: RedemptionCode, RedemptionCodeRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record, one_dragon.utils；外部库: yaml
- 使用的外部库：yaml
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/ridu_weekly/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/ridu_weekly/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/ridu_weekly/ridu_weekly_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: RiduWeeklyApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_notify, one_dragon.base.operation.operation_round_result；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/ridu_weekly/ridu_weekly_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: RiduWeeklyAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record, zzz_od.application.ridu_weekly
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/ridu_weekly/ridu_weekly_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/ridu_weekly/ridu_weekly_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: RiduWeeklyRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/scratch_card/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/scratch_card/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/scratch_card/scratch_card_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: ScratchCardApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_notify, one_dragon.base.operation.operation_round_result
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/scratch_card/scratch_card_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/scratch_card/scratch_card_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: ScratchCardFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record, zzz_od.application.scratch_card
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/scratch_card/scratch_card_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: ScratchCardRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/shiyu_defense/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/shiyu_defense/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/shiyu_defense/agent_selector.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：函数: get_best_agent_for_moving, _get_agent_priority
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: zzz_od.auto_battle.auto_battle_agent_context, zzz_od.game_data.agent
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/shiyu_defense/shiyu_defense_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: ShiyuDefenseApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.application, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/shiyu_defense/shiyu_defense_app_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: ShiyuDefenseAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.application.application_config, one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/shiyu_defense/shiyu_defense_battle.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: ShiyuDefenseBattle
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.rectangle, one_dragon.base.operation.operation, one_dragon.base.operation.operation_base, one_dragon.base.operation.operation_edge；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/shiyu_defense/shiyu_defense_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: ShiyuDefenseTeamConfig, ShiyuDefenseConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config, zzz_od.game_data.agent
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/zzz_od/application/shiyu_defense/shiyu_defense_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/shiyu_defense/shiyu_defense_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: CriticalNode, ShiyuDefenseRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record, zzz_od.application.shiyu_defense.shiyu_defense_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/shiyu_defense/shiyu_defense_team_utils.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: DefensePhaseTeamInfo, DefenseTeamSearcher；函数: calc_teams, check_type_by_area
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.screen.screen_area, one_dragon.utils, one_dragon.utils.i18_utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/suibian_temple/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 目录：`src/zzz_od/application/suibian_temple/operations/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/application/suibian_temple/operations/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/suibian_temple/operations/suibian_temple_adventure_dispatch.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: SuibianTempleAdventureDispatchDuration, SuibianTempleAdventureDispatch；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/suibian_temple/operations/suibian_temple_adventure_squad.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: SuibianTempleAdventureSquad；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.application, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/suibian_temple/operations/suibian_temple_auto_manage.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: SuibianTempleAutoManage；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/suibian_temple/operations/suibian_temple_boo_box.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: SuibianTempleBooBox；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.base.matcher.ocr, one_dragon.base.operation.application
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/suibian_temple/operations/suibian_temple_craft.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: SuibianTempleCraft；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/suibian_temple/operations/suibian_temple_craft_dispatch.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: SuibianTempleCraftDispatch；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.base.matcher.ocr.ocr_match_result, one_dragon.base.operation.application
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/suibian_temple/operations/suibian_temple_good_goods.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: SuibianTempleGoodGoods；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.base.operation.application, one_dragon.base.operation.operation_edge
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/suibian_temple/operations/suibian_temple_pawnshop.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: GoodsPos, SuibianTemplePawnshop；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.base.operation.application, one_dragon.base.operation.operation_edge；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/suibian_temple/operations/suibian_temple_sales_stall.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: SuibianTempleSalesStall；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/application/suibian_temple/operations/suibian_temple_yum_cha_sin.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: RegularProcurementPos, SuibianTempleYumChaSin；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.base.operation.application, one_dragon.base.operation.operation_edge；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/suibian_temple/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/suibian_temple/suibian_temple_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: SuibianTempleApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_notify
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/suibian_temple/suibian_temple_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: SuibianTempleConfig, SuibianTempleAdventureMission, BangbooPrice, PawnshopOmnicoinGoods, PawnshopCrestGoods
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config, zzz_od.application.suibian_temple.operations.suibian_temple_adventure_dispatch
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/zzz_od/application/suibian_temple/suibian_temple_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/suibian_temple/suibian_temple_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: SuibianTempleFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config, one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/suibian_temple/suibian_temple_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: SuibianTempleRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/trigrams_collection/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/application/trigrams_collection/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/trigrams_collection/trigrams_collection_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: TrigramsCollectionApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.matcher.ocr, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/trigrams_collection/trigrams_collection_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/trigrams_collection/trigrams_collection_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: TrigramsCollectionFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record, zzz_od.application.trigrams_collection
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/trigrams_collection/trigrams_collection_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: TrigramsCollectionRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/application/world_patrol/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 目录：`src/zzz_od/application/world_patrol/operation/`
说明：步骤节点层：封装可调度的自动化动作。

###### 脚本：`src/zzz_od/application/world_patrol/operation/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/application/world_patrol/operation/transport_by_3d_map.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: TransportBy3dMap；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/application/world_patrol/operation/world_patrol_run_route.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: WorldPatrolRunRoute；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.base.operation.application, one_dragon.base.operation.operation_base
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/application/world_patrol/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/world_patrol/cal_pos_utils.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：函数: cal_pos
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.base.matcher.match_result, one_dragon.utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/world_patrol/mini_map_wrapper.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: MiniMapWrapper
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/world_patrol/world_patrol_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: WorldPatrolApp；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_notify
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/zzz_od/application/world_patrol/world_patrol_area.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: WorldPatrolEntry, WorldPatrolArea, WorldPatrolLargeMapIcon, WorldPatrolLargeMap；函数: world_patrol_dir, entry_dir, area_dir, road_mask_path, icon_yaml_path
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/world_patrol/world_patrol_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: WorldPatrolConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

##### 脚本：`src/zzz_od/application/world_patrol/world_patrol_const.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/world_patrol/world_patrol_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: WorldPatrolAppFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_config, one_dragon.base.operation.application.application_factory, one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/application/world_patrol/world_patrol_route.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: WorldPatrolOpType, WorldPatrolOperation, WorldPatrolRoute
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, zzz_od.application.world_patrol.world_patrol_area
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/world_patrol/world_patrol_route_list.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: RouteListType, WorldPatrolRouteList
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/world_patrol/world_patrol_run_record.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: WorldPatrolRunRecord
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_run_record
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/application/world_patrol/world_patrol_service.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: WorldPatrolService；函数: area_route_dir, route_list_dir
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.yaml_operator, one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.base.matcher.match_result；外部库: cv2, numpy, yaml
- 使用的外部库：cv2, numpy, yaml
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/application/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/application/zzz_application.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: ZApplication
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application_base, one_dragon.base.operation.application_run_record, one_dragon.base.operation.operation, one_dragon.base.operation.operation_base
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/application/zzz_application_launcher.py`
- 脚本职责：启动入口脚本：负责参数解析、上下文创建和运行模式切换。
- 关键类/函数：类: ZApplicationLauncher
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.launcher.application_launcher, zzz_od.context.zzz_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/zzz_od/auto_battle/`
说明：自动战斗核心层：状态识别、原子动作与策略执行。

#### 目录：`src/zzz_od/auto_battle/agent_state/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/auto_battle/agent_state/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/agent_state/agent_state_checker.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：函数: get_template, check_cnt_by_color_range, check_exist_by_color_range, check_length_by_background_gray, check_length_by_foreground_gray, check_length_by_foreground_color, check_template_not_found, check_template_found
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils, one_dragon.utils.log_utils, zzz_od.context.zzz_context, zzz_od.game_data.agent；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/auto_battle/atomic_op/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/atomic_op_factory.py`
- 脚本职责：工厂脚本：统一创建应用对象、配置对象或运行记录对象。
- 关键类/函数：类: AtomicOpFactory
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, one_dragon.base.conditional_operation.operation_def, zzz_od.auto_battle.atomic_op.btn_chain_cancel, zzz_od.auto_battle.atomic_op.btn_chain_left
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先理解“工厂=统一创建对象”，你会更快看懂系统如何装配模块。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_chain_cancel.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnChainCancel
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, zzz_od.auto_battle.auto_battle_context, zzz_od.auto_battle.auto_battle_state
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_chain_left.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnChainLeft
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, zzz_od.auto_battle.auto_battle_context, zzz_od.auto_battle.auto_battle_state
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_chain_right.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnChainRight
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, zzz_od.auto_battle.auto_battle_context, zzz_od.auto_battle.auto_battle_state
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_common.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: BtnWayEnum, BtnRunStatus, AtomicBtnCommon
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, one_dragon.base.conditional_operation.operation_def, zzz_od.auto_battle.auto_battle_context, zzz_od.auto_battle.auto_battle_state
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_dodge.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnDodge
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, zzz_od.auto_battle.auto_battle_context, zzz_od.auto_battle.auto_battle_state
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_lock.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnLock
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, zzz_od.auto_battle.auto_battle_context, zzz_od.auto_battle.auto_battle_state
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_move_a.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnMoveA
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, zzz_od.auto_battle.auto_battle_context, zzz_od.auto_battle.auto_battle_state
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_move_d.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnMoveD
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, zzz_od.auto_battle.auto_battle_context, zzz_od.auto_battle.auto_battle_state
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_move_s.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnMoveS
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, zzz_od.auto_battle.auto_battle_context, zzz_od.auto_battle.auto_battle_state
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_move_w.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnMoveW
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, zzz_od.auto_battle.auto_battle_context, zzz_od.auto_battle.auto_battle_state
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_normal_attack.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnNormalAttack
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, zzz_od.auto_battle.auto_battle_context, zzz_od.auto_battle.auto_battle_state
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_quick_assist.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnQuickAssist
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, one_dragon.base.conditional_operation.operation_def, zzz_od.auto_battle.atomic_op.btn_common, zzz_od.auto_battle.auto_battle_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_special_attack.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnSpecialAttack
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, zzz_od.auto_battle.auto_battle_context, zzz_od.auto_battle.auto_battle_state
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_switch_agent.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnSwitchAgent
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, one_dragon.base.conditional_operation.operation_def, zzz_od.auto_battle.atomic_op.btn_common, zzz_od.auto_battle.auto_battle_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_switch_next.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnSwitchNext
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, zzz_od.auto_battle.auto_battle_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_switch_prev.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnSwitchPrev
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, zzz_od.auto_battle.auto_battle_context, zzz_od.auto_battle.auto_battle_state
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/btn_ultimate.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicBtnUltimate
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, zzz_od.auto_battle.auto_battle_context, zzz_od.auto_battle.auto_battle_state
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/state_clear.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicClearState
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, one_dragon.base.conditional_operation.operation_def, zzz_od.auto_battle.auto_battle_custom_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/state_set.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicSetState
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, one_dragon.base.conditional_operation.operation_def, zzz_od.auto_battle.auto_battle_custom_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/turn.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicTurn
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, zzz_od.auto_battle.auto_battle_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/atomic_op/wait.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AtomicWait
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, one_dragon.base.conditional_operation.operation_def
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/auto_battle/target_state/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/auto_battle/target_state/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/auto_battle/target_state/target_state_checker.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: TargetStateChecker
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_pipeline, one_dragon.utils, one_dragon.utils.log_utils, zzz_od.context.zzz_context；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/auto_battle/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/auto_battle/auto_battle_agent_context.py`
- 脚本职责：上下文脚本：集中管理共享状态、服务对象与运行期资源。
- 关键类/函数：类: AgentInfo, TeamInfo, CheckAgentState, AutoBattleAgentContext；函数: _debug_check_agent_in_parallel
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.state_recorder, one_dragon.base.screen.screen_area, one_dragon.utils, one_dragon.utils.log_utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：把它看作“共享工具箱”，很多模块都从这里拿公共能力。

#### 脚本：`src/zzz_od/auto_battle/auto_battle_context.py`
- 脚本职责：上下文脚本：集中管理共享状态、服务对象与运行期资源。
- 关键类/函数：类: AutoBattleContext
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.state_recorder, one_dragon.base.matcher.match_result, one_dragon.base.screen, one_dragon.base.screen.screen_area；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：把它看作“共享工具箱”，很多模块都从这里拿公共能力。

#### 脚本：`src/zzz_od/auto_battle/auto_battle_custom_context.py`
- 脚本职责：上下文脚本：集中管理共享状态、服务对象与运行期资源。
- 关键类/函数：类: AutoBattleCustomContext
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.state_recorder, zzz_od.context.zzz_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它看作“共享工具箱”，很多模块都从这里拿公共能力。

#### 脚本：`src/zzz_od/auto_battle/auto_battle_dodge_context.py`
- 脚本职责：上下文脚本：集中管理共享状态、服务对象与运行期资源。
- 关键类/函数：类: AudioRecorder, YoloStateEventEnum, AutoBattleDodgeContext
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.state_recorder, one_dragon.utils, one_dragon.utils.log_utils, zzz_od.auto_battle.auto_battle_operator；外部库: cv2, librosa, numpy, scipy
- 使用的外部库：cv2, librosa, numpy, scipy, sklearn, soundcard
- 新手理解要点：把它看作“共享工具箱”，很多模块都从这里拿公共能力。

#### 脚本：`src/zzz_od/auto_battle/auto_battle_operator.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AutoBattleOperator；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, one_dragon.base.conditional_operation.loader, one_dragon.base.conditional_operation.operation_def, one_dragon.base.conditional_operation.operator
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/auto_battle/auto_battle_state.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: BattleStateEnum
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/auto_battle/auto_battle_state_record_service.py`
- 脚本职责：服务脚本：提供跨流程复用的能力（下载、数据、调度、推送等）。
- 关键类/函数：类: AutoBattleStateRecordService
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.state_record_service, one_dragon.base.conditional_operation.state_recorder, one_dragon.utils.log_utils, zzz_od.auto_battle.auto_battle_dodge_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/auto_battle/auto_battle_target_context.py`
- 脚本职责：上下文脚本：集中管理共享状态、服务对象与运行期资源。
- 关键类/函数：类: AutoBattleTargetContext
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.state_recorder, one_dragon.utils.log_utils, zzz_od.auto_battle.auto_battle_operator, zzz_od.auto_battle.target_state.target_state_checker；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：把它看作“共享工具箱”，很多模块都从这里拿公共能力。

#### 脚本：`src/zzz_od/auto_battle/auto_battle_utils.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：函数: switch_to_best_agent_for_moving, check_battle_encounter, check_battle_encounter_in_period
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: zzz_od.application.shiyu_defense.agent_selector, zzz_od.auto_battle.auto_battle_dodge_context, zzz_od.context.zzz_context, zzz_od.game_data.agent；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/auto_battle/build_utils.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：函数: build_all_merge
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: zzz_od.application.battle_assistant.auto_battle_config, zzz_od.auto_battle.auto_battle_operator, zzz_od.context.zzz_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/zzz_od/config/`
说明：配置层：将参数与策略从代码中解耦。

#### 脚本：`src/zzz_od/config/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/config/game_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: GamepadTypeEnum, GameConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.basic_game_config, one_dragon.base.config.config_item, one_dragon.base.controller.pc_button.ds4_button_controller, one_dragon.base.controller.pc_button.xbox_button_controller
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

#### 脚本：`src/zzz_od/config/model_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: ModelConfig；函数: get_flash_classifier_opts, get_hollow_zero_event_opts, get_lost_void_det_opts
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.basic_model_config, one_dragon.base.config.config_item, one_dragon.base.web.common_downloader, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

#### 脚本：`src/zzz_od/config/team_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: PredefinedTeamInfo, TeamConfig
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.yaml_config, zzz_od.game_data.agent
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

### 目录：`src/zzz_od/const/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

#### 脚本：`src/zzz_od/const/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/const/game_const.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/zzz_od/context/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

#### 脚本：`src/zzz_od/context/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/context/zzz_context.py`
- 脚本职责：上下文脚本：集中管理共享状态、服务对象与运行期资源。
- 关键类/函数：类: ZContext
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.game_account_config, one_dragon.base.operation.one_dragon_context, zzz_od.application.battle_assistant.auto_battle.auto_battle_app_factory, zzz_od.application.battle_assistant.battle_assistant_config
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：把它看作“共享工具箱”，很多模块都从这里拿公共能力。

### 目录：`src/zzz_od/controller/`
说明：输入与窗口控制层：执行真实点击/按键/截图。

#### 脚本：`src/zzz_od/controller/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/controller/zzz_pc_controller.py`
- 脚本职责：控制脚本：封装键鼠/手柄/窗口/截图等系统交互能力。
- 关键类/函数：类: ZPcController
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.controller.pc_controller_base, one_dragon.utils, zzz_od.config.game_config, zzz_od.const；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：这层直接和系统输入交互，问题常见于权限、窗口焦点、分辨率。

### 目录：`src/zzz_od/game_data/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

#### 脚本：`src/zzz_od/game_data/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/game_data/agent.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AgentTypeEnum, DmgTypeEnum, RareTypeEnum, AgentStateCheckWay, AgentStateDef, CommonAgentStateEnum
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/game_data/compendium.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CompendiumTab, CompendiumCategory, CompendiumMissionType, CompendiumMission, CompendiumData, Coffee
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.utils, one_dragon.utils.log_utils；外部库: yaml
- 使用的外部库：yaml
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/game_data/map_area.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: MapArea, MapAreaService
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils, one_dragon.utils.i18_utils, one_dragon.utils.log_utils；外部库: yaml
- 使用的外部库：yaml
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/game_data/target_state.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: TargetCheckWay, TargetStateDef, DetectionTask
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/zzz_od/gui/`
说明：业务 GUI 层：页面组装与用户操作入口。

#### 目录：`src/zzz_od/gui/view/`
说明：页面层：功能页交互逻辑。

##### 目录：`src/zzz_od/gui/view/accounts/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/gui/view/accounts/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/accounts/app_accounts_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: AccountsInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.widgets.pivot_navi_interface, zzz_od.context.zzz_context, zzz_od.gui.view.setting.zzz_setting_instance_interface；外部库: qfluentwidgets
- 使用的外部库：qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 目录：`src/zzz_od/gui/view/battle_assistant/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/gui/view/battle_assistant/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/battle_assistant/auto_battle_editor_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: TeamSettingCard, AutoBattleEditorInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.utils.i18_utils, one_dragon_qt.widgets.column, one_dragon_qt.widgets.combo_box；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/battle_assistant/auto_battle_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: AutoBattleInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.context_event_bus, one_dragon.utils.i18_utils, one_dragon_qt.utils.config_utils, one_dragon_qt.view.app_run_interface；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/battle_assistant/battle_assistant_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: BattleAssistantInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.widgets.pivot_navi_interface, zzz_od.context.zzz_context, zzz_od.gui.view.battle_assistant.auto_battle_editor_interface, zzz_od.gui.view.battle_assistant.auto_battle_interface；外部库: qfluentwidgets
- 使用的外部库：qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/battle_assistant/battle_state_display.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: StateIndicatorColors, BattleStateDisplay, TaskDisplay
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.state_recorder, one_dragon.utils.i18_utils, zzz_od.context.zzz_context；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/battle_assistant/dodge_assistant_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: DodgeAssistantInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.context_event_bus, one_dragon_qt.view.app_run_interface, one_dragon_qt.widgets.column, one_dragon_qt.widgets.setting_card.combo_box_setting_card；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/battle_assistant/operation_debug_interface.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: OperationDebugInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.view.app_run_interface, one_dragon_qt.widgets.column, one_dragon_qt.widgets.setting_card.combo_box_setting_card, one_dragon_qt.widgets.setting_card.editable_combo_box_setting_card；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 目录：`src/zzz_od/gui/view/devtools/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/gui/view/devtools/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/devtools/app_devtools_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: AppDevtoolsInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.view.devtools.devtools_image_analysis_interface, one_dragon_qt.view.devtools.devtools_screen_manage_interface, one_dragon_qt.view.devtools.devtools_template_helper_interface, one_dragon_qt.widgets.pivot_navi_interface；外部库: qfluentwidgets
- 使用的外部库：qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/devtools/devtools_screenshot_helper_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: DevtoolsScreenshotHelperInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon_qt.utils.config_utils, one_dragon_qt.view.app_run_interface, one_dragon_qt.widgets.column；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/devtools/icon_editor_dialog.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: IconEditorDialog
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: zzz_od.application.world_patrol.world_patrol_area；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 目录：`src/zzz_od/gui/view/game_assistant/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/gui/view/game_assistant/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/game_assistant/commission_assistant_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: CommissionAssistantRunInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon_qt.utils.config_utils, one_dragon_qt.view.app_run_interface, one_dragon_qt.widgets.row；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/game_assistant/game_assistant_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: GameAssistantInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.widgets.pivot_navi_interface, zzz_od.context.zzz_context, zzz_od.gui.view.game_assistant.commission_assistant_interface, zzz_od.gui.view.game_assistant.life_on_line_run_interface；外部库: qfluentwidgets
- 使用的外部库：qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/game_assistant/life_on_line_run_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: LifeOnLineRunInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.operation.application, one_dragon_qt.utils.config_utils, one_dragon_qt.view.app_run_interface；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/game_assistant/mouse_sensitivity_checker_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: MouseSensitivityCheckerInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.view.app_run_interface, zzz_od.application.game_config_checker, zzz_od.application.zzz_application, zzz_od.context.zzz_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/game_assistant/predefined_team_checker_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: PredefinedTeamCheckerInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.view.app_run_interface, one_dragon_qt.widgets.column, one_dragon_qt.widgets.setting_card.help_card, zzz_od.application.game_config_checker；外部库: PySide6
- 使用的外部库：PySide6
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 目录：`src/zzz_od/gui/view/hollow_zero/`
说明：空洞玩法层：事件识别、路径与战斗交互。

###### 脚本：`src/zzz_od/gui/view/hollow_zero/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/hollow_zero/hollow_zero_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: HollowZeroInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.widgets.pivot_navi_interface, zzz_od.context.zzz_context, zzz_od.gui.view.hollow_zero.lost_void_challenge_config_interface, zzz_od.gui.view.hollow_zero.lost_void_run_interface；外部库: qfluentwidgets
- 使用的外部库：qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/hollow_zero/lost_void_challenge_config_interface.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: LostVoidChallengeConfigInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.utils.i18_utils, one_dragon_qt.widgets.column, one_dragon_qt.widgets.combo_box；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

###### 脚本：`src/zzz_od/gui/view/hollow_zero/lost_void_run_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: LostVoidRunInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.operation.application, one_dragon.utils.log_utils, one_dragon_qt.utils.config_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/hollow_zero/withered_domain_challenge_config_interface.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: WitheredDomainChallengeConfigInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.utils.i18_utils, one_dragon_qt.widgets.column, one_dragon_qt.widgets.combo_box；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

###### 脚本：`src/zzz_od/gui/view/hollow_zero/withered_domain_run_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: WitheredDomainRunInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.operation.application, one_dragon.utils.log_utils, one_dragon_qt.utils.config_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 目录：`src/zzz_od/gui/view/home/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/gui/view/home/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/home/home_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ButtonGroup, BaseThread, CheckRunner, BackgroundImageDownloader, HomeInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.custom_config, one_dragon.utils, one_dragon.utils.log_utils, one_dragon_qt.services.theme_manager；外部库: PySide6, qfluentwidgets, requests
- 使用的外部库：PySide6, qfluentwidgets, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 目录：`src/zzz_od/gui/view/installer/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/gui/view/installer/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/installer/extend_install_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ExtendInstallInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.utils.i18_utils, one_dragon_qt.widgets.log_display_card, one_dragon_qt.widgets.vertical_scroll_interface；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/installer/gamepad_install_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: GamepadInstallCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.utils, one_dragon.utils.i18_utils, one_dragon.utils.log_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 目录：`src/zzz_od/gui/view/one_dragon/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/gui/view/one_dragon/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/one_dragon/charge_plan_dialog.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ChargePlanDialog
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils, zzz_od.application.charge_plan.charge_plan_config, zzz_od.context.zzz_context, zzz_od.gui.view.one_dragon.charge_plan_interface；外部库: qfluentwidgets
- 使用的外部库：qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/one_dragon/charge_plan_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ChargePlanCard, ChargePlanInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.operation.application, one_dragon.utils.i18_utils, one_dragon_qt.utils.config_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/one_dragon/coffee_plan_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: CoffeePlanInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.operation.application.application_const, one_dragon_qt.utils.config_utils, one_dragon_qt.widgets.column；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/one_dragon/notorious_hunt_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ChargePlanCard, NotoriousHuntPlanInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.operation.application, one_dragon.utils.i18_utils, one_dragon_qt.widgets.column；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/one_dragon/setting_team_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: TeamSettingCard, SettingTeamInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon_qt.widgets.column, one_dragon_qt.widgets.combo_box, one_dragon_qt.widgets.editable_combo_box；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/one_dragon/shiyu_defense_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ShiyuDefenseInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.utils.i18_utils, one_dragon_qt.widgets.column, one_dragon_qt.widgets.setting_card.push_setting_card；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/one_dragon/suibian_temple_setting_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: SuibianTempleSettingInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.operation.application, one_dragon_qt.utils.config_utils, one_dragon_qt.widgets.column；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/one_dragon/zzz_one_dragon_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ZOneDragonInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.widgets.pivot_navi_interface, one_dragon_qt.widgets.setting_card.app_run_card, zzz_od.context.zzz_context, zzz_od.gui.view.one_dragon.charge_plan_interface；外部库: qfluentwidgets
- 使用的外部库：qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/one_dragon/zzz_one_dragon_run_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ZOneDragonRunInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.view.one_dragon.one_dragon_run_interface, zzz_od.context.zzz_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/one_dragon/zzz_one_dragon_setting_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ZOneDragonSettingInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.utils.i18_utils, one_dragon_qt.utils.config_utils, one_dragon_qt.widgets.column；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 目录：`src/zzz_od/gui/view/setting/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/gui/view/setting/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/setting/app_setting_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: AppSettingInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.view.setting.setting_custom_interface, one_dragon_qt.view.setting.setting_env_interface, one_dragon_qt.view.setting.setting_push_interface, one_dragon_qt.widgets.pivot_navi_interface；外部库: qfluentwidgets
- 使用的外部库：qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/setting/setting_game_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: SettingGameInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.basic_game_config, one_dragon.base.controller.pc_button.ds4_button_controller, one_dragon.base.controller.pc_button.xbox_button_controller, one_dragon.utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/setting/zzz_resource_download_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ZResourceDownloadInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.web.common_downloader, one_dragon_qt.view.setting.resource_download_interface, one_dragon_qt.widgets.download_card.onnx_model_download_card, zzz_od.config.model_config；外部库: qfluentwidgets
- 使用的外部库：qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/setting/zzz_setting_instance_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ZSettingInstanceInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_context, one_dragon_qt.view.setting.setting_instance_interface
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 目录：`src/zzz_od/gui/view/world_patrol/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

###### 脚本：`src/zzz_od/gui/view/world_patrol/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/world_patrol/route_operation_editor_dialog.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: RouteOperationEditorDialog
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: zzz_od.application.world_patrol.world_patrol_route；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

###### 脚本：`src/zzz_od/gui/view/world_patrol/world_patrol_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: WorldPatrolInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.widgets.pivot_navi_interface, zzz_od.context.zzz_context, zzz_od.gui.view.world_patrol.world_patrol_large_map_recorder_interface, zzz_od.gui.view.world_patrol.world_patrol_route_list_interface；外部库: qfluentwidgets
- 使用的外部库：qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/world_patrol/world_patrol_large_map_recorder_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: LargeMapRecorderInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.geometry.point, one_dragon.base.matcher.match_result, one_dragon.base.operation.context_event_bus；外部库: PySide6, cv2, qfluentwidgets
- 使用的外部库：PySide6, cv2, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/world_patrol/world_patrol_route_list_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: WorldPatrolRouteListInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.utils.log_utils, one_dragon_qt.widgets.combo_box, one_dragon_qt.widgets.editable_combo_box；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/world_patrol/world_patrol_route_recorder_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: DebugRouteRunner, WorldPatrolRouteRecorderInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.geometry.point, one_dragon.base.matcher.match_result, one_dragon.base.operation.context_event_bus；外部库: PySide6, cv2, qfluentwidgets
- 使用的外部库：PySide6, cv2, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

###### 脚本：`src/zzz_od/gui/view/world_patrol/world_patrol_run_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: WorldPatrolRunInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.operation.application, one_dragon.utils.log_utils, one_dragon_qt.utils.config_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/gui/view/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/gui/widgets/`
说明：控件层：可复用 UI 组件。

##### 脚本：`src/zzz_od/gui/widgets/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/gui/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/gui/app.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_context, one_dragon.utils, one_dragon.utils.i18_utils, one_dragon.utils.log_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/gui/zzz_installer.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.utils.i18_utils, one_dragon_qt.app.directory_picker, zzz_od.gui.zzz_installer_window；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/gui/zzz_installer_window.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ZInstallerWindow
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon_qt.app.installer, one_dragon_qt.view.installer_interface, one_dragon_qt.view.source_config_interface
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/zzz_od/hollow_zero/`
说明：空洞玩法层：事件识别、路径与战斗交互。

#### 目录：`src/zzz_od/hollow_zero/event/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/hollow_zero/event/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/bamboo_merchant.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: BambooMerchant；函数: __debug_check_screen
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.matcher.match_result, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/call_for_support.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: RejectOption, CallForSupport；函数: __debug, __debug_support_agent, __debug_current_agent, __debug_check_screen
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.rectangle, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/choose_resonium.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ChooseResonium；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/confirm_resonium.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ConfirmResonium
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils, zzz_od.context.zzz_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/critical_stage.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: CriticalStage
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/door_battle.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: DoorBattle
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, zzz_od.context.zzz_context, zzz_od.hollow_zero.event
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/drop_resonium.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: DropResoniumBase, DropResonium, DropResonium2
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/event_ocr_result_handler.py`
- 脚本职责：识别脚本：负责 OCR、目标检测或模板匹配能力封装。
- 关键类/函数：类: EventOcrResultHandler
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.rectangle, one_dragon.base.operation.operation_round_result
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：这层是“看懂画面”的关键，模型文件、阈值、输入尺寸很重要。

##### 脚本：`src/zzz_od/hollow_zero/event/full_in_bag.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: FullInBag；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/hollow_event_utils.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：函数: check_event_at_right, check_entry_opt_at_right, check_entry_opt_pos_at_right, check_event_text_and_run, click_empty, click_rect, get_event_text_area, run_event_handler
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.base.matcher.match_result, one_dragon.base.operation.operation_round_result；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/hollow_interact.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: HollowInteract
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils, zzz_od.context.zzz_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/leave_random_zone.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: LeaveRandomZone
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils, zzz_od.context.zzz_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/normal_event_handler.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: NormalEventHandler；函数: __debug_opts
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/old_capital.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: OldCapital
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils, zzz_od.context.zzz_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/remove_corruption.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: RemoveCorruption
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils, zzz_od.context.zzz_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/resonium_utils.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：函数: get_to_choose_list, choose_resonium_by_priority
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.matcher.match_result, one_dragon.utils, one_dragon.utils.i18_utils, zzz_od.context.zzz_context；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/swift_supply.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: SwiftSupply
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils, zzz_od.context.zzz_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/switch_resonium.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: SwitchResonium；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/event/upgrade_resonium.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: UpgradeResonium
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/hollow_zero/game_data/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/hollow_zero/game_data/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/game_data/hollow_zero_event.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: HollowZeroEntry, HallowZeroNormalEventOption, HallowZeroEvent, HollowZeroSpecialEvent
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/game_data/hollow_zero_resonium.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: Resonium
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/zzz_od/hollow_zero/hollow_map/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/hollow_zero/hollow_map/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/hollow_map/hollow_map_utils.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：函数: construct_map_from_yolo_result, construct_map_from_nodes, _at_left, _at_right, _above, _under, _is_same_row, _is_same_col
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.rectangle, one_dragon.utils, one_dragon.yolo.detect_utils, zzz_od.context.zzz_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/hollow_map/hollow_pathfinding.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：函数: search_map, _bfs_search_map, get_route_in_1_step, get_route_by_entry, get_route_by_direction, had_been_visited, draw_map
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.utils, zzz_od.hollow_zero.hollow_map.hollow_map_utils, zzz_od.hollow_zero.hollow_map.hollow_zero_map；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/hollow_map/hollow_zero_map.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: HollowZeroMapNode, HollowZeroMap
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.rectangle, one_dragon.utils.log_utils, zzz_od.hollow_zero.game_data.hollow_zero_event
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/zzz_od/hollow_zero/hollow_map/hollow_zero_map_service.py`
- 脚本职责：服务脚本：提供跨流程复用的能力（下载、数据、调度、推送等）。
- 关键类/函数：类: HollowZeroMapService；函数: __debug_cal_current_map_by_screen
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils, one_dragon.utils.log_utils, zzz_od.context.zzz_context, zzz_od.hollow_zero.hollow_map；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/hollow_zero/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/hollow_zero/hollow_battle.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: HollowBattle；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.rectangle, one_dragon.base.operation.operation, one_dragon.base.operation.operation_base, one_dragon.base.operation.operation_edge；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/hollow_zero/hollow_exit_by_menu.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: HollowExitByMenu
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/hollow_zero/hollow_level_info.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: HollowLevelInfo
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/hollow_zero/hollow_runner.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: HollowRunner；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.base.operation.application, one_dragon.base.operation.operation_edge；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/hollow_zero/hollow_zero_challenge_config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: HollowZeroChallengePathFinding, HollowZeroChallengeConfig；函数: get_all_hollow_zero_challenge_config, get_hollow_zero_challenge_new_name
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.config.yaml_config, one_dragon.utils, one_dragon.utils.log_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

#### 脚本：`src/zzz_od/hollow_zero/hollow_zero_data_service.py`
- 脚本职责：服务脚本：提供跨流程复用的能力（下载、数据、调度、推送等）。
- 关键类/函数：类: HallowZeroDataService
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils, one_dragon.utils.i18_utils, one_dragon.utils.log_utils, zzz_od.hollow_zero.game_data.hollow_zero_event；外部库: yaml
- 使用的外部库：yaml
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/zzz_od/operation/`
说明：步骤节点层：封装可调度的自动化动作。

#### 目录：`src/zzz_od/operation/arcade/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/operation/arcade/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/arcade/arcade_snake_suicide.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: ArcadeSnakeSuicide
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/arcade/arcade_start_game.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: ArcadeStartGame
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 目录：`src/zzz_od/operation/challenge_mission/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/operation/challenge_mission/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/challenge_mission/check_next_after_battle.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: ChooseNextOrFinishAfterBattle
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/challenge_mission/exit_in_battle.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: ExitInBattle
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/challenge_mission/restart_in_battle.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: RestartInBattle；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 目录：`src/zzz_od/operation/compendium/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/operation/compendium/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/compendium/area_patrol.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: AreaPatrol；函数: __debug_charge, __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.application, one_dragon.base.operation.operation, one_dragon.base.operation.operation_edge
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/compendium/combat_simulation.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: CombatSimulation；函数: __debug_coffee, __debug_charge, __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.application, one_dragon.base.operation.operation, one_dragon.base.operation.operation_edge
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/compendium/compendium_choose_category.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: CompendiumChooseCategory；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/compendium/compendium_choose_mission_type.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: MissionTypeTargetWrapper, CompendiumChooseMissionType；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.geometry.rectangle, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/compendium/compendium_choose_tab.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: CompendiumChooseTab；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/compendium/coupon.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: Coupon；函数: __debug_charge
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.application, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/compendium/expert_challenge.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: ExpertChallenge；函数: __debug_charge, __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.operation, one_dragon.base.operation.operation_base, one_dragon.base.operation.operation_edge
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/compendium/notorious_hunt.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: NotoriousHunt；函数: __debug_charge, __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.matcher.match_result, one_dragon.base.operation.application, one_dragon.base.operation.operation
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/compendium/open_compendium.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: OpenCompendium
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/compendium/tp_by_compendium.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: TransportByCompendium；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 目录：`src/zzz_od/operation/enter_game/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/operation/enter_game/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/enter_game/auto_hdr.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: DisableAutoHDR, EnableAutoHDR
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/enter_game/enter_game.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: EnterGame；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.basic_game_config, one_dragon.base.config.game_account_config, one_dragon.base.config.one_dragon_config, one_dragon.base.controller.pc_clipboard；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/enter_game/open_and_enter_game.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: OpenAndEnterGame
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_notify
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/enter_game/open_game.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: OpenGame
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/enter_game/switch_account.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: SwitchAccount；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 目录：`src/zzz_od/operation/goto/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/operation/goto/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/goto/goto_menu.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: GotoMenu
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils, zzz_od.context.zzz_context；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 目录：`src/zzz_od/operation/hdd/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/zzz_od/operation/hdd/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

##### 脚本：`src/zzz_od/operation/hdd/enter_hdd_mission.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: EnterHddMission
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 脚本：`src/zzz_od/operation/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 脚本：`src/zzz_od/operation/back_to_normal_world.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: BackToNormalWorld；函数: __debug_op, _debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils, one_dragon.utils.i18_utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 脚本：`src/zzz_od/operation/choose_predefined_team.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: ChoosePredefinedTeam；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.matcher.match_result, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 脚本：`src/zzz_od/operation/deploy.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: Deploy；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 脚本：`src/zzz_od/operation/eat_noodle.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: EatNoodle
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 脚本：`src/zzz_od/operation/key_sim_runner.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: KeySimRunner
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.conditional_operation.atomic_op, one_dragon.base.conditional_operation.operation_def, one_dragon.base.config.yaml_config, one_dragon.base.operation.operation_edge
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 脚本：`src/zzz_od/operation/restore_charge.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: RestoreCharge；函数: __debug_charge, __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.application, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 脚本：`src/zzz_od/operation/transport.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: Transport；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.point, one_dragon.base.operation.operation_edge, one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 脚本：`src/zzz_od/operation/wait_normal_world.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: WaitNormalWorld
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation_node, one_dragon.base.operation.operation_round_result, one_dragon.utils.i18_utils, zzz_od.context.zzz_context
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

#### 脚本：`src/zzz_od/operation/zzz_operation.py`
- 脚本职责：操作脚本：实现可复用自动化步骤节点。
- 关键类/函数：类: ZOperation
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.operation, one_dragon.base.operation.operation_base, zzz_od.context.zzz_context, zzz_od.operation.enter_game.open_and_enter_game
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：按“输入-处理-输出”读最容易：先看它依赖什么，再看它产出什么动作。

### 目录：`src/zzz_od/screen_area/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

#### 脚本：`src/zzz_od/screen_area/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/screen_area/screen_normal_world.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ScreenNormalWorldEnum
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.geometry.rectangle, one_dragon.base.screen.screen_area
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/zzz_od/telemetry/`
说明：遥测层：事件采集、性能监控、隐私控制。

#### 脚本：`src/zzz_od/telemetry/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/telemetry/aliyun_web_tracking.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AliyunWebTrackingClient
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.log_utils；外部库: requests
- 使用的外部库：requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/telemetry/auto_telemetry.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AutoTelemetryMixin, TelemetryApplicationMixin, TelemetryInterfaceMixin, TelemetryOperationMixin；函数: auto_telemetry_method
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/telemetry/config.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: TelemetryConfigLoader, PrivacySettingsManager
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: , yaml
- 使用的外部库：, yaml
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

#### 脚本：`src/zzz_od/telemetry/data_sanitizer.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: DataSanitizer
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/telemetry/error_tracker.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ErrorTracker
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: 
- 使用的外部库：
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/telemetry/event_collector.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: EventCollector
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: 
- 使用的外部库：
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/telemetry/event_formatter.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: LokiLogEntry, EventFormatConfig, EventFormatter, LabelStrategy
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: 
- 使用的外部库：
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/telemetry/hollow_telemetry.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: HollowTelemetryMixin；函数: track_hollow_level_progress
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/telemetry/loki_client.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: LokiClient
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.log_utils；外部库: , requests
- 使用的外部库：, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/telemetry/models.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: TelemetryEvent, ErrorEvent, PerformanceEvent, TelemetryConfig, PrivacySettings
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/telemetry/performance_monitor.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: PerformanceMetrics, TimingRecord, PerformanceMonitor, PerformanceContext；函数: get_global_monitor, monitor_performance
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/telemetry/privacy_controller.py`
- 脚本职责：控制脚本：封装键鼠/手柄/窗口/截图等系统交互能力。
- 关键类/函数：类: PrivacyController
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: 
- 使用的外部库：
- 新手理解要点：这层直接和系统输入交互，问题常见于权限、窗口焦点、分辨率。

#### 脚本：`src/zzz_od/telemetry/telemetry_manager.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: TelemetryManager, _AliyunTelemetryAdapter
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.game_account_config, one_dragon.utils, one_dragon.utils.log_utils；外部库: 
- 使用的外部库：
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/telemetry/ui_support.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: TelemetryUISupport
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: 
- 使用的外部库：
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/zzz_od/utils/`
说明：通用工具层：日志、字符串、文件、线程等。

#### 脚本：`src/zzz_od/utils/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/zzz_od/win_exe/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

#### 脚本：`src/zzz_od/win_exe/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/win_exe/launcher.py`
- 脚本职责：启动入口脚本：负责参数解析、上下文创建和运行模式切换。
- 关键类/函数：类: ZLauncher
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.devtools, one_dragon.launcher.exe_launcher, one_dragon.version
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/zzz_od/yolo/`
说明：YOLO 模型封装层：检测与分类能力。

#### 脚本：`src/zzz_od/yolo/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/yolo/flash_classifier.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: FlashClassifier；函数: __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils, one_dragon.yolo.yolo_utils, one_dragon.yolo.yolov8_onnx_cls
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/zzz_od/yolo/hollow_event_detector.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: HollowEventDetector
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils, one_dragon.yolo.yolo_utils, one_dragon.yolo.yolov8_onnx_det
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`src/zzz_od/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。
