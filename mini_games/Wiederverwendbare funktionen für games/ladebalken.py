import time


def ladebalken():
    for i in range(1, 51):
        percent = i * 2
        orange = "\033[93m"
        green = "\033[92m"
        reset = "\033[0m"
        print(f"\r{percent:3}% [{orange}{'#' * i}{reset}{'-' * (50 - i)}]", end="", flush=True)
        time.sleep(0.5)
    print(f"\r{percent:3}% [{green}{'#' * i}{reset}{'-' * (50 - i)}]", end="", flush=True)

ladebalken()


def loading():
    orange = "\033[93m"
    green = "\033[92m"
    reset = "\033[0m"

    for count in range(1, 10):
        points = "." * ((count - 1) % 3 + 1)
        print(f"\r\033[K{orange}Loading{points}{reset}", end="", flush=True)
        time.sleep(0.5)

    print(f"\r\033[K{green}Loading... fertig{reset}")


loading()