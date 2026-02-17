from pathlib import Path
from colorama import Fore


def print_dir(path_str: str):
    path = Path(path_str)
    if not path.exists():
        print(f"Path {path_str} does not exist.")
        return
    print_dir_struct(path)


def print_dir_struct(base_path, level=0):
    if base_path.is_dir():
        print_dir_name(base_path.name, level)
        for path in base_path.iterdir():
            print_dir_struct(path, level + 1)
    else:
        print_dir_name(base_path.name, level, is_dir=False)


def print_dir_name(name, level, is_dir=True):
    color = Fore.BLUE if is_dir else Fore.GREEN
    suffix = "/" if is_dir else ""
    tab_size = 3
    print(f"{' ' * tab_size * level}{color}{name}{suffix}{Fore.RESET}")
