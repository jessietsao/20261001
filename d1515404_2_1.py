a=int(input()) 
b=int(input()) 
if (a != 0 and a != 1) or (b != 0 and b != 1):
    print("輸入錯誤")  
else: 
    if a == 1 or b == 1:
        or_result = 1
    else:
        or_result = 0
    if a == 1 and b == 1:
        and_result = 1
    else:
        and_result = 0 
    if a != b:
        xor_result = 1
    else:
        xor_result = 0 
print(f"OR={or_result}")
print(f"AND={and_result}")
print(f"XOR={xor_result}")