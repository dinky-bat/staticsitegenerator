import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq1(self):
        node1 = TextNode("another text node", TextType.ITALIC)
        node2 = TextNode("another text node", TextType.ITALIC)
        self.assertEqual(node1, node2)

    def test_text_neq(self):
        node1 = TextNode("does this match the other node?", TextType.CODE)
        node2 = TextNode("this better not match", TextType.CODE)
        self.assertNotEqual(node1, node2)

    def test_type_neq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_url_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "http://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://google.com")
        self.assertEqual(node1, node2)

    def test_url_neq(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "http://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD,)
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()