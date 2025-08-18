'''room_temperature = 0
outside_temperature = 40
if room_temperature < 30:
    print('Heat mode ON')
elif room_temperature > 30:
    print('Heat mode OFF')
elif outside_temperature >= room_temperature :
    print("Turning on AC")
else:
    print('NO ACTION')

for x in "Python":
    print(x)
for x in ["Python"]:
    print(x)
#while LOop
#while loop is ued to repeat something until the condition is met.
number = 100
while number > 0:
    print(number)
    number //=2

command = ""
while command.lower() != "exit":
    command = input(">")
    print("Echo",command)
  '''
count = 0
for number in range(1,100):
    if number % 2 ==0:
        print(number)
print (f"We have {count} chances left")