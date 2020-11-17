# Moivtov,  Carina,     
# Flaum,    Arthur,     
# Ewald,    Florian,    333 068 94

# check wheather input is inside the range of 128 ASCII symbols
while True:
    s = input("Enter a String from the first 128 ASCII symbols: ")
    for letter in s:
        if ord(letter) > 127:
            print("Invalid Input!")
            print("Input is outside the Range of 0-127!")
            break

    if ord(letter) < 127:
        break

while True:
    v = int( input("Displacement of symbols by a non negative integer: ") )
    if v >= 0:
        break
    else:
        print("Invalid Input!")
        print("Integer is negative!")

w = ""
for letter in s:
    w = w + chr( ( ord(letter) + v ) % 128 )

print(repr(w)[1:len(repr(w))-1])