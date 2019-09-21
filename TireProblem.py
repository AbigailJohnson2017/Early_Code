print('A car with __ wheels carrying __ spares makes a ___ mile trip\nIf the driver rotates their tires so that each one is on the road for the same distance, how far did each tire drive?')
tires_used=float(input("Enter number of wheels:"))
tires_spare=float(input('Enter number of spares:'))
tires=tires_used+tires_spare
miles=float(input('Enter total miles travelled:'))
useprop=tires_used/tires
mpt=useprop*miles
print("Each tire is in use for ", useprop, " of the trip")
print("Each tire travels ",mpt," over the course of the trip")
