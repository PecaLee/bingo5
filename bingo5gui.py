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
        
        bingo = [0, 0, 0, 0, "fr", 0, 0, 0, 0]

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
                        print(f"{play}番目抽選", " ", "="*16, f"=  {bingo[0]} =  {bingo[1]} = {bingo[2]} =", "="*16, f"= {bingo[3]} = {bingo[4]} = {bingo[5]} =", "="*16, f"= {bingo[6]} = {bingo[7]} = {bingo[8]} =", "="*16, " ", sep='\n' )
                    print("当たりますように")
            elif num == 0:
                print(" ", "ビンゴ５抽選を辞めます。", sep='\n')
            else:
                print(" ", "宝くじは２回までやりましょう。", sep='\n')

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