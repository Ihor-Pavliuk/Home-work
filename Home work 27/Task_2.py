from html.parser import HTMLParser

class Node:
    def __init__(self, tag, text=""):
        self.tag = tag
        self.text = text.strip() if text else ""
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"Node(tag={self.tag}, text={self.text})"

class DOMParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = None
        self.current_node = None
        self.stack = []

    def handle_starttag(self, tag, attrs):
        node = Node(tag)
        if self.current_node:
            self.current_node.add_child(node)
        else:
            self.root = node
        self.stack.append(node)
        self.current_node = node

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()
            self.current_node = self.stack[-1] if self.stack else None

    def handle_data(self, data):
        if self.current_node:
            self.current_node.text += data.strip()

    def parse(self, html):
        self.feed(html)
        return self.root

def search_by_tag(node, tag):
    if not node:
        return []

    result = []
    if node.tag == tag and node.text:
        result.append(node.text)

    for child in node.children:
        result.extend(search_by_tag(child, tag))

    return result


if __name__ == "__main__":
    with open("example.html", "r", encoding="utf-8") as html_doc:
        html_content = html_doc.read() 

        parser = DOMParser()
        dom_tree = parser.parse(html_content)

        search_tag = "h2"
        #search_tag = input("Enter the tag to search for: ").strip()
        found_texts = search_by_tag(dom_tree, search_tag)
    
        print(f"Texts found under tag <{search_tag}>:")
        for text in found_texts:
            print(f"- {text}")
