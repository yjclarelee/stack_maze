import matplotlib.pyplot as plt


# The stack class
class Stack:
    # The node class inside of the stack class
    class Node:
        # Node consists of an element and next
        def __init__(self, element, next):
            self.element = element
            self.next = next

    # A stack consists of nodes and the head
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, element):
        # The next element is the previous head
        node = self.Node(element, self.head)
        self.head = node
        self.size += 1

    def pop(self):
        # Raise an exception if the stack is empty
        if self.size == 0:
            raise Exception("The stack is empty.")
        element = self.head.element
        self.head = self.head.next
        self.size -= 1
        # Return the value of the element
        return element

    def top(self):
        # Raise an exception if the stack is empty
        if self.size == 0:
            raise Exception("The stack is empty.")
        # Return the value of the element
        return self.head.element

    # Return true or false
    def isEmpty(self):
        return self.size == 0


# boolean if the point is blocked in 3 directions
def blocked(point, i):
    total = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for j in range(4):
        if i != j:
            temp_point = maze[point[0]+dx[j]][point[1]+dy[j]]
            # if wall or traversed
            if temp_point == 1 or temp_point == 3:
                total += 1
    return total == 3


# open file
file = open("./maze.txt")
maze = []
# set elements into the array
for line in file:
    maze.append([int(x) for x in line.strip().split(',')])


# coordinates for right, down, left and up
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

stack = Stack()
# push starting point
point = [1, 1]
stack.push(point)
maze[point[0]][point[1]] = 2

# flag to finish when food is found
flag = 1
while not stack.isEmpty() and flag:
    for i in range(4):
        # coordinates of new path
        x_temp = point[0]+dx[i]
        y_temp = point[1]+dy[i]
        # if food is found, stop
        if maze[x_temp][y_temp] == 4:
            flag = 0
            break
        # if the path has not been traversed
        if maze[x_temp][y_temp] == 0:
            point = [x_temp, y_temp]
            # push the point into the stack
            stack.push(point)
            maze[point[0]][point[1]] = 2
            break
        # if there is a wall
        elif maze[x_temp][y_temp] == 1:
            continue
        # if the path has been traversed
        elif maze[x_temp][y_temp] == 2:
            # if there is no other path
            if blocked(point, i):
                # pop the point from the stack
                stack.pop()
                maze[point[0]][point[1]] = 3
                point = [x_temp, y_temp]
                break
        # if the coordinate has been popped
        elif maze[x_temp][y_temp] == 3:
            continue

# print the stack by popping the elements
print_stack = []
temp_stack_size = stack.size
for i in range(temp_stack_size):
    print_stack.append(stack.pop())
for i in range(temp_stack_size-1, 0, -1):
    print('({}, {})->'.format(print_stack[i][0], print_stack[i][1]), end="")
print('({}, {})'.format(print_stack[0][0], print_stack[0][1]))

plt.imshow(maze, cmap='jet')
plt.savefig('./solution.png')
