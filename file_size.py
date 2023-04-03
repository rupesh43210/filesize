import os
import sys
import argparse
from tabulate import tabulate
from functions import format_size, get_folder_size, scan_directory, create_banner, display_animated_banner
from datetime import datetime

def main():
    display_animated_banner()

    parser = argparse.ArgumentParser(description="Scan files and folders for their sizes.")
    parser.add_argument("-d", "--depth", type=int, help="Depth of the scan")
    parser.add_argument("-ss", "--size", type=str, help="Minimum file/folder size to include in the scan (e.g. 1KB, 2MB, 3GB, 4TB)")
    parser.add_argument("-o", "--output", type=str, help="Name of the output file")

    args = parser.parse_args()

    if args.depth:
        depth = args.depth
    else:
        depth = int(input("Enter the depth of the scan: "))

    if args.size:
        size_input = args.size
    else:
        size_input = input("Enter the minimum file/folder size to include in the scan (e.g. 1KB, 2MB, 3GB, 4TB): ")

    size_unit = size_input[-2:].strip().upper()
    size_value = float(size_input[:-2].strip())

    units = {"B": 1, "KB": 1024, "MB": 1048576, "GB": 1073741824, "TB": 1099511627776}
    min_size = size_value * units[size_unit]

    if args.output:
        output_file = args.output
    else:
        output_file = input("Enter the name of the output file: ")

    with open(output_file, "a") as f:
        banner = create_banner()
        print(banner)
        f.write(banner)

        scan_info = f"Scan depth: {depth}\nItems skipped below size: {size_input}\nScan start directory: {os.getcwd()}\n\n"
        print(scan_info)
        f.write(scan_info)

        items = scan_directory(os.getcwd(), depth, min_size)
        formatted_items = [(item[0], format_size(item[1]), item[2]) for item in items]
        table = tabulate(formatted_items, headers=["Path", "Size", "Type"], tablefmt="grid")
        print(table)
        f.write(table)

        scan_end_info = f"\n\n--- Scan finished at {datetime.now()} ---\nIn case of any issues, contact Rupesh.\n\n"
        print(scan_end_info)
        f.write(scan_end_info)

if __name__ == "__main__":
    main()
