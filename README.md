# Мини-игры для визуальных новелл на движке RenPY  
## 1. Поиск предметов:  
  Необходимо найти и собрать все предметы(предметы подсвечиваются при наведении)

  ### Как добавит игру в код новеллы: 
  
        # передаем задний фон, изображения предметов и координаты
        $ hf_init("bg room",
            ("1", 100, 100),
            ("2", 100, 150),
            ("3", 200, 250),
            ("4", 500, 250),
            ("5", 750, 500),
        )
    
        # покажем фон и фигурки
        $ hf_bg()
        with dissolve
        
        $ hf_start() # запустим игру

## 2. Вращение колец:
  Необходимо вращать 3 кольца, чтобы собрался рисунок из кусочков изображений на этих кольцах   

  ### Как добавит игру в код новеллы:  

        $ hf_init("bg_room", "1", "2", "3", "4") # передаем задний фон и изображения для дисков
        
        # покажем фон и диски
        $ hf_bg()
        with dissolve
        
        $ hf_start() # запустим игру
