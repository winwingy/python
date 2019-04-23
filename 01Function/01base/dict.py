# _*_ coding: utf-8 _*_
dict1={"a":1, "b":2}
print(dict1["a"])

dict1["c"]=10
print(dict1)

val = dict1.get("d", -1)
print(val)

dict1.pop("c")
print(dict1)
