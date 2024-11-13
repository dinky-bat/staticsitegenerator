class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        attributes = []
        for key, value in self.props.items():
            attributes.append(f" {key}=\"{value}\"")
        return "".join(attributes)

    def __repr__(self):
        if self.props is None:
            return ""
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.tag is None:
            return self.value
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        child_content = []
        # child_content = ''.join(child.to_html() for child in self.children)
        child_content = ''.join(map(lambda child: child.to_html(), self.children))
        full_html = f"<{self.tag}>{child_content}</{self.tag}>"
        return full_html
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"