from textnode import TextType,TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception("invalid markdown syntax")
            for i, part in enumerate(parts):
                if i % 2 == 0:
                     new_list.append(TextNode(part, TextType.TEXT))
                else: 
                    new_list.append(TextNode(part, text_type))
        else:
            new_list.append(node)
    return new_list
        
def extract_markdown_images(text): 
    extracted = (re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text))
    result = [tuple(match) for match in extracted]
    return result

def extract_markdown_links(text):
    extracted = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    result = [tuple(match) for match in extracted]
    return result

def split_nodes_image(old_nodes):
    new_list = []
    for node in old_nodes:
        pass

def split_nodes_link(old_nodes):
    new_list = []
    for node in old_nodes:
        extracted = extract_markdown_links(node.text)

