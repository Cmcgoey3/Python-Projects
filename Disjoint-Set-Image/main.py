"""
Name: Connor McGoey
Date: March 2, 2023
"""

import sys

"""
disjointSet class for creating a disjoint set using a hashmap to store nodes based on keys.
"""
class disjointSet:

    # Subclass Node to store node information in a disjoint set including its data, parent, rank, and size.
    class Node:
        def __init__(self, data, parentNode, rank):
            self.data = data
            self.parentNode = parentNode
            self.rank = rank
            self.size = 1

    # Class variables. nodes hashmap to store the nodes, size of the entire disjoint set, and boolean variable
    # finalSets to determine if make_set or union_sets can be performed.
    nodes = dict()
    size = 0
    finalSets = False

    # initialize the size of the entire disjoint set.
    def uandf(self, n):
        self.size = n

    # make a set with only one piece of data 'i'. Set its parent to itself, increment the size variable.
    def make_set(self, i):
        if self.finalSets:
            return

        if i not in self.nodes:
            newNode = self.Node(i, None, 0)
            newNode.parentNode = newNode
            self.nodes[i] = newNode

        self.size = max(self.size, len(self.nodes))

    """
    find_set method to find the representative of a node. Recursively calls itself and updates the parent node of each
    node in the path to the representative of that path.
    """
    def find_set(self, i):
        if self.nodes[i].parentNode == self.nodes[i]:
            return self.nodes[i].data
        root = self.find_set(self.nodes[i].parentNode.data)
        self.nodes[i].parentNode = self.nodes[root]
        return root

    """
    union_sets method to union two sets based off of their ranks. Sets the representative of the smaller set to be the
    representative of the larger set. If the two sets are equal in rank, update the rank of the new set. Also, update
    the size of the new set.
    """
    def union_sets(self, i, j):
        if self.finalSets:
            return

        if j not in self.nodes:
            return

        iRoot = self.nodes[self.find_set(i)]
        jRoot = self.nodes[self.find_set(j)]

        if iRoot.data == jRoot.data:
            return

        if iRoot.rank >= jRoot.rank:
            if iRoot.rank == jRoot.rank:
                iRoot.rank += 1
            iRoot.size += jRoot.size
            jRoot.parentNode = iRoot
        else:
            jRoot.size += iRoot.size
            iRoot.parentNode = jRoot

    """
    final_sets method sets the class variable finalSets to True, returns a list of representatives and the size of the
    disjoint set. Additionally, resets the elements in the disjoint set to be single node sets.
    """
    def final_sets(self):
        representatives = set()
        for key in self.nodes.keys():
            representatives.add(self.find_set(key))

        self.finalSets = True
        self.nodes.clear()
        for i in range(1, self.size + 1):
            newNode = self.Node(i, None, 0)
            newNode.parentNode = newNode
            self.nodes[i] = newNode

        return [len(representatives), self.size]

"""
fins_binary_components function uses the disjointSet class to scan a binary image for components represented by "+"
and connected by the surrounding 8 tiles around it. It then prints the following after doing so:
1. The original binary image
2. The connected component image where each component is labelled with a unique character
3. A list sorted by component size, where each line of the list contains the size and the label of a component
4. Same as 2, but only the connected components whose sizes are greater than 1 will be printed
5. Same as 2, but only the connected components whose sizes are greater than 11 will be printed.
"""
def find_binary_components(binaryFile):
    try:
        img = open(binaryFile, 'r')
    except FileNotFoundError:
        print("No such file:", binaryFile)
        return

    imgSet = disjointSet()

    print("1. Input Binary Image:\n")
    fileLine = 0
    for line in img:
        print(line, end="")
        currChar = 0
        for char in line:
            if char == '+':
                newItem = tuple([fileLine, currChar])
                imgSet.make_set(newItem)
                if fileLine == 5:
                    fileLine = 5
                if tuple([fileLine, currChar - 1]) in imgSet.nodes:
                    imgSet.union_sets(newItem, tuple([fileLine, currChar - 1]))
                if tuple([fileLine - 1, currChar - 1]) in imgSet.nodes:
                    imgSet.union_sets(newItem, tuple([fileLine - 1, currChar - 1]))
                if tuple([fileLine - 1, currChar]) in imgSet.nodes:
                    imgSet.union_sets(newItem, tuple([fileLine - 1, currChar]))
                if tuple([fileLine - 1, currChar + 1]) in imgSet.nodes:
                    imgSet.union_sets(newItem, tuple([fileLine - 1, currChar + 1]))
            currChar += 1
        fileLine += 1

    c = ord('a')
    reps = dict()
    for key in imgSet.nodes.keys():
        representative = imgSet.find_set(key)
        if representative not in reps:
            reps[representative] = [chr(c), imgSet.nodes[representative].size]
            c += 1

    img.seek(0)
    labelledString = ""
    labelledString2 = ""
    labelledString3 = ""
    fileLine = 0
    for line in img:
        currChar = 0
        for char in line:
            if char == '+':
                rep = imgSet.find_set(tuple([fileLine, currChar]))
                labelledString += reps[rep][0]
                if imgSet.nodes[rep].size > 1:
                    labelledString2 += reps[rep][0]
                    if imgSet.nodes[rep].size > 11:
                        labelledString3 += reps[rep][0]
                    else:
                        labelledString3 += " "
                else:
                    labelledString2 += " "
                    labelledString3 += " "

            else:
                labelledString += char
                labelledString2 += char
                labelledString3 += char
            currChar += 1
        fileLine += 1

    print("\n\n\n2. Labelled String:\n")
    print(labelledString)

    finalList = []
    for key in reps.keys():
        finalList.append([key, reps[key][0], reps[key][1]])
    finalList.sort(key=lambda x: x[2])

    print("\n\n\n3. Sorted List of Representatives:\n")
    for item in finalList:
        print("Representative:", item[0], "Label:", item[1], "Size:", item[2])

    print("\n\n\n4. Labelled String with size > 1:\n")
    print(labelledString2)

    print("\n\n\n5. Labelled String with size > 11:\n")
    print(labelledString3)



"""
Main driver function to call the find_binary_components function with the binary file name passed as a command line
parameter 
"""
if __name__ == '__main__':
    if len(sys.argv) > 1:
        find_binary_components(sys.argv[1])
