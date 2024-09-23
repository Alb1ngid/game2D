import pgzrun

TITLE = "2DGAME"

WIDTH = 600
HEIGHT = 400


current_screen = "menu"


menu_options = ["Start game", "MaS", "Quit"]
selected_option = 0

music_on = True
sound_on = True


music.play('background_music')
music.set_volume(0.5)
DEFAULT_FONT="fonts/kenney_blocks"


def draw():
    screen.fill((128, 0, 0))
    if current_screen == "menu":
        draw_menu()
    elif current_screen == "game":
        screen.draw.text("Game Screen", center=(WIDTH // 2, HEIGHT // 2), fontsize=50)


def draw_menu():
    screen.draw.text("Main Menu", center=(WIDTH // 2, 100), fontsize=50,fontname=DEFAULT_FONT)
    for i, option in enumerate(menu_options):
        color = "yellow" if i == selected_option else "white"
        screen.draw.text(option, center=(WIDTH // 2, 200 + i * 50), fontsize=40, color=color,fontname=DEFAULT_FONT)

    screen.draw.text(f"Music and Saunds: {'On' if music_on and sound_on else 'Off'}", topleft=(10, 10),
                     fontsize=15, color="white", fontname=DEFAULT_FONT)


def on_key_down(key):
    global current_screen, selected_option, music_on, sound_on

    if current_screen == "menu":
        if key == keys.UP:
            selected_option = (selected_option - 1) % len(menu_options)
        elif key == keys.DOWN:

            selected_option = (selected_option + 1) % len(menu_options)
        elif key == keys.RETURN:  # Нажатие Enter
            if menu_options[selected_option] == "Start game":
                current_screen = "game"
            elif menu_options[selected_option] == "MaS":
                toggle_music()
            elif menu_options[selected_option] == "Quit":
                exit()


def toggle_music():
    global music_on,sound_on
    music_on = not music_on
    sound_on = not sound_on
    if music_on:
        music.play('background_music')

    else:
        music.stop()

pgzrun.go()