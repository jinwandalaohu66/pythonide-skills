# PythonIDE Skills

[PythonIDE](https://pythonide.xin) 的可安装 [Agent Skills](https://agentskills.io) 包。让 Cursor、Codex、Claude Code、Gemini CLI 等编码 Agent 正确编写：

- **AppUI MiniApp**（原生 iOS 界面）
- **iOS 桌面小组件**（WidgetKit）
- **iOS 原生能力**（相机、定位、通知、网络等）
- **2D 场景 / 小游戏**（`scene`）
- **自动化脚本**（Shortcuts、`ui`、批处理）

一行命令安装，无需把完整文档复制进仓库。

## 安装

通过 [`npx skills`](https://github.com/vercel-labs/skills) 安装（支持 Cursor、Codex、Claude Code 等）：

```bash
# 仅当前项目
npx skills add Python-IDE/pythonide-skills

# 全局（推荐，所有项目可用）
npx skills add Python-IDE/pythonide-skills -g

# 仅安装到 Cursor
npx skills add Python-IDE/pythonide-skills -a cursor -g
```

安装后**重启 Agent** 即可生效。

## Skills 一览

| Skill | 何时使用 |
| --- | --- |
| [`pythonide`](pythonide/SKILL.md) | 不确定用什么运行时；先路由到正确 skill |
| [`pythonide-appui`](pythonide-appui/SKILL.md) | 做/改 AppUI 小程序：列表、表单、导航、Tab、媒体控件 |
| [`pythonide-native`](pythonide-native/SKILL.md) | 选型并调用 iOS 原生模块：权限、存储、传感器、网络 |
| [`pythonide-widget`](pythonide-widget/SKILL.md) | 做 iOS 主屏幕小组件 |
| [`pythonide-scene`](pythonide-scene/SKILL.md) | 2D 游戏、精灵动画、触摸场景、turtle |
| [`pythonide-automation`](pythonide-automation/SKILL.md) | Shortcuts、键盘片段、legacy `ui`、纯 Python 脚本 |

一次安装会带上表内**全部** skill。做带相机/定位的 AppUI 应用时，Agent 应同时遵循 `pythonide-appui` 与 `pythonide-native`（skill 内已互链）。

## 示例

每个 skill 目录下有可复制的示例：

| 示例 | 路径 |
| --- | --- |
| 计数器 MiniApp | [`pythonide-appui/examples/counter/`](pythonide-appui/examples/counter/) |
| 相册笔记（PhotoPicker + storage） | [`pythonide-appui/examples/photo_notes/`](pythonide-appui/examples/photo_notes/) |
| 设备信息快照 | [`pythonide-native/examples/device_snapshot/`](pythonide-native/examples/device_snapshot/) |
| 进度小组件 | [`pythonide-widget/examples/progress/`](pythonide-widget/examples/progress/) |
| 点击移动小球 | [`pythonide-scene/examples/tap_ball/`](pythonide-scene/examples/tap_ball/) |
| 运行 Shortcut | [`pythonide-automation/examples/run_shortcut/`](pythonide-automation/examples/run_shortcut/) |

## 文档分工

| 层级 | 内容 | 链接 |
| --- | --- | --- |
| **Skill（本仓库）** | 执行规则：怎么写、禁止什么、何时配对哪个 skill | 各目录 `SKILL.md` |
| **在线文档** | 完整模块说明与中文场景示例 | [pythonide.xin/docs](https://pythonide.xin/docs/) |
| **机器可读契约** | API 签名、原生能力路由、生成硬规则 | 见下表 |

### 机器可读链接（Agent 查 API 时优先）

- [AI 一页指南](https://pythonide.xin/docs/ai/)
- [llms-full.txt](https://pythonide.xin/llms-full.txt)
- [Native capabilities schema](https://pythonide.xin/schemas/native_capabilities_schema.json)
- [AppUI schema](https://pythonide.xin/schemas/appui_api_schema.json)
- [Widget schema](https://pythonide.xin/schemas/widget_api_schema.json)
- [appui.pyi](https://pythonide.xin/stubs/appui.pyi) · [widget.pyi](https://pythonide.xin/stubs/widget.pyi)

用户文档以中文为主；skill 与 schema 以英文为主，便于 Agent 稳定生成代码。

## 运行时速查

| 用户需求 | 导入 | Skill |
| --- | --- | --- |
| 原生小程序 | `import appui` | `pythonide-appui` |
| 桌面小组件 | `import widget` | `pythonide-widget` |
| 2D 游戏 / 场景 | `import scene` | `pythonide-scene` |
| Pythonista 风格 UI | `import ui` | `pythonide-automation` |
| 纯脚本 + 原生能力 | `import photos` 等 | `pythonide-native` |

## AppUI 与原生能力

AppUI 常用能力有两种接法：

1. **内联控件（优先）**：`PhotoPicker`、`CameraPicker`、`MapView`、`FileImporter`、`ShareLink`、`VideoPlayer`
2. **回调里调模块**：`import location`、`photos`、`notification` 等（须在按钮回调中，不能写在 `body()` 里）

详见 [`pythonide-appui/SKILL.md`](pythonide-appui/SKILL.md) 中的桥接表，以及 [`pythonide-native/references.md`](pythonide-native/references.md) 中的全量路由表。

## 链接

- [PythonIDE 官网 / 文档](https://pythonide.xin)
- [本仓库](https://github.com/Python-IDE/pythonide-skills)
- [Agent Skills 规范](https://agentskills.io)

## License

MIT — see [LICENSE](LICENSE).
