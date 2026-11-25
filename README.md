# pairwise-redstone-cross-chunk

## 领域

游戏、图形与多媒体

## 主题

沙盒电路信号传播与跨区块更新

## 说明

路径延迟建模、区块状态持久化、更新队列稳定排序。

初始状态下 `game/redstone_circuit.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
