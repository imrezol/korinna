# https://www.w3schools.com/python/python_arrays.asp

def print_podium(places):
    print("podium:")
    print('First place:', places[0])
    print('Second place', places[1])
    print('Third place', places[2])
    print()

# There is a cross fit contest with 5 competitors
places = ['']*5
places[0] = "Korinna"
places[1] = "John"
places[2] = "Noah"
places[3] = "Emma"
places[4] = "Penny"

print("There were {} competitors".format(len(places)))
print()

print("all places:")
for x in range(5):
  print(x+1,'.',places[x])
print()

print("all competitors")
for competitor in places:
    print(competitor)
print()

print_podium(places)

# There was a problem
places[1] = "Emma"
places[3] = "Noah"

print_podium(places)

if "Emma" in places:
    print("Emma was a competitor")
else:
    print("Emma wasn't a competitor")


