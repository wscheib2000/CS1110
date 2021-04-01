import str_redux

print(str_redux.myfind("divided", "d"))
print(str_redux.myfind("divided", "id"))
print(str_redux.myfind("divided", "ido"))
print(str_redux.myfind("hello", "o"))

print()

print("divided".find("d"))
print("divided".find("id"))
print("divided".find("ido"))
print("hello".find("o"))

print()

print(str_redux.mysplit('a string divided'))
print(str_redux.mysplit(' divided'))
print(str_redux.mysplit(' divided '))
print(str_redux.mysplit('   '))  # there are 3 spaces here

print()

print("a string divided".split(" "))
print(" divided".split(" "))
print(" divided ".split(" "))
print("   ".split(" "))
