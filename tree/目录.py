


class Node:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None
    
    # def __str__(self):
    #     return self.name
    
    def __repr__(self):
        return self.name
    

# a = Node('hello')
# b = Node('world')

# b.children.apppend(a)
# a.parent = b

class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        # name 必须是以/结尾
        if name[-1] != "/":
            name += "/"
        
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now
    
    def ls(self):
        return self.now.children
    
    def cd(self, name):
        # 支持相对路径
        if name[-1] != "/":
            name += "/"
        # 返回上一级目录
        if name == "../":
            self.now = self.now.parent
            return
        for child in self.now.children:
            if child.name == name:
                self.now = child
                break
        else:
            raise ValueError("invalid dir") 
    

tree = FileSystemTree()
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("usr/")

print(tree.ls())
tree.cd("bin/")
tree.mkdir('python/')
print(tree.ls())
