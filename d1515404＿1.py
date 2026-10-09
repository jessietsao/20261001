x = int(input())
if x < 0 or x > 15:
    print("輸入錯誤")
else:
    b3=x//8 
    r3=x%8 
    b2=r3//4 
    r2=r3%4 
    b1=r2//2
    b0=r2%2 
binary_str = f"{b3}{b2}{b1}{b0}"   
o1=x//8 
o0=x%8
octal_str=f"{o1}{o0}" 
if x == 10:
        h = "A"
elif x == 11:
        h = "B"
elif x == 12:
        h = "C"
elif x == 13:
        h = "D"
elif x == 14:
        h = "E"
elif x == 15:
        h = "F"
else:
        h = str(x) 
print(f"二進制={b3}{b2}{b1}{b0}")
print(f"八進制={o1}{o0}")
print(f"十六進制={h}")