import copy


class Living(object):
    def __del__(self):
        undead_hoard.append(self)

a = Living()
b = copy.copy(a)
undead_hoard = []
del a
print(len(undead_hoard)),
print(b)
del b
print(len(undead_hoard)),
del undead_hoard[0]
print(len(undead_hoard)),
undead_hoard = []
print(len(undead_hoard))