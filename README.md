# PrimePlus

PrimePlus is a simple Python program that displays real-time resource usage statistics for CPU, memory, and disk on Windows systems. It continuously updates these metrics to provide a live view of the system's current performance.

## Features

- **CPU Usage**: Displays the current CPU usage percentage.
- **Memory Usage**: Shows the percentage of memory used, along with the actual used and total memory in gigabytes.
- **Disk Usage**: Provides the percentage of disk space used, along with the actual used and total disk space in gigabytes.

## Requirements

- Python 3.x
- `psutil` library

## Installation

First, ensure that you have Python installed on your system. You can download it from the [official website](https://www.python.org/).

Next, install the `psutil` library using pip:

```bash
pip install psutil
```

## Usage

To run the PrimePlus program, simply execute the `primeplus.py` script:

```bash
python primeplus.py
```

The program will display the current resource usage and update the information every second.

## Notes

- This program is designed for Windows systems. If you are using a different operating system, you may need to adjust the code for console clearing.
- Ensure that your terminal or console window is large enough to display all the information clearly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.