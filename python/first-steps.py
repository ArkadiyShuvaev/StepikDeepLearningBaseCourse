file_path = "./python/temp.txt"
file = open(file_path, "w")
for i in range(5):
    file.write(str(i))
file.close()
file = open(file_path, "w")
for i in range(5, 10):
    file.write(str(i))
file.close()



def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: square(x), numbers))
print(result)

result2 = list(square(x) for x in numbers)
print(result2)



text = "hello"
print(text[4:100])


try:
    list(range(3))[3]
except Exception as ex:
    print(f"Something went wrong: {ex}")


try:
    raise Exception("Test try catch block.")
except Exception as ex:
    print(f"Something went wrong: {ex}")


print(True + 5)


float_value = 5.44
print(float_value / 5.4)


value = True
if value == True:
    print("true")
else:
    print("false")


# age = input("How old are you?")
# print(int(age))
