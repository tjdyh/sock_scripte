#!/usr/bin/env python

class Group(object):
    def __init__(self, group_id, members=[]):
        self.group_id = group_id
        self.members = members

    def add_member(self, member):
        self.members.append(member)

group1 = Group(1)
group1.add_member("Wang")
group1.add_member("Sun")

print(id(group1))
print(group1.members)

group2 = Group(2)
group2.add_member("Zhang")
group2.add_member("Li")

print(id(group2))
print(group1.members)
