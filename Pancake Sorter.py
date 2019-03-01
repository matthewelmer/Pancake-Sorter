class Node:
    def __init__(self, state, flip_index=-1, parent=None):
        self.state = state
        self.flip_index = flip_index
        self.parent = parent
        self.children = []

    def add_node(self, state, flip_index, parent):
        """adds a node to the specified parent target, adding the new node in its list of children
        and creating the new node object itself."""
        new_node = Node(state, flip_index, parent)
        self.children.append(new_node)
        return new_node

    def trace_to_root(self, flip_index):
        """traces the path back to the root and reverses it so that it returns a list of the steps it took to get to the
        optimal path"""
        path = [flip_index]
        trace_node = self
        while trace_node.parent is not None:
            path.append(trace_node.flip_index)
            trace_node = trace_node.parent
        path.reverse()
        return path

    def verbose_trace_to_root(self, flip_index):
        """shows each update in the path to the """
        path = [flip_index]
        trace_node = self
        verbose_path = [trace_node.children[0].state]
        verbose_path.append(trace_node.state)
        while trace_node.parent is not None:
            path.append(trace_node.flip_index)
            trace_node = trace_node.parent
            verbose_path.append(trace_node.state)
        path.reverse()
        verbose_path.reverse()
        for state in verbose_path:
            print(state)
        return path

    def flipped_state(self, flip_index):
        """given a node, returns its state flipped at the specified index. Could be made into a static method that
        acts directly on the state instead"""
        unflipped_part = self.state[:flip_index + 1]  # need to include the flip index part
        flipped_part = unflipped_part[::-1]
        flipped_state = flipped_part + self.state[flip_index + 1:]
        return flipped_state


root = Node('2461357')
goal = '1234567'
explored_states = []  # all of the states that have already been explored
queue = [root]  # where the nodes go in order to get processed. Use queue.pop(0).

best_state = root.state  # checks to see if root node happens to be optimal and allows for entry into the loop
while best_state != goal:
    current_node = queue.pop(0)
    explored_states.append(current_node.state)

    for i in range(1, len(current_node.state)):  # i cycles through each useful flip index (0 is purposefully skipped)
        result_node = current_node.add_node(current_node.flipped_state(i), i, current_node)  # flip at i

        if result_node.state == goal:  # for when the flipped pancakes are proper
            best_state = result_node.state  # when the optimal node is found, the best state is updated to exit the loop
            print('Done! Path taken:')
            print(current_node.verbose_trace_to_root(i))

        if result_node.state not in explored_states:  # remember what's been explored so it doesn't go back and forth
            queue.append(result_node)
