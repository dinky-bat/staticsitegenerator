import unittest
from htmlnode import HTMLNode,LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("h1", "Heading", children=None, props={"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("h1", "Heading", children=None, props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node1, node2)

    def test_empty_eq(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph.", children=None, props={"class": "text"})
        expected_repr = "HTMLNode(p, This is a paragraph., None, {'class': 'text'})"
        self.assertEqual(repr(node), expected_repr)
    
    def test_props_to_html(self):
        node = HTMLNode("a", "Click here", children=None, props={"href": "https://example.com", "target": "_blank"})
        expected_props_html = ' href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props_html)

    def test_leaf(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_html = '<p>This is a paragraph of text.</p>'
        self.assertEqual(node.to_html(), expected_html)

    def test_leaf_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_html)

    def test_leaf_empty_value(self):
        node = LeafNode("h1")
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_raw_text(self):
        node = LeafNode(value="This is just raw text")
        expected = "This is just raw text"
        self.assertEqual(node.to_html(), expected)

    def test_leaf_empty_props(self):
        node = LeafNode("p", "Hello", {})
        expected = "<p>Hello</p>"
        self.assertEqual(node.to_html(), expected)

    def test_leaf_multi_props(self):
        node = LeafNode("input", "Submit", {"type": "submit","class": "btn","id": "submit-btn"})
        expected = '<input type="submit" class="btn" id="submit-btn">Submit</input>'
        self.assertEqual(node.to_html(), expected)

    def test_leaf_special_chars(self):
        node = LeafNode("p", "Hello & goodbye < > \" '")
        expected = '<p>Hello & goodbye < > " \'</p>'
        self.assertEqual(node.to_html(), expected)