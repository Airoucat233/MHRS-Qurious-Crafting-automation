import time
import tkinter as tk

import pydirectinput
from pynput.keyboard import Listener, Key,KeyCode

def press(key):
    global switch
    if isinstance(key,KeyCode):
        key = key.char
    elif isinstance(key,Key):
        key = key.name
    global record_key
    if not record_key.__contains__(key):
        record_key.append(key)
    global times
    if record_key.__contains__('alt_l'):
        if record_key.__contains__('a'):
            pydirectinput.press(['up','up','space','right','space','down','space','space'])
            times += 1
            label_text.set(times)
            print(times)
            record_key = []
        elif record_key.__contains__('s'):
            pydirectinput.press(['left','space','left','space','space'])
            record_key = []
        elif record_key.__contains__('d'):
            times = 0
            label_text.set(times)
            record_key = []
        elif record_key.__contains__('w'):
            pydirectinput.press(['space', 'left', 'space', 'space','space'])
            record_key = []
        elif record_key.__contains__('r'):
            try:
                t = int(enrty.get())
                for i in range(t):
                    pydirectinput.press(['up', 'up', 'space', 'right', 'space', 'down', 'space', 'space'])
                    time.sleep(0.5)
                    pydirectinput.press(['space', 'left', 'space', 'space', 'space'])
                    times += 1
                    label_text.set(times)
            except Exception as e:
                print(e)
            record_key = []
    if record_key.__contains__('shift_r'):
        if record_key.__contains__('esc'):
            button_text.set('开启')
            record_key = []
            switch = False
            return False

def release(key):
    if isinstance(key,KeyCode):
        key = key.char
    if isinstance(key,Key):
        key = key.name
    global record_key
    try:
        record_key.remove(key)
    except:
        record_key = []


record_key = []
times = 0
app = tk.Tk()  # 根窗口的实例(root窗口)
app.geometry('300x300')
app.resizable(width=False,height=False)
app.title('一键炼金')  # 根窗口标题
switch = False
button_text = tk.StringVar()
button_text2 = tk.StringVar()
label_text = tk.StringVar()
button_text.set('开启')
button_text2.set('重新计数(ALT+D)')
label_text.set(times)

def controller():
    global switch,button_text
    if switch == False:
        switch = True
        t = Listener(on_press=press, on_release=release)
        t.start()
        button_text.set('关闭(右SHIFT+ESC)')
    else:
        record_key.append('shift_r')
        pydirectinput.press('esc')
        button_text.set('开启')
        switch = False
def controller2():
    global times
    times = 0
    label_text.set(times)
b=tk.Button(app,textvariable=button_text,width=10,height=2,command=controller)
b1=tk.Button(app,textvariable=button_text2,width=10,height=2,command=controller2)
label = tk.Label(app,textvariable=label_text,width=10,height=2)

label_p = tk.Label(app,textvariable=tk.StringVar(value='按一次ALT+R练'),width=15,height=2)
enrty = tk.Entry(app,width=6)
label_a = tk.Label(app,textvariable=tk.StringVar(value='次'),width=3,height=2)

label.grid(row=1,column=1,columnspan = 3)
b.grid(row=2,column=1,columnspan = 3,sticky="ew")
b1.grid(row=3,column=1,columnspan = 3,sticky="ew")

label_p.grid(row=4,column=1,sticky="ew")
enrty.grid(row=4,column=2,sticky="ew")
label_a.grid(row=4,column=3,sticky="ew")
app.grid_columnconfigure((0, 4), weight=1)
app.mainloop()


