# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Harrison"
print("Hello", name)	# with a comma
print( "Hello " + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name2 = 42
print( "Hello", name2 )	# with a comma
print( "Hello " + str(name2) )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I love to eat {} and {}!".format(fave_food1, fave_food2) ) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}!") # with an f string

# Bouns
print("Hello my name is %s, and I love to eat %d peices of %s and %s!" % (name, name2, fave_food1, fave_food2)) 

print("Hello my name is {}, and I love to eat {} peices of {} and {}!".format(name, str(name2), fave_food1, fave_food2)) 

print(f"Hello my name is {name}, and I love to eat {str(name2)} peices of {fave_food1} and {fave_food2}!")

#==========================================
# what I have found is that you          ||
# can not combine diffrent methods       ||
# into one string. you must have one     ||
# consistant method for it to exicute    ||
# properly                               ||
#==========================================