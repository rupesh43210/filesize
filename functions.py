import os
from datetime import datetime
from termcolor import colored
import random
import time

def format_size(size):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0

def get_folder_size(folder, depth, min_size, current_depth=0):
    total_size = 0
    for entry in os.scandir(folder):
        if entry.is_file():
            entry_size = entry.stat().st_size
            if entry_size >= min_size:
                total_size += entry_size
        elif entry.is_dir() and current_depth < depth:
            total_size += get_folder_size(entry.path, depth, min_size, current_depth + 1)

    return total_size

def scan_directory(path, depth, min_size, current_depth=0):
    items = []
    for entry in os.scandir(path):
        if entry.is_file():
            size = entry.stat().st_size
            if size >= min_size:
                items.append((entry.path, size, "File"))
        elif entry.is_dir():
            folder_size = get_folder_size(entry.path, depth, min_size, current_depth + 1)
            if folder_size >= min_size:
                items.append((entry.path, folder_size, "Folder"))
            if current_depth < depth:
                items.extend(scan_directory(entry.path, depth, min_size, current_depth + 1))

    return items

def create_banner():
    banner = f"{'*' * 50}\n"
    banner += f"* Scan started at {datetime.now()} *\n"
    banner += f"{'*' * 50}\n"
    return banner

def display_animated_banner():
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    text = "Credits - Rupesh"

    # Get terminal width
    _, term_width = os.popen("stty size", "r").read().split()
    term_width = int(term_width)

    # Calculate the padding needed to center the text
    padding = " " * ((term_width - len(text)) // 2)

    for _ in range(40):  # Increase the number of iterations for a longer duration
        color = random.choice(colors)
        print(colored(padding + text + padding, color, attrs=["bold"]))
        time.sleep(0.1)
        print("\033[F" + "\033[K", end="")  # Move cursor up and clear line

