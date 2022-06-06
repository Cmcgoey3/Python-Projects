if __name__ == '__main__':
    print('Please input a matrix of 0s and 1s where each row is separated by a newline, once done enter Q or q')

    #Take in user input to create the matrix
    userIn = input()
    Matrix = []
    while userIn != ('Q') and userIn != ('q'):
        temp = []
        for i in userIn:
            temp.append(int(i))
        Matrix.append(temp)
        userIn = input()

    # Set up variables for what needs to be found
    edges = 0
    non_incident = []
    only_loops = []
    degrees = []

    # Initialize degrees to 0 for each vertex in the graph
    for i in range(0, len(Matrix)):
        degrees.append(0)

    # Iterate through each row and column
    for i in range(0, len(Matrix)):
        for j in range(0, len(Matrix[i])):
            # If there is no edge and the same is true for the reverse ordering of vertices AND it is not a loop.
            # add that pair to the list of non-incidents
            if (Matrix[i][j] == 0) and (Matrix[j][i] == 0) and (i != j):
                temp = []
                temp.append(i)
                temp.append(j)
                non_incident.append(temp)
            # If there is an edge, determine whether it is a loop
            if Matrix[i][j] != 0:
                # if it is a loop, add it to the list of loops, if it is not a loop then remove it from the list if
                # there
                if (i == j) and (only_loops.__contains__(i) == False):
                    only_loops.append(i)
                else:
                    if (only_loops.__contains__(i)) and (i != j):
                        only_loops.remove(i)
                # Increase edges if an edge is found
                edges = edges + Matrix[i][j]
                # Increase the degree of the two edges even if a loop
                degrees[i] = degrees[i] + 1
                degrees[j] = degrees[j] + 1

    # Print results
    print("\nResults:")
    print("Edges:", edges)
    print("Non-Incidents:", non_incident)
    print("Only Loops:", only_loops)
    print("Degrees:", degrees)




