default game2_win = False
init python:
    # автоматическое объявление спрайтов (включая webp)
    images_auto()
    can_click = False

# НАСТРОЙКИ
    # имя папки со спрайтами игры в директории images плюс пробел
    hf_dir = "game1"

# ВНУТРЕННИЕ ПЕРЕМЕННЫЕ
    # режим игры (False - режим фона)
    hf_game_mode = False
    # предметы, которые нужно найти
    hf_needed = []
    # фон игры
    hf_back = "black"

    def hf_init(bg, *args, **kwargs):
        """инициализация игры"""
        global hf_needed, hf_back
        # обнуляем списки и переменные
        hf_needed = []
        hf_back = bg
        # добавляем в список предметы, которые нужно найти
        for item in args:
            hf_needed.append((item))

    def hf_bg():
        """показать игру в виде фона"""
        store.hf_game_mode = False
        show_s("game")

    def hf_hide():
        """спрятать игру-фон"""
        hf_bg()
        renpy.with_statement(None)
        hide_s("game")

    def hf_start():
        global can_click
        global degs1, degs2, degs3
        """запуск игры"""

        degs1 = renpy.random.randint(1,4) * 72
        degs2 = renpy.random.randint(1,4) * 72
        degs3 = renpy.random.randint(1,4) * 72
        can_click = True
        store.hf_game_mode = True
        renpy.call_screen("game")
        hf_bg()


screen game():
    add hf_back

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        idle "figure1"
        action SetVariable("degs1", degs1 + 72) at rotary(degs1) focus_mask True

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        idle "figure2"
        action SetVariable("degs2", degs2 + 72) at rotary(degs2) focus_mask True

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        idle "figure3"
        action SetVariable("degs3", degs3 + 72) at rotary(degs3) focus_mask True

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        idle "figure4"

    if degs1 % 360 == 0 and degs2 % 360 == 0 and degs3 % 360 == 0 and can_click == True:
        $ can_click = False
        $ store.game2_win = True
        #$ Hide('RotateTheImage_0')
        timer 1.5 repeat True action Return()
