import curses
import time
import random
import pyfiglet

name = "Jᴀɪ ❖Sʜʀᴇᴇ🦚❖𝐊ʀɪ𝐬ʜɴᴀ༆ "
glitch_chars = ['$', '#', '@', '%', '&', '*', '!', '?', '/', '•', '.', '×', '+']
background_chars = ['.', '•', '·', '°', ' ']

def draw_background(stdscr, max_y, max_x):
    for y in range(max_y):
        for x in range(max_x):
            # Random chance to show a glitch dot
            char = random.choice(background_chars)
            try:
                stdscr.addstr(y, x, char, curses.color_pair(4))
            except curses.error:
                pass

def draw_banner(stdscr, max_y, max_x):
    banner_text = pyfiglet.figlet_format("ABHI", font= "slant")
    banner_lines = banner_text.split('\n')
    start_y = max_y // 8 - len(banner_lines) // 5
    for i, line in enumerate(banner_lines):
        x_pos = max_x // 2 - len(line) // 2
        if 0 <= start_y + i < max_y:
            try:
                stdscr.addstr(start_y + i, x_pos, line[:max_x], curses.color_pair(4) | curses.A_BOLD)
            except curses.error:
                pass

def draw_scrolling_text(stdscr, max_y, max_x, position):
    line = ""
    for j in range(len(name)):
        char = name[(position + j) % len(name)]
        if random.random() < 0.05:
            char = random.choice(glitch_chars)
        line += char
    try:
        stdscr.addstr(max_y - 30, (max_x - len(line)) // 2, line[:max_x], curses.color_pair(random.choice([1, 2, 3])) | curses.A_BOLD)
    except curses.error:
        pass

def hacker_krishna_fullscreen(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_GREEN, -1)    # Scrolling
    curses.init_pair(2, curses.COLOR_CYAN, -1)     # Banner
    curses.init_pair(3, curses.COLOR_WHITE, -1)    # Alt text
    curses.init_pair(4, curses.COLOR_RED, -1)      # Background

    position = 0

    while True:
        max_y, max_x = stdscr.getmaxyx()
        stdscr.clear()

        draw_background(stdscr, max_y, max_x)
        draw_banner(stdscr, max_y, max_x)
        draw_scrolling_text(stdscr, max_y, max_x, position)

        stdscr.refresh()
        position = (position + 1) % len(name)
        time.sleep(0.1)

def main():
    curses.wrapper(hacker_krishna_fullscreen)

if __name__ == "__main__":
    main()