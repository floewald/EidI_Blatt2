# Moivtov,  Carina,     
# Flaum,    Arthur,     
# Ewald,    Florian,    333 068 94
def printResult(Choice, Result):
    print("Schaltjahr nach dem ", Choice, " Kalender: ", Result)

o           = 0
j           = 0
isSchalt    = False

print("Wählen Sie bitte eine Option aus: (1-3)")
print("1. Julianischer Kalender")
print("2. Gregorianischer Kalender")
print("3. Orthodoxer Kalender")
o = float( input("Auswahl: ") )
# using float to allow invalid input like 2.45. No try-except statemant necessary to deal with ValueError using int(2.45)

if not( float(o == 1) + float(o == 2) + float(o == 3) ):
    print("Keine gültige Auswahl!")
    print("Programm wird beendet!")
    exit()

j = int( input("Geben Sie ein Jahr ein: ") )

if o == 1:
    # Schaltjahr nach julianischem Kalender
    # Fehler: alle 128 Jahre fehlt ein Tag
    isSchalt = ( j%4 ) == 0
    printResult("julianischen", isSchalt)
elif o == 2:
    # Schaltjahr nach gregorianischer Kalender
    isSchalt = ( ( j%4 ) == 0 ) and ( ( ( j%100 ) != 0 )  or ( ( j%400 ) == 0 ) )
    printResult("gregorianischen", isSchalt)
elif o == 3:
    # Schaltjahr nach orthodoxem Kalender
    isSchalt = ( ( j%4 ) == 0 ) and ( ( ( j%100 ) != 0 )  or ( ( j%900 ) == 200 ) or ( ( j%900 ) == 600 ) )
    printResult("gregorianischen", isSchalt)