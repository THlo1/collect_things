#author:Fla5hback
#依赖安装：pip install tkinter requests scapy
#功能：一个简单的Tkinter界面，允许用户输入URL并发送请求,接收请求的html；后续可使用Scapy库修改HTTP和HTTPS数据包，并使用Burp API将修改后的数据包传递给Burp Suite

import tkinter as tk
from tkinter import ttk
import requests

def send_request():
    url = url_entry.get()
    response = requests.get(url)
    print(response.text)

root = tk.Tk()
root.title("URL Request Tool")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

url_label = ttk.Label(frame, text="URL:")
url_label.grid(row=0, column=0, sticky=tk.W)

url_entry = ttk.Entry(frame, width=40)
url_entry.grid(row=0, column=1)

send_button = ttk.Button(frame, text="Send Request", command=send_request)
send_button.grid(row=1, column=1, sticky=tk.E)

root.mainloop()