immutable_var = 1, True, 1.5,'string'
print(immutable_var)
print(type(immutable_var))
#immutable_var [1] = False
#print(immutable_var)
#кортеж, неизменяемый объект(это встроенная функция самой программы, которую не возможно изменить с помощью кода)
mutable_list = ([1,2], False, 1.0, 'string')
print(mutable_list)
mutable_list [0][0] = 3
print(mutable_list)