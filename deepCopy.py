from copy import deepcopy

class Member1:
    ID = 0
    def __init__(self, idIn):
        print("----Member1 Constructor with ID ", idIn)
        self.ID = idIn
        return
    def __del__(self):
        print("----Member1 Destructor with ID ", self.ID)
        return
    def setID(self, idIn):
        print("----Change Member1 ID from ", self.ID, " to ", idIn)
        self.ID = idIn
        return
    def printID(self):
        print("----Member1, ID: ", self.ID)
        return

class Member2:
    # has a default constructor, unlike Member1
    ID = 0
    def __init__(self, idIn=0):
        print("----Member2 Constructor with ID ", idIn)
        self.ID = idIn
        return
    def __del__(self):
        print("----Member2 Destructor with ID ", self.ID)
        return
    def setID(self, idIn):
        print("----Change Member2 ID from ", self.ID, " to ", idIn)
        self.ID = idIn
        return
    def printID(self):
        print("----Member2, ID: ", self.ID)
        return

class Container1:
    member = Member1(-1)
    def __init__(self, idIn):
        self.member = Member1(idIn)
        return
    def __del__(self):
        # del self.member
        return
    def setID(self, idIn):
        self.member.setID(idIn)
        return
    def printID(self):
        print("----Print Container1 ID")
        self.member.printID()
        return

class Container2:
    member = Member2(-1)
    def __init__(self, idIn=-1):
        self.member = Member2(idIn)
        return
    def __del__(self):
        # del self.member
        return
    def setID(self, idIn):
        self.member.setID(idIn)
        return
    def printID(self):
        print("----Print Container2 ID")
        self.member.printID()
        return

def main():
    print("")
    print("--------------------o--------------------")
    print("")
    print("-----------Test member classes-----------")
    print("")
    print("--------------------o--------------------")
    print("")

    print("--------------------")
    print("INITIALIZE WITH ID = 1")
    m1 = Member1(1)
    m2 = Member2(1)
    print("")

    #TODO: tests

    print("--------------------")
    print("CLEANUP")
    del m1
    del m2
    print("")

    print("")
    print("--------------------o--------------------")
    print("")
    print("---------Test container classes----------")
    print("")
    print("--------------------o--------------------")
    print("")

    print("--------------------")
    print("INITIALIZE WITH ID = 1")
    print("Initializing Container1")
    c1 = Container1(1)
    print("Container1 ID:")
    c1.printID()
    print("")
    print("Initializing Container2")
    c2 = Container2(1)
    print("Container2 ID:")

    print("--------------------")
    print("TEST COPY")
    print("Make copy of Container1 instance")
    c1Copy = c1
    print("")
    print("Original Container1 ID")
    c1.printID()
    print("Copied Container1 ID")
    c1Copy.printID()
    print("")
    print("Change original Container1 ID to 3")
    c1.setID(3)
    c1.printID()
    print("Get copied Container1 ID")
    c1Copy.printID()
    print("")
    print("Change copied Container1 ID to 4")
    c1Copy.setID(4)
    c1Copy.printID()
    print("Get original Container1 ID")
    c1.printID()
    print("")
    print("")
    print("")

    print("Make copy of Container2 instance")
    c2Copy = c2
    print("")
    print("Original Container2 ID")
    c2.printID()
    print("Copied Container2 ID")
    c2Copy.printID()
    print("")
    print("Change original Container2 ID to 3")
    c2.setID(3)
    c2.printID()
    print("Get copied Container2 ID")
    c2Copy.printID()
    print("")
    print("Change copied Container2 ID to 4")
    c2Copy.setID(4)
    c2Copy.printID()
    print("Get original Container2 ID")
    c2.printID()
    print("")
    print("")
    print("")

    print("--------------------")
    print("TEST DEEP COPY")

    print("Make deep copy of Container1 instance")
    c1DeepCopy = deepcopy(c1)
    print("")
    print("Original Container1 ID")
    c1.printID()
    print("Deep copied Container1 ID")
    c1DeepCopy.printID()
    print("")
    print("Change original Container1 ID to 10")
    c1.setID(10)
    c1.printID()
    print("Get deep copied Container1 ID")
    c1DeepCopy.printID()
    print("")
    print("Change deep copied Container1 ID to 11")
    c1DeepCopy.setID(11)
    c1DeepCopy.printID()
    print("Get original Container1 ID")
    c1.printID()
    print("")
    print("")
    print("")

    print("Make deep copy of Container2 instance")
    c2DeepCopy = deepcopy(c2)
    print("")
    print("Original Container2 ID")
    c2.printID()
    print("Deep copied Container2 ID")
    c2DeepCopy.printID()
    print("")
    print("Change original Container2 ID to 10")
    c2.setID(10)
    c2.printID()
    print("Get deep copied Container2 ID")
    c2DeepCopy.printID()
    print("")
    print("Change deep copied Container2 ID to 11")
    c2DeepCopy.setID(11)
    c2DeepCopy.printID()
    print("Get original Container2 ID")
    c2.printID()
    print("")
    print("")
    print("")

    print("--------------------")
    print("CLEANUP")
    del c1
    del c2
    del c1Copy
    del c2Copy
    del c2DeepCopy

main()

