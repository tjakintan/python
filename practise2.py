import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "Node({})".format(self.data)

    __repr__ = __str__



class Stack:
    """
    >>> x = Stack()
    >>> x.isEmpty()
    True
    >>> len(x)
    0
    >>> x.peek()
    >>> x.pop()
    >>> x
    Top: None
    Stack: 
    >>> x.push(2)
    >>> x.isEmpty()
    False
    >>> len(x)
    1
    >>> x.peek()
    2
    >>> x.pop()
    2
    >>> x
    Top: None
    Stack: 
    >>> x.push(2)
    >>> x.push(4)
    >>> x.push(6)
    >>> x.isEmpty()
    False
    >>> len(x)
    3
    >>> x
    Top: Node(6)
    Stack: 6 <= 4 <= 2
    >>> x.peek()
    6
    >>> x.pop()
    6
    """

    # DO NOT modify this method
    def __init__(self):
        self.top = None

    # DO NOT modify this method
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.data))
            temp = temp.next
        out = ' <= '.join(out)
        return ('Top: {}\nStack: {}'.format(self.top, out))

    # DO NOT modify this method
    __repr__ = __str__

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False
            pass

    def __len__(self):
        count = 0
        temp = self.top
        while temp is not None:
            count += 1
            temp = temp.next
        return count

        pass

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode

        pass

    def pop(self):
        if self.top is None:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.data

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data
        pass


# =============================================== Part II==============================================


class Calculator:
    # DO NOT modify this member
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # DO NOT modify this method
    def __init__(self):
        self.__expr = None

    # DO NOT modify this method
    @property
    def expr(self):
        return self.__expr

    # DO NOT modify this method
    @expr.setter
    def expr(self, new_expr):
        if isinstance(new_expr, str) and self._validate(new_expr):
            self.__expr = new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, token):
        """
        >>> x=Calculator()
        >>> x._isNumber('5')
        True
        >>> x._isNumber('+5')
        True
        >>> x._isNumber('-5')
        True
        >>> x._isNumber('5.')
        True
        >>> x._isNumber('-5.')
        True
        >>> x._isNumber('+5.')
        True
        >>> x._isNumber('0.5')
        True
        >>> x._isNumber('-0.5')
        True
        >>> x._isNumber('.5')
        True
        >>> x._isNumber('-.5')
        True
        >>> x._isNumber(' 4.560 ')
        True
        >>> x._isNumber('4 56')
        False
        >>> x._isNumber('4.56a')
        False
        >>> x._isNumber('-4.56a')
        False
        >>> x._isNumber('4.5a6')
        False
        """
        try:
            float(token)
            return True
        except ValueError:
            return False
        pass

    def _validate(self, expr):
        """
        >>> x=Calculator(); x._validate('2 ^ 4')
        True
        >>> x=Calculator(); x._validate('2')
        True
        >>> x=Calculator(); x._validate('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
        True
        >>> x=Calculator(); x._validate('2 * 5.34 + 3 ^ 2 + 1 + 4')
        True
        >>> x=Calculator(); x._validate('2.1 * 5 + 3 ^ 2 + 1 + 4')
        True
        >>> x=Calculator(); x._validate('( 2.5 )')
        True
        >>> x=Calculator(); x._validate ('( ( 2 ) )')
        True
        >>> x=Calculator(); x._validate ('2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )')
        True
        >>> x=Calculator(); x._validate ('( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )')
        True
        >>> x=Calculator(); x._validate ('( ( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ) )')
        True
        >>> x=Calculator(); x._validate('2 * ( -5 + 3 ) ^ 2 + ( 1 + 4 )')
        True
        >>> x = Calculator(); x._validate('2 * 5 + 3 ^ + -2 + 1 + 4')
        False
        >>> x = Calculator(); x._validate('2 * 5 + 3 ^ - 2 + 1 + 4')
        False
        >>> x = Calculator(); x._validate('2    5')
        False
        >>> x = Calculator(); x._validate('25 +')
        False
        """

        operators = (['+', '-', '*', '/', '^'])
        opening_parens = (['(', '[', '{'])
        closing_parens = ([')', ']', '}'])
        parens_map = dict(zip(opening_parens, closing_parens))
        digits = (['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        decimal = (['.'])
        negative_sign = (['-'])
        space = ([' '])
        parentheses = {'(': ')'}
        a = expr


        if len(expr) == 0:
            return False
        expr = expr.replace(' ', '')

        stack = []
        last_token = None
        for i, token in enumerate(expr):
            if token in digits:
                if last_token in digits or last_token == ')':
                    for g,token2 in enumerate(a):
                        if a[g].isdigit() and a[g-2] == '-' or ' ':
                            if a[g-2] in operators:
                                return True
                            elif a[-1] not in digits:
                                return False

                    return False
            elif token in decimal:
                if last_token in decimal or last_token == ')' or last_token is None:
                    return False
                if last_token in digits:
                    return True

            elif token in negative_sign:
                for b, token1 in enumerate(a):
                    if a[b] == '-' and a[b + 2].isdigit() and a[b - 2] in operators:
                        return False

            elif token in operators:
                if last_token in operators or last_token == '(' or last_token is None:
                    return False

            elif token in opening_parens:
                for c in a:
                    if c == "(":
                        stack.append(c)
                    elif c == ")":
                        if not stack:
                            return False
                        stack.pop()
                return not stack
            else:
                return False

            last_token = token

        if len(stack) > 0:
            return False

        return True

        pass

    # self.__expr must be a valid expression
    # validity of self.__expr is checked when calling the property method @expr.setter
    # - see @expr.setter for detail
    def _getPostfix(self):
        """
        Required: _getPostfix must create and use a Stack for expression processing
        >>> x=Calculator()
        >>> x.expr = '2 ^ 4'; x._getPostfix()
        '2.0 4.0 ^'
        >>> x.expr = '2'; x._getPostfix()
        '2.0'
        >>> x.expr = '2.1 * 5 + 3 ^ 2 + 1 + 4.45'; x._getPostfix()
        '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
        >>> x.expr ='2 * 5.34 + 3 ^ 2 + 1 + 4'; x._getPostfix()
        '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
        >>> x.expr = '2.1 * 5 + 3 ^ 2 + 1 + 4'; x._getPostfix()
        '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
        >>> x.expr = '( 2.5 )'; x._getPostfix()
        '2.5'
        >>> x.expr = '( ( 2 ) )'; x._getPostfix()
        '2.0'
        >>> x.expr = '2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )'; x._getPostfix()
        '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
        >>> x.expr = '( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )'; x._getPostfix()
        '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
        >>> x.expr = '( ( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ) )'; x._getPostfix()
        '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
        """

        ## YOUR CODE STARTS HERE
        ratorStack = Stack()  # must use ratorStack to get a postfix expression of self.__expr
        lst = []
        infix = self.__expr.strip().split()
        for token in infix:
            if self._isNumber(token):
                lst.append(str(float(token)))
            elif token == '(':
                ratorStack.push(token)
            elif token == ')':
                while ratorStack.peek() != '(':
                    lst.append(ratorStack.pop())
                ratorStack.pop()

            elif token == '*' or token == '/' or token == '+' or token == '-':
                while not ratorStack.isEmpty() and ratorStack.peek() != '(' and self.priority[ratorStack.peek()] >= \
                        self.priority[token]:
                    lst.append(ratorStack.pop())
                ratorStack.push(token)
            elif token == '^':
                while not ratorStack.isEmpty() and ratorStack.peek() != '(' and self.priority[ratorStack.peek()] > \
                        self.priority[token]:
                    lst.append(ratorStack.pop())
                ratorStack.push(token)
            else:
                return None

        while not ratorStack.isEmpty():
            lst.append(ratorStack.pop())

        postfix = ' '.join(lst)
        return postfix

        pass

    # This property method must
    # 1. converts self.__expr to a postfix expression by calling self._getPostfix
    # 2. use a stack to compute the final result of the postfix expression
    @property
    def value(self):
        '''
        >>> x=Calculator()
        >>> x.expr = '4 + 3 - 2'; x.value
        5.0
        >>> x.expr = '-2 + 3.5'; x.value
        1.5
        >>> x.expr = '4 + 3.65 - 2 / 2'; x.value
        6.65
        >>> x.expr = '23 / 12 - 223 + 5.25 * 4 * 3423'; x.value
        71661.91666666667
        >>> x.expr = ' 2 - 3 * 4'; x.value
        -10.0
        >>> x.expr = '7 ^ 2 ^ 3'; x.value
        5764801.0
        >>> x.expr = ' 3 * ( ( ( 10 - 2 * 3 ) ) )'; x.value
        12.0
        >>> x.expr = '8 / 4 * ( 3 - 2.45 * ( 4 - 2 ^ 3 ) ) + 3'; x.value
        28.6
        >>> x.expr = '2 * ( 4 + 2 * ( 5 - 3 ^ 2 ) + 1 ) + 4'; x.value
        -2.0
        >>> x.expr = ' 2.5 + 3 * ( 2 + ( 3.0 ) * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 / 3 ) ) - 2 / 3 ^ 2'; x.value
        1442.7777777777778
        '''

        if not isinstance(self.__expr, str) or len(self.__expr) <= 0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()  # must use calcStack to compute the expression
        a = self.__expr
        self.__expr = self._getPostfix()
        value = self.__expr

        for token in value.split():
            if self._isNumber(token):
                a = float(token)
                calcStack.push(a)
            else:
                operand2 = calcStack.pop()
                operand1 = calcStack.pop()
                if token == '+':
                    calcStack.push(operand1 + operand2)
                elif token == '-':
                    calcStack.push(operand1 - operand2)
                elif token == '*':
                    calcStack.push(operand1 * operand2)
                elif token == '/':
                    if operand2 == 0.0:
                        raise ValueError("division by zero found")
                    calcStack.push(operand1 / operand2)
                elif token == '^':
                    calcStack.push(operand1 ** operand2)


        if calcStack.__len__() == 1:
            b = calcStack.pop()
            return b
        else:
            return None



        pass

    def SortedArrays(self, x, y):

        list1 = [x]
        list2 = [y]

        list3 = sorted(list1 + list2)
        length = list3.__len__()

        if (length % 2) == 0:
            middle1 = (n // 2) - 1
            middle2 = middle1 + 1
            median = (list3[middle1] + list3[middle2]) / 2
            return median
        13791

        else:
            index = (length // 2)
            return list3[index]














if __name__ == '__main__':
    import doctest

    ## Uncomment this line if you want to run doctest by function.
    ## Replace get_words with the name of the function you want to run
    # doctest.run_docstring_examples(Calculator.value, globals(), verbose=True, name='hw5')

    ## Uncomment this line if you want to run the docstring
    ## in all functions
    # doctest.testmod()

    sys.version_info.major






