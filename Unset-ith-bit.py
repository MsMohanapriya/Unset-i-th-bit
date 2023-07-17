def Unset_ith_bit(number,bit_position):
    mask=(1<<bit_position)
    if number & mask:
        number=number & ~mask
    return number   
    
    
    
number=int(input("enter number: "))
bit_position=int(input("enter bit to be changed: "))
print(Unset_ith_bit(number,bit_position))