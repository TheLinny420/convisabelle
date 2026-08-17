import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import date
import random
import math


# ============================================================
# CONFIGURAÇÕES
# ============================================================

root = tk.Tk()
root.title("Um convite...")
root.geometry("1000x720")
root.minsize(760, 620)
root.configure(bg="#02040d")

# Permite minimizar / maximizar / redimensionar
root.resizable(True, True)


# ============================================================
# PALETA
# ============================================================

BG = "#02040d"
BG2 = "#050918"
PANEL = "#080d20"
PANEL2 = "#0b122b"

BLUE = "#63ddff"
BLUE2 = "#9cecff"

PURPLE = "#8b5cf6"
PURPLE2 = "#c5a8ff"

WHITE = "#f5f1ff"
SOFT = "#bfc5df"

BLACK = "#010208"

CARD = "#0c1430"
CARD_HOVER = "#121d42"


# ============================================================
# FONTES
# ============================================================

# Tentamos usar fontes mais elegantes.
# Se alguma não existir, o Tkinter usa a alternativa.

FONT_TITLE = ("Georgia", 27, "bold")
FONT_SUBTITLE = ("Palatino Linotype", 14, "italic")
FONT_TEXT = ("Palatino Linotype", 12)
FONT_SMALL = ("Palatino Linotype", 10)
FONT_BUTTON = ("Georgia", 11, "bold")


# ============================================================
# FUNDO PRINCIPAL
# ============================================================

background = tk.Canvas(
    root,
    bg=BG,
    highlightthickness=0
)

background.pack(
    fill="both",
    expand=True
)


# ============================================================
# ESTRELAS
# ============================================================

stars = []

for _ in range(220):

    x = random.randint(0, 1400)
    y = random.randint(0, 900)

    size = random.choice([1, 1, 1, 2, 2, 3])

    speed = random.uniform(
        0.15,
        0.75
    )

    twinkle = random.choice([
        True,
        False
    ])

    color = random.choice([
        BLUE,
        BLUE2,
        WHITE,
        PURPLE2
    ])

    obj = background.create_oval(
        x,
        y,
        x + size,
        y + size,
        fill=color,
        outline=""
    )

    stars.append({
        "obj": obj,
        "speed": speed,
        "size": size,
        "twinkle": twinkle,
        "base": color
    })


# ============================================================
# LUA
# ============================================================

def draw_moon():

    w = background.winfo_width()

    x = w - 130
    y = 85

    background.delete("moon")

    background.create_oval(
        x - 45,
        y - 45,
        x + 45,
        y + 45,
        fill="#b9f3ff",
        outline="",
        tags="moon"
    )

    background.create_oval(
        x - 25,
        y - 53,
        x + 55,
        y + 27,
        fill=BG,
        outline="",
        tags="moon"
    )


# ============================================================
# ESTRELAS CADENTES
# ============================================================

shooting_stars = []

for _ in range(5):

    x = random.randint(
        0,
        1000
    )

    y = random.randint(
        30,
        500
    )

    line = background.create_line(
        x,
        y,
        x + 20,
        y + 20,
        fill=BLUE2,
        width=1,
        tags="shooting"
    )

    shooting_stars.append({
        "obj": line,
        "x": x,
        "y": y,
        "speed": random.uniform(
            1.5,
            3.0
        )
    })


# ============================================================
# ANIMAÇÃO DO CÉU
# ============================================================

def animate():

    width = background.winfo_width()
    height = background.winfo_height()

    # estrelas
    for star in stars:

        background.move(
            star["obj"],
            star["speed"],
            0
        )

        coords = background.coords(
            star["obj"]
        )

        if coords and coords[0] > width:

            new_y = random.randint(
                0,
                max(100, height)
            )

            background.coords(
                star["obj"],
                -5,
                new_y,
                -5 + star["size"],
                new_y + star["size"]
            )

    # estrelas cadentes
    for shooting in shooting_stars:

        shooting["x"] += shooting["speed"]
        shooting["y"] += shooting["speed"]

        background.coords(
            shooting["obj"],
            shooting["x"],
            shooting["y"],
            shooting["x"] + 35,
            shooting["y"] + 35
        )

        if (
            shooting["x"] > width
            or
            shooting["y"] > height
        ):

            shooting["x"] = random.randint(
                -400,
                0
            )

            shooting["y"] = random.randint(
                20,
                max(100, height // 2)
            )

    draw_moon()

    root.after(
        35,
        animate
    )


# ============================================================
# PAINEL CENTRAL
# ============================================================

panel = tk.Frame(
    root,
    bg=PANEL,
    highlightthickness=1,
    highlightbackground="#293b73"
)

panel.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    relwidth=0.76,
    relheight=0.84
)


# ============================================================
# BORDA DECORATIVA
# ============================================================

border = tk.Frame(
    panel,
    bg=PANEL,
    highlightthickness=1,
    highlightbackground="#51429a"
)

border.place(
    x=12,
    y=12,
    relwidth=1,
    relheight=1,
    width=-24,
    height=-24
)


# ============================================================
# ÁREA DAS TELAS
# ============================================================

screen_area = tk.Frame(
    border,
    bg=PANEL
)

screen_area.place(
    x=20,
    y=15,
    relwidth=1,
    relheight=1,
    width=-40,
    height=-100
)


# ============================================================
# RODAPÉ
# ============================================================

footer = tk.Frame(
    border,
    bg="#050a18"
)

footer.place(
    x=0,
    rely=1,
    anchor="sw",
    relwidth=1,
    height=70
)


# ============================================================
# TELAS
# ============================================================

screens = []

for _ in range(5):

    frame = tk.Frame(
        screen_area,
        bg=PANEL
    )

    screens.append(frame)


current_screen = 0


# ============================================================
# OLHO DE BOTÃO
# ============================================================

def create_button_eye(
    parent,
    x,
    y,
    size=34
):

    canvas = tk.Canvas(
        parent,
        width=size,
        height=size,
        bg=parent.cget("bg"),
        highlightthickness=0
    )

    # botão
    canvas.create_oval(
        3,
        3,
        size - 3,
        size - 3,
        fill="#03050c",
        outline="#28304c",
        width=2
    )

    # pequenos detalhes de costura
    canvas.create_arc(
        5,
        5,
        size - 5,
        size - 5,
        start=20,
        extent=80,
        outline="#58617e",
        width=1
    )

    canvas.create_arc(
        5,
        5,
        size - 5,
        size - 5,
        start=200,
        extent=80,
        outline="#58617e",
        width=1
    )

    # duas pequenas perfurações
    hole = size * 0.34

    canvas.create_oval(
        hole - 2,
        hole - 2,
        hole + 2,
        hole + 2,
        fill="#11182d",
        outline=""
    )

    canvas.create_oval(
        size - hole - 2,
        hole - 2,
        size - hole + 2,
        hole + 2,
        fill="#11182d",
        outline=""
    )

    return canvas


# ============================================================
# BOTÕES DE NAVEGAÇÃO COM OLHOS
# ============================================================

def create_nav_button(
    parent,
    text,
    command,
    reverse=False
):

    frame = tk.Frame(
        parent,
        bg="#050a18",
        cursor="hand2"
    )

    eye = create_button_eye(
        frame,
        0,
        0,
        32
    )

    eye.pack(
        side="left" if not reverse else "right",
        padx=6
    )

    label = tk.Label(
        frame,
        text=text,
        font=FONT_BUTTON,
        bg="#050a18",
        fg=WHITE,
        cursor="hand2"
    )

    label.pack(
        side="left" if not reverse else "right",
        padx=5
    )

    def click(event=None):
        command()

    frame.bind(
        "<Button-1>",
        click
    )

    label.bind(
        "<Button-1>",
        click
    )

    eye.bind(
        "<Button-1>",
        click
    )

    def enter(event=None):

        label.config(
            fg=BLUE
        )

    def leave(event=None):

        label.config(
            fg=WHITE
        )

    frame.bind(
        "<Enter>",
        enter
    )

    frame.bind(
        "<Leave>",
        leave
    )

    label.bind(
        "<Enter>",
        enter
    )

    label.bind(
        "<Leave>",
        leave
    )

    return frame


# ============================================================
# INDICADOR DE PÁGINA
# ============================================================

page_indicator = tk.Label(
    footer,
    text="01  •  05",
    font=("Georgia", 9),
    bg="#050a18",
    fg="#727b9e"
)

page_indicator.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)


# ============================================================
# VARIÁVEIS
# ============================================================

chosen_date = ""
chosen_time = ""
chosen_food = ""


# ============================================================
# NAVEGAÇÃO
# ============================================================

def show_screen(number):

    global current_screen

    if number < 0:
        return

    if number >= len(screens):
        return

    current_screen = number

    for screen in screens:

        screen.place_forget()

    screens[number].place(
        x=0,
        y=0,
        relwidth=1,
        relheight=1
    )

    update_navigation()


# ============================================================
# NAVEGAÇÃO
# ============================================================

back_button = create_nav_button(
    footer,
    "voltar",
    lambda: show_screen(
        current_screen - 1
    )
)

back_button.place(
    x=18,
    rely=0.5,
    anchor="w"
)


next_button = create_nav_button(
    footer,
    "avançar",
    lambda: show_screen(
        current_screen + 1
    ),
    reverse=True
)

next_button.place(
    relx=1,
    x=-18,
    rely=0.5,
    anchor="e"
)


# ============================================================
# ATUALIZAR NAVEGAÇÃO
# ============================================================

def update_navigation():

    page_indicator.config(
        text=f"{current_screen + 1:02d}  •  05"
    )

    if current_screen == 0:

        back_button.place_forget()

    else:

        back_button.place(
            x=18,
            rely=0.5,
            anchor="w"
        )


    if current_screen == 0:

        next_button.pack_forget()

        next_button.place(
            relx=1,
            x=-18,
            rely=0.5,
            anchor="e"
        )

    elif current_screen == 1:

        next_button.place(
            relx=1,
            x=-18,
            rely=0.5,
            anchor="e"
        )

    elif current_screen == 2:

        next_button.place(
            relx=1,
            x=-18,
            rely=0.5,
            anchor="e"
        )

    elif current_screen == 3:

        next_button.place(
            relx=1,
            x=-18,
            rely=0.5,
            anchor="e"
        )

    else:

        next_button.place_forget()


# ============================================================
# TELA 1
# ============================================================

screen = screens[0]


tk.Label(
    screen,
    text="☾        ✦        ☽",
    font=("Georgia", 20),
    bg=PANEL,
    fg=BLUE
).pack(
    pady=(12, 2)
)


tk.Label(
    screen,
    text="Oi, Isabele...",
    font=FONT_TITLE,
    bg=PANEL,
    fg=BLUE2
).pack()


tk.Label(
    screen,
    text="um pequeno convite ",
    font=FONT_SUBTITLE,
    bg=PANEL,
    fg=PURPLE2
).pack(
    pady=5
)


tk.Label(
    screen,
    text="✦",
    font=("Georgia", 13),
    bg=PANEL,
    fg=BLUE
).pack(
    pady=2
)


invitation = """
Esse convite é pra saber se você me concede um date.

Não quero simplesmente marcar um encontro.

Quero que VOCÊ escolha o dia.
Quero que VOCÊ escolha a hora.
E quero que VOCÊ escolha o que deseja comer.

Pode escolher algo que ama,
algo que tenha vontade de experimentar...

ou pode deixar tudo por minha conta
e transformar nosso date em uma pequena surpresa.

Eu só tenho uma condição:

QUE VOCÊ APAREÇA.  ♥
"""


tk.Label(
    screen,
    text=invitation,
    font=FONT_TEXT,
    bg=PANEL,
    fg=WHITE,
    justify="center",
    wraplength=590
).pack(
    pady=4
)


tk.Label(
    screen,
    text="O restante deixo por conta do universo,",
    font=FONT_TEXT,
    bg=PANEL,
    fg=SOFT
).pack(
    pady=1
)


tk.Label(
    screen,
    text="das bruxas ...",
    font=FONT_SUBTITLE,
    bg=PANEL,
    fg=PURPLE2
).pack(
    pady=2
)


# ============================================================
# NÃO FUGINDO
# ============================================================

escape_area = tk.Frame(
    screen,
    bg=PANEL,
    height=45
)

escape_area.pack(
    fill="x",
    pady=2
)

escape_area.pack_propagate(False)


no_button = tk.Label(
    escape_area,
    text="não quero 😈",
    font=("Palatino Linotype", 9),
    bg="#11162b",
    fg="#777f9d",
    padx=13,
    pady=7,
    cursor="hand2"
)

no_button.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)


def run_away(event=None):

    width = escape_area.winfo_width()
    height = escape_area.winfo_height()

    x = random.randint(
        10,
        max(10, width - 100)
    )

    y = random.randint(
        3,
        max(3, height - 30)
    )

    no_button.place(
        x=x,
        y=y
    )


no_button.bind(
    "<Enter>",
    run_away
)

no_button.bind(
    "<Button-1>",
    run_away
)


# ============================================================
# TELA 2 — DATA
# ============================================================

screen = screens[1]


tk.Label(
    screen,
    text="☾",
    font=("Georgia", 27),
    bg=PANEL,
    fg=BLUE
).pack(
    pady=(3, 0)
)


tk.Label(
    screen,
    text="Escolha a noite",
    font=FONT_TITLE,
    bg=PANEL,
    fg=BLUE2
).pack()


tk.Label(
    screen,
    text="Você decide babe.",
    font=FONT_SUBTITLE,
    bg=PANEL,
    fg=PURPLE2
).pack(
    pady=2
)


calendar_frame = tk.Frame(
    screen,
    bg="#0b122b",
    highlightbackground="#3a4d80",
    highlightthickness=1
)

calendar_frame.pack(
    pady=5
)


calendar = Calendar(
    calendar_frame,
    selectmode="day",
    date_pattern="dd/mm/yyyy",
    mindate=date.today(),

    background="#0b122b",
    foreground=WHITE,

    headersbackground="#16113b",
    headersforeground=BLUE2,

    selectbackground=PURPLE,
    selectforeground=WHITE,

    normalbackground="#0b122b",
    normalforeground=WHITE,

    weekendbackground="#10152d",
    weekendforeground=PURPLE2,

    othermonthbackground="#070b19",
    othermonthforeground="#4d5470",

    bordercolor="#3c4d78",

    font=("Palatino Linotype", 10),
    headersfont=("Georgia", 9, "bold")
)

calendar.pack(
    padx=8,
    pady=8
)


def confirm_date():

    global chosen_date

    chosen_date = calendar.get_date()

    show_screen(2)


# ============================================================
# TELA 3 — HORA
# ============================================================

screen = screens[2]


tk.Label(
    screen,
    text="⌁",
    font=("Georgia", 35),
    bg=PANEL,
    fg=BLUE
).pack(
    pady=(35, 0)
)


tk.Label(
    screen,
    text="E a hora?",
    font=FONT_TITLE,
    bg=PANEL,
    fg=BLUE2
).pack()


date_preview = tk.Label(
    screen,
    text="",
    font=FONT_SUBTITLE,
    bg=PANEL,
    fg=PURPLE2
)

date_preview.pack(
    pady=5
)


times = [
    "17:00",
    "17:30",
    "18:00",
    "18:30",
    "19:00",
    "19:30",
    "20:00",
    "20:30",
    "21:00",
    "21:30",
    "22:00"
]


time_var = tk.StringVar(
    value="20:00"
)


time_box = tk.Frame(
    screen,
    bg="#0b122b",
    highlightbackground="#394a78",
    highlightthickness=1
)

time_box.pack(
    pady=10
)


time_menu = tk.OptionMenu(
    time_box,
    time_var,
    *times
)

time_menu.config(
    font=("Georgia", 13),
    bg="#111838",
    fg=WHITE,
    activebackground=PURPLE,
    activeforeground=WHITE,
    relief="flat",
    highlightthickness=0,
    width=12
)

time_menu["menu"].config(
    bg="#0b1025",
    fg=WHITE,
    activebackground=PURPLE,
    activeforeground=WHITE
)

time_menu.pack(
    padx=12,
    pady=8
)


def confirm_time():

    global chosen_time

    chosen_time = time_var.get()

    show_screen(3)


# ============================================================
# TELA 4 — COMIDA
# ============================================================

screen = screens[3]


tk.Label(
    screen,
    text="✦",
    font=("Georgia", 27),
    bg=PANEL,
    fg=BLUE
).pack(
    pady=(2, 0)
)


tk.Label(
    screen,
    text="Agora me diga...",
    font=FONT_TITLE,
    bg=PANEL,
    fg=BLUE2
).pack()


tk.Label(
    screen,
    text="o que a bruxa gostaria de comer?",
    font=FONT_SUBTITLE,
    bg=PANEL,
    fg=PURPLE2
).pack(
    pady=3
)


food_frame = tk.Frame(
    screen,
    bg=PANEL
)

food_frame.pack(
    pady=5
)


foods = [
    ("🍕", "Pizza"),
    ("🍔", "Hambúrguer"),
    ("🍣", "Japonês"),
    ("🍝", "Massa"),
    ("🌮", "Mexicano"),
    ("🍰", "Doces"),
    ("🍓", "Algo que eu gosto"),
    ("🔮", "Quero uma surpresa")
]


food_buttons = []


def select_food(value, button):

    global chosen_food

    chosen_food = value

    for b in food_buttons:

        b.config(
            bg=CARD,
            fg=WHITE
        )

    button.config(
        bg="#182451",
        fg=BLUE2
    )


for icon, name in foods:

    card = tk.Frame(
        food_frame,
        bg=CARD,
        width=210,
        height=42,
        cursor="hand2"
    )

    card.grid_propagate(False)

    # duas colunas
    index = len(food_buttons)

    row = index // 2
    col = index % 2

    card.grid(
        row=row,
        column=col,
        padx=6,
        pady=4
    )

    eye = create_button_eye(
        card,
        0,
        0,
        25
    )

    eye.place(
        x=8,
        y=8
    )

    label = tk.Label(
        card,
        text=f"{icon}   {name}",
        font=("Palatino Linotype", 10, "bold"),
        bg=CARD,
        fg=WHITE,
        anchor="w",
        cursor="hand2"
    )

    label.place(
        x=40,
        y=7,
        relwidth=0.75,
        height=28
    )

    def make_click(value, widget):

        return lambda event: select_food(
            value,
            widget
        )

    card.bind(
        "<Button-1>",
        make_click(
            name,
            card
        )
    )

    label.bind(
        "<Button-1>",
        make_click(
            name,
            card
        )
    )

    eye.bind(
        "<Button-1>",
        make_click(
            name,
            card
        )
    )

    def hover_on(event, widget=card):

        if chosen_food != widget:

            widget.config(
                bg=CARD_HOVER
            )

    def hover_off(event, widget=card):

        if widget.cget("bg") != "#182451":

            widget.config(
                bg=CARD
            )

    card.bind(
        "<Enter>",
        hover_on
    )

    card.bind(
        "<Leave>",
        hover_off
    )

    food_buttons.append(card)


def confirm_food():

    if not chosen_food:

        messagebox.showinfo(
            "Ainda falta uma coisa... ✦",
            "Escolha alguma coisa para comer. "
            "Ou escolha 'Quero uma surpresa'. 😏"
        )

        return

    update_final()

    show_screen(4)


# ============================================================
# TELA 5 — FINAL
# ============================================================

screen = screens[4]


tk.Label(
    screen,
    text="☾   ✦   ☽",
    font=("Georgia", 20),
    bg=PANEL,
    fg=BLUE
).pack(
    pady=(12, 3)
)


tk.Label(
    screen,
    text="Então está combinado.",
    font=FONT_TITLE,
    bg=PANEL,
    fg=BLUE2
).pack()


tk.Label(
    screen,
    text="O destino acaba de ganhar uma data.",
    font=FONT_SUBTITLE,
    bg=PANEL,
    fg=PURPLE2
).pack(
    pady=4
)


summary = tk.Frame(
    screen,
    bg="#0b122b",
    highlightbackground="#3f4f7c",
    highlightthickness=1
)

summary.pack(
    padx=50,
    pady=10,
    fill="x"
)


final_date = tk.Label(
    summary,
    text="",
    font=("Palatino Linotype", 11, "bold"),
    bg="#0b122b",
    fg=WHITE
)

final_date.pack(
    pady=5
)


final_time = tk.Label(
    summary,
    text="",
    font=("Palatino Linotype", 11, "bold"),
    bg="#0b122b",
    fg=WHITE
)

final_time.pack(
    pady=5
)


final_food = tk.Label(
    summary,
    text="",
    font=("Palatino Linotype", 11, "bold"),
    bg="#0b122b",
    fg=WHITE
)

final_food.pack(
    pady=5
)


final_message = """
Agora eu só preciso de uma coisa:

você aparecer.

O resto...
deixa comigo.

Talvez seja só um date.

Talvez seja o começo de uma pequena história
que nenhuma de nós estava esperando. 🖤
"""


tk.Label(
    screen,
    text=final_message,
    font=FONT_TEXT,
    bg=PANEL,
    fg=WHITE,
    justify="center"
).pack(
    pady=7
)


tk.Label(
    screen,
    text="✦  🔮  ✦  🖤  ✦  🔮  ✦",
    font=("Georgia", 16),
    bg=PANEL,
    fg=PURPLE2
).pack(
    pady=2
)


# ============================================================
# ATUALIZAR FINAL
# ============================================================

def update_final():

    final_date.config(
        text="📅   " + chosen_date
    )

    final_time.config(
        text="⏰   " + chosen_time
    )

    final_food.config(
        text="✦   " + chosen_food
    )


# ============================================================
# ATUALIZAÇÕES ANTES DE MUDAR DE TELA
# ============================================================

original_show = show_screen


def show_screen(number):

    if number == 2:

        date_preview.config(
            text="📅  " + chosen_date
        )

    original_show(number)


# ============================================================
# CORRIGIR AÇÕES DOS BOTÕES
# ============================================================

# Botão da tela inicial
def go_from_start():

    show_screen(1)


# botão avançar
def next_action():

    if current_screen == 0:

        show_screen(1)

    elif current_screen == 1:

        confirm_date()

    elif current_screen == 2:

        confirm_time()

    elif current_screen == 3:

        confirm_food()


# botão voltar
def back_action():

    show_screen(
        current_screen - 1
    )


# ============================================================
# RECRIAR AÇÕES DOS BOTÕES
# ============================================================

# O botão visual já existe.
# Aqui trocamos a ação através do bind.

def next_click(event=None):

    next_action()


def back_click(event=None):

    back_action()


next_button.bind(
    "<Button-1>",
    next_click
)

back_button.bind(
    "<Button-1>",
    back_click
)


# Também vinculamos os filhos
for widget in next_button.winfo_children():

    widget.bind(
        "<Button-1>",
        next_click
    )


for widget in back_button.winfo_children():

    widget.bind(
        "<Button-1>",
        back_click
    )


# ============================================================
# INÍCIO
# ============================================================

show_screen(0)

animate()

root.mainloop()