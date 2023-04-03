# File Size Scanner

This `README.md` provides an introduction to the project, prerequisites, usage instructions, and options for running the script.

File Size Scanner is a Python script that scans the specified directory for files and folders, and reports their sizes. It allows the user to set the depth of the scan, minimum file size to include in the scan, and the name of the output file. The script will output the result to the specified file as well as display it in the terminal.

## Prerequisites

Before running the script, you need to have Python 3 installed on your system. In addition, the following Python libraries are required:

- `tabulate`
- `termcolor`

You can install these libraries using `pip`:

```bash
pip install tabulate termcolor

Usage
To run the script, execute the following command in your terminal or command prompt:

python file_size.py [options]


Options
-d, --depth: Depth of the scan (default: prompt user)
-ss, --size: Minimum file/folder size to include in the scan, e.g. 1KB, 2MB, 3GB, 4TB (default: prompt user)
-o, --output: Name of the output file (default: prompt user)


Example

python file_size.py -d 1 -ss 1MB -o output.txt

This command will scan the current directory with a depth of 1, skipping files and folders smaller than 1MB, and output the result to output.txt.

Issues and Support
In case of any issues, please contact Rupesh.




