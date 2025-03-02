import pygame as pg # підключаємо бібліотеку Pygame
pg.init() # активізуємо всі модулі та функції
mw = pg.display.set_mode((1220, 580)) # створюємо вікно розміром 1220 x 580
bg = pg.image.load("Space.jpg") # завантажуємо тло
bg = pg.transform.scale(bg, (1220, 580)) # змінюємо розмір тла до відповідного розміру
mw.blit(bg, (0, 0)) # прикріплюємо тло
rules_p1 = pg.image.load("Rules1.png") # завантажуємо фото для правила 1
rules_p2 = pg.image.load("Rules2.png") # завантажуємо фото для правила 2
rules_p3 = pg.image.load("Rules3.png") # завантажуємо фото для правила 3
rules_p1 = pg.transform.scale(rules_p1, (610, 290)) # маштабуємо фото для правила 1
rules_p2 = pg.transform.scale(rules_p2, (610, 290)) # маштабуємо фото для правила 2
rules_p3 = pg.transform.scale(rules_p3, (610, 290)) # маштабуємо фото для правила 3
class Hitbox(): # створюємо клас Hitbox
    def __init__ (self, image, x, y, width, height): # створюємо конструктор класу
        self.r = pg.Rect(x, y, width, height) # створюємо прямокутну область задаємо координати та розміри
        self.image = pg.image.load(image) # завантажуємо зображення хітбоксу
        self.image = pg.transform.scale(self.image, (self.r.width, self.r.height)) # змінюємо розмір до відповідного розміру
    def reset(self): # створюємо метод прикріплення хітбоксу
        mw.blit(self.image, (self.r.x, self.r.y)) # прикріплюємо хітбокс
    def collidepoint(self, x, y): # створюємо метод точки зіткнення
        return self.r.collidepoint(x, y) # повертаємо значення координат точки зіткнення
class Label(Hitbox): # створюємо клас Label, який успадковується від класу Hitbox
    def set_text(self, Text, fsize = 12, text_color = (255, 255, 255)): # створюємо метод задання тексту
        self.texto = pg.font.Font('Pixel.ttf', fsize).render(Text, True, text_color) # задаємо шрифт, текст, колір тексту та згладжуємо текст
    def draw(self, shift_x=0, shift_y=0): # створюємо метод виведення тексту
        mw.blit(self.texto, (self.r.x + shift_x, self.r.y + shift_y)) # виводимо текст за заданими відступами
c = pg.time.Clock() # створення годинника для FPS
music_volume = 0.5 # гучність музики дорівнює 0.5
sound_volume = 1 # гучність звуку дорівнює 1
fps = 40 # FPS дорівнює 40
pg.mixer.music.load("Game.mp3") # завантажуємо музику
pg.mixer.music.set_volume(music_volume) # задаємо гучність музики
pg.mixer.music.play(-1) # відтворюємо музику нескінченно
collide_ball = pg.mixer.Sound("Collide_platform.mp3") # завантажуємо звук відбивання м'яча
collide_ball.set_volume(sound_volume) # задаємо гучність звуку
button_play = Label("Button.png", 410, 300, 400, 50) # створюємо кнопку "Грати" класу Label
button_play.set_text("Грати", 26) # задаємо текст "Грати"
ball = Hitbox("Ball.png", 610, 300, 50, 50) # створюємо м'яч з класу Hitbox
pong = Hitbox("Pong.png", 610, 480, 200, 50) # створюємо ракетку з класу Hitbox
exit_button = Hitbox("Exit button.png", 20, 20, 50, 50) # створюємо кнопку виходу класу Hitbox
game_logo = Hitbox("Arcanoid logo.png", 380, 100, 380, 100) # створюємо лого гри
retry_button = Label("Button.png", 410, 300, 400, 50) # створюємо кнопку "Спробувати ще раз" класу Label
retry_button.set_text("Спробувати ще раз", 26) # задаємо текст "Спробувати ще раз"
mm_button = Label("Button.png", 410, 400, 400, 50) # створюємо кнопку виходу у головне меню класу Label
mm_button.set_text("Головне меню", 26) # задаємо текст "Головне меню"
rules_button = Label("Button.png", 410, 360, 400, 50) # створюємо кнопку правила з класу Label
rules_button.set_text("Як грати?", 26) # задаємо текст "Як грати?"
next_button = Hitbox("Next.png", 960, 520, 250, 50) # створюємо кнопку далі з класу Hitbox
priv_button = Hitbox("Privious.png", 10, 520, 250, 50) # створюємо кнопку назад з класу Hitbox
set_button = Label("Button.png", 410, 420, 400, 50) # створюємо кнопку налаштування з класу Label
set_button.set_text("Налаштування", 26) # задаємо текст "Налаштування"
plus_volume = Hitbox("Plus.png", 400, 200, 60, 60) # створюємо кнопку додати гучність музики з класу Hitbox
minus_volume = Hitbox("Minus.png", 200, 200, 60, 60) # створюємо кнопку 
plus_volume_s = Hitbox("Plus.png", 900, 200, 60, 60) # створюємо кнопку додати гучність звуку з класу Hitbox
minus_volume_s = Hitbox("Minus.png", 700, 200, 60, 60) # створюємо кнопку
minus_fps = Hitbox("Minus.png", 500, 450, 60, 60) # створюємо кнопку відняти FPS з класу Hitbox
plus_fps = Hitbox("Plus.png", 700, 450, 60, 60) # створюємо кнопку додати FPS з класу Hitbox
mute_music = Hitbox("Mute.png", 130, 200, 60, 60) # створюємо кнопку без музики з класу Hitbox
mute_sound = Hitbox("Mute sound.png", 630, 200, 60, 60) # створюємо кнопку без звуку з класу Hitbox
font1 = pg.font.Font("Pixel.ttf", 60) # задаємо шрифт для текстів "Ви перемогли!!!", "Game over!!!"
font2 = pg.font.Font("Pixel.ttf", 20) # задаємо шрифт для текстів для правил
font3 = pg.font.Font("Pixel.ttf", 40) # задаємо шрифт для текстів для значень
rules_t1 = font2.render("Щоб рухати платформою потрібно натискати клавіші вправо або вліво.", True, (255, 255, 255)) # задаємо текст з першим правилом
rules_t2 = font2.render("М'яч відбивається від платформи. Якщо він опуститься нижче платформи, то ви програєте.", True, (255, 255, 255)) # задаємо текст з другим правилом
rules_t3 = font2.render("Ваша місія - збити всіх прибульців і не дати м'ячу опуститися нижче платформи.", True, (255, 255, 255)) # задаємо текст з третім правилом
game_over_t = font1.render("Game over!!!", True, (255, 255, 255)) # створюємо текст "Game over"
win_t = font1.render("Ви перемогли!!!", True, (255, 255, 255)) # створюємо текст "Ви перемогли"
music_setting = font3.render("Гучність музики", True, (255, 255, 255)) # задаємо текст "Гучність музики"
sound_setting = font3.render("Гучність звуку", True, (255, 255, 255)) # задаємо текст "Гучність звуку"
fps_setting = font3.render("Налаштування FPS", True, (255, 255, 255)) # задаємо текст "Налаштування FPS"
alliens = [] # створюємо порожній список прибульців
x = 100 # x дорівнює 100
a = 0 # a дорівнює 0
move_right = False # рух праворуч не працює
move_left = False # рух ліворуч не працює
for i in range(10): # для і в діапазоні 10
    allien = Hitbox("Allien.png", x, 100, 100, 100) # створюємо прибульця з класу Hitbox
    alliens.append(allien) # до списку додаємо прибульця
    x += 100 # переміщуємо нового прибкльця на 100 правіше
y = 200 # y дорівнює 200
x = 100 # x дорівнює 100
for i in range(10): # для і в діапазоні 10
    allien = Hitbox("Allien.png", x, y, 100, 100) # створюємо прибульця з класу Hitbox
    alliens.append(allien) # до списку додаємо прибульця
    x += 100 # переміщуємо нового прибкльця на 100 правіше
game = 1 # змінна game набуває значенню True
screen = "main_menu" # тип екрану - головне меню
speed_x = 3 # швидкість по горизонталі дорівнює 3
speed_y = 3 # швидкість по вертикалі дорівнює 3
animation = [ # створюємо список анімацій для прибульців
    pg.image.load("Allien.png"),
    pg.image.load("Allien2.png"),
    pg.image.load("Allien3.png"),
    pg.image.load("Allien.png")
]
counter = 0 # лічільник анімацій дорівнює 0
wait = 0 # створюємо змінну для сповільненя циклу
points = 0 # кількість балів дорівнює 0
while game: # поки йде гра
    if screen == "main_menu": # якщо екран дорівнює головне меню
        mw.blit(bg, (0, 0)) # прикріплюємо тло
        button_play.reset() # прикріплюємо кнопку "Грати"
        button_play.draw(190, 15) # прикріплюємо текст
        game_logo.reset() # прикрріплюємо логотип гри
        rules_button.reset() # прикріплюємо кнопку з правилами
        rules_button.draw(190, 15) # прикріплюємо текст "Як грати?"
        set_button.reset() # прикріплюємо кнопку налаштування
        set_button.draw(150, 15) # прикріплюємо текст "Налаштування"
        for e in pg.event.get(): # перебираємо події для e
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1: # якщо тип події - натискання лівою кнопкою миші
                x, y = e.pos # позиції для e
                if button_play.collidepoint(x, y): # якшо відбулось зіткнення на кнопку "Грати"
                    screen = "game" # переходимо до гри
                if rules_button.collidepoint(x, y): # якщо відбулось зіткнення на кнопку з правилами
                    screen = "rules1" # переходимо до правила 1
                if set_button.collidepoint(x, y): # якщо відбулось зіткнення на кнопку налаштування
                    screen = "settings" # переходимо до налаштувань
            if e.type == pg.QUIT: # якщо тип події - закриття вікна
                pg.quit() # вихід з pygame
        c.tick(fps) # FPS
        pg.display.update() # оновлюємо екран
    if screen == "game": # якщо екран дорівнює грі
        mw.blit(bg, (0, 0)) # прикріплюємо тло
        allien.reset() # прикріплюємо прибульця
        pong.reset() # прикріплюємо ракетку
        ball.reset() # прикріплюємо м'яч
        ball.r.x += speed_x # рухаємо м'яч по горизонталі
        ball.r.y += speed_y # рухаємо м'яч по вертикалі
        exit_button.reset() # прикріплюємо кнопку виходу
        for allien in alliens: # для прибульця в кількості прибульців
            mw.blit(animation[counter], (allien.r.x, allien.r.y)) # прикріплюємо анімацію для прибульця
            if counter == 3: # якщо лічільник анімації дорівнює 0
                counter = 0 # обнулюємо лічільник
            else: # інакше
                if wait == 0: # якщо wait дорівнює 0
                    counter += 1 # до лічільника анімацій додаємо 1
                    wait = 50 # wait дорівнює 50
                else: # інакше
                    wait -= 1 # від wait віднімаємо 1
            if allien.r.colliderect(ball.r): # якщо прибулець зіштовхується з м'ячем
                alliens.remove(allien) # видаляємо прибульця з списку
                speed_y *= -1 # змінюємо швидкість м'яча по вертикалі на протилежну
                points += 1 # додаємо 1 до кількості балів
                collide_ball.play() # відтворюємо звук відбиття м'яча
        if ball.r.colliderect(pong.r): # якщо м'яч зіштовхується з ракеткою
            speed_y *= -1 # змінюємо швидкість м'яча по вертикалі на протилежну
            collide_ball.play() # відтворюємо звук відбиття м'яча
        if ball.r.y < 0: # якщо м'яч зіштовхується з верхнім краєм
            speed_y *= -1 # змінюємо швидкість м'яча по вертикалі на протилежну
            collide_ball.play() # відтворюємо звук відбиття м'яча
        if ball.r.x > 1170: # якщо м'яч зіштовхується з правим краєм
            speed_x *= -1 # змінюємо швидкість м'яча по горизонталі на протилежну
            collide_ball.play() # відтворюємо звук відбиття м'яча
        if ball.r.x < 0: # якщо м'яч зіштовхується з лівим краєм
            speed_x *= -1 # змінюємо швидкість м'яча по горизонталі на протилежну
            collide_ball.play() # відтворюємо звук відбиття м'яча
        if ball.r.y > 530: # якщо м'яч знаходиться нижче ракетки
            screen = "game_over" # переходимо до екрану програшу
        if points == 20: # якщо всіх прибульців збито
            screen = "win" # переходимо до екрану виграшу
        for e in pg.event.get(): # перебираємо події для e
            if e.type == pg.KEYDOWN: # якшо тип події - натискання на клавішу
                if e.key == pg.K_LEFT: # якщо кнопку вліво натиснуто
                    move_left = True # рух ліворуч працює
                if e.key == pg.K_RIGHT: # якщо кнопку право натиснуто
                    move_right = True # рух праворуч працює
            if e.type == pg.KEYUP: # якщо тип події - опускання клавіші
                if e.key == pg.K_LEFT: # якщо клавішу вліво опущено
                    move_left = False # рух ліворуч не працює
                if e.key == pg.K_RIGHT: # якщо клавішу право опущено
                    move_right = False # рух праворуч не працює
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1: # якщо тип події - натискання лівої кнопки миші
                x, y = e.pos # позиції для e
                if exit_button.collidepoint(x, y): # якщо відбулось зіткнення на кнопку виходу
                    screen = "main_menu" # переходимо до головнго меню
                    ball.r.x = 610 # повертаємо початковий х м'яча 
                    ball.r.y = 300 # повертаємо початковий y м'яча 
                    pong.r.x = 610 # повертаємо початковий х ракетки
                    x = 100 # координата x прибульця дорівнює 100
                    points = 0 # обнулюємо кількість балів
                    speed_x = 3 # швидкість по горинзонталі дорівнює 3
                    speed_y = 3 # швидкість по вертикалі дорівнює 3
                    alliens.clear() # очищуємо список прибульців
                    for i in range(10): # для і в діапазоні 10
                        allien = Hitbox("Allien.png", x, 100, 100, 100) # створюємо прибульця з класу Hitbox
                        alliens.append(allien) # до списку додаємо прибульця
                        x += 100 # переміщуємо нового прибкльця на 100 правіше
                    x = 100 # x дорівнює 100
                    y = 200 # y дорівнює 200
                    for i in range(10): # для і в діапазоні 10
                        allien = Hitbox("Allien.png", x, y, 100, 100) # створюємо прибульця з класу Hitbox
                        alliens.append(allien) # до списку додаємо прибульця
                        x += 100 # переміщуємо нового прибкльця на 100 правіше
            if e.type == pg.QUIT: # якщо тип події - закриття вікна
                pg.quit() # вихід з pygame
        if move_left == True: # якщо рух ліворуч працює
            if not pong.r.x < 20: # якщо ракетка знаходиться далі від лівого краю
                pong.r.x -= 10 # переміщуємо ракетку вліво
        if move_right == True: # якщо рух праворуч працює
            if not pong.r.x > 1000: # якщо ракетка знаходиться далі від првого краю
                pong.r.x += 10 # переміщуємо ракетку вправо
        c.tick(fps) # FPS
        pg.display.update() # оновлюємо екран
    if screen == "game_over": # якщо тип екрану - екран програшу
        mw.blit(bg, (0, 0)) # прикріплюємо тло
        retry_button.reset() # прикрплюємо кнопку "Спробувати ще раз"
        retry_button.draw(80, 15) # прикрплюємо текст "Спрбувати ще раз"
        mm_button.reset() # прикріплюємо кнопку "Головне меню"
        mm_button.draw(150, 15) # прикраплюємо текст "Головне меню"
        mw.blit(game_over_t, (380, 100)) # прикріплюємо текст "Game over!!!"
        for e in pg.event.get(): # перебираємо події для e
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1: # якщо тип події - натискання лівої кнопки миші
                x, y = e.pos # позиції для e
                if retry_button.collidepoint(x, y): # якщо відбулось зіткнення на кнопку "Спробувати ще раз"
                    screen = "game" # тип екрану - гра
                    ball.r.x = 610 # повертаємо початковий х м'яча
                    ball.r.y = 300 # повертаємо початковий y м'яча
                    pong.r.x = 610 # повертаємо початковий х ракетки
                    x = 100 # координата x прибульця дорівнює 100
                    points = 0 # обнулюємо кількість балів
                    speed_x = 3 # швидкість по горинзонталі дорівнює 3
                    speed_y = 3 # швидкість по вертикалі дорівнює 3
                    alliens.clear() # очищуємо список прибульців
                    for i in range(10): # для і в діапазоні 10
                        allien = Hitbox("Allien.png", x, 100, 100, 100) # створюємо прибульця з класу Hitbox
                        alliens.append(allien) # до списку додаємо прибульця
                        x += 100 # переміщуємо нового прибкльця на 100 правіше
                    x = 100 # x дорівнює 100
                    y = 200 # y дорівнює 200
                    for i in range(10): # для і в діапазоні 10
                        allien = Hitbox("Allien.png", x, y, 100, 100) # створюємо прибульця з класу Hitbox
                        alliens.append(allien) # до списку додаємо прибульця
                        x += 100 # переміщуємо нового прибкльця на 100 правіше
                if mm_button.collidepoint(x, y): # якщо відбулось зіткнення на кнопку "Головне меню"
                    screen = "main_menu" # тип екрану - головне меню
                    ball.r.x = 610 # повертаємо початковий х м'яча
                    ball.r.y = 300 # повертаємо початковий y м'яча
                    pong.r.x = 610 # повертаємо початковий х ракетки
                    x = 100 # координата x прибульця дорівнює 100
                    points = 0 # обнулюємо кількість балів
                    speed_x = 3 # швидкість по горинзонталі дорівнює 3
                    speed_y = 3 # швидкість по вертикалі дорівнює 3
                    alliens.clear() # очищуємо список прибульців
                    for i in range(10): # для і в діапазоні 10
                        allien = Hitbox("Allien.png", x, 100, 100, 100) # створюємо прибульця з класу Hitbox
                        alliens.append(allien) # до списку додаємо прибульця
                        x += 100 # переміщуємо нового прибкльця на 100 правіше
                    x = 100 # x дорівнює 100
                    y = 200 # y дорівнює 200
                    for i in range(10): # для і в діапазоні 10
                        allien = Hitbox("Allien.png", x, y, 100, 100) # створюємо прибульця з класу Hitbox
                        alliens.append(allien) # до списку додаємо прибульця
                        x += 100 # переміщуємо нового прибкльця на 100 правіше
            if e.type == pg.QUIT: # якщо тип події - закриття вікна
                pg.quit() # вихід з pygame
        c.tick(fps) # FPS
        pg.display.update() # оновлюємо екран
    if screen == "win": # якщо тип екрану - екран виграшу
        mw.blit(bg, (0, 0)) # прикріплюємо тло
        mw.blit(win_t, (380, 100)) # прикрвплюємо текст "Ви перемогли"
        mm_button.reset() # прикрплюємо кнопку головного меню
        mm_button.draw(150, 15) # прикріплюємо текст "Головне меню"
        for e in pg.event.get(): # перебираємо події для e
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1: # якщо тип події - натискання лівої кнопки миші
                x, y = e.pos # позиції для e
                if mm_button.collidepoint(x, y): # якщо відбулось зіткнення кнопки головного меню
                    screen = "main_menu" # тип екрану - головне меню
                    ball.r.x = 610 # повертаємо початковий х м'яча
                    ball.r.y = 300 # повертаємо початковий y м'яча
                    pong.r.x = 610 # повертаємо початковий х ракетки
                    x = 100 # координата x прибульця дорівнює 100
                    points = 0 # обнулюємо кількість балів
                    speed_x = 3 # швидкість по горинзонталі дорівнює 3
                    speed_y = 3 # швидкість по вертикалі дорівнює 3
                    alliens.clear() # очищуємо список прибульців
                    for i in range(10): # для і в діапазоні 10
                        allien = Hitbox("Allien.png", x, 100, 100, 100) # створюємо прибульця з класу Hitbox
                        alliens.append(allien) # до списку додаємо прибульця
                        x += 100 # переміщуємо нового прибкльця на 100 правіше
                    x = 100 # x дорівнює 100
                    y = 200 # y дорівнює 200
                    for i in range(10): # для і в діапазоні 10
                        allien = Hitbox("Allien.png", x, y, 100, 100) # створюємо прибульця з класу Hitbox
                        alliens.append(allien) # до списку додаємо прибульця
                        x += 100 # переміщуємо нового прибкльця на 100 правіше
            if e.type == pg.QUIT: # якщо тип події - закриття вікна
                pg.quit() # вихід з pygame
        c.tick(fps) # FPS
        pg.display.update() # оновлюємо екран
    if screen == "rules1": # якщо тип екрану - правило 1
        mw.blit(bg, (0, 0)) # прикрплюємо тло
        exit_button.reset() # прикріплюємо кнопку виходу
        next_button.reset() # прикріплюємо кнопку далі
        mw.blit(rules_t1, (250, 450)) # прикріплюємо правило 1
        mw.blit(rules_p1, (300, 100)) # прикріплюємо фото для правила 1
        for e in pg.event.get(): # перебираємо події для e
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1: # якщо тип події - натискання лівої кнопки миші
                x, y = e.pos # позиції для e
                if exit_button.collidepoint(x, y): # якщо відбулось зіткнення на кнопку виходу
                    screen = "main_menu" # переходимо до головнго меню
                if next_button.collidepoint(x, y): # якщо відбулось зіткнення на кнопку далі 
                    screen = "rules2" # переходимо до правила 2
            if e.type == pg.QUIT: # якщо тип події - закриття вікна
                pg.quit() # вихід з pygame
        c.tick(fps) # FPS
        pg.display.update() # оновлюємо екран
    if screen == "rules2": # якщо тип екрану - правило 2
        mw.blit(bg, (0, 0)) # прикріплюємо тло
        exit_button.reset() # прикріплюємо кнопку виходу
        next_button.reset() # прикріплюємо кнопку далі
        priv_button.reset() # прикріплюємо кнопку назад
        mw.blit(rules_t2, (120, 450)) # прикріплюємо правило 2
        mw.blit(rules_p2, (300, 100)) # прикріплюємо фото для правила 2
        for e in pg.event.get(): # перебираємо події для e
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1: # якщо тип події - натискання лівої кнопки миші
                x, y = e.pos # позиції для e
                if exit_button.collidepoint(x, y): # якщо відбулось зіткнення на кнопку виходу
                    screen = "main_menu" # переходимо до головнго меню
                if priv_button.collidepoint(x, y): # якщо відбулось зіткнення на кнопку назад
                    screen = "rules1" # переходимо до попереднього правила
                if next_button.collidepoint(x, y): # якщо відбулось зіткнення на кнопку далі
                    screen = "rules3" # переходимо до правила 3
                    button_play.r.x = 810 # x кнопки "Грати" дорівнює 810
                    button_play.r.y = 520 # y кнопки "Грати" дорівнює 520
            if e.type == pg.QUIT: # якщо тип події - закриття вікна
                pg.quit() # вихід з pygame
        c.tick(fps) # FPS
        pg.display.update() # оновлюємо екран
    if screen == "rules3": # якщо тип екрану - правило 3
        mw.blit(bg, (0, 0)) # прикріплюємо тло
        exit_button.reset() # прикріплюємо виходу
        priv_button.reset() # прикріплюємо кнопку назад
        button_play.reset() # прикріплюємо кнопку "Грати"
        button_play.draw(190, 15) # прикріплюємо текст "Грати"
        mw.blit(rules_t3, (250, 450)) # прикріплюємо правило 3
        mw.blit(rules_p3, (300, 100)) # прикріплюємо фото для правило 3
        for e in pg.event.get(): # перебираємо події для e
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1: # якщо тип події - натискання лівої кнопки миші
                x, y = e.pos # позиції для e
                if exit_button.collidepoint(x, y): # якщо відбулось зіткнення на кнопку виходу
                    screen = "main_menu" # переходимо до головнго меню
                    button_play.r.x = 410 # x кнопки "Грати" дорівнює 410 
                    button_play.r.y = 300 # y кнопки "Грати" дорівнює 300
                if priv_button.collidepoint(x, y): # якщо відбулось зіткнення на кнопку назад
                    screen = "rules2" # переходимо до попереднього правила
                if button_play.collidepoint(x, y): # якщо відбулося зіткнення на кнопку "Грати"
                    screen = "game" # переходимо до гри
                    button_play.r.x = 410 # x кнопки "Грати" дорівнює 410
                    button_play.r.y = 300 # y кнопки "Грати" дорівнює 300
            if e.type == pg.QUIT: # якщо тип події - закриття вікна
                pg.quit() # вихід з pygame
        c.tick(fps) # FPS
        pg.display.update() # оновлюємо екран
    if screen == "settings": # якщо тип екрану - налаштування
        mw.blit(bg, (0, 0)) # прикріплюємо тло
        m_volume = font3.render(str(music_volume), True, (255, 255, 255)) # задаємо значення гучності музики
        s_volume = font3.render(str(sound_volume), True, (255, 255, 255)) # задаємо значення гучності звуку
        fps_s = font3.render(str(fps), True, (255, 255, 255)) # задаємо значення FPS
        exit_button.reset() # прикріплюємо кнопку виходу
        plus_volume.reset() # прикріплюємо кнопку додати гучність музики
        minus_volume.reset() # прикріплюємо кнопку відняти гучність музики
        plus_volume_s.reset() # прикріплюємо кнопку додати гучність звуку
        minus_volume_s.reset() # прикріплюємо кнопку відняти гучність звуку
        plus_fps.reset() # прикріплюємо кнопку додати FPS
        minus_fps.reset() # прикріплюємо кнопку відняти FPS
        mute_music.reset() # прикріплюємо кнопку без музики
        mute_sound.reset() # прикріплюємо кнопку без звуку
        mw.blit(music_setting, (130, 100)) # прикріплюємо текст "Гучність музики"
        mw.blit(sound_setting, (630, 100)) # прикріплюємо текст "Гучність звуку"
        mw.blit(m_volume, (270, 200)) # прикріплюємо значення гучності музики
        mw.blit(s_volume, (770, 200)) # прикріплюємо значення гучності звуку
        mw.blit(fps_setting, (500, 350)) # прикріплюємо текст "Налаштування FPS"
        mw.blit(fps_s, (570, 450)) # прикріплюємо значення FPS
        for e in pg.event.get(): # перебираємо події для e
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1: # якщо тип події - натискання лівої кнопки миші
                x, y = e.pos # позиції для e
                if exit_button.collidepoint(x, y): # якщо відбулось зіткнення на кнопку виходу
                    screen = "main_menu" # переходимо до головнго меню
                if plus_volume.collidepoint(x, y): # якщо відбулось зіткнення з кнопкою додати гучність музики
                    if music_volume < 1: # якщо гучність музики менше 1
                        music_volume += 0.1 # до гучності музики додаємо 0.1
                        pg.mixer.music.set_volume(music_volume) # задаємо гучність музики
                if minus_volume.collidepoint(x, y): # якщо відбулось зіткнення з кнопкою відняти гучність музики
                    if music_volume > 0: # якщо гучність музики більше 0
                        music_volume -= 0.1 # від гучності музики віднімаємо 0.1
                        pg.mixer.music.set_volume(music_volume) # задаємо гучність музики
                if plus_volume_s.collidepoint(x, y): # якщо відбулось зіткнення з кнопкою додати гучність звуку
                    if sound_volume < 1: # якщо гучність звуку менше 1
                        sound_volume += 0.1 # до гучності звуку додаємо 0.1
                        collide_ball.set_volume(sound_volume) # задаємо гучність звуку
                if minus_volume_s.collidepoint(x, y): # якщо відбулось зіткнення з кнопкою відняти гучність звуку
                    if sound_volume > 0: # якщо гучність звуку більше 0
                        sound_volume -= 0.1 # від гучності звуку віднімаємо 0.1
                        collide_ball.set_volume(sound_volume) # задаємо гучність звуку
                if plus_fps.collidepoint(x, y): # якщо відбулось зіткнення з кнопкою додати FPS
                    if fps < 60: # якщо FPS менше 60
                        fps += 10 # до FPS додаємо 10
                if minus_fps.collidepoint(x, y): # якщо відбулось зіткнення з кнопкою відняти FPS
                    if fps > 40: # якщо FPS більше 40
                        fps -= 10 # до FPS віднімаємо 10
                if mute_music.collidepoint(x, y): # якщо відбулось зіткнення з кнопкою без музики
                    music_volume = 0 # гучність музики дорівнює 0
                    pg.mixer.music.set_volume(music_volume) # задаємо гучність музики
                if mute_sound.collidepoint(x, y): # якщо відбулось зіткнення з кнопкою без звуку
                    sound_volume = 0 # гучність звуку дорівнює 0
                    collide_ball.set_volume(sound_volume) # задаємо гучність звуку
            if e.type == pg.QUIT: # якщо тип події - закриття вікна
                pg.quit() # вихід з pygame
        c.tick(fps) # FPS
        pg.display.update() # оновлюємо екран