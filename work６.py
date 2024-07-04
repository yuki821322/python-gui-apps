import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


# プレイヤー　＝　まる
class MARU:
    # ボタンが押された時の処理
    def button_action(i, j):
        if buttons[i][j].cget("text") == "":
            buttons[i][j].config(text="◯")
            buttons[i][j].config(state="disabled")
            if check_win():
                label2.config(text="まるの勝ちです")
                return True
        return False


# コンピュータ　＝　ばつ
class BATU:
    def button_action(i, j):
        if buttons[i][j].cget("text") == "":
            buttons[i][j].config(text="✖️")
            buttons[i][j].config(state="disabled")
            if check_win2():
                label2.config(text="ばつの勝ちです")
                return True
        return False


XO = 0
player_turn = True  # プレイヤーのターンを管理するフラグ


def button_action(i, j):
    global XO, player_turn  # 上の二つをグローバル関数で持ってくる
    if player_turn:
        if XO == 0:
            if MARU.button_action(i, j):
                player_turn = False  # ゲーム終了
            else:
                XO = 1
                player_turn = False  # プレイヤーのターン終了
                window.after(100, computer_turn)
        elif XO == 1:
            if BATU.button_action(i, j):
                player_turn = False  # ゲーム終了
            else:
                XO = 0
                player_turn = True  # プレイヤーのターンに戻す


def computer_turn():
    global XO, player_turn
    c_cellse = [
        (i, j) for i in range(3) for j in range(3) if buttons[i][j].cget("text") == ""
    ]
    if c_cellse:
        i, j = computer_reinforcement()
        if BATU.button_action(i, j):
            player_turn = False  # ゲーム終了
        else:
            XO = 0
            player_turn = True  # 自分のターンに戻す


def computer_reinforcement():  # コンピューター強化
    # 勝利できる場所があれば、その場所に置く
    for i in range(3):
        for j in range(3):
            if buttons[i][j].cget("text") == "":
                buttons[i][j].config(text="✖️")
                if check_win2():
                    buttons[i][j].config(text="")
                    return i, j
                buttons[i][j].config(text="")
    # プレイヤーが次に勝利できる場所を防ぐ
    for i in range(3):
        for j in range(3):
            if buttons[i][j].cget("text") == "":
                buttons[i][j].config(text="◯")
                if check_win():
                    buttons[i][j].config(text="")
                    return i, j
                buttons[i][j].config(text="")
    # それ以外の場合、ランダムに空きマスを選ぶ
    return random.choice(
        [(i, j) for i in range(3) for j in range(3) if buttons[i][j].cget("text") == ""]
    )


# まるの勝利
def check_win():
    for row in buttons:
        if (
            row[0].cget("text") == "◯"
            and row[1].cget("text") == "◯"
            and row[2].cget("text") == "◯"
        ):
            return True
    for col in range(3):
        if (
            buttons[0][col].cget("text") == "◯"
            and buttons[1][col].cget("text") == "◯"
            and buttons[2][col].cget("text") == "◯"
        ):
            return True
    if (
        buttons[2][0].cget("text") == "◯"
        and buttons[1][1].cget("text") == "◯"
        and buttons[0][2].cget("text") == "◯"
    ):
        return True
    if (
        buttons[0][0].cget("text") == "◯"
        and buttons[1][1].cget("text") == "◯"
        and buttons[2][2].cget("text") == "◯"
    ):
        return True
    return False


# ばつの勝利
def check_win2():
    for row in buttons:
        if (
            row[0].cget("text") == "✖️"
            and row[1].cget("text") == "✖️"
            and row[2].cget("text") == "✖️"
        ):
            return True
    for col in range(3):
        if (
            buttons[0][col].cget("text") == "✖️"
            and buttons[1][col].cget("text") == "✖️"
            and buttons[2][col].cget("text") == "✖️"
        ):
            return True
    if (
        buttons[2][0].cget("text") == "✖️"
        and buttons[1][1].cget("text") == "✖️"
        and buttons[0][2].cget("text") == "✖️"
    ):
        return True
    if (
        buttons[0][0].cget("text") == "✖️"
        and buttons[1][1].cget("text") == "✖️"
        and buttons[2][2].cget("text") == "✖️"
    ):
        return True
    return False


# 勝利時の出力ラベル
label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)


# リセットボタンが押された時の処理
def reset_action():
    global player_turn, XO
    for row in buttons:
        for button in row:
            button.config(text="")
            button.config(state="normal")  # ボタンを有効にする
    label2.config(text="")
    XO = 0
    player_turn = True


# 出力ラベルの作成
label1 = tk.Label(window, text="あなたは◯です", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# リセットボタンの作成
button_set = tk.Button(
    window,
    text="リセット",
    command=reset_action,
    bg=fg_color,
    fg=bg_color,
    font=("Helvetica", 25),
)
button_set.pack(pady=10)

# ボタンをまとめて配置するためのフレームを作成
button_frame = tk.Frame(window, bg=fg_color)
button_frame.pack(pady=10)


# frameの中にボタンを配置するループ
buttons = []  # それぞれのボタンが入るリストを用意
for i in range(3):
    row_button = []  # 行を確保して保持するためのリスト
    for j in range(3):
        button = tk.Button(
            button_frame,  # button_frameに配置する
            text="",
            # r=i c=jを引数に指定しbutton_actionに渡す　そしてcommandで関数を呼び出せるようにする
            command=lambda r=i, c=j: button_action(r, c),
            bg=fg_color,
            fg=bg_color,
            font=("Helvetica", 25),
        )
        button.grid(row=i, column=j, padx=10, pady=10)
        # ループ処理で作成したボタンを行を確保するためrow_buttonリストに追加する
        row_button.append(button)
    buttons.append(row_button)  # 行を確保したリストをbuttonsリストに追加する


# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
