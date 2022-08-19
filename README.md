# MHRS-qurious-crafting-automation
A tool for Monster Hunter Rise:Sunbreak qurious crafting automation

### 使用方法
1. 双击打开exe,点击开启按键检测按键输入
2. 在游戏界面键入快捷键组合触发脚本自动按键

### 四种自动按键
- 炼成一次(默认`alt+a`)
- 炼成完成界面保留炼成结果(默认`alt+w`)
- 炼成完成界面不保留炼成结果(默认`alt+d`)
- 重复完整炼金过程n次(默认`alt+r`),n为界面上输入框输入的数字

### 使用源码

### 依赖
    pydirectinput 用于发送按键指令(pyautogui无法在游戏界面生效)
    tkinter 主界面绘制
    pynput 检测输入
    pyinstaller 打包成exe
### 打包
    pyinstaller -F -w main.py --distpath .\target -n newname