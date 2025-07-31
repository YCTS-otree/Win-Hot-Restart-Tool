# 🌀 Win Hot Restart Tool · Windows 热重启工具

> ✨ 一键热重启 Explorer、网络、音频、剪贴板等组件，释放系统卡顿，清理服务进程，无需重启整个系统！

![badge](https://img.shields.io/badge/Platform-Windows-blue?logo=windows)
![badge](https://img.shields.io/badge/Python-3.6%2B-yellow?logo=python)
![badge](https://img.shields.io/badge/Admin--Mode-Required-critical?logo=security)

---

## 📌 项目简介 | Project Introduction

本工具是一个用 Python + PowerShell 实现的轻量级 Windows 热重启脚本，适用于：

* 快速修复网络异常、音频无响应、剪贴板失效等问题；
* 替代系统重启，释放被卡住的服务或图形界面；
* 快速测试系统组件是否可热重启；
* 自定义调试系统服务或构建“无缝重启”方案。

支持自我提升管理员权限，无需额外依赖，适用于所有现代 Windows 系统。

> A powerful but lightweight script to hot-restart essential Windows components and services without rebooting. Ideal for developers, power users, or anyone tired of random Windows hiccups.

---

## 🎯 功能特性 | Features

* ✅ 自动检测并提升管理员权限
* ✅ 重启桌面（Explorer.exe）
* ✅ 重启网络堆栈、DHCP、NlaSvc 等网络服务
* ✅ 重启音频服务（Audiosrv）
* ✅ 重启剪贴板（rdpclip）
* ✅ 重启打印服务（Spooler）
* ✅ 深度重启：批量重启可停止的服务 + Explorer + DWM
* ⚠️ 危险功能：强制杀死所有 `svchost.exe`（调试用）

---

## 🚀 快速开始 | Quick Start

### ✅ 运行方式（推荐直接双击运行）

确保你安装了 Python（建议 3.6 以上）并右键选择「以管理员身份运行」：

```bash
python Win_Hot_Restart_v1.py
```

首次运行时会自动尝试拉起管理员权限。

---

## 🧭 菜单选项说明

| 编号 | 功能描述                          |
| -- | ----------------------------- |
| 0  | 检查是否为管理员运行                    |
| 1  | 重启桌面界面 Explorer.exe           |
| 2  | 重启网络堆栈及相关服务                   |
| 3  | 重启音频服务 Audiosrv               |
| 4  | 重启剪贴板服务 rdpclip               |
| 5  | 重启打印服务 Spooler                |
| 6  | 深度重启（批量服务 + 桌面图形层）⚠️ 高风险      |
| 7  | 杀死所有非系统 `svchost.exe` ⚠️ 极高风险 |
| 8  | 退出工具                          |

---

## ⚠️ 风险提示 | Risk Warning

* **方法 6 和 7 有可能造成蓝屏或系统部分功能失效！**
* 特别是方法 7（杀掉所有 svchost）仅限测试使用，执行后部分服务可能无法恢复，需重启；
* 网络重启可能导致 VPN、代理断开；
* **强烈建议保存好当前工作内容**后再执行重操作！

---

## 📁 文件结构 | Files

```
Win_Hot_Restart/
├── Win_Hot_Restart_v1.py     # 主脚本，管理员自提升
└── README.md                 # 使用说明（本文件）
```

---

## 🛠️ 系统要求 | Requirements

* Windows 10 / 11
* Python 3.6+
* 管理员权限（脚本会自动尝试提升）

---

## 🧑‍💻 作者 | Authors

* 🧠 项目主创：[@OTREE](https://github.com/YCTS-otree)
* 🤖 协作者：ChatGPT (by OpenAI)

---

## 📜 协议 | License

MIT License.
本工具可自由使用、修改、发布，仅需保留原始作者信息。

---

## 🙌 鸣谢 | Acknowledgements

* Microsoft PowerShell Team
* StackOverflow 技术社区
* 每一位测试和提供建议的朋友！

---

## 📷 计划中的功能 | TODO

* [ ] GUI 界面可视化（使用 PyQt/Tkinter）
* [ ] 日志输出和恢复记录
* [ ] 支持任务栏托盘图标驻留
* [ ] 自定义服务组的“重启方案”配置

---

