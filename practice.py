class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    # Write your code here
    def add_member(self, member):
        self.members.append(member)

    def delete_member(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception("Member does not exist")

    def get_members(self):
        return sorted(self.members)


group1 = Group("Justice League")
group1.add_member("Zion")
group1.add_member("Batman")
group1.add_member("Robin")
group1.add_member("Superman")

group1.delete_member("Robin")
print(group1.get_members())
print(group1.name)

