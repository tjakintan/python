#############################################################
#
# CMPSC 132: Homework 4
#
#
# For each function, minimal test cases are provided.
# - You may test individual functions separately
#   or test all functions at once.
# - Read the comments at the end of this file
#   to learn how to do it
# - These test cases are not meant to be comprehensive.
#   They are provided simply to demonstrate the use cases
#   of each method.
# - Testing and debugging is your responsibility
#############################################################

student_name = "Tife Akintan"
student_email = "taa5555@psu.edu"
student_section = "003"


# DO NOT modify this class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class SortedLinkedList:

    # DO NOT modify this method
    def __init__(self):
        self.head = None
        self.tail = None

    # DO NOT modify this method
    def __str__(self):
        temp = self.head
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = ' -> '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    # DO NOT modify this method
    __repr__ = __str__

    def isEmpty(self):
        """
        >>> x=SortedLinkedList(); x.isEmpty()
        True
        >>> x.head = Node(10); x.isEmpty()
        False
        """
        if self.head is None:
            return True
        else:
            return False

        pass

    def __len__(self):
        """
        >>> x=SortedLinkedList(); len(x)
        0
        >>> x.head = Node(10); len(x)
        1
        >>> x.head.next = Node(20); x.head.next.next = Node(20); len(x)
        3
        """
        curr = self.head
        count = 0
        while curr is not None:
            curr = curr.next
            count += 1
        return count

        pass

    def add(self, value):
        """
        >>> x=SortedLinkedList(); x.add(10)
        Head:Node(10)
        Tail:Node(10)
        List:10
        >>> x.add(20)
        Head:Node(10)
        Tail:Node(20)
        List:10 -> 20
        >>> x.add(5)
        Head:Node(5)
        Tail:Node(20)
        List:5 -> 10 -> 20
        >>> x.add(7).add(15)
        Head:Node(5)
        Tail:Node(20)
        List:5 -> 7 -> 10 -> 15 -> 20
        >>> x.add(25).add(13).add(9.54).add(-10.3)
        Head:Node(-10.3)
        Tail:Node(25)
        List:-10.3 -> 5 -> 7 -> 9.54 -> 10 -> 13 -> 15 -> 20 -> 25
        >>> x=SortedLinkedList(); x.add()
        Traceback (most recent call last):
        TypeError: SortedLinkedList.add() missing 1 required positional argument: 'value'
        """

        new_node = Node(value)

        # if the list is empty, set the new node as the head and the tail
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return self

        # if the new node value is smaller than the head value, insert at the beginning
        if self.head.value > value:
            new_node.next = self.head
            self.head = new_node
            return self

        # if the new node value is greater than the tail value, insert at the end
        if self.tail.value <= value:
            self.tail.next = new_node
            self.tail = new_node
            return self

        # find the node after which to insert the new node
        current_node = self.head
        while current_node.next is not None and current_node.next.value < value:
            current_node = current_node.next

        # insert the new node after the current node
        new_node.next = current_node.next
        current_node.next = new_node

        return self

        pass

    # To pass the tests, you must implement add() first
    def remove(self, value):
        """
        >>> x=SortedLinkedList(); x.remove(4)
        Head:None
        Tail:None
        List:
        >>> x.add(4)
        Head:Node(4)
        Tail:Node(4)
        List:4
        >>> x.remove(4)
        Head:None
        Tail:None
        List:
        >>> x.add(1).add(2).add(3).add(4).add(5)
        Head:Node(1)
        Tail:Node(5)
        List:1 -> 2 -> 3 -> 4 -> 5
        >>> x.remove(1)
        Head:Node(2)
        Tail:Node(5)
        List:2 -> 3 -> 4 -> 5
        >>> x.remove(5)
        Head:Node(2)
        Tail:Node(4)
        List:2 -> 3 -> 4
        >>> x.remove(3)
        Head:Node(2)
        Tail:Node(4)
        List:2 -> 4
        >>> x.add(1).add(3).add(5)
        Head:Node(1)
        Tail:Node(5)
        List:1 -> 2 -> 3 -> 4 -> 5
        >>> x.remove(3).remove(1).remove(5).remove(2).remove(4)
        Head:None
        Tail:None
        List:
        >>> x.add(1).add(3).add(5).remove(2).remove(3).add(4)
        Head:Node(1)
        Tail:Node(5)
        List:1 -> 4 -> 5
        """
        if self.head is None:
            return self

        # if the head node is the node to remove, update the head
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return self

            # find the node before the node to remove
        current_node = self.head
        while current_node.next is not None and current_node.next.value != value:
            current_node = current_node.next

        # if the node to remove is not found, return
        if current_node.next is None:
            return self

        # if the tail node is the node to remove, update the tail
        if current_node.next == self.tail:
            self.tail = current_node

        # remove the node
        current_node.next = current_node.next.next
        return self

    # To pass the tests, you must implemente add() first
    def duplicate(self):
        """
        >>> x=SortedLinkedList(); x.duplicate()
        Head:None
        Tail:None
        List:
        >>> x.add(2).duplicate()
        Head:Node(2)
        Tail:Node(2)
        List:2 -> 2
        >>> x.add(3).duplicate()
        Head:Node(2)
        Tail:Node(3)
        List:2 -> 2 -> 3 -> 3 -> 3
        >>> x.add(1).duplicate()
        Head:Node(1)
        Tail:Node(3)
        List:1 -> 2 -> 2 -> 3 -> 3 -> 3
        >>> x.add(0).duplicate()
        Head:Node(0)
        Tail:Node(3)
        List:0 -> 1 -> 2 -> 2 -> 3 -> 3 -> 3
        >>> x.add(-5).duplicate()
        Head:Node(-5)
        Tail:Node(3)
        List:-5 -> -5 -> 0 -> 1 -> 2 -> 2 -> 3 -> 3 -> 3
        >>> x.add(4.5).duplicate()
        Head:Node(-5)
        Tail:Node(4.5)
        List:-5 -> -5 -> 0 -> 1 -> 2 -> 2 -> 3 -> 3 -> 3 -> 4.5 -> 4.5
        >>> x
        Head:Node(-5)
        Tail:Node(4.5)
        List:-5 -> 0 -> 1 -> 2 -> 3 -> 4.5
        """
        a = []
        current = self.head

        # Traverse the original linked list and add each value to the new list
        while current is not None:
            a.append(current.value)
            current = current.next

        result = []
        for num in a:
            if isinstance(num, float):
                result += [num] * 2
            elif num > 0:
                result += [num] * num
            elif num < 0:
                result += [num] * 2
            elif num == 0:
                result += [num] * 1
            else:
                result.append(num)

        v = SortedLinkedList()
        for i in result:
            v.add(i)

        return v

    # To pass the tests, you must implement add() first
    def removeDuplicates(self):
        """
        >>> x=SortedLinkedList(); x.removeDuplicates(); x
        Head:None
        Tail:None
        List:
        >>> x=SortedLinkedList(); x.add(2).add(2).removeDuplicates(); x
        Head:Node(2)
        Tail:Node(2)
        List:2
        >>> x=SortedLinkedList(); x.add(1).add(2).add(2).removeDuplicates(); x
        Head:Node(1)
        Tail:Node(2)
        List:1 -> 2
        >>> x=SortedLinkedList(); x.add(1).add(2).add(3).add(3).removeDuplicates(); x
        Head:Node(1)
        Tail:Node(3)
        List:1 -> 2 -> 3
        >>> x.add(1).add(2).add(2).add(4).add(4).add(5).add(5).removeDuplicates(); x
        Head:Node(1)
        Tail:Node(5)
        List:1 -> 2 -> 3 -> 4 -> 5
        """
        current = self.head

        # Traverse the linked list and remove duplicate nodes
        while current is not None and current.next is not None:
            if current.value == current.next.value:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
            else:
                current = current.next

        pass


if __name__ == '__main__':
    import doctest

    ## Uncomment this line if you want to run doctest by function.
    ## Replace isEmpty with the name of the function you want to run
    # doctest.run_docstring_examples(SortedLinkedList.add, globals(), verbose=True, name='hw4')

    ## Uncomment this line if you want to run the docstring
    ## in all functions
    # doctest.testmod()
