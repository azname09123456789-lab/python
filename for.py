#برنامه تست حلقه با for
a=2
b=3
for i in range(1,3):
    for j in range(2,10,3):
        a+=b
        b+=a
        b+=1
        print(f"a is {a},b is {b},i is {i},j is {j}")
