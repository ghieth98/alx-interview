#!/usr/bin/python3
"""Module for parsing logs."""

import re
import sys
from collections import Counter
from typing import Tuple, Optional


def parse_log(log: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Parse a log entry, extracting the status code and file size.
    """
    parts = (
        r"(?P<ip>\S+)\d+\.\d+\.\d+\.\d+\s+",
        r"- \[",
        r"(?P<date>[^\]]+)",
        r'\] "(?P<method>GET) (?P<res>/projects/260) (?P<proto>HTTP/1\.1)" ',
        r"(?P<status_code>\d+)",
        r" ",
        r"(?P<file_size>\d+)",
    )

    log_fmt = "{}{}{}{}{}{}{}\\s*".format(parts[0], parts[1], parts[2],
                                          parts[3], parts[4], parts[5],
                                          parts[6])

    match = re.fullmatch(log_fmt, log.strip())
    if match:
        status = match.group("status_code")
        size = match.group("file_size")
        if status.isdigit() and status in {
            "200", "301", "400", "401", "403", "404", "405", "500"
        }:
            return status, size
    return None, None


def process_logs() -> None:
    """
    Process logs from standard input.
    """
    status_counter, size_counter = Counter(), Counter()
    try:
        for idx, log in enumerate(sys.stdin, start=1):
            status, size = parse_log(log)
            if status and size:
                status_counter[status] += 1
                size_counter["size"] += int(size)
            if idx % 10 == 0:
                print_stats(status_counter, size_counter)
    except (KeyboardInterrupt, EOFError):
        print_stats(status_counter, size_counter)
        sys.exit(0)


def print_stats(status_counter: Counter, size_counter: Counter) -> None:
    """
    Print statistics about the processed logs.
    Prints the total file size and the count of each status code
    """
    print(f"\nFile size: {size_counter['size']}")
    for status in sorted(status_counter):
        print(f"{status}: {status_counter[status]}")


if __name__ == "__main__":
    process_logs()
