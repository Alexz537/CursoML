#jalaaaaaaaaa

#Una lista es una coleccion que es ordenada y puede ser cambiada

#1st way to create a list
numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#Create a list using a constructor
numbers2 = list((1,2,3,4,5))

print (numbers, fruits)

#index of a list
print (fruits[0])

#length of a list
print (len(fruits))

#append to the list (agrega uno nuevo al ultimo de la lista)
fruits.append('Mangos')

#remove from the list
fruits.remove('Grapes')

#insert to position
fruits.insert(2, 'Strawberries')
print(fruits)

#Remove from a position with pop
fruits.pop(2)
print(fruits)

#Remove the last element
fruits.pop()
print(fruits)

#reverse the list
fruits.reverse()
print(fruits)

#sort alphabetically
fruits.sort()
print(fruits)

fruits.push('Pepinos')
print(fruits)