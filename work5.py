import tkinter as tk
import random

# お約束のコード
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# お約束のコード終わり

str_list = ["フリーザ", "ビルス", "悟空", "ゴジラ", "ベジータ", "クリリン"]


def button_action():
    global odai
    user_input_text = user_input.get()
    if user_input_text == odai:
        label1.config(text="")
        odai = random.choice(str_list)
        text1.config(text=odai)
    else:
        label1.config(text="")
    user_input.delete(0, tk.END)


odai = random.choice(str_list)

# テキストボックス
text1 = tk.Label(window, text=odai, bg=bg_color, fg=fg_color)
text1.pack(pady=10)

# 入力フィールドの作成
user_input = tk.Entry(window, bg=fg_color, fg=bg_color)
user_input.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="ok", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# お約束のコード
window.mainloop()
# お約束のコード終わり
