# AGENTS.md

本项目是游戏 [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) 的自动化脚本存档。

## 项目概述

这是一个编程自动化农场游戏，玩家通过编写代码控制无人机自动完成种植、浇水、收割等农场操作。游戏使用一种类似 Python 的专用脚本语言。

- **游戏存档位置**: `C:\Users\UserX\AppData\LocalLow\TheFarmerWasReplaced\TheFarmerWasReplaced\Saves\Save0`
- **农场大小**: 6×6 网格 (由 `get_world_size()` 获取)
- **主要作物**: 胡萝卜 (Carrot)、树 (Tree)、灌木 (Bush)

## 文件结构

```
.
├── AGENTS.md           # 本文件 - 项目说明文档
├── __builtins__.py     # 游戏 API 类型定义文件（用于编辑器代码提示）
├── judgement_canharv.py # 判断作物是否可以收割的模块
├── main.py             # 主程序入口
├── plant_carrot.py     # 胡萝卜种植逻辑模块
├── readme.md           # 开发笔记/待办事项
├── save.json           # 游戏存档数据（物品、解锁状态等）
└── water.py            # 自动浇水逻辑模块
```

## 技术栈

- **语言**: 游戏专用脚本语言（语法类似 Python）
- **运行环境**: The Farmer Was Replaced 游戏内嵌脚本引擎
- **编辑器**: 任何支持 Python 的编辑器（利用 `__builtins__.py` 获得代码提示）

## 模块说明

### main.py - 主程序

程序的入口文件，实现无人机遍历整个农场的逻辑：
- 使用双重循环遍历 6×6 农场网格
- 在边缘位置 (x=0,5 和 y=0,5) 种植胡萝卜和树（棋盘格模式）
- 在第1行和第4行 (x=1,4) 种植灌木
- 调用 `judgement_canharv.judgement()` 判断收割
- 调用 `water.water(target)` 为指定作物浇水

### judgement_canharv.py - 收割判断

```python
def judgement():
    # 用于判断田地是否可以收割的代码，可以返回1，不可以返回0
```

使用 `can_harvest()` 检查作物是否成熟，若成熟则调用 `harvest()` 收割。

### plant_carrot.py - 胡萝卜种植

处理胡萝卜种植逻辑：
- 如果地面是土壤 (Soil)，直接种植
- 如果地面是草地 (Grassland)，先 `till()` 翻地再种植

### water.py - 自动浇水

```python
def water(target):
    # target: 需要浇水的作物类型列表
```

- 检查当前格子的水分含量 (`get_water()`)
- 如果作物类型在目标列表中且水分低于 0.25，自动使用水桶浇水

## 核心游戏 API

游戏提供的主要函数（详见 `__builtins__.py`）：

### 基础操作
- `harvest()` - 收割当前格子的作物
- `can_harvest()` - 检查作物是否可以收割
- `plant(entity)` - 种植指定作物
- `move(direction)` - 向指定方向移动 (North, South, East, West)
- `till()` - 翻耕土地（草地↔土壤切换）

### 状态查询
- `get_pos_x()`, `get_pos_y()` - 获取无人机位置
- `get_world_size()` - 获取农场大小
- `get_entity_type()` - 获取当前格子作物类型
- `get_ground_type()` - 获取当前格子地面类型
- `get_water()` - 获取当前格子水分含量
- `num_items(item)` - 获取背包中物品数量

### 物品使用
- `use_item(item)` - 使用物品（如水桶、肥料等）

### 实体类型 (Entities)
- `Entities.Carrot` - 胡萝卜
- `Entities.Tree` - 树
- `Entities.Bush` - 灌木
- `Entities.Grass` - 草
- `Entities.Pumpkin` - 南瓜
- `Entities.Sunflower` - 向日葵

### 地面类型 (Grounds)
- `Grounds.Soil` - 土壤（可种植胡萝卜等）
- `Grounds.Grassland` - 草地（可种植树、灌木等）

### 物品类型 (Items)
- `Items.Water` - 水
- `Items.Carrot` - 胡萝卜
- `Items.Wood` - 木材
- `Items.Hay` - 干草
- `Items.Fertilizer` - 肥料

## 开发约定

1. **模块化设计**: 将不同功能拆分到独立文件，通过 `import` 引入
2. **函数命名**: 使用下划线命名法（如 `plant_carrot`, `judgement`）
3. **注释**: 使用中文注释说明代码逻辑
4. **返回值**: 习惯用 `return 1` 表示操作成功

## 当前策略

农场布局策略（6×6网格）：
```
列:  0    1    2    3    4    5
行0: C/T  B    C/T  C/T  B    C/T
行1: C/T  B    -    -    B    C/T
行2: C/T  -    -    -    -    C/T
行3: C/T  -    -    -    -    C/T
行4: C/T  B    -    -    B    C/T
行5: C/T  B    C/T  C/T  B    C/T
```
- C/T: 胡萝卜和树交替种植（偶数位置胡萝卜，奇数位置树）
- B: 灌木
- -: 空地（不种植）

## 注意事项

1. **非真实 Python**: 游戏语言虽然类似 Python，但有一些限制和差异
2. **Tick 系统**: 每个操作消耗特定的 tick（时间单位），优化 tick 使用是游戏核心玩法
3. **存档文件**: `save.json` 是游戏自动生成的，不建议手动修改
4. **导入限制**: 游戏支持 `import` 其他文件，但语法可能与标准 Python 略有不同

## 未来计划（来自 readme.md）

- [x] 种树（边缘棋盘格模式）
- [x] 浇水系统（水分低于 0.25 自动补水）
- [ ] 向日葵种植策略（暂时跳过，触发条件较复杂）
- [ ] 南瓜种植
- [ ] 增加胡萝卜储备
