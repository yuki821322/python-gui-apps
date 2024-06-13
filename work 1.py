import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def button1_action():  # 関数の定義 ※ボタンが押されたときの動き
    user_input = entry1.get()  # 入力値を取得
    user_input2 = entry2.get()
    user_input3 = int(user_input) + int(user_input2)
    label1.config(text=f"{user_input3}")  # 画面に出力


def button2_action():  # 関数の定義 ※ボタンが押されたときの動き
    user_input = entry1.get()  # 入力値を取得
    user_input2 = entry2.get()
    user_input3 = int(user_input) - int(user_input2)
    label1.config(text=f"{user_input3}")  # 画面に出力


def button3_action():  # 関数の定義 ※ボタンが押されたときの動き
    user_input = entry1.get()  # 入力値を取得
    user_input2 = entry2.get()
    user_input3 = int(user_input) * int(user_input2)
    label1.config(text=f"{user_input3}")  # 画面に出力


def button4_action():  # 関数の定義 ※ボタンが押されたときの動き
    user_input = entry1.get()  # 入力値を取得
    user_input2 = entry2.get()
    user_input3 = int(user_input) // int(user_input2)
    label1.config(text=f"{user_input3}")  # 画面に出力


# def button_action():  # 関数の定義 ※ボタンが押されたときの動き
# user_input = entry1.get()  # 入力値を取得
# label1.config(text=f"Hello, {user_input}!")  # 画面に出力


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

entry2 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry2.pack(pady=10)


# ボタンの作成
button1 = tk.Button(window, text="＋", command=button1_action)
button1.pack(pady=10)

button2 = tk.Button(window, text="-", command=button2_action)
button2.pack(pady=10)

button3 = tk.Button(window, text="×", command=button3_action)
button3.pack(pady=10)

button4 = tk.Button(window, text="÷", command=button4_action)
button4.pack(pady=10)


# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
