class Node:
    def __init__(self, text=""):
        self.text = text
        self.children = {}
        self.is_word = False

    def __repr__(self):
        return f"Node('{self.text}')"

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        if not word:
            return
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]
        current.is_word = True

    def find(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_word

    def remove(self, node, word, depth=0):
        if not node:
            return None

        # If we've reached the end of the word
        if depth == len(word):
            if node.is_word:
                node.is_word = False
            # If the node has no children, it can be deleted
            if not node.children:
                return None
            return node

        char = word[depth]
        if char in node.children:
            node.children[char] = self.remove(node.children[char], word, depth + 1)

        # If child node is deleted, remove the reference from parent node
        if char in node.children and not node.children[char]:
            del node.children[char]

        # If the current node is not a word and has no children, delete it
        if not node.is_word and not node.children:
            return None

        return node

    def delete(self, word):
        self.root = self.remove(self.root, word)

    def starts_with(self, prefix):
        words = []
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        self._collect_words(current, prefix[:-1], words)
        return words

    def _collect_words(self, node, prefix, words):
        if node.is_word:
            words.append(prefix + node.text)
        for char, child in node.children.items():
            self._collect_words(child, prefix + node.text, words)

    def visualize(self):
        def dfs(node, depth=0):
            lines = []
            if not node:
                return lines
            for char, child_node in node.children.items():
                if child_node:
                    lines.append(" " * (depth * 2) + f"({char}, {'END' if child_node.is_word else ''})")
                    lines.extend(dfs(child_node, depth + 1))
            return lines

        result = "\n".join(dfs(self.root))
        return result if result else "Trie is empty."

# Testing
tree = Trie()
tree.insert("app")
tree.insert("apple")
tree.insert("abs")
tree.insert("absorb")
tree.insert("apricot")
tree.insert("bill")
tree.insert("bills")
tree.insert("bow")
tree.insert("bowling")
tree.insert("cat")
tree.insert("caterpillar")

print("Before deletion:")
print(tree.visualize())

tree.delete("bowling")

print("\nAfter deletion of 'bowling':")
print(tree.visualize())
