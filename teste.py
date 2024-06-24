from tkinter import *
from tkinter import font
from customtkinter import *
from PIL import ImageTk, Image, ImageOps, ImageEnhance
from ctype import windll, byref, sizeof, c_int
from tktimepicker import AnalogPicker, AnalogThemes
from tksheet import *
from tkinter import ttk
from datetime import datetime
import calendar
from myfirebase import MyFireBase
from operator import itemgetter
from main import Relogio
import getpass
import os
import sys
import subprocess
import wmi




janela = CTk()
janela.title("pull-it train")

height = janela.winfo_screenheight() / 2
width = janela.winfo_screenwidth() / 2
janela.geometry(f"355x520+600+200")

janela.iconbitmap("calendar.ico")
#
# janela.resizable(width=FALSE, height=FALSE)
janela.config(background="#000000")

HWND = windll.user32.GetParent(janela.winfo_id())
titlebar_color = 0x00141414
windll.dwmapi.DwmSetWindowAttribute(HWND,
                                    35,
                                    byref(c_int(titlebar_color)),
                                    sizeof(c_int))



font.families()


img = Image.open("imgs/bg.jpg")
img = img.resize((700, 700))
bg = ImageTk.PhotoImage(img)
janela.bg = bg

button_true = False

agenda_i = [['15:35', 'café', 'Beber', 'dom-seg-ter-qua-qui-sex-sab'], ['22:34', 'teste', 'Trabalhar', 'dom-seg-ter-qua-qui-sex-sab'], ['23:30', 'dormir', 'Dormir', 'dom-seg-ter-qua-qui-sex-sab']]

def printLn():
    global canvas3
    canvas3.destroy()
    canvas3 = CTkCanvas(janela, highlightthickness=0)
    canvas3.pack(fill="both", expand=True)
    canvas3.configure(background="#F0F0F0")
    rect = CTkLabel(canvas3, text='', fg_color='#141414', height=180, width=2000)
    rect.place(relx=0.4, rely=0, anchor=CENTER)
    title = CTkLabel(canvas3, text=f'Agenda', fg_color="#141414", width=200, height=40,
                     font=("Arial", 15),
                     pady=10)
    title.place(relx=0.4, rely=0.1, anchor=CENTER)
    rect = CTkLabel(canvas3, text='', fg_color='#141414', height=130, width=2000)
    rect.place(relx=0.4, rely=1, anchor=CENTER)
    sheet = Sheet(canvas3, table_bg="#FFFFFF", index_bg="#FFFFFF", header_bg="#141414", height=200, width=400,
                  header_fg="#00E88F", frame_bg="#141414", header_grid_fg="#141414", index_grid_fg="#FFFFFF",
                  row_index_width=20, align="center", column_width=80,
                  table_selected_cells_border_fg="#00E88F", table_selected_cells_bg="#FFFFFF",
                  table_selected_cells_fg="#000000",
                  table_selected_box_cells_fg="#00E88F", table_selected_box_rows_fg="#FFFFFF",
                  table_selected_box_columns_fg='#000000',
                  table_selected_columns_border_fg="#00E88F", table_selected_columns_bg="#FFFFFF",
                  table_selected_columns_fg="#000000",
                  table_selected_rows_border_fg="#00E88F", table_selected_rows_bg="#FFFFFF",
                  table_selected_rows_fg="#000000",
                  header_selected_cells_bg="#00E88F", header_selected_cells_fg="#000000",
                  header_selected_columns_bg="#00E88F", header_selected_columns_fg="#000000",
                  index_selected_cells_bg="#00E88F", index_selected_cells_fg="#000000",
                  index_selected_rows_bg="#00E88F", index_selected_rows_fg="#000000",
                  popup_menu_fg="#000000", popup_menu_bg='#FFFFFF', popup_menu_highlight_bg="#00E88F",
                  popup_menu_highlight_fg="#000000",
                  headers=["horário", "nome", "tipo", "dias"]
                  )
    sheet.set_sheet_data(data=agenda_i)
    sheet.column_width(column=3, width=200, redraw=True)
    sheet.column_width(column=1, width=150, redraw=True)
    # sheet.change_theme("light green", redraw=True)
    sheet.place(relx=0.5, rely=0.4, anchor=CENTER)
    sheet.pack(padx=60, pady=150)

    items = sheet["A1"].expand().options(header=True, index=True).data
    home_a = Image.open("imgs/home_active.png")
    home_a = home_a.resize((60, 60))
    home_a = ImageTk.PhotoImage(home_a)

    botao_home = CTkButton(canvas3, image=home_a, text="",
                           compound=LEFT, border_width=0, fg_color="#141414", width=30, corner_radius=0, hover=True,
                           hover_color="#141414", command=LogIn)
    botao_home.place(relx=0.1, rely=0.9)
    botao_agenda = CTkButton(canvas3, image=home_a, text="",
                             compound=LEFT, border_width=0, fg_color="#141414", width=30, corner_radius=0, hover=True,
                             hover_color="#141414")
    botao_agenda.place(relx=0.45, rely=0.9)
    botao_balance = CTkButton(canvas3, image=home_a, text="",
                              compound=LEFT, border_width=0, fg_color="#141414", width=30, corner_radius=0, hover=True,
                              hover_color="#141414")
    botao_balance.place(relx=0.8, rely=0.9)
    global botao_edit
    botao_edit = Button(canvas3, text="edit", width=10, background="#141414", activebackground="#08784d",
                        activeforeground="#00E88F", fg="#00E88F", font=("Arial", 13), borderwidth=0,
                        cursor="hand2")
    global botao_add
    botao_add = Button(canvas3, text="+", width=10, background="#00E88F", activebackground="#1bfaa5",
                       activeforeground="#000000", fg="#000000", font=("Arial", 13), borderwidth=0,
                       cursor="hand2")
    botao_edit.place(relx=0.5, rely=0.75, anchor=CENTER)
    botao_add.place(relx=0.5, rely=0.7, anchor=CENTER)

def LogIn():
    global canvas1
    canvas1.destroy()
    global canvas3
    try:
        canvas3.destroy()
    except:
        pass
    canvas3 = CTkCanvas(janela, highlightthickness=0)
    canvas3.pack(fill="both", expand=True)
    canvas3.configure(background="#F0F0F0")

    rect = CTkLabel(canvas3, text='', fg_color='#141414', height=180, width=2000)
    rect.place(relx=0.4, rely=0, anchor=CENTER)
    title = CTkLabel(canvas3, text=f'Home', fg_color="#141414", width=200, height=40,
                     font=("Arial", 15),
                     pady=10)
    title.place(relx=0.4, rely=0.1, anchor=CENTER)
    rect = CTkLabel(canvas3, text='', fg_color='#141414', height=130, width=2000)
    rect.place(relx=0.4, rely=1, anchor=CENTER)

    home_a = Image.open("imgs/home_active.png")
    home_a = home_a.resize((60, 60))
    home_a = ImageTk.PhotoImage(home_a)

    botao_home = CTkButton(canvas3, image=home_a, text="",
                           compound=LEFT, border_width=0, fg_color="#141414", width=30, corner_radius=0, hover=True, hover_color="#141414")
    botao_home.place(relx=0.1, rely=0.9)
    botao_agenda = CTkButton(canvas3, image=home_a, text="",
                            compound=LEFT, border_width=0, fg_color="#141414", width=30, corner_radius=0, hover=True, hover_color="#141414", command=printLn)
    botao_agenda.place(relx=0.45, rely=0.9)
    botao_balance = CTkButton(canvas3, image=home_a, text="",
                            compound=LEFT, border_width=0, fg_color="#141414", width=30, corner_radius=0, hover=True, hover_color="#141414")
    botao_balance.place(relx=0.8, rely=0.9)

    iframe = CTkScrollableFrame(canvas3, height=250, width=300, fg_color="#F0F0F0", scrollbar_fg_color="#F0F0F0",
                                scrollbar_button_color="#F0F0F0", scrollbar_button_hover_color="#F0F0F0")
    iframe.place(relx=0.5, rely=0.5, anchor=CENTER)
    progress_bar = CTkProgressBar(canvas3, orientation="horizontal", progress_color="#00E88F", fg_color="#dbdbdb")
    progress_bar.set(value=0)
    progress_bar.place(relx=0.5, rely=0.23, anchor=CENTER)

    dict_button = {}
    cont = 0
    for event in agenda_i:
        dict_button[f"{cont}"] = CTkCheckBox(iframe, text=f'teste', onvalue=1, offvalue=0,
                                             text_color="#141414", checkmark_color="#141414", checkbox_width=20,
                                             checkbox_height=20,
                                             hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5,
                                             fg_color="#00E88F", border_width=2)
        aum = cont / 20

        # dict_button[f'{cont}'].place(relx=0.5, rely=0.3 + aum, anchor=CENTER)
        dict_button[f"{cont}"].pack(pady=10)
        cont += 1
        if cont == 6:
            iframe.configure(scrollbar_fg_color="#F0F0F0", scrollbar_button_color="#dbdbdb",
                             scrollbar_button_hover_color="#00E88F")

    label_porcentagem = CTkLabel(canvas3, text=f'Vamos lá! Há muito pela frente', fg_color="#F0F0F0",
                                 text_color="#00E88F", width=200, height=20,
                                 font=("Arial", 15),
                                 pady=10)
    label_porcentagem.place(relx=0.5, rely=0.8, anchor=CENTER)


global canvas1
canvas1 = CTkCanvas(janela, highlightthickness=0)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(-50, 0, image=bg,
                     anchor="nw")


shade  = Image.new( mode = "RGBA", size = (600, 900), color = (20, 20, 20, 180))
shade.save("imgs/img.png")
shade = Image.open("imgs/img.png")
enhancer = ImageEnhance.Contrast(shade)
shade = enhancer.enhance(0.9)
shade = ImageTk.PhotoImage(shade)
janela.shade = shade
canvas1.create_image(0, 0, image=shade,
                     anchor="nw")

img = Image.open("imgs/pull-it.jpg")
img = img.resize((350, 150))
img = ImageTk.PhotoImage(img)
janela.img = img
canvas1.create_image(45, 110, image=img, anchor="nw")

label2 = CTkLabel(janela, text="Email", fg_color="#141414", width=200, height=20, font=("Arial", 15), pady=10)
label2.place(relx=0.5, rely=0.6, anchor=CENTER)


label_rect = CTkLabel(canvas1, text='', bg_color='#F0F0F0', height=500, width=280)
label_rect.place(relx=0.5, rely=1, anchor=CENTER)

label_rect = CTkLabel(canvas1, text='', fg_color='#141414', height=498, width=279)
label_rect.place(relx=0.5, rely=1, anchor=CENTER)


email = CTkEntry(janela, width=200, fg_color="#FFFFFF", border_width=0, text_color="#141414")
email.place(relx=0.5, rely=0.65, anchor=CENTER)

label3 = CTkLabel(janela, text="Senha", fg_color="#141414", width=200, height=20, font=("Arial", 15), pady=10)
label3.place(relx=0.5, rely=0.73, anchor=CENTER)
senha = CTkEntry(janela, width=200, fg_color="#FFFFFF", border_width=0, text_color="#141414")
senha.configure(show="*")
senha.place(relx=0.5, rely=0.78, anchor=CENTER)

botao = Button(janela, text="Login", width=20, background="#3b7a3b", activebackground="#FFFFFF", activeforeground="black", fg="white", font=("Arial", 13), borderwidth=0, command=LogIn, cursor="hand2")
botao.place(relx=0.5, rely=0.88, anchor=CENTER)

botao2 = Button(janela, text="Sing Up", width=0, background="#141414", activeforeground="#51519e", activebackground="#141414", fg="#7f7ff5", font=("Arial", 13), borderwidth=0, cursor="hand2")
botao2.place(relx=0.5, rely=0.93, anchor=CENTER)


janela.mainloop()