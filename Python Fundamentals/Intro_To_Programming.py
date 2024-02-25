# ----- Arithmetic and Variables -----

print("Hello, world!")
print("How much second in a year ?")

days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year
print("Total sec in a year :", total_secs) #Total sec in a year : 31536000


# ----- Functions -----

def add_three(input_var1, input_var2, or0inputvar):
    output_var = input_var1 + input_var2 / or0inputvar
    return output_var


# ----- Data Types -----

print(type(days_per_year)) #<class 'int'>
almost_pi = 3.141592653589793238462643383279502884197169399375105820974944
rounded_pi = round(almost_pi, 2)
print(rounded_pi, type(rounded_pi)) #3.14 <class 'float'>

michel = True
print(type(michel)) #<class 'bool'>

isit = 1 < 2
print(isit, type(isit)) #True <class 'bool'>

isitstill = not isit
print(isitstill) #False

string = "abc"
new_string = string * 3 #Cannot multiply by a float
print(new_string) #abcabcabc

pi_integer = int(almost_pi)
print(pi_integer) #3

whathappen = pi_integer * False
print(whathappen) #Multiply by True and nothing changes, multiply by false and you'll get 0 or "" for string

print(False + True) # 1, True = 1, False = 0

solid_gold = False
solid_gold_price, basic_price, costengravement = 100, 50, 5
engravement = "jeanmichel<3"

price = solid_gold * (solid_gold_price + costengravement * len(engravement)) + (not solid_gold) * (basic_price + costengravement * len(engravement))
print(price)

#----- Conditions and Conditional Statements -----

if 1 <= pi_integer <= 3:
    print("coucou") # I don't need much in this chapter, I know theses shit

# ----- Intro to List -----
liste = []
print(liste[:3]) # First 3
print(liste[-2:]) # Last 2
liste.remove("michel") #remove "michel"
liste.append("michel") #add "michel"
print(min(liste), max(liste)) #print the minimal and maximal value
print(sum(liste)) # add everything in the list
print(sum(liste[:5])/5) # sum of the five first and divide it by 5

test_ratings = [1, 2, 3, 4, 5]
test_liked = [i>=4 for i in test_ratings] #False False False True True
