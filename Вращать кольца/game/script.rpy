init python:
    investigation_points = 0
default degs1 = 0
default degs2 = 0
default degs3 = 0

transform rotary(degrees=0):
    subpixel True
    linear 1.0 rotate degrees

label start:
    scene bg black

    $ hf_init("bg_room", (0),(1),(2),(3))

    # покажем вместе с фоном и фигурки на нём
    $ hf_bg()
    with dissolve

    centered "{size=+24}Нужно собрать головоломку.\nНачинаем!"
    # запустим игру
    $ hf_start()

    $ renpy.pause(1, hard=True)

    if game2_win == True:
        $ investigation_points += 5
        centered "{size=+24}Вторая улика найдена - схема"

    return