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
    seireki = int(entry1.get())  # 入力値を取

    if seireki > 1869 and seireki <= 1912:
        gengou = "明治"
        wareki = seireki - 1867
    elif seireki > 1912 and seireki <= 1958:
        gengou = "大正"
        wareki = seireki - 1911

    elif seireki > 1958 and seireki <= 1989:
        gengou = "昭和"
        wareki = seireki - 1925

    elif seireki > 1989 and seireki <= 2019:
        gengou = "平成"
        wareki = seireki - 1988

    elif seireki > 2019 and seireki <= 2024:
        gengou = "令和"
        wareki = seireki - 2018

    label1.config(text=f"{gengou}{wareki}")


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="和暦", command=button1_action)
button1.pack(pady=10)


# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)


# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
