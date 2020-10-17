"""
#  Q3 :- VOLUME OF SPHERE

radius = float(input("ENTER THE RADIUS OF SPHERE"))

def VOLUME(radius):

    volume = 4/3 * 3.14 * radius * radius *radius

    return volume

print("VOLUME OF SPHERE : {}".format(VOLUME(radius)))

"""



"""
# Q2  

first_name = str(input("Enter Your First Name : - "))
last_name = str(input("Enter Your Last Name : - "))


def reverse_name(fist_name,last_name):
    print("My Name is {} {}".format(first_name,last_name))
    print("My Name is {} {}".format(first_name[::-1],last_name[::-1]))
    

print(reverse_name(first_name,last_name))
"""



"""
# Q1

for i in range(2000,3201):
    if i % 7 == 0 and i % 5 !=0:
        print(i,end = " ")

"""