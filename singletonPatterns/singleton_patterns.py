from singleton import Singleton
from not_singleton import NotSingleton


a = NotSingleton()
b = NotSingleton()

print(f"{id(a)} --> {a}")
print(f"{id(b)} --> {b}")
print(f"is a == b {a is b}")

c = Singleton()
d = Singleton()

print(f"{id(c)} --> {c}")
print(f"{id(d)} --> {d}")
print(f"is c == d {c is d}")