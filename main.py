speed = input("Type your speed (km/h): ")
reactionTime = int(Speed) / 10 * 3
breakTime = reactionTime * 2
stopTime = reactionTime + breakTime

print("1 - Reaction Time")
print("2 - Break Time")
print("3 - Stop Time")
print("4 - All")
print("")
print("....................................")
print("")
question = input("What do you need to know?: ")
print("")

if (question == '1'):
    print(reactionTime)
elif (question == '2'):
    print(breakTime)
elif (question == '3'):
    print(stopTime)
elif (question == '4'):
    print(f"Reaction Time: {reactionTime}")
    print(f"Break Time: {breakTime}")
    print(f"Stop Time: {stopTime}")
    
#    /\_____/\
#   /  o   o  \
#  ( ==  ^  == )
#   )         (
#  (           )
# ( (  )   (  ) )
# (__(__)___(__)__)
