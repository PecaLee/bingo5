import tkinter
import tkinter.font as tkFont

bingo_window = tkinter.Tk()
font_style = tkFont.Font(size = 20)

bingo_window.title("bingo5 抽選機")
bingo_window.geometry("400x400")
bingo_window.resizable(False, True)

title = tkinter.Label(bingo_window, text = "bingo5 抽選機", height = 5, font = font_style)
title.pack()

bingo_window.mainloop()