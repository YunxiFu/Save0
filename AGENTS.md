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
├── plant_vegetable.py  # 作物种植逻辑模块（胡萝卜、树、灌木）
├── readme.md           # 开发笔记/待办事项
├── save.json           # 游戏存档数据（物品、解锁状态等）
└── water.py            # 自动浇水逻辑模块
```

## 技术栈

- **语言**: 游戏专用脚本语言（语法类似 Python，但非真实 Python）
- **运行环境**: The Farmer Was Replaced 游戏内嵌脚本引擎
- **编辑器**: 任何支持 Python 的编辑器（利用 `__builtins__.py` 获得代码提示）
- **导入系统**: 支持 `import` 语法导入其他文件，但语法与标准 Python 略有不同

## 模块说明

### main.py - 主程序

程序的入口文件，实现无人机遍历整个农场的逻辑：
- 使用双重循环遍历 6×6 农场网格
- 调用 `judgement_canharv.judgement()` 判断并执行收割
- 调用 `plant_vegetable.plant_tree(tag)` 种植树或灌木（交替种植）
- `tag` 参数用于控制树和灌木的交替种植（偶数种 Tree，奇数种 Bush）

**注意**: 当前代码中浇水功能 (`water.water(target)`) 和胡萝卜种植 (`plant_vegetable.plant_carrot()`) 被注释掉了

### judgement_canharv.py - 收割判断

```python
def judgement():
    # 用于判断田地是否可以收割的代码，可以返回1，不可以返回0
```

- 使用 `can_harvest()` 检查作物是否成熟
- 若成熟则调用 `harvest()` 收割并返回 1
- 否则返回 0

### plant_vegetable.py - 作物种植

包含两个主要函数：

**`plant_carrot()`** - 胡萝卜种植逻辑：
- 如果地面是土壤 (Soil)，直接种植 `Entities.Carrot`
- 如果地面是草地 (Grassland)，先 `till()` 翻地再种植

**`plant_tree(tag)`** - 树和灌木交替种植：
- `tag` 为偶数时种植树 (`Entities.Tree`)，返回 1
- `tag` 为奇数时种植灌木 (`Entities.Bush`)，返回 0
- 通过返回值实现交替种植效果

### water.py - 自动浇水

```python
def water(target):
    # target: 需要浇水的作物类型列表
```

- 检查当前格子的水分含量 (`get_water()`)
- 如果作物类型在目标列表中且水分低于 0.25，自动使用水桶浇水 (`use_item(Items.Water)`)
- 循环浇水直到水分充足

## 核心游戏 API

游戏提供的主要函数（详见 `__builtins__.py`）：

### 基础操作
| 函数 | 功能 | 耗时 (ticks) |
|------|------|-------------|
| `harvest()` | 收割当前格子的作物 | 200 (成功) / 1 (失败) |
| `can_harvest()` | 检查作物是否可以收割 | 1 |
| `plant(entity)` | 种植指定作物 | 200 (成功) / 1 (失败) |
| `move(direction)` | 向指定方向移动 (North, South, East, West) | 200 (成功) / 1 (失败) |
| `till()` | 翻耕土地（草地↔土壤切换） | 200 |
| `use_item(item, n=1)` | 使用物品 n 次 | 200 (成功) / 1 (失败) |

### 状态查询
| 函数 | 功能 | 耗时 (ticks) |
|------|------|-------------|
| `get_pos_x()`, `get_pos_y()` | 获取无人机位置 | 1 |
| `get_world_size()` | 获取农场大小 | 1 |
| `get_entity_type()` | 获取当前格子作物类型 | 1 |
| `get_ground_type()` | 获取当前格子地面类型 | 1 |
| `get_water()` | 获取当前格子水分含量 (0-1) | 1 |
| `num_items(item)` | 获取背包中物品数量 | 1 |
| `get_time()` | 获取游戏时间（秒） | 1 |
| `get_tick_count()` | 获取已执行的 tick 数 | 0 |

### 高级功能
| 函数 | 功能 |
|------|------|
| `clear()` | 清空农场，重置无人机位置和帽子 |
| `unlock(unlock)` | 解锁指定项目 |
| `num_unlocked(thing)` | 检查解锁状态 |
| `get_cost(thing)` | 获取物品/解锁的成本 |
| `measure()` | 测量特定作物属性（向日葵花瓣数、仙人掌大小等） |
| `get_companion()` | 获取作物的伴生偏好 |
| `spawn_drone(function)` | 生成额外无人机（需解锁 Megafarm） |
| `wait_for(drone)` | 等待指定无人机完成 |
| `leaderboard_run(...)` | 开始排行榜计时运行 |
| `simulate(...)` | 运行模拟测试 |

### 实体类型 (Entities)
- `Entities.Carrot` - 胡萝卜（生长时间约 6 秒，需在 Soil 上种植）
- `Entities.Tree` - 树（生长时间约 7 秒，相邻树会延长生长时间）
- `Entities.Bush` - 灌木（生长时间约 4 秒）
- `Entities.Grass` - 草（生长时间约 0.5 秒，自动生长在 Grassland 上）
- `Entities.Pumpkin` - 南瓜（生长时间约 2 秒，可合并生长）
- `Entities.Sunflower` - 向日葵（生长时间约 5 秒，产出 Power）
- `Entities.Cactus` - 仙人掌（10 种不同大小，排序收获有加成）
- `Entities.Dinosaur` - 恐龙（生长时间约 0.2 秒）
- `Entities.Treasure` - 迷宫宝藏
- `Entities.Hedge` - 迷宫树篱
- `Entities.Dead_Pumpkin` - 死亡南瓜（无法收获）
- `Entities.Apple` - 苹果

### 地面类型 (Grounds)
- `Grounds.Soil` - 土壤（可种植胡萝卜、南瓜、向日葵等）
- `Grounds.Grassland` - 草地（草会自动生长，可种植树、灌木）

### 物品类型 (Items)
- `Items.Water` - 水（用于浇水）
- `Items.Carrot` - 胡萝卜
- `Items.Wood` - 木材
- `Items.Hay` - 干草
- `Items.Fertilizer` - 肥料（减少 2 秒生长时间）
- `Items.Pumpkin` - 南瓜
- `Items.Power` - 能量（来自向日葵，自动用于加速移动）
- `Items.Cactus` - 仙人掌
- `Items.Bone` - 骨头
- `Items.Gold` - 黄金
- `Items.Weird_Substance` - 奇怪物质（用于生成迷宫或切换感染状态）

### 解锁类型 (Unlocks)
主要解锁项包括：
- `Unlocks.Carrots` - 胡萝卜种植
- `Unlocks.Trees` - 树和灌木
- `Unlocks.Pumpkins` - 南瓜
- `Unlocks.Sunflowers` - 向日葵和能量
- `Unlocks.Cactus` - 仙人掌
- `Unlocks.Watering` - 浇水系统
- `Unlocks.Fertilizer` - 肥料
- `Unlocks.Mazes` - 迷宫
- `Unlocks.Dinosaurs` - 恐龙
- `Unlocks.Leaderboard` - 排行榜
- `Unlocks.Megafarm` - 多无人机系统
- `Unlocks.Simulation` - 模拟功能
- `Unlocks.Functions` - 自定义函数
- `Unlocks.Loops` - 循环
- `Unlocks.Variables` - 变量
- `Unlocks.Import` - 导入其他文件

## 开发约定

1. **模块化设计**: 将不同功能拆分到独立文件，通过 `import` 引入
2. **函数命名**: 使用下划线命名法（如 `plant_carrot`, `judgement`）
3. **注释**: 使用中文注释说明代码逻辑
4. **返回值**: 习惯用 `return 1` 表示操作成功
5. **代码提示**: 利用 `__builtins__.py` 在编辑器中获得类型提示

## 当前策略

农场布局策略（6×6网格）：
- 边缘位置 (x=0,5 和 y=0,5)：树和灌木交替种植
- 内部区域：根据需求种植（当前代码主要使用树/灌木交替种植）

## 注意事项

1. **非真实 Python**: 游戏语言虽然类似 Python，但有一些限制和差异：
   - 部分 Python 语法可能不支持
   - 导入语法略有不同
   - 类型提示仅用于编辑器，运行时忽略

2. **Tick 系统**: 
   - 每个操作消耗特定的 tick（时间单位）
   - 优化 tick 使用是游戏核心玩法
   - `get_tick_count()` 可用于性能测量（0 tick 开销）
   - `quick_print()` 不消耗 tick，适合调试输出

3. **存档文件**: `save.json` 是游戏自动生成的，不建议手动修改。包含：
   - 物品数量（`items`）
   - 已解锁项目（`unlocks`）
   - 文件停靠状态（`dockedFiles`）
   - 窗口位置和大小（`openFilePositions` 等）

4. **移动机制**: 
   - 农场边缘会循环（从东边出去会从西边进入）
   - 每次移动消耗 200 ticks（成功）或 1 tick（失败）

5. **水分系统**:
   - 水分范围 0-1
   - 使用 `use_item(Items.Water)` 增加水分
   - 不同作物对水分需求不同

6. **作物生长时间**（平均秒数）：
   - 草：0.5s
   - 恐龙：0.2s
   - 仙人掌：1s
   - 南瓜：2s
   - 灌木：4s
   - 向日葵：5s
   - 胡萝卜：6s
   - 树：7s（相邻树会延长）

## 开发计划（来自 readme.md）

已完成：
- [x] 种树（边缘棋盘格模式）
- [x] 浇水系统（水分低于 0.25 自动补水）

待完成：
- [ ] 向日葵种植策略（暂时跳过，触发条件较复杂）
- [ ] 南瓜种植
- [ ] 增加胡萝卜储备

## 调试与优化建议

1. **使用 `set_execution_speed(speed)`** 限制执行速度以便观察
2. **使用 `set_world_size(size)`** 缩小农场规模进行测试
3. **使用 `simulate()`** 进行模拟测试，不消耗实际游戏资源
4. **使用 `quick_print()`** 进行零开销调试输出
5. **使用 `get_tick_count()`** 测量代码性能

## 扩展功能

游戏支持的高级功能：
- **多无人机**: 解锁 Megafarm 后可使用 `spawn_drone()` 生成多个无人机并行工作
- **排行榜**: 使用 `leaderboard_run()` 参与官方排行榜
- **模拟器**: 使用 `simulate()` 在虚拟环境中测试策略
- **帽子系统**: 使用 `change_hat()` 更换无人机外观，部分帽子有特殊功能
