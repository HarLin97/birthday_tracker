# 🎂 生日日历追踪器（Birthday Tracker）

一个适用于 Home Assistant 的生日追踪插件，支持阳历与阴历生日计算，自动更新年龄、倒计时、提醒状态等信息。适合家庭自动化场景，轻松掌握亲友生日动态。

---

## 功能特色

- 支持阳历与阴历生日
- 自动计算年龄、下次生日日期、倒计时
- 每天凌晨自动刷新实体状态
- 每个字段独立实体，便于展示与自动化引用
- 高度模块化，易于扩展与维护

---

## 安装方式

### 方法一：HACS 安装（推荐）

1. 确保已安装 [HACS](https://hacs.xyz/)
2. 在 HACS 中点击"集成"
3. 点击右上角的三点菜单，选择"自定义存储库"
4. 添加此存储库地址：`https://github.com/VergilGao/birthday_tracker`
5. 类别选择"集成"
6. 点击"添加"
7. 搜索"Birthday Tracker"并点击"下载"
8. 重启 Home Assistant

### 方法二：GitHub 直接下载

1. 下载最新的 [Release](https://github.com/VergilGao/birthday_tracker/releases) 文件
2. 解压到 Home Assistant 的 `custom_components/` 目录下
3. 确保目录结构为 `custom_components/birthday_tracker/`
4. 重启 Home Assistant

### 方法三：手动安装

1. 克隆或下载本仓库
2. 将 `custom_components/birthday_tracker/` 目录复制到 Home Assistant 的 `custom_components/` 目录下
3. 重启 Home Assistant

### 添加集成

1. 在 Home Assistant 中，进入"设置" > "设备与服务"
2. 点击"添加集成"按钮
3. 搜索并选择"生日追踪器"
4. 按照提示填写信息完成配置
5. 可重复添加多个人的生日信息

---

## 配置项说明

| 字段名             | 类型       | 说明                         |
|--------------------|------------|------------------------------|
| `name`             | `string`   | 姓名或标识                   |
| `birth_date`       | `date`     | 出生日期（阳历）             |
| `enable_lunar`     | `boolean`  | 是否启用阴历支持（默认启用） |

---

## 注册的实体

每个生日对象会注册以下实体（若启用阴历）：

- 当前周岁
- 出生阳历日期
- 出生阴历日期
- 下一个阳历生日日期
- 下一个阴历生日日期
- 距离阳历生日还有几天
- 距离阴历生日还有几天
- 是否是阳历生日（true/false）
- 是否是阴历生日（true/false）

---

## 自动刷新机制

插件会在每天凌晨 0 点自动刷新所有生日实体，无需用户手动创建自动化。

---

## 开发者指南

- 所有字段实体位于 `sensors/` 文件夹中，按类型分组
- 使用 `BirthdayCoordinator` 统一调度计算逻辑
- 支持扩展提醒服务、图表展示、分组管理等功能

---

## 开源协作

欢迎提交 PR、Issue 或功能建议。您可以：

- 提供翻译支持
- 改进配置 UI

---

## 许可证

本项目采用 [MIT License](https://github.com/VergilGao/birthday_tracker/blob/master/LICENSE) 开源协议。

