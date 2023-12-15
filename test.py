class UserMainCode(object):
    @classmethod
    def toffees(cls, input1, input2):
        # Read input values
        N = input1
        K = input2

        i = 0  # Index to keep track of the current child
        op = []  # Initialize a list to store the number of toffees received by each child

        while i < N:
            for j in range(K):
                v = j + 1  # Calculate the number of toffees for the current child
                op.append(v)  # Add the number of toffees to the result list
                i += 1

        return op


# Example usage:
input1 = 7
input2 = 4
result = UserMainCode.toffees(input1, input2)
print(result)  # Output: [1, 2, 3, 4, 1, 2, 3]