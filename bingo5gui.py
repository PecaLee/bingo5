import tkinter
import tkinter.font as tkFont

bingo_window = tkinter.Tk()
font_style = tkFont.Font(size = 20)

bingo_window.title("bingo5 抽選機")
bingo_window.geometry("400x250")
bingo_window.resizable(False, False)

title = tkinter.Label(bingo_window, text = "bingo5 抽選機", height = 5, font = font_style)
title.pack()

start_button = tkinter.Button(bingo_window, text = "start!", height = 1, font = font_style)
start_button.pack()

bingo_window.mainloop()