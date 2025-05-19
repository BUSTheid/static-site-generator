import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        hello_node = HTMLNode(tag="p", value="Hello!")
        youtube_link = HTMLNode(tag="a", value="YouTube", props={"href": "https://www.youtube.com"})
        node = HTMLNode("h1", "This is a node", [hello_node, youtube_link], {"test": "pass"})
        node2 = HTMLNode("h1", "This is a node", [hello_node, youtube_link], {"test": "pass"})
        self.assertEqual(node, node2)

    def test_noteq_tag(self):
        hello_node = HTMLNode(tag="p", value="Hello!")
        youtube_link = HTMLNode(tag="a", value="YouTube", props={"href": "https://www.youtube.com"})
        node = HTMLNode("a", "This is a node", [hello_node, youtube_link], {"test": "pass"})
        node2 = HTMLNode("h1", "This is a node", [hello_node, youtube_link], {"test": "pass"})
        self.assertNotEqual(node, node2)

    def test_noteq_value(self):
        hello_node = HTMLNode(tag="p", value="Hello!")
        youtube_link = HTMLNode(tag="a", value="YouTube", props={"href": "https://www.youtube.com"})
        node = HTMLNode("h1", "This is a node", [hello_node, youtube_link], {"test": "pass"})
        node2 = HTMLNode("h1", "This is a node2", [hello_node, youtube_link], {"test": "pass"})
        self.assertNotEqual(node, node2)

    def test_noteq_children(self):
        hello_node = HTMLNode(tag="p", value="Hello!")
        youtube_link = HTMLNode(tag="a", value="YouTube", props={"href": "https://www.youtube.com"})
        node = HTMLNode("h1", "This is a node", [hello_node, youtube_link], {"test": "pass"})
        node2 = HTMLNode("h1", "This is a node",  [youtube_link], {"test": "pass"})
        self.assertNotEqual(node, node2)

    def test_noteq_props(self):
        hello_node = HTMLNode(tag="p", value="Hello!")
        youtube_link = HTMLNode(tag="a", value="YouTube", props={"href": "https://www.youtube.com"})
        node = HTMLNode("h1", "This is a node", [hello_node, youtube_link], {"test": "pass"})
        node2 = HTMLNode("h1", "This is a node", [hello_node, youtube_link], {"test": "false"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        youtube_link = HTMLNode(tag="a", value="YouTube", props={"href": "https://www.youtube.com", "color": "blue"})
        self.assertEqual(youtube_link.props_to_html(), ' href="https://www.youtube.com" color="blue"')


    def test_repr(self):
        node = HTMLNode("p", "What a strange world", None, {"class": "primary"})
        self.assertEqual(node.__repr__(), "HTMLNode(tag: p, value: What a strange world, children: None, props: {'class': 'primary'})")







if __name__ == "__main__":
    unittest.main()
