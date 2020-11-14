# Moivtov,  Carina,     
# Flaum,    Arthur,     
# Ewald,    Florian,    333 068 94
def bin2dez(numb_bin):
    numb_bin = numb_bin[::-1]
    numb_dez = 0
    for index, digit  in enumerate(numb_bin):
        if digit == "1":
            numb_dez += 2**index
    return numb_dez

numb_bin = input("Enter a binary number: ")
for digit in numb_bin:
    if not( ( digit == "0" ) or ( digit == "1" ) ):
        print("Invalid input!")
        exit()

numb_dez = bin2dez(numb_bin)
print(numb_bin," (2) = ", str(numb_dez), " (10)")
