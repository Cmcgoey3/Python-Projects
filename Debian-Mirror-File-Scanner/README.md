Author
Connor McGoey

Overview
In this project, I wrote code to take in command lane parameters and fetch information regarding files for a debian mirror given a specific architecture.

Usage
To run the tool, use the following command in the terminal:
  python package_stats.py arm64

File Structure
package_stats.py: This is the main file that drives the command-line tool. It imports the typer library and initializes the typer application. It calls the handler function debianStats located in the debian_stats.py file.

debian_stats.py: This file contains the main driving function debianStats, which takes a parameter representing the architecture file to be parsed in the Debian mirror. The function utilizes the urllib and gzip libraries to fetch and decompress the .gz zip file from the mirror. It processes the information to determine the number of files each package contains and identifies the top 10 packages with the most files.

Implementation Details
The debianStats function uses a try/except block to handle errors during the URL call.
It creates a hashmap (Python dictionary) to store the count of files for each package by analyzing each line of the file.
A heapq heap of size 10 is maintained to store the 10 packages with the most files.
The function sorts the heap and passes the sorted list to the printList helper function to display the top 10 packages.
The entire process runs in O(nlogn) time complexity for heap operations and O(n) space complexity for the hashmap.
The heap's space complexity is O(1) since it contains at most 10 elements.
The top 10 package list is printed with O(1) time complexity as there are only 10 elements at most.

Notes on Running
To execute the tool, ensure that the typer library is installed within the same library as the Python files. Run the following command using the appropriate architecture parameter:
  python package_stats.py arm64
Please replace arm64 with the desired architecture parameter.

Feel free to reach out if you have any questions or feedback!
