ls = []
for i in range(100):
	if i % 3 == 0:
		ls.append(i)
print(ls)

print("this will print just a list of above conditions:\n")

#[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

print("Now comprehesion (list) like one-liner code which will print above result:\n")

ls = [i for i in range(100) if i % 3 == 0]

print(ls)

print("this will print just a list of above conditions: ")

#[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

print("without comprehesion (dictionary)")

dicts = {}
for i in range(5):
	dicts['SerialNo-'+ str(i)] = i
	dicts[f'SerialNo-{i}'] = i
	dicts.update({'SerialNo-' + str(i): i})
print(dicts)

print("Comprehesion (dictionary)")

dict1 = {f"SerialNo-{i}": i for i in range(5)}
print(dict1)

#we reversing this dictionary like this" 
dict2 = {value : key for key, value in dict1.items()}

print(dict2)

print("without comprehesion (SET)")

dress = {"d1", "d2", "d3", "d4", "d5", "d6", "d6", "d3"}

for i in [dress]:
	print(i)

print("with comprehesion (SET)")

dressed = {i for i in {"d1", "d2", "d3", "d4", "d5", "d6", "d6", "d3"}}
print(dressed)

print("Generator Comprehension")

evens = (i for i in range(100) if i%2 ==0)
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
# for ii in evens:
# 	print(ii)



no_of_list = input("How many items add in a list: ")

input_string = input("Enter a list element separated by space ")
list = input_string.split()
print(list)
t = int(input(""" Which type of comprehension you use 
	1. List Comprehension 
	2. Dictionary Comprehension
	3. Set Comprehension """))

if t==1:
    ls = [i for i in list]
    print(ls)
    print(type(ls))

elif t==2:
    dict1 = {f'item{i}': i for i in list}
    print(dict1)
    print(type(dict1))

elif t==3:
    s = {i for i in list}
    print(s)
    print(type(s))
