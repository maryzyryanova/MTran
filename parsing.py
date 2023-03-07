from errors import (
    SyntaxError,
    SemanticsError
)
from patterns import(
    ASSIGNMENT_OPERATORS,
    BINARY_OPERATORS,
    CLOSE,
    DATA_TYPES,
    ENDLINE,
    OPEN,
    UNARY_OPERATORS
)

class Node(object):
    def __init__(self, value, parent=None) -> None:
        self.value = value
        self.parent = parent
        self.children = []

class Parser(object):
    def __init__(self, tokens) -> None:
        self.tokens = [t for t in tokens if t[2] not in DATA_TYPES]
        self.node = Node('node')
        self.parenthesis = []
    
    def add(self, parent, value) -> None:
        new = Node(value, parent)
        parent.children.append(new)

    def check_syntax(self, node):
        if node.value[2] in ASSIGNMENT_OPERATORS and len(node.children) != 2:
            raise SyntaxError('Expected expression after assignment', node.value[0], node.value[1])
        for c in node.children:
            self.check_syntax(c)

    def print_tree(self, node, indent):
        print('|' * indent, node.val[2], sep='', )
        for child in node.children:
            self.print_tree(child, indent + 1)


    def parse(self, show=False):
        current = self.node
        assignment = False
        binary = False
        for t in self.tokens:
            new = Node(t, current)
            if t[2] in OPEN:
                current = current.children[-1]
                self.parenthesis.append(t)
                continue
            if t[2] in CLOSE:
                current = current.parent
                if len(self.parenthesis) > 0:
                    p = self.parenthesis.pop()
                else:
                    raise SyntaxError(f'Unexpected parenthesis "{t[2]}"', t[0], t[1])
                if p[2] == '{' and t[2] == ')':
                    raise SyntaxError('Expected "}" but got ")"', p[0], p[1])
                if p[2] == '(' and t[2] == '}':
                    raise SyntaxError('Expected ")" but got "}"', p[0], p[1])
                continue
            if t[2] in BINARY_OPERATORS:
                binary = True
                current.children.append(new)
                left_neighbour = current.children[-2]
                left_neighbour.parent.children.remove(left_neighbour)
                left_neighbour.parent = new
                new.children.append(left_neighbour)
                continue
            if t[2] in ASSIGNMENT_OPERATORS:
                assignment = True
                current.children.append(new)
                left_neighbour = current.children[-2]
                left_neighbour.parent.children.remove(left_neighbour)
                left_neighbour.parent = new
                new.children.append(left_neighbour)
                current = current.children[-1]
                continue
            if t[2] in UNARY_OPERATORS:
                current.children.append(new)
                left_neighbour = current.children[-2]
                left_neighbour.parent.children.remove(left_neighbour)
                left_neighbour.parent = new
                new.children.append(left_neighbour)
                continue
            if binary and t[2] != ENDLINE:
                binary = False
                new = Node(t, current.children[-1])
                current.children[-1].children.append(new)
                continue
            if assignment:
                if t[2] == ENDLINE:
                    assignment = False
                    current = current.parent
                    continue
                current.children.append(new)
                continue
            if t[2] != ENDLINE:
                current.children.append(new)
        self.check_syntax(self.node)
        if show:
            self.print_tree(self.node, 0)