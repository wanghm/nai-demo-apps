import tkinter as tk
from tkinter import ttk
import requests
import json
from dotenv import load_dotenv
import os

# 環境変数を読み込む
load_dotenv()
endpoint = os.getenv("NAI_ENDPOINT")
api_key = os.getenv("NAI_API_KEY")

# メインウィンドウの設定
root = tk.Tk()
root.title("Chatbot GUI")
root.geometry("500x400")

# スタイルの設定
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 14), padding=10)
style.configure("TEntry", font=("Helvetica", 12), padding=10)

# ラベルの作成
label = ttk.Label(root, text="Enter your message:", style="TLabel")
label.pack(pady=10)

# テキストエントリーの作成
entry = ttk.Entry(root, width=50, style="TEntry")
entry.pack(pady=10)

# レスポンス表示用のテキストボックスの作成
response_text = tk.Text(root, height=10, width=60, wrap="word")
response_text.pack(pady=10)

# ボタンの作成
def on_button_click():
    user_message = entry.get()
    if user_message:
        data = {
            "model": "qwen25-3b",
            "messages": [
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            "max_tokens": 256,
            "stream": False
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.post(endpoint, headers=headers, data=json.dumps(data), verify=False)
        if response.status_code == 200:
            response_data = response.json()
            bot_response = response_data['choices'][0]['message']['content']
            response_text.delete(1.0, tk.END)  # テキストボックスをクリア
            response_text.insert(tk.END, f"User: {user_message}\nBot: {bot_response}\n\n")
        else:
            response_text.delete(1.0, tk.END)  # テキストボックスをクリア
            response_text.insert(tk.END, f"Error: {response.status_code}\n{response.text}\n\n")
    else:
        response_text.delete(1.0, tk.END)  # テキストボックスをクリア
        response_text.insert(tk.END, "Please enter a message.\n\n")

button = ttk.Button(root, text="Send", style="TButton", command=on_button_click)
button.pack(pady=10)

# メインループの開始
root.mainloop()

