Connected Components Detection Algorithm

final_set()

Algorithm:
The final_set() algorithm aims to identify the final sets of a disjoint set data structure. It follows these steps:

1. Initialize a hash set called 'representatives' to store the representatives.
2. Traverse all nodes and apply the find_set() operation, adding the representative to the 'representatives' hash set. If the representative already exists, no action is taken.
3. Set the class variable 'finalSets' to True.
4. Clear all nodes in the hash set.
5. Repopulate the hash set with 'n' (size of the original class hashmap's nodes) single-value disjoint sets, where each node has a value from 1 to 'n'.
6. Return an array containing the length of the 'representatives' set and the size of the hashmap.

Correctness:
The algorithm is correct as it produces the accurate output and terminates correctly. The function terminates after two passes over the size of the original hashmap 'n': one to find the representatives and another to repopulate the hashmap with values from 1 to 'n'. If the hashmap is initially empty, both loops are skipped, resulting in constant time complexity. The algorithm also generates correct output; using a hash set to store representatives ensures there are no duplicates. Additionally, the algorithm's use of path compression in the find_set() method improves performance by shortening paths. The 'size' class variable corresponds to the size of the class hashmap, ensuring the creation of exactly one new node for each original node.

Complexity:
The algorithm's time complexity depends on the order of the find_set() operation. With rank and path compression implemented, each find operation takes at most O(log n) time. The first for loop executes the find_set() method, leading to O(n * log n) time complexity, while the second loop performs n operations, resulting in O(n) time complexity. Overall, the algorithm's complexity is O(n * log n).

Connected Components Detection Algorithm

Algorithm:
The algorithm takes a binary image file as input and identifies connected components. The steps include:

1. Print the original image.
2. Instantiate a disjoint set class.
3. Iterate over each character in the file; if a "+" is found, use line and character numbers to represent its coordinate and key in the disjoint set hashmap. Additionally, perform a union_sets operation on connected nodes: to the left on the same line, on the previous line and one place to the left, on the previous line and the same position, and on the previous line and one position to the right.
4. Iterate over all keys in the disjoint set, find the representatives, and assign each unique representative a lowercase alphabet letter.
5. Iterate through the file again, replacing "+" symbols with the corresponding alphabetical label of the representative. Create three new strings: "labelledString", "labelledString2", and "labelledString3".
6. Sort connected components by size.
7. Print labeled images and the list of components.

Correctness:
The algorithm is correct as it both terminates correctly and provides the expected output. The termination process involves parsing the input file, finding representatives, relabeling and printing new string representations of the files, and returning. If the input file is empty or contains no "+" points, both the disjoint set and label hashmap remain empty, resulting in no output.

Complexity:
The most intensive portions of the algorithm are scanning the images during the disjoint set's creation and labeled components' generation. These involve find_set() or union_sets() operations, each taking O(log n) time. Thus, the algorithm's time complexity is O(n * log n).