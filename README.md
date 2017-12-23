# twig
Twig coding challenge.

The code consists of a single function that splits a list in to a specified number of sub-lists. The function returns a list of lists or an empty list.

The size of the new lists to be created is calculated as the number of new lists to create divided by the size of the original list, rounded up to the nearest whole integer. If 0 is provided as the number of new lists to create then a ZeroDivisionError will be caught and an empty list will be returned.

The function makes use of list comprehension in order to construct the return value. The for clause makes use of the range function in order to calculate the index within the original list to start each new list from. Each new list is created by slicing the original list from the calculated starting index through to the calculated ending index.

Associated unit tests have been added for a series of test cases including: an original list that divides equally; an original list that divides unequally; an empty original list; a positive number of new lists to create; a negative number of new lists to create; one new list to create; zero new lists to create.
