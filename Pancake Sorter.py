class Node:
    def __init__(self, state, flip_index=-1, parent=None):
        self.state = state  # stores state of pancakes
        self.flip_index = flip_index  # stores index
        self.parent = parent  # stores the node's parent
        self.children = []  # stores the node's children

    def add_node(self, state, flip_index, parent):
        self.children.append(Node(state, flip_index, parent))
        return Node(state, flip_index, parent)

    def trace_to_root(self, flip_index):
        path = [flip_index]
        trace_node = self
        while trace_node.parent is not None:
            path.append(trace_node.flip_index)
            trace_node = trace_node.parent
        path.reverse()
        return path

    def flipped_state(self, flip_index):  # I really need to test this
        """given a node, returns a flipped copy of its state, flipped at the specified flip index"""
        aux_list = []
        state_copy = self.state[:]
        for f in range(flip_index + 1):  # f for flip :)
            aux_list.append(state_copy.pop(0))  # could do for item in self
        # for item in self.state:
        #     if self.state.index(item) <= flip_index:  # here this is okay because the items are unique
        #         flip_state.append(item)
        for item in aux_list:
            state_copy.insert(0, item)
        # state copy is now flipped
        return state_copy


root = Node([1, 3, 2, 4])
explored_states = []  # all of the states that have already been explored
queue = [root]  # where the nodes go in order to get processed. Use queue.pop(0).


# n1 = root.add_node([3,1,2], 1, root)  # proving trace function works
# n4 = n1.add_node([2,1,3], 2, n1)
# n7 = n4.add_node([1,2,3], 1, n4)
# n7.trace_to_root()
# print(path)


# pancake flip optimal path program
best_state = root.state
goal = [1, 2, 3, 4]
while best_state != goal:
    current_node = queue.pop(0)
    explored_states.append(current_node.state)
    for i in range(1, len(current_node.state)):
        result_node = current_node.add_node(current_node.flipped_state(i), i, current_node)
        if result_node.state == goal:
            best_state = result_node.state
            print('Done! Path taken:')
            print(current_node.trace_to_root(i))
        if result_node.state not in explored_states:
            queue.append(result_node)

# could do cleanup like queue = []


# def result(cnode, a):  # Sournav's node creation
#     temp_node = Node()
#     temp_node.state = flip(cnode.state, a)  # I made my flip function work directly on the node
#     temp_node.flip = a
#     temp_node.parent = cnode
#     cnode.children.append(temp_node)


