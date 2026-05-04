# 06 DFS-资源与配置数据-assets-config-service

## 目录：`assets/`
说明：运行资源总仓（当前约 1449 个文件），核心作用是“把识别能力和业务数据配置化”。

### 技术：模板资源体系（`assets/template/`）
- 技术是什么：`raw.png + mask.png + config.yml` 的模板匹配资产。
- 为什么用：把“识别目标”从代码拆到资源，便于快速迭代。
- 仓库里在哪里：`assets/template/**`。
- 对项目价值：调优识别时优先改资源，不必频繁改逻辑。

### 技术：游戏静态数据（`assets/game_data/`）
- 技术是什么：角色、关卡、空洞事件、地图区域等 YAML 数据。
- 为什么用：以数据驱动业务流程，减少硬编码。
- 仓库里在哪里：`assets/game_data/**`。
- 对项目价值：新增内容时可先补数据，再补逻辑。

### 技术：屏幕语义定义（`assets/game_data/screen_info/`）
- 技术是什么：页面、区域、按钮与锚点的结构化描述。
- 为什么用：自动化系统先理解“画面结构”再执行动作。
- 仓库里在哪里：`assets/game_data/screen_info/*.yml`。
- 对项目价值：识别与导航逻辑可读、可维护。

### 技术：图像分析流水线配置（`assets/image_analysis_pipelines/`）
- 技术是什么：CV 步骤参数（阈值、形态学、轮廓筛选、OCR步骤）。
- 为什么用：让图像算法流程可配置、可快速试错。
- 仓库里在哪里：`assets/image_analysis_pipelines/*.yml`。
- 对项目价值：无需改代码即可快速调参。

### 技术：多语言资源（`assets/text/`）
- 技术是什么：`po/mo` 文本资源。
- 为什么用：支持多语言界面和提示。
- 仓库里在哪里：`assets/text/**`。
- 对项目价值：提升可用范围。

## 目录：`config/`
说明：用户配置与样例模板目录（当前约 479 个文件）。

### 技术：样例模板（`.sample.yml`）
- 技术是什么：可复制后直接改参数的配置模板。
- 为什么用：降低新手配置门槛。
- 仓库里在哪里：`config/**/*.sample.yml`。
- 对项目价值：减少格式错误，提高上手效率。

### 技术：策略数据配置
- 技术是什么：路线配置、挑战配置、自动战斗状态处理配置等。
- 为什么用：同一套代码支持不同玩法与偏好。
- 仓库里在哪里：`config/world_patrol_route*`、`config/hollow_zero_challenge*`、`config/auto_battle_state_handler*` 等。
- 对项目价值：功能扩展优先改配置，维护成本更低。

### 技术：项目级元配置
- 技术是什么：项目基础参数与格式化辅助。
- 为什么用：统一分辨率、仓库地址、下载源、公告地址等。
- 仓库里在哪里：`config/project.yml`、`config/format.py`。
- 对项目价值：减少硬编码，提高可迁移性。

## 目录：`service/`（核心脚本逐个讲）
说明：该目录为运行链路中的独立服务脚本，这里按核心模板逐脚本说明。

### 脚本：`service/zzz_base_scheduler.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: apscheduler, zzz_syn_battle_service
- 使用的外部库：apscheduler, zzz_syn_battle_service
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`service/zzz_data_model.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: BattleInfo；函数: get_db_session, get_battle_info, get_battle_url, get_battle_by_name, clear_battle_info_table
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: sqlalchemy
- 使用的外部库：sqlalchemy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`service/zzz_save_battle_class.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: fastapi, requests, yaml, zzz_data_model
- 使用的外部库：fastapi, requests, yaml, zzz_data_model
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`service/zzz_shared_battle_service.py`
- 脚本职责：服务脚本：提供跨流程复用的能力（下载、数据、调度、推送等）。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: fastapi, uvicorn, zzz_data_model, zzz_save_battle_class
- 使用的外部库：fastapi, uvicorn, zzz_data_model, zzz_save_battle_class
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`service/zzz_syn_battle_service.py`
- 脚本职责：服务脚本：提供跨流程复用的能力（下载、数据、调度、推送等）。
- 关键类/函数：类: SynBattle；函数: file_name_tool
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: requests, zzz_data_model, zzz_save_battle_class
- 使用的外部库：requests, zzz_data_model, zzz_save_battle_class
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。
