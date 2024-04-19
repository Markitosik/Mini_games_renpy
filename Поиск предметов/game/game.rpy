init python:
    # автоматическое объявление спрайтов (включая webp)
    images_auto()

# НАСТРОЙКИ
    # имя папки со спрайтами игры в директории images плюс пробел
    hf_dir = "game"

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
        for item, x, y in args:
            hf_needed.append((item, x, y))

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
        """запуск игры"""
        store.hf_game_mode = True
        renpy.call_screen("game")
        hf_bg()

    # клик по предмету (перенести его в инвентарь или убрать оттуда)
    def hf_click(item, x, y):
        """обработка клика по предмету"""
        store.hf_needed.pop(hf_needed.index((item, x, y)))
        renpy.restart_interaction()
        # осталось собрать
    HFClick = renpy.curry(hf_click)


screen game():
    add hf_back

    # все предметы на экране
    for i, x, y in hf_needed:
        $ item = hf_dir + " " + i
        # предмет-кнопка
        imagebutton:
            idle item
            pos(x, y)
            # наведение на пиксель
            focus_mask True
            if hf_game_mode:
                hover At(item, brightness(.1))
                # обработка клика
                action HFClick(i, x, y)

    # анимация таймера
    if hf_game_mode:
        if len(hf_needed) < 1:
            timer .01 repeat True action Return()
