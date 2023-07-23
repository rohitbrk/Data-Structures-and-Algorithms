class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        flag = " "*int(self.get_level()*2)+"|--" if self.parent else ""
        print(flag+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


if __name__ == "__main__":
    root = Tree("Electronics")

    laptops = Tree("laptops")
    dell = Tree("dell")
    hp = Tree("hp")
    mac = Tree("mac")
    laptops.add_child(dell)
    laptops.add_child(hp)
    laptops.add_child(mac)

    tvs = Tree("tvs")
    samsung = Tree("samsung")
    lg = Tree("lg")
    tvs.add_child(samsung)
    tvs.add_child(lg)

    mobiles = Tree("mobiles")
    redmi = Tree("redmi")
    realme = Tree("realme")
    apple = Tree("apple")
    mobiles.add_child(redmi)
    mobiles.add_child(realme)
    mobiles.add_child(apple)

    root.add_child(laptops)
    root.add_child(tvs)
    root.add_child(mobiles)

    root.print_tree()
