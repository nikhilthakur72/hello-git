#1>
list = []
x = int(input("enter the the number of elements "))
for i in range(x):
    list.append(input("enter the values"))
print(list)
#used for appending the list
#2>
list1 = ['google','microsoft','tesla','facebook','apple']
list1.extend(li2)
print(list1)
#used for extend
#3>
li3 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,5,6,4,6,4,64,5]
print(li3.count(1))
#counting in a list
#4>
lo = [5,3,6,3,6,3,6,2345,2,426,663,16,31,6,34]
lo.sort()
print(lo)
#used for sorting the list

#5>
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]
list1.extend(list2)
list1.sort()
print(list1)

#6>
#use of stack in list
non = []
while(True):
    print("press 1 to add\npress 2 to delete\npress 3 to display\npress 4 to exit")
    option = int(input("enter the option"))
    if(option ==1):
        non.append(input("enter the value in stack"))
    elif(option ==2):
        if len(non)>0:
            non.pop()
        else:
            print("stack is empty")
    elif(option ==3):
        print(non)
    else:
        break

#list with queue
xyz = []
while(True):
    print("press 1 to add\npress 2 to delete\npress 3 to display\npress 4 to exit")
    option = int(input("enter the option"))
    if(option ==1):
        xyz.append(input("enter the value in queue"))
    elif(option ==2):
        if len(li)>0:
            xyz.pop(0)
        else:
            print("queue is empty")
    elif(option ==3):
        print(xyz)
    else:
        break
#extra question
v=0
z=0
    for i in xyz:
        if i%2==0:
            v=v+1
        else:
            z=z+1
print(v)
print(z)
