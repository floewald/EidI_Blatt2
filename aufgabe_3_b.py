# Moivtov,  Carina,     
# Flaum,    Arthur,     
# Ewald,    Florian,    333 068 94
def dez2bin(numb_dez):
    numb_bin = ""
    k = 0

    while numb_dez >= 2**k:
        k += 1
    
    # range(k, -1, -1) = [k, k-1, .... , 1, 0]
    for m in range(k, -1, -1):
        if numb_dez - 2**m >= 0:
            numb_bin += "1"
            numb_dez -= 2**m
        elif ( numb_dez - 2**m < 0 ) and ( m != k):
            numb_bin += "0"
        
    return numb_bin

numb_dez = int( input("Enter a positive integer: ") )
if numb_dez < 0:
    print("Input is not a positive Integer!")
    exit()

numb_bin = dez2bin(numb_dez)
print(numb_dez," (10) = ", str(numb_bin), " (2)")
