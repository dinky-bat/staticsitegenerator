class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemente")
    
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
        # return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
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
        super().__init__(tag, value, props)
        self.value = value
        self.tag = tag
        self.props = props
    
    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node missing value")
        if self.tag == None:
            return self.value
        # if self.props != None:
        #    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        # # return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

