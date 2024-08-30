immutable_var = 1, True, 1.5,'string'
print(immutable_var)
print(type(immutable_var))
#immutable_var [1] = False
#print(immutable_var)
#кортеж, неизменяемый объект(это встроенная функция самой программы, которую не возможно изменить с помощью кода)
mutable_list = ["one","two","three","four"]
print(mutable_list)
print(type(mutable_list))

mutable_list[0] = 1
mutable_list[1] = 2
mutable_list[2] = 3
mutable_list[3] = 4

print(mutable_list)
print(type(mutable_list))
