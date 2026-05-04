# 04 DFS-核心运行层-one_dragon_qt-onnxocr

> 说明：本卷采用“目录前序 DFS + 同级字典序”，核心脚本逐文件讲解。

## 目录：`src/one_dragon_qt/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

### 目录：`src/one_dragon_qt/_rc/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

#### 目录：`src/one_dragon_qt/_rc/qss/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 目录：`src/one_dragon_qt/_rc/qss/dark/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 目录：`src/one_dragon_qt/_rc/qss/light/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

#### 脚本：`src/one_dragon_qt/_rc/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/_rc/resource.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：函数: qInitResources, qCleanupResources
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PySide6
- 使用的外部库：PySide6
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/one_dragon_qt/app/`
说明：运行入口层：创建窗口与应用主流程。

#### 目录：`src/one_dragon_qt/app/devtools/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/one_dragon_qt/app/devtools/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/app/devtools/devtools_app.py`
- 脚本职责：应用脚本：组织某个功能的完整流程（识别-决策-执行）。
- 关键类/函数：类: DevtoolsAppWindow；函数: create_devtools_app
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_context, one_dragon.utils.i18_utils, one_dragon_qt.app.devtools.image_processing_interface, one_dragon_qt.services.styles_manager；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：把它当“总导演”即可：它调度多个步骤，不会把细节全写在一个文件。

##### 脚本：`src/one_dragon_qt/app/devtools/image_matting_interface.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ImageMattingInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_context, one_dragon.utils, one_dragon.utils.i18_utils, one_dragon_qt.widgets.click_image_label；外部库: PySide6, cv2, numpy, qfluentwidgets
- 使用的外部库：PySide6, cv2, numpy, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/app/devtools/image_processing_interface.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ImageProcessingInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_context, one_dragon_qt.app.devtools.image_matting_interface, one_dragon_qt.app.devtools.image_stitching_interface, one_dragon_qt.widgets.pivot_navi_interface；外部库: qfluentwidgets
- 使用的外部库：qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/app/devtools/image_stitching_interface.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ImageStitchingInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_context, one_dragon.utils, one_dragon.utils.log_utils, one_dragon_qt.widgets.image_viewer_widget；外部库: PySide6, cv2, numpy, qfluentwidgets
- 使用的外部库：PySide6, cv2, numpy, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/app/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/app/directory_picker.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: DirectoryPickerTranslator, DirectoryPickerInterface, DirectoryPickerWindow
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.services.styles_manager, one_dragon_qt.utils.image_utils, one_dragon_qt.windows.window；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/app/installer.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: InstallerWindowBase
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.utils, one_dragon.version, one_dragon_qt.services.styles_manager；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/one_dragon_qt/logic/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

#### 脚本：`src/one_dragon_qt/logic/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/logic/image_analysis_logic.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ImageAnalysisLogic
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_code_generator, one_dragon.base.cv_process.cv_pipeline, one_dragon.base.cv_process.cv_step, one_dragon.base.operation.one_dragon_context；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/one_dragon_qt/mixins/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

#### 脚本：`src/one_dragon_qt/mixins/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/mixins/history_mixin.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: HistoryMixin
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils, one_dragon_qt.widgets.setting_card.multi_push_setting_card；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/one_dragon_qt/services/`
说明：UI 服务层：主题、样式等基础服务。

#### 脚本：`src/one_dragon_qt/services/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/services/styles_manager.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: OdQtStyleSheet
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: , qfluentwidgets
- 使用的外部库：, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/services/theme_manager.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ThemeManager
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/one_dragon_qt/utils/`
说明：通用工具层：日志、字符串、文件、线程等。

#### 脚本：`src/one_dragon_qt/utils/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/utils/color_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：类: ColorUtils
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PySide6
- 使用的外部库：PySide6
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/utils/config_utils.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：函数: get_prop_adapter
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.yaml_operator, one_dragon_qt.widgets.setting_card.yaml_config_adapter
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

#### 脚本：`src/one_dragon_qt/utils/image_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：函数: _scale_image_object_for_high_dpi, scale_pixmap_for_high_dpi, scale_image_for_high_dpi
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PySide6
- 使用的外部库：PySide6
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/utils/layout_utils.py`
- 脚本职责：工具脚本：提供通用函数，支撑其他模块复用。
- 关键类/函数：类: Margins, IconSize
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/one_dragon_qt/view/`
说明：页面层：功能页交互逻辑。

#### 目录：`src/one_dragon_qt/view/devtools/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/one_dragon_qt/view/devtools/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/view/devtools/devtools_image_analysis_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: PipelineNameDialog, DevtoolsImageAnalysisInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.cv_process.cv_step, one_dragon.base.operation.one_dragon_context, one_dragon.utils.i18_utils, one_dragon_qt.logic.image_analysis_logic；外部库: PySide6, numpy, qfluentwidgets
- 使用的外部库：PySide6, numpy, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/view/devtools/devtools_screen_manage_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ScreenInfoWorker, DevtoolsScreenManageInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.geometry.rectangle, one_dragon.base.operation.one_dragon_context, one_dragon.base.screen.screen_area；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/view/devtools/devtools_template_helper_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: DevtoolsTemplateHelperInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.geometry.point, one_dragon.base.operation.one_dragon_context, one_dragon.base.screen.template_info；外部库: PySide6, cv2, qfluentwidgets
- 使用的外部库：PySide6, cv2, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/one_dragon_qt/view/one_dragon/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/one_dragon_qt/view/one_dragon/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/view/one_dragon/one_dragon_run_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: OneDragonRunInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.one_dragon_config, one_dragon.base.operation.application, one_dragon.base.operation.application.application_group_config, one_dragon.base.operation.application_base；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/one_dragon_qt/view/setting/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/one_dragon_qt/view/setting/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/view/setting/resource_download_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ResourceDownloadInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.basic_model_config, one_dragon.base.operation.one_dragon_context, one_dragon.base.web.common_downloader, one_dragon.utils.i18_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/view/setting/setting_custom_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: SettingCustomInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.custom_config, one_dragon.base.operation.one_dragon_context, one_dragon.utils, one_dragon.utils.i18_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/view/setting/setting_env_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: SettingEnvInterface, SpeedTestRunnerBase, PythonSourceSpeedTestThread, PipSourceSpeedTestThread
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_context, one_dragon.envs.env_config, one_dragon.utils.i18_utils, one_dragon_qt.widgets.setting_card.combo_box_setting_card；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/view/setting/setting_instance_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: InstanceSettingCard, SettingInstanceInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.game_account_config, one_dragon.base.config.one_dragon_config, one_dragon.base.operation.one_dragon_context, one_dragon.utils.i18_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/view/setting/setting_push_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: SettingPushInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.controller.pc_clipboard, one_dragon.base.operation.one_dragon_context, one_dragon.base.push.curl_generator；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/view/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/view/app_run_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: AppRunner, AppRunInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application, one_dragon.base.operation.application.application_run_context, one_dragon.base.operation.application_base, one_dragon.base.operation.context_event_bus；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/view/code_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: FetchTotalRunner, FetchPageRunner, CodeInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.envs.git_service, one_dragon.utils.app_utils, one_dragon.utils.i18_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/view/context_event_signal.py`
- 脚本职责：上下文脚本：集中管理共享状态、服务对象与运行期资源。
- 关键类/函数：类: ContextEventSignal
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PySide6
- 使用的外部库：PySide6
- 新手理解要点：把它看作“共享工具箱”，很多模块都从这里拿公共能力。

#### 脚本：`src/one_dragon_qt/view/installer_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: UnpackResourceRunner, ClickableStepCircle, StepIndicator, InstallStepWidget, InstallerInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.utils, one_dragon.utils.i18_utils, one_dragon.utils.log_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/view/like_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: LikeInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.utils, one_dragon.utils.i18_utils, one_dragon_qt.widgets.column；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/view/source_config_interface.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: SourceConfigInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.envs.env_config, one_dragon.utils.i18_utils, one_dragon_qt.widgets.column；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

### 目录：`src/one_dragon_qt/widgets/`
说明：控件层：可复用 UI 组件。

#### 目录：`src/one_dragon_qt/widgets/download_card/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/one_dragon_qt/widgets/download_card/launcher_download_card.py`
- 脚本职责：启动入口脚本：负责参数解析、上下文创建和运行模式切换。
- 关键类/函数：类: LauncherVersionChecker, LauncherDownloadCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.operation.one_dragon_env_context, one_dragon.base.web.common_downloader, one_dragon.envs.env_config；外部库: PySide6, packaging, qfluentwidgets
- 使用的外部库：PySide6, packaging, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/download_card/onnx_model_download_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: OnnxModelDownloadCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_context, one_dragon_qt.widgets.setting_card.common_download_card；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/one_dragon_qt/widgets/install_card/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/one_dragon_qt/widgets/install_card/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/install_card/all_install_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: AllInstallCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.utils, one_dragon.utils.i18_utils, one_dragon.utils.log_utils；外部库: qfluentwidgets
- 使用的外部库：qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/install_card/base_install_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: InstallRunner, DisplayChecker, BaseInstallCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.utils.i18_utils, one_dragon.utils.log_utils, one_dragon_qt.widgets.setting_card.multi_push_setting_card；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/install_card/code_install_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: CodeInstallCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.envs.env_config, one_dragon.utils.i18_utils, one_dragon_qt.widgets.combo_box；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/install_card/launcher_install_card.py`
- 脚本职责：启动入口脚本：负责参数解析、上下文创建和运行模式切换。
- 关键类/函数：类: LauncherInstallCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.base.web.common_downloader, one_dragon.base.web.zip_downloader, one_dragon.envs.env_config；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/install_card/python_install_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: PythonInstallCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.envs.env_config, one_dragon.utils.i18_utils, one_dragon_qt.widgets.install_card.wtih_existed_install_card；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/install_card/uv_install_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: UVInstallCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.envs.env_config, one_dragon.utils.i18_utils, one_dragon_qt.widgets.install_card.wtih_existed_install_card；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/install_card/venv_install_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: VenvInstallCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.utils.i18_utils, one_dragon_qt.widgets.install_card.base_install_card；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/install_card/wtih_existed_install_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: WithExistedInstallCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.one_dragon_env_context, one_dragon.utils, one_dragon.utils.i18_utils, one_dragon.utils.log_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 目录：`src/one_dragon_qt/widgets/setting_card/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/app_run_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: AppRunCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.operation.application.application_group_config, one_dragon.base.operation.application_run_record, one_dragon.utils.i18_utils, one_dragon_qt.widgets.setting_card.multi_push_setting_card；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/check_box_setting_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: CheckBoxSettingCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils, one_dragon_qt.utils.layout_utils, one_dragon_qt.widgets.setting_card.setting_card_base；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/code_editor_setting_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: TemplateVariables, TemplateVariableMenu, LineNumberArea, CodeEditor, CodeEditorMixin, CodeEditorDialog
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils, one_dragon.utils.log_utils, one_dragon_qt.utils.layout_utils, one_dragon_qt.widgets.adapter_init_mixin；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/combo_box_setting_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ComboBoxSettingCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon_qt.utils.layout_utils, one_dragon_qt.widgets.adapter_init_mixin, one_dragon_qt.widgets.combo_box；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/common_download_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: DownloadRunner, CommonDownloaderSettingCard, ZipDownloaderSettingCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon.base.operation.one_dragon_context, one_dragon.base.web.common_downloader, one_dragon.base.web.zip_downloader；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/editable_combo_box_setting_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: EditableComboBoxSettingCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon_qt.utils.layout_utils, one_dragon_qt.widgets.adapter_init_mixin, one_dragon_qt.widgets.editable_combo_box；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/help_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: HelpCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils；外部库: qfluentwidgets
- 使用的外部库：qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/key_setting_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: KeyEventWorker, KeySettingCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.controller.pc_button.pc_button_listener, one_dragon.utils.i18_utils, one_dragon_qt.utils.layout_utils, one_dragon_qt.widgets.adapter_init_mixin；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/key_value_setting_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: KeyValueSettingCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils, one_dragon_qt.utils.layout_utils, one_dragon_qt.widgets.adapter_init_mixin, one_dragon_qt.widgets.setting_card.setting_card_base；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/multi_push_setting_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: MultiPushSettingCard, MultiLineSettingCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.utils.layout_utils, one_dragon_qt.widgets.setting_card.setting_card_base；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/password_switch_setting_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: PasswordSwitchSettingCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils, one_dragon_qt.utils.layout_utils, one_dragon_qt.widgets.adapter_init_mixin, one_dragon_qt.widgets.setting_card.setting_card_base；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/push_setting_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: PushSettingCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils, one_dragon_qt.utils.layout_utils, one_dragon_qt.widgets.setting_card.setting_card_base；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/setting_card_base.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: SettingCardBase
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils, one_dragon_qt.utils.layout_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/spin_box_setting_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: SpinBoxSettingCardBase, SpinBoxSettingCard, DoubleSpinBoxSettingCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.utils.layout_utils, one_dragon_qt.widgets.adapter_init_mixin, one_dragon_qt.widgets.setting_card.setting_card_base, one_dragon_qt.widgets.setting_card.yaml_config_adapter；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/switch_setting_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: SwitchSettingCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils, one_dragon_qt.utils.layout_utils, one_dragon_qt.widgets.adapter_init_mixin, one_dragon_qt.widgets.setting_card.setting_card_base；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/text_setting_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: TextSettingCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils, one_dragon_qt.utils.layout_utils, one_dragon_qt.widgets.adapter_init_mixin, one_dragon_qt.widgets.setting_card.setting_card_base；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

##### 脚本：`src/one_dragon_qt/widgets/setting_card/yaml_config_adapter.py`
- 脚本职责：配置脚本：定义配置结构并负责读写 YAML/JSON 配置。
- 关键类/函数：类: YamlConfigAdapter
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.yaml_operator
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先把它当“设置说明书”：改这里通常是在改行为参数，不是改算法本身。

#### 脚本：`src/one_dragon_qt/widgets/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/adapter_init_mixin.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: AdapterInitMixin
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.log_utils, one_dragon_qt.widgets.setting_card.yaml_config_adapter；外部库: PySide6
- 使用的外部库：PySide6
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/banner.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: Banner
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.utils.image_utils；外部库: PySide6
- 使用的外部库：PySide6
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/base_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: BaseInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils, zzz_od.telemetry.auto_telemetry；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/click_image_label.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ImageScaleEnum, ClickImageLabel
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item；外部库: PySide6, cv2, numpy, qfluentwidgets
- 使用的外部库：PySide6, cv2, numpy, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/color_channel_dialog.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ColorChannelDialog
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PySide6, cv2, numpy
- 使用的外部库：PySide6, cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/color_tip.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ColorInfoWidget, MultiColorFlyoutView, ColorTip
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/column.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: Column
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PySide6
- 使用的外部库：PySide6
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/combo_box.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ComboBox
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item, one_dragon_qt.widgets.adapter_init_mixin, one_dragon_qt.widgets.setting_card.yaml_config_adapter；外部库: qfluentwidgets
- 使用的外部库：qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/cv2_image.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: Cv2Image
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PySide6, cv2
- 使用的外部库：PySide6, cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/editable_combo_box.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: EditableComboBox
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.config_item；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/fixed_size_image_label.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: FixedSizeImageLabel
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.utils.image_utils；外部库: PySide6
- 使用的外部库：PySide6
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/game_dialog.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: GameDialog
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.services.styles_manager；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/horizontal_setting_card_group.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: HorizontalSettingCardGroup
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PySide6
- 使用的外部库：PySide6
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/icon_button.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: IconButton
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/image_viewer_widget.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ImageDisplayLabel, OptimizedImageDisplayLabel, ImageViewerWidget
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils；外部库: PySide6, numpy, qfluentwidgets
- 使用的外部库：PySide6, numpy, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/label.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: EllipsisLabel
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PySide6
- 使用的外部库：PySide6
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/language_menu.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: LanguageMenu
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.custom_config, one_dragon.utils, one_dragon.utils.i18_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/log_display_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: LogSignal, LogReceiver, LogDisplayCard
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.log_utils, one_dragon.yolo.log_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/notice_card.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: SkeletonBanner, SkeletonContent, BannerImageLoader, RoundedBannerView, DataFetcher, AcrylicBackground；函数: get_notice_theme_palette
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils, one_dragon.utils.log_utils, one_dragon_qt.services.styles_manager, one_dragon_qt.utils.image_utils；外部库: , PySide6, qfluentwidgets, requests
- 使用的外部库：, PySide6, qfluentwidgets, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/notify_dialog.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: NotifyDialog
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.base.config.notify_config, one_dragon.base.operation.one_dragon_context, one_dragon.utils.i18_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/pivot.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: PhosPivot, PhosPivotItem, CustomListItemDelegate, PivotNavigatorContainer
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.services.styles_manager；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/pivot_navi_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: PivotNavigatorInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.widgets.base_interface；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/row.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: Row
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PySide6
- 使用的外部库：PySide6
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/shared_battle_dialog.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: BattleInfo, SharedConfigDialog
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils, one_dragon_qt.services.styles_manager；外部库: PySide6, qfluentwidgets, qframelesswindow, requests
- 使用的外部库：PySide6, qfluentwidgets, qframelesswindow, requests
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/vertical_scroll_interface.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: VerticalScrollInterface
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.widgets.base_interface；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/welcome_dialog.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: WelcomeDialog
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils.i18_utils；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/widgets/zoomable_image_label.py`
- 脚本职责：界面脚本：负责窗口、页面、控件与交互逻辑。
- 关键类/函数：类: ZoomableClickImageLabel
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon_qt.utils.image_utils；外部库: PySide6
- 使用的外部库：PySide6
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 目录：`src/one_dragon_qt/windows/`
说明：该目录按子模块拆分职责，脚本间通过导入关系协作。

#### 脚本：`src/one_dragon_qt/windows/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/windows/app_window_base.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: AppWindowBase
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.envs.project_config, one_dragon.utils, one_dragon_qt.widgets.base_interface, one_dragon_qt.windows.window；外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

#### 脚本：`src/one_dragon_qt/windows/window.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: PhosFluentWindowBase, PhosWindow, PhosNavigationBar, PhosNavigationBarPushButton, PhosTitleBar, PhosStackedWidget
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PySide6, qfluentwidgets
- 使用的外部库：PySide6, qfluentwidgets
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`src/one_dragon_qt/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

## 目录：`src/onnxocr/`
说明：OCR 引擎实现层：检测/分类/识别流水线。

### 脚本：`src/onnxocr/__init__.py`
- 脚本职责：包初始化脚本：用于声明模块边界、导出符号或执行轻量初始化。
- 关键类/函数：无显式顶层 class/def（多为常量、导出或初始化逻辑）
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`src/onnxocr/cls_postprocess.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: ClsPostProcess
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`src/onnxocr/db_postprocess.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: DBPostProcess, DistillationDBPostProcess
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: cv2, numpy, pyclipper, shapely
- 使用的外部库：cv2, numpy, pyclipper, shapely
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`src/onnxocr/imaug.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：函数: transform, create_operators
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: onnxocr.operators
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`src/onnxocr/logger.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: Logger；函数: GetLog
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：以下游导入较少为主，更多承担结构定义或简单封装。
- 使用的外部库：未直接依赖第三方库（或仅依赖标准库/项目内模块）
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`src/onnxocr/onnx_paddleocr.py`
- 脚本职责：识别脚本：负责 OCR、目标检测或模板匹配能力封装。
- 关键类/函数：类: ONNXPaddleOcr；函数: sav2Img, __debug
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: one_dragon.utils, onnxocr.predict_system, onnxocr.utils；外部库: PIL, cv2
- 使用的外部库：PIL, cv2
- 新手理解要点：这层是“看懂画面”的关键，模型文件、阈值、输入尺寸很重要。

### 脚本：`src/onnxocr/operators.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: NormalizeImage, DetResizeForTest, ToCHWImage, KeepKeys
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PIL, cv2, numpy
- 使用的外部库：PIL, cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`src/onnxocr/predict_base.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: PredictBase
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: onnxruntime
- 使用的外部库：onnxruntime
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`src/onnxocr/predict_cls.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: TextClassifier
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: onnxocr.cls_postprocess, onnxocr.predict_base；外部库: cv2, numpy
- 使用的外部库：cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`src/onnxocr/predict_det.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: TextDetector
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: onnxocr.db_postprocess, onnxocr.imaug, onnxocr.predict_base；外部库: numpy
- 使用的外部库：numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`src/onnxocr/predict_rec.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: TextRecognizer
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: onnxocr.predict_base, onnxocr.rec_postprocess；外部库: PIL, cv2, numpy
- 使用的外部库：PIL, cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`src/onnxocr/predict_system.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: TextSystem；函数: sorted_boxes
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：内部模块: onnxocr.predict_cls, onnxocr.predict_det, onnxocr.predict_rec, onnxocr.utils；外部库: cv2
- 使用的外部库：cv2
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`src/onnxocr/rec_postprocess.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：类: BaseRecLabelDecode, CTCLabelDecode, DistillationCTCLabelDecode, AttnLabelDecode, RFLLabelDecode, SEEDLabelDecode
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: numpy
- 使用的外部库：numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。

### 脚本：`src/onnxocr/utils.py`
- 脚本职责：功能脚本：承载该模块的具体实现。
- 关键类/函数：函数: get_rotate_crop_image, get_minarea_rect_crop, resize_img, str_count, text_visual, draw_ocr, base64_to_cv2, str2bool
- 调用上下游：上游：由运行上下文、应用工厂、UI 页面或其他操作节点触发。 下游：外部库: PIL, cv2, numpy
- 使用的外部库：PIL, cv2, numpy
- 新手理解要点：先看类名和函数名，再顺着导入关系追主调用链，效率最高。
