import time
from logging import Logger, getLogger
from curses import wrapper, noecho, initscr, cbreak, napms, KEY_UP, KEY_DOWN

log: Logger = getLogger(__name__)

def main(stdscr):
    log.info("Welcome to Driving CLI")
    log.info("CLI simulates vehicle driving")




def real_time_loop(dt: float, max_steps: int = None):
    """
    Loop in real time, step every dt seconds. Compensates execution time of update() by sleep.
    :param dt: Seconds to wait.
    :param max_steps: Maximum steps number.
    :return:
    """
    step = 0
    t0 = time.perf_counter()
    next_time = t0

    noecho()
    cbreak()
    last_time = time.perf_counter()

    stdscr.addstr(0, 0, "Sterowanie: ↑ przyspiesz, ' ' hamuj, ←/→ skręt, ESC wyjście")

    while True:
        now = time.perf_counter()
        elapsed = now - last_time

        if elapsed < dt:
            time.sleep(dt - elapsed)
            continue
        last_time = now

        key = stdscr.getch()
        if key == KEY_UP:
            stdscr.addstr(2, 0, "Up arrow pressed")
            # speed up
        elif key == ord(' '):
            stdscr.addstr(2, 0, "Space pressed")
            # speed down
        elif key == 27:
            stdscr.addstr(2, 0, "ESC key pressed")
            log.info("Stopping the CLI")
            stdscr.refresh()
            napms(500)
            break

        stdscr.clear()
        stdscr.addstr(0, 0, "Predkosc: ")
        stdscr.addstr(2, 0, "Kierunek: ")
        stdscr.addstr(3, 0, "Czas symulacji: ")


if __name__ == "__main__":
    stdscr = initscr()
    wrapper(main(stdscr))