#Excercise 1:

string_text = "Good morning"  
year_number = 2025
validation = True
list_years = [2023, 2024, 2025, 'hola' ]

#Excercise 2:

three_letters = string_text [0 : 3]
print(three_letters)

#Excercise 3:
one_element = list_years[0]
print(one_element)

#Excercise 4:
new_number = 10
year_number = year_number + new_number
print(year_number)

#Excercise 5:
last_element = list_years [-1]
print(last_element)

#Excercise 6:
names = 'harry,alex,susie,jared,gail,conner'
list_names = names.split(',')
print(list_names)

#Excercise 7:
one_string, space, two_string = string_text.partition (' ')
text_final = one_string.upper() + space +  two_string
print(text_final)

#Excercise 8:
string_text = "Good morning"
year_number = 2025
new_text = f'{string_text}, happy new year {year_number}'
print(new_text)

#Excercise 8:
greeting = "\"hello world\""
print(greeting)
              
#Excercise 9:
message = "Hace mucho tiempo no hablabamos, hoy solo quiero decirte hola"
message = message.replace('hola','adiós')
print(message)