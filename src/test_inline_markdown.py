import unittest
from textnode import TextType,TextNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestInlineMarkdown(unittest.TestCase):
    def test_basic_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_node, expected)

    def test_no_delimiters(self):
        node = TextNode("No special formatting", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("No special formatting", TextType.TEXT)
        ]
        self.assertEqual(new_node, expected)

    def test_unmatched_delimiters(self):
        node = TextNode("A `code block without closure", TextType.TEXT)
        try:
            new_node = split_nodes_delimiter([node], "`", TextType.CODE)
        except Exception as e:
            assert str(e) == "invalid markdown syntax"
        self.assertRaises(Exception)

    def test_mixed_types(self):
        mixed_node = TextNode("Some text", TextType.BOLD)
        split_node = TextNode("Here is `code` inside", TextType.TEXT)
        new_node = split_nodes_delimiter([mixed_node, split_node], "`", TextType.CODE)
        expected = [
            TextNode("Some text", TextType.BOLD),
            TextNode("Here is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" inside", TextType.TEXT)
        ]
        self.assertEqual(new_node, expected)

    def test_image_extraction(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extracted, expected)

    def test_link_extraction(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extracted, expected)

    def test_no_extraction(self):
        text = "A sentence without images?"
        extracted = extract_markdown_images(text)
        self.assertListEqual(extracted, [])

    def test_mixed_content(self):
        text = "Here's a mix ![image](https://example.com/image.png) and a [link](https://example.com)"
        extracted = extract_markdown_links(text)
        expected = [("link", "https://example.com")]
        self.assertEqual(extracted, expected)