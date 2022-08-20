import json
import os
import time
import tkinter as tk
import pydirectinput
from pynput.keyboard import Listener, Key,KeyCode
pydirectinput.PAUSE = 0.05
record_key=[]
config = {
    "shortcut_keys": {
        "alt_l+a":{"action":[["x","space","space"]],"count":True},
        "alt_l+s":{"action":[['left','space','left','space','space']]},
        "alt_l+w":{"action":[['space', 'left', 'space', 'space','space']]},
        "alt_l+d":{"action":"reset"},
        "shift_r+esc":{"action":"stop"},

        "alt_l+r":{"action":[
                ['x', 'space', 'space'],['left','space','left','space','space']
            ],"delay":0.4
        }
    }
}

def log(e):
    log_str.set('error:'+str(e))

def init():
    global config
    try:
        if not os.path.exists('./config.json'):
            with open('./config.json', 'w') as f:
                f.write(json.dumps(config,indent=4))
        with open('./config.json','r') as f:
            config = json.loads(f.read())
    except Exception as e:
        log('读取配置文件失败,使用默认配置')
def action_chains(keys_list:list[list],delay):
    for index,keys in enumerate(keys_list):
        pydirectinput.press(keys)
        if index < len(keys_list)-1:
            time.sleep(delay)

def press(key):
    global record_key, t
    if isinstance(key,KeyCode):
        key = key.char
    elif isinstance(key,Key):
        key = key.name
    if not key in record_key:
        record_key.append(key)
    key_map = config.get("shortcut_keys")
    if len(record_key)>1:
        for hotkey in key_map.keys():
            keys = hotkey.split('+')
            if len(keys)== len(record_key) and all(k in record_key for k in keys):
                action = key_map.get(hotkey).get("action")
                if isinstance(action,str):
                    if action == 'stop':
                        switch_text.set('开启')
                        record_key = []
                        return False
                    elif action == 'reset':
                        count_reset()
                        record_key = []
                elif isinstance(action,list):
                    delay = key_map.get(hotkey).get("delay")
                    count = key_map.get(hotkey).get("count")
                    if delay:
                        try:
                            repeat_time = int(enrty.get())
                            for i in range(repeat_time):
                                action_chains(action,delay)
                                time.sleep(0.05)
                        except Exception as e:
                            log(e)
                            record_key = []
                            break
                    else:
                        action_chains(action, 0)
                        if count:
                            count_increase()
                    record_key = []
                    break

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

t = Listener(on_press=press, on_release=release)

def switch_controller():
    global switch_text,t
    if not t.running:
        t = Listener(on_press=press, on_release=release)
        t.start()
        switch_text.set('关闭(右SHIFT+ESC)')
    else:
        t.stop()
        switch_text.set('开启')
def count_increase():
    label_text.set(int(label_text.get()) + 1)
    enrty_text.set(int(label_text.get()) - 1)
def count_reset():
    label_text.set(0)

if __name__=='__main__':
    app = tk.Tk()  # 根窗口的实例(root窗口)
    app.geometry('300x300')
    app.resizable(width=False,height=False)
    app.title('一键怪异炼成')  # 根窗口标题

    switch_text = tk.StringVar()
    log_str = tk.StringVar()
    label_text = tk.StringVar(value=0)
    enrty_text = tk.StringVar(value=0)
    switch_text.set('开启')

    switch_btn=tk.Button(app,textvariable=switch_text,width=10,height=2,command=switch_controller)
    count_btn=tk.Button(app, textvariable=tk.StringVar(value='重新计数(ALT+D)'), width=10, height=2, command=count_reset)
    proceed_label = tk.Label(app,textvariable=tk.StringVar(value='已进行次数:'),width=15,height=2)
    label = tk.Label(app,textvariable=label_text,width=5,height=2)

    label_p = tk.Label(app,textvariable=tk.StringVar(value='按一次ALT+R炼'),width=15,height=2)
    enrty = tk.Entry(app,width=6,textvariable=enrty_text)
    label_a = tk.Label(app,textvariable=tk.StringVar(value='次'),width=3,height=2)
    log_label = tk.Label(app,textvariable=log_str,width=30,height=2)

    proceed_label.grid(row=1,column=1,columnspan = 2)
    label.grid(row=1,column=2)
    switch_btn.grid(row=2,column=1,columnspan = 3,sticky="ew")
    count_btn.grid(row=3, column=1, columnspan = 3, sticky="ew")

    label_p.grid(row=4,column=1,sticky="ew")
    enrty.grid(row=4,column=2,sticky="ew")
    label_a.grid(row=4,column=3,sticky="ew")

    log_label.grid(row=5,column=1,columnspan = 3)

    app.grid_columnconfigure((0, 4), weight=1)
    init()
    app.mainloop()


