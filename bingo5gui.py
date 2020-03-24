from random import randrange
import tkinter
import tkinter.font as tkFont

bingo_window = tkinter.Tk()
title_style = tkFont.Font(size = 20)
article_style = tkFont.Font(size = 11)

bingo_window.title("bingo5 抽選機")
bingo_window.geometry("400x800")
bingo_window.resizable(False, False)

def s_button_destroy():
    def save_num(event):
        num = int(input_text.get())
        text_input.destroy()
        input_text.destroy()
        text_enter.destroy()
        
        bingo = [0, 0, 0, 0, "free", 0, 0, 0, 0]

        def end_app():
            bingo_window.destroy()

        def bingo5():
            bingo[0] = randrange(1, 5)
            bingo[1] = randrange(6, 10)
            bingo[2] = randrange(11, 15)
            bingo[3] = randrange(16, 20)
            bingo[5] = randrange(21, 25)
            bingo[6] = randrange(26, 30)
            bingo[7] = randrange(31, 35)
            bingo[8] = randrange(36, 40)

        def takara():
            if 0 < num < 3:
                if num < 3:
                    for play in range(1, num+1):
                        bingo5()
                        bingo1_info = tkinter.Label(bingo_window, text = f"{play}番目の抽選", font = article_style)
                        bingo1_info.pack()

                        globals()[f"frame{play}"] = tkinter.Frame(bingo_window)
                        globals()[f"frame{play}"].pack()
                        anchor_row = [0, 0, 0, 1, 1, 1, 2, 2, 2]
                        anchor_column = [1, 2, 3, 1, 2, 3, 1, 2, 3]
                        for bingo_num in range(1, 10):
                            bingo1_info = tkinter.Label(bingo_window, text = f"{play}番目抽選", font = article_style)
                            globals()[f"bingo_{bingo_num}"] = tkinter.Label(globals()[f"frame{play}"], text = bingo[bingo_num-1], font = article_style, height = 2, width = 2)
                            globals()[f"bingo_{bingo_num}"].grid(row = anchor_row[bingo_num-1], column = anchor_column[bingo_num-1], padx = 20, pady = 20)

                    pray = tkinter.Label(bingo_window, text = "当たりますように", font = article_style)
                    pray.pack()
            elif num == 0:
                end_bingo = tkinter.Label(bingo_window, text = "ビンゴ５抽選を辞めます。", font = article_style, height = 5)
                end_bingo.pack()
            else:
                limit_bingo = tkinter.Label(bingo_window, text = "宝くじは２回までやりましょう。", font = article_style, height = 5)
                limit_bingo.pack()

            end_app_button = tkinter.Button(bingo_window, command = end_app, text = "終了", font = title_style)
            end_app_button.pack(padx = 30, pady = 30)

        takara()

    start_button.destroy()
    text_input = tkinter.Label(bingo_window, text = "ビンゴ５を何回しまうか？ 最大は２回までです。", font = article_style)
    text_input.pack()
    input_text = tkinter.Entry(bingo_window, width = 20)
    input_text.bind("<Return>", save_num)
    input_text.pack()
    text_enter = tkinter.Label(bingo_window, text = "入力後エンターキーを押してください。", font = article_style)
    text_enter.pack()

title = tkinter.Label(bingo_window, text = "bingo5 抽選機", height = 5, font = title_style)
title.pack()

start_button = tkinter.Button(bingo_window,command = s_button_destroy, text = "start!", height = 1, font = title_style)
start_button.pack()

bingo_window.mainloop()