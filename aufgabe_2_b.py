# Moivtov,  Carina,     
# Flaum,    Arthur,     
# Ewald,    Florian,    333 068 94

# Alloc
w       = ""
wnew    = ""
A       = ""
B       = ""
n       = 0

# check wheather input is inside the range of 128 ASCII symbols
while True:
    s = input("Enter a String from the first 128 ASCII symbols: ").encode("ascii").decode("unicode_escape")
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

for letter in s:
    w = w + chr( ( ord(letter) - v ) % 128 )
    wnew = wnew + "$" + chr( ( ord(letter) - v ) % 128 )

wnew    = wnew[1:]
n       = len(w)
if n%2 == 0:
    A = w[:n/2]
    B = w[n/2:]
elif n%2 != 0:
    A = w[:n//2]
    B = w[n//2:]

print(repr(w))
print(repr(wnew))
print("A    = ", repr(A)[1:len(repr(A))-1]) #repr(w)[1:len(repr(w))-1]
print("B    = ", repr(B)[1:len(repr(B))-1])
print("B+A  = ", repr(B+A)[1:len(repr(A+B))-1])