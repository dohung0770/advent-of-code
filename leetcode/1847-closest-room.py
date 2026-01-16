class Solution:
    def closestRoom(self, rooms: list[list[int]], queries: list[list[int]]) -> list[int]:
        # Sort the queries by room's min size in decreasing order
        q = sorted(
            [(min_size, preferred, orig_idx) for orig_idx, (preferred, min_size) in enumerate(queries)],
            key=lambda x: x[0],
            reverse=True
        ) # q[i] = (min_size, preferred, original query index)

        # Process all rooms with larger or equals size to q[i]'s min size
        # Maintain a sorted list + bisect to find two rooms with closest id to q[i]'s preferred
        
        m = len(queries)
        output = [-1] * m

        n = len(rooms)
        rooms.sort(key=lambda x: x[1], reverse=True) # Sort rooms by size in decreasing order
        room_idx = 0

        # current = SortedList()
        current = AVLTree()

        for min_size, preferred, orig_idx in q:
            while room_idx < n and rooms[room_idx][1] >= min_size:
                current.add(rooms[room_idx][0]) # Add room id to sorted list
                room_idx += 1

            output[orig_idx] = current.bisect(preferred)

            # idx = current.bisect_left(preferred)

            # print(current, idx, preferred, orig_idx)

            # if 0 <= idx < len(current) and current[idx] == preferred:
            #     output[orig_idx] = current[idx]
            # else:
            #     if idx > 0:
            #         output[orig_idx] = current[idx - 1]
            #     if idx < len(current) and \
            #         (output[orig_idx] == -1 or (abs(preferred - output[orig_idx]) > abs(current[idx] - preferred))):
            #         output[orig_idx] = current[idx]

        # T: O(m*logn + nlogn)
        # S: O(m + n)
        return output

# AVLTree
class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' | None = None, right: 'TreeNode' | None = None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0
        self.bf = 0 # balance factor

class AVLTree:
    def __init__(self):
        self.root = None

    def add(self, val: int):
        self.root = self._insert(self.root, val)

    def bisect(self, val: int) -> int:
        '''
        Find the closest value to the given val in tree
        '''

        result = self._bisect(self.root, val)
        return result if result != float('inf') else -1

    # Private methods
    def _insert(self, root: TreeNode | None, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)

        if root.val < val:
            root.right = self._insert(root.right, val)
        else:
            root.left = self._insert(root.left, val)

        self._update(root)
        return self._balance(root)

    def _update(self, root: TreeNode):
        height_left = root.left.height if root.left else -1
        height_right = root.right.height if root.right else -1

        root.height = 1 + max(height_left, height_right)
        root.bf = height_left - height_right

    def _balance(self, root: TreeNode) -> TreeNode:
        if root.bf != 2 and root.bf != -2:
            return root

        # Left heavy
        if root.bf == 2:
            # Case Left-Right
            if root.left.bf < 0:
                root.left = self._rotate_left(root.left)

            return self._rotate_right(root)

        # Right heavy
        # Case Right-Left
        if root.right.bf > 0:
            root.right = self._rotate_right(root.right)

        return self._rotate_left(root)

    def _rotate_left(self, root: TreeNode) -> TreeNode:
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        self._update(root)
        self._update(new_root)
        return new_root

    def _rotate_right(self, root: TreeNode) -> TreeNode:
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        self._update(root)
        self._update(new_root)
        return new_root

    def _bisect(self, root: TreeNode | None, val: int) -> int:
        if root is None:
            return float('inf') # No nodes with the closest value to val found

        if root.val == val:
            return root.val

        if root.val < val:
            result = self._bisect(root.right, val)

            return result if val - root.val > abs(result - val) else root.val

        result = self._bisect(root.left, val)
        return result if root.val - val > abs(result - val) else root.val
