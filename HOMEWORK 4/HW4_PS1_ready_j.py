# Joseph Ready
# 1300529
# Homework 4 Program Set 1
#

#  Program to test functions a to j.
#
# Define constant variables for testing.
TEST_ONE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
TEST_TWO = [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
TEST_THREE = [1, 25, 25, 4, 5, 4, 7, 60, 9, 10]
TEST_FOUR = [75, 54, 7, 9, 87, 8, 30]


def main():
    test_cases = [TEST_ONE, TEST_TWO, TEST_THREE, TEST_FOUR]
    for test_num in range(len(test_cases)):
        print("Run test: ", test_num + 1)
        test_functions(test_cases[test_num])
        print("")


def test_functions(test):
    print("The original data for all functions is: ", test)

    # a. Demonstrate swapping the first and last element.
    data = list(test)
    swapFirstLast(data)  # call this function
    print("After swapping first and last: ", data)

    # b. Demonstrate shifting to the right.
    data = list(test)
    shiftRight(data)  # call this function
    print("After shifting right: ", data)

    # c. Demonstrate replacing even elements with zero.
    data = list(test)
    replaceEven(data)  # call this function
    print("After replacing even elements: ", data)

    # d. Demonstrate replacing values with the larger of their neighbors.
    data = list(test)
    replaceNeighbors(data)  # call this function
    print("After replacing with neighbors: ", data)

    # # e. Demonstrate removing the middle element.
    # data = list(test)
    # removeMiddle(data)  # call this function
    # print("After removing the middle element(s): ", data)
    #
    # # f. Demonstrate moving even elements to the front of the list.
    # data = list(test)
    # evenToFront(data)  # call this function
    # print("After moving even elements: ", data)
    #
    # # g. Demonstrate finding the second largest value.
    # print("The second largest value is: ", secondLargest(test))
    #
    # # h. Demonstrate testing if the list is in increasing order.
    # print("The list is in increasing order: ", isIncreasing(test))
    #
    # # i. Demonstrate testing if the list contains adjacent duplicates.
    # print("The list has adjacent duplicates: ", hasAdjacentDuplicate(test))
    #
    # # j. Demonstrate testing if the list contains duplicates.
    # print("The list has duplicates: ", hasDuplicate(test))


# Complete the codes for the functions a. to j. below.

# a.
def swapFirstLast(data: list) -> None:
    '''Swap the first and last element in a list.'''
    first_num = data[0]
    last_num = data[-1]
    data[0] = last_num
    data[-1] = first_num


# b.
def shiftRight(data: list) -> None:
    '''Shift the elements to the right.'''
    temp = data[-1]
    for i in range(len(data)-1, -1, -1):
        data[i] = data[i-1]
    data[0] = temp


# c.
def replaceEven(data: list) -> None:
    '''Replace all even elements in the list with 0.'''
    for i in range(len(data)):
        if data[i] %2 == 0:
            data[i] = 0


# d.
def replaceNeighbors(data: list) -> None:
    '''Replace each value with the larger of its neighbors.'''
    for i in range(1, len(data) - 1):
        left_num = data[i - 1]
        right_num = data[i + 1]

        if left_num > right_num:
            data[i] = left_num
        else:
            data[i] = right_num



# # e.
# def removeMiddle(data: list) -> None:
#     '''Remove the middle element or elements from a list.'''
#     ??? replace
#     with your codes here ???
#
#
# # f.
# def evenToFront(data: list) -> None:
#     '''Move even elements to the front of the list.'''
#     ??? replace
#     with your codes here ???
#
#
# # g.
# def secondLargest(data: list) -> int:
#     '''Identify the second largest value in a list.
#         return the second largest value in the list'''
#     ??? replace
#     with your codes here ???
#
#
# # h.
# def isIncreasing(data: list) -> bool:
#     '''Determine whether or not the list is in increasing order.
#         return True if the list is in increasing order, False otherwise'''
#     ??? replace
#     with your codes here ???
#
#
# # i.
# def hasAdjacentDuplicate(data: list) -> bool:
#     '''Determine if the list contains adjacent duplicate elements.
#        return True if the list contains adjacent duplicates, False otherwise'''
#     ??? replace
#     with your codes here ???
#
#
# # j.
# def hasDuplicate(data: list) -> bool:
#     '''Determine if the list contains duplicate elements.
#         return True if the list contains duplicates, False otherwise'''
#     ??? replace
#     with your codes here ???
#

if __name__ == "__main__":
    main()


