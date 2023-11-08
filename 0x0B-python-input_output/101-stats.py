#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys

if __name__ == "__main__":
    file_sizes = []
    status_codes = []
    default_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    lines = []
    counter = 1
    try:
        for line in sys.stdin:
            lines.append(line)
        for line in lines:
            inputs = line.split()
            file_size = inputs[-1]
            status_code = inputs[-2]
            file_sizes.append(int(file_size))
            status_codes.append(int(status_code))

            if ((counter % 10) == 0 or len(lines) < 9):
                print("File size: {:d}".format(sum(file_sizes)))
                for code in sorted(default_status_codes):
                    code_total = sum([1 for i in status_codes if i == code])
                    if (code_total > 0):
                        print("{}: {:d}".format(str(code), code_total))

            counter += 1
    except KeyboardInterrupt:
        print("File size: {:d}".format(sum(file_sizes)))
        for code in sorted(default_status_codes):
            code_total = sum([1 for i in status_codes if i == code])
            if (code_total > 0):
                print("{}: {:d}".format(str(code), code_total))
