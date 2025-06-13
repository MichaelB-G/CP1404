"""Prac_04 CP1404
lists_warmup
"""

numbers = [3,1,4,1,5,9,2]

  # numbers[0]: this should print the first element in the list i.e., " 3 ".
  # Python Console confirms 3 as the output.
  # numbers[-1]: I believe this should start from the end of the list so "2", due to the
  # way python is structured.
  # Python Console confirms 2 as the output.
  # numbers[3]: this will print the 4th element in the list, which starting from
  # 0, is 1.
  # Python Console confirms 1 as the output.
  # numbers[:-1]: I am sure this cuts off the end of the list.
  # Python Console has confirmed this, 2 is removed from the list.
  # numbers[3:4}: the output of this line, should print 1 as its the 4th element from the LHS,
  # and the 4 element from the RHS.
  # Python Console confirms this.
  # 5 in numbers: This should return a true if there is a 5 present in the list.
  # Python Console confirms this.
  # 7 in numbers: This will return a False, as there is no 7 in the list.
  # Python Console confirms this is False.
  # "3" in numbers: This will output False, because there are no elements that contain
  # a string that matches "3".
  # Python Confirms this.
  # numbers + [6,5,3]: This will add the listed elements to the list in the form of integers.
  # Python Console confirms this.

numbers[0] = "ten"  # to fix this warning from the editor,
                    # allowing for multiple types of elements.
numbers[-1] = 1
print(numbers[2:])
print(9 in numbers)


