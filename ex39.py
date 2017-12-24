# create a mapping of state to abbreviation
states = {
 'Oregon': 'OR',
 'Floria': 'FL',
 'California': 'CA',
 'New York': 'NY',
 'Michigan': "MI"
}

# create a basic set of states and some cities in them
cities = {
 'CA': 'San Francisco',
 'MI': 'Detroit',
 'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Floria's abbreviation is: ", states['Floria'])

#do it by using the state then cities dict
print("-" * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Floria has: ", cities[states['Floria']])

#print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-'*10)
for abbrev, city in list(cities.items()):
    print(f"({abbrev} has the city {city}.)")

#now do both at the same time
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-'*10)
# safely get a abbreviation by state that might not be there
state = states.get('TEXAS', 'TX')
states['Washton DC'] = 'WC'
print(state)
print(states)

if not state:  #这个if not从句也没学过
    print("Sorry, no Texas.")

#get a city with a default value
city = cities.get("TX", "Does not exist")
print(f"The city for the state 'TX' is: {city}")
