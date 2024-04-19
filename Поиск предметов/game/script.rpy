define gui.text_outlines = [(4, "0124", 0, 0), (3, "0124", 0, 0), (1, "0124", 0, 0), (1, "0124", 0, 0)]

label splashscreen:
    # громкость по умолчанию
    python:
        # при первом запуске
        if not persistent.set_volumes:
            persistent.set_volumes = True
            # музыку потише
            _preferences.volumes['music'] = .5
            _preferences.volumes['sfx'] = .5
            # игра на весь экран
            _preferences.fullscreen = True
    return

# Игра начинается здесь:
label start:

    # определим фон игры, время игры в секундах
    # и зададим параметры игры - спрайты и положение для собираемых предметов
    $ hf_init("bg room",
        ("beer", 1013, 705),
        ("elf", 111, 560),
        ("flowers", 700, 615),
        ("skull", 1813, 161),
        ("sprite", 355, 240),
         )

    # покажем вместе с фоном и фигурки на нём
    $ hf_bg()
    with dissolve
    "Играть"
    centered "{size=+24}Нужно собрать все предметы.\nНачинаем!"

    # запустим игру
    $ hf_start()

    # жёсткая пауза, чтобы игрок перестал кликать и не пропустил результаты
    $ renpy.pause(1, hard=True)

    # результаты
    if len(hf_needed) == 0:
        centered "{size=+24}Ура! Все предметы собраны!"

    menu:
        "Ещё раз":
            jump start

        "Хватит":
            pass

    $ hf_hide()
    with dissolve
    return
