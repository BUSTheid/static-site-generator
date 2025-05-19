import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_normal(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertEqual(node, node2)

    def test_eq_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is a bold text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        node2 = TextNode("This is an italic text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_eq_code(self):
        node = TextNode("This is a code snippet", TextType.CODE)
        node2 = TextNode("This is a code snippet", TextType.CODE)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.youtube.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://www.youtube.com")
        self.assertEqual(node, node2)

    def test_eq_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "image.png")
        node2 = TextNode("This is an image", TextType.IMAGE, "image.png")
        self.assertEqual(node, node2)

    def test_noteq_no_url(self):
        node = TextNode("This is a text node", TextType.NORMAL, "https://www.youtube.com")
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_noteq_diff_text(self):
        node = TextNode("YouTube", TextType.NORMAL, "https://www.youtube.com")
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_noteq_diff_type(self):
        node = TextNode("Hello!", TextType.NORMAL)
        node2 = TextNode("Hello!", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("Hello!", TextType.BOLD, "https://youtube.com")
        self.assertEqual(
            "TextNode(Hello!, bold, https://youtube.com)", repr(node)
        )







if __name__ == "__main__":
    unittest.main()
