"""
Author: Connor McGoey
Version: 1.0.0
Date: July 15, 2023
File: debian_stats.py
"""

# import libraries for URL handling, unzipping .gz files, heap, and system/os libraries.
import urllib.request
import urllib.error
import gzip
import heapq
import os
import sys

# global variable for debian mirror URL.
pattern = "http://ftp.uk.debian.org/debian/dists/stable/main/Contents-{}.gz"

# helper function to print a sorted list of elements. Used to print top 10 elements from heap.
def printList(sortedList: list):
    i = 1
    while sortedList:
        count, package = sortedList.pop()
        line = f"{i}. {package}   {count}"
        print(line)
        i += 1

# function to handle the URL request and parsing of .gz file.
def debianStats(architecture: str):
    # Construct the URL and filename based on the provided architecture and global URL pattern string.
    url = pattern.format(architecture)
    filename = f"Contents-{architecture}.gz"

    try:
        # Attempt to retrieve the file from the URL.
        urllib.request.urlretrieve(url, filename)
    except urllib.error.URLError as e:
        # Handle URL-related errors.
        print(f"An error occurred while retrieving the file: {e}")
        print("Please ensure the architecture is valid and maps to the proper debian mirror "
              "'/Contents-__.gz' file"
              "located at: \nhttp://ftp.uk.debian.org/debian/dists/stable/main")
        sys.exit(1)
    except OSError as e:
        # Handle OS-related errors.
        print(f"An OS error occurred: {e}")
        sys.exit(1)

    # Initialize dictionary to store the number of files in each package.
    packages = {}
    with gzip.open(filename, 'rt', encoding="utf8") as file:
        # Read and process the lines of the gzip file.
        for line in file:
            # Extract the package name from the line.
            package = line.split()[-1]
            # Increment the package's file count by one.
            packages[package] = packages.get(package, 0) + 1

    # Initialize a heap to store the 10 packages with the most files.
    heap = []
    for package, numFiles in packages.items():
        item = tuple([numFiles, package])
        # Add the item to the heap if the heap size is less than 10.
        if len(heap) < 10:
            heapq.heappush(heap, item)
        elif item[0] > heap[0][0]:
            # Add the item to the heap and remove the smallest item.
            heapq.heappushpop(heap, item)

    # Sort the resulting heap of 10 elements in increasing order.
    heap.sort(key=lambda x: x[0])
    printList(heap)

    # Remove the saved .gz file from directory.
    os.remove(filename)
