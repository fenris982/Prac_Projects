
##############################################################################################
###                                                                                        ###
###   /$$$$$$  /$$$$$$$$ /$$$$$$$        /$$      /$$                 /$$       /$$$$$$$   ###
###  /$$__  $$| $$_____/| $$__  $$      | $$$    /$$$                | $$      | $$____/   ###
### | $$  \__/| $$      | $$  \ $$      | $$$$  /$$$$  /$$$$$$   /$$$$$$$      | $$        ###
### | $$      | $$$$$   | $$$$$$$/      | $$ $$/$$ $$ /$$__  $$ /$$__  $$      | $$$$$$$   ###
### | $$      | $$__/   | $$____/       | $$  $$$| $$| $$  \ $$| $$  | $$      |_____  $$  ###
### | $$    $$| $$      | $$            | $$\  $ | $$| $$  | $$| $$  | $$       /$$  \ $$  ###
### |  $$$$$$/| $$      | $$            | $$ \/  | $$|  $$$$$$/|  $$$$$$$      |  $$$$$$/  ###
###  \______/ |__/      |__/            |__/     |__/ \______/  \_______/       \______/   ###
###                                                                                        ###                                                                                     
##############################################################################################                                                                                     

##########################################                                                                                     
###  CFP Module 5 Bringing it Together ###
##########################################
###     Task Data - DO NOT EDIT!!!     ###
##########################################

names = ['Theodora', 'Poppy', 'Crispin', 'Peregrine', 'Imogen', 'Arabella', 'Barnaby', 'Hamish', 'Alistair', 'Elowen']
numbers_ints = [5, 17, 9, 8, 5, 12, 4, 5, 6, 3, 15, 2, 11, 7, 4, 5, 3, 5]
numbers_floats = [1.56, 73.40, 23.55, 12.34, 3.14, 52.84, 9.00, 8.32, 1.11, 0.90]
characters = "fhgcxywsjdbvaljkbvjlntrbinrtibaerpuibvaiornvrknvjarehnbibrtnunroainbijnbhentbuaneribunareyubreunvrinvauyirebvybvunvoinrtbuntrsbuntarubnaubntubnaerubnareubnatunbvejrkbngkejanbvfjkavfuhvaiubvtbvaoertyvjafjfbvtvtapgatpvjjvfpvirtevvyfjkfbvnaoeivrnbvaeuprvrebuaebvjfvjifdureiu"
fruity_dict =  {1 : "Apple",
            2 : "Banana",
            3 : "Orange",
            4 : "Mango",
            5 : "Watermelon"
            }
job_tuple = ("Police", "Fireman", "Teacher", "Doctor")
setlist = ['Ford Mustang', 'Honda Civic', 'Toyota Corolla','Honda Civic', 'BMW 3 Series', 'Audi A4', 'Mercedes-Benz C-Class', 'Chevrolet Camaro', 'Toyota Corolla', 'Volkswagen Golf', 'Subaru Outback', 'Audi A4']

#############################################
###     Task 1 - Assigning Variables      ###
### Assign the Variables "new_name1" to   ###
### value "Steve" and "new_name2" to the  ###
### name of your choice. Ensure you do not###
### use a name that is currently in the   ###
### "names" variable!                     ###
#############################################
###       Write your code below           ###
#############################################





#############################################
###     DO NOT EDIT BELOW THIS LINE       ###
#############################################

print("Task 1 Results")

def test_task_1():
    score = 0
    if 'new_name1' and 'new_name2' in globals():
        print("new_name1 and new_name2 are correctly assigned! Great Job!")
        score += 1
    else:
        print('The variables are not assigned correctly. Recheck the instructions and try again! You got this!')
    return score
       
test_task_1()

###############################################    
###     Task 2 - Creating f strings         ###
### Create an f string and assign it to     ###
### the variable "hello_friend". The        ###
### string is "hello 'x' this is 'y'. It    ###
### is nice to meet you." Replace x and y   ###
### with new_name1 and new_name2            ###
### DO NOT use the "string".format() method ### 
###############################################
###       Write your code below             ###
###############################################





#############################################
###     DO NOT EDIT BELOW THIS LINE       ###
#############################################

print("Task 2 Results")

def test_task_2():
    score = 0
    if 'hello_friend' in globals():
        print("hello_friend has been assigned! Good Job")
        score += 1
    else:
        print("You have not assigned the correct variable!")

    if hello_friend == f"hello {new_name1} this is {new_name2}. It is nice to meet you":
        print("You have correctly entered the f-string. Remember, you can make normal strings without the f at the start but it can be harder to format.")
        score += 1
    else:
        print("You have not entered the f-string correctly! Check the intructions again and check your spelling!") 
    return score

test_task_2()

###############################################
###     Task 3 - Arithmetic Functions       ###
### Using the numbers_ints variable at the  ###
### top of the script, complete the tasks   ###
### that are indicated in the comments below###
###############################################
###       Write your code below             ###
###############################################

#Create the sum of all the numbers and assign it to the variable below:

sum_of_ints = 

#Use the len function to get the average of numbers_ints and assign it to the variable below.

average_of_ints = 

#Sort the numbers to put them in numerical order. Lowest number first. Assign them to the variable below.

sorted_ints = 

#divide numbers_ints index 5 by index 13 and cast the result as an integer. Assign the calculation to the variable below.

divide_int =

#############################################
###     DO NOT EDIT BELOW THIS LINE       ###
#############################################

print("Task 3 Results")

def test_task_3():
    score = 0
    if sum_of_ints == 126:
        print("sum_of_ints correct!")
        score += 1
    else:
        print("sum_of_ints is incorrect!")

    if average_of_ints == 7.0:
        print("average_of_ints correct!")
        score += 1
    else:
        print("average_of_ints inorrect!")

    if sorted_ints == [2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 7, 8, 9, 11, 12, 15, 17]:
        print("sorted_ints correctly ordered!")
        score += 1
    else:
        print("The numbers are not in the correct order.")
        
    if divide_int == 1:
        print("You have correctly divided and cast the number! Good job!")
        score += 1
    else:
        print("You have not carried out the correct divide calculation. Try again!")
    return score

test_task_3()

###############################################
###     Task 4 - Working with lists         ###
### Using the names variable at the         ###
### top of the script, complete the tasks   ###
### that are indicated in the comments below###
###############################################
###       Write your code below             ###
###############################################

#slice the list at the first four names and assign it to the variable below.

first_four = 

#slice the list and get the last three names. HINT - You don't have to put a number on both sides of the : in a slice.

last_three = 

#Append the variable new_name1 to the list new_names.

new_names = names ###<<< DO NOT EDIT THIS LINE

#############################################
###     DO NOT EDIT BELOW THIS LINE       ###
#############################################

print("Task 4 Results")

def test_task_4():
    score = 0
    if first_four == ['Theodora', 'Poppy', 'Crispin', 'Peregrine']:
        print("You have correctly sliced the list and got the first four names. Good job!")
        score += 1
    else:
        print("You didn't slice the list correctly and get the first four names. Try again")

    if last_three == ['Hamish', 'Alistair', 'Elowen']:
        print("You have correctly sliced the list and got the last three names. Good job!")
        score += 1
    else:
        print("You didn't slice the list correctly and get the last three names. Try again")

    if new_names == ['Theodora', 'Poppy', 'Crispin', 'Peregrine', 'Imogen', 'Arabella', 'Barnaby', 'Hamish', 'Alistair', 'Elowen', 'Steve']:
        print("You have correctly appended the name. Good Job!")
        score += 1
    else:
        print("You have not appended the name to the list. Try again!")
    return score

test_task_4()

###############################################
###     Task 5 - Working with dicts         ###
### Using the fruity_dict at the            ###
### top of the script, complete the tasks   ###
### that are indicated in the comments below###
###############################################
###       Write your code below             ###
###############################################

### Create a list that returns values from the dictionary and assign it to the variable below. Hint - you need a FOR loop.

dict_values = 



### Add Cherry as the 6th fruit in the dictionary. Hint - Cherry is case sensitive!.



#############################################
###     DO NOT EDIT BELOW THIS LINE       ###
#############################################

print("Task 5 Results")

def test_task_5():
    score = 0
    if 'Apple' in dict_values and 'Banana' in dict_values and 'Orange' in dict_values and 'Mango' in dict_values and 'Watermelon' in dict_values:
        print("You have correctly extracted the fruit. Nom Nom")
        score += 1
    else:
        print("You have not extracted the fruit!")
        
    if "Cherry" in fruity_dict:
        print("You have added Cherry to your diet!")
        score += 1
    else:
        print("You have not added a Cherry to your diet. Try again.")
    return score
    
test_task_5()

###############################################
###     Task 6 - Iterating a string         ###
### Using the characters variable at the    ###
### top of the script, complete the tasks   ###
### that are indicated in the comments below###
###############################################
###       Write your code below             ###
###############################################

#Iterate through the string and count how many "p"'s are in the string. Assign the answer to the variable below.

char_count = 



#use a string method to remove all occurances of the letter "y". Hint -  The method you required starts with the letter "R" 

new_char_string = 

#############################################
###     DO NOT EDIT BELOW THIS LINE       ### 
#############################################

print("Task 6 Results") 

def test_task_6():
    score = 0
    if char_count == 5:
        print("You have counted all the \"p's\" correctly!")
        score += 1
    else:
        print("You have missed some \"P's\"! Try again!")

    if 'y' not in new_char_string:
        print("ou have successfull removed all the \" \"s!")
        score += 1
    else:
        print("There are still some Y's remaining! Try again!")
    return score

test_task_6()

###############################################
###     Task 7 - Sets and Lists!            ###
### Using the setlist list at the           ###
### top of the script, complete the task    ###
### that is indicated in the comments below ###
###############################################
###       Write your code below             ###
###############################################

#Cast the setlist as a set and then assign it to the variable below as a new list.

new_setlist = 

#############################################
###     DO NOT EDIT BELOW THIS LINE       ###
#############################################

print("Task 7 Results")

def test_task_7():
    score = 0
    if len(new_setlist) == 9:
        print("You have succesfullt got rid of all the duplicate cars! Good Job!")
        score += 1
    else:
        print("You seem to have missed something. Try again.")
    return score
    
test_task_7()

#############################################
###     DO NOT EDIT BELOW THIS LINE       ###
#############################################

def marking_scheme():
    mark_counter = 0
    mark_counter += test_task_1()
    mark_counter += test_task_2()
    mark_counter += test_task_3()
    mark_counter += test_task_4()
    mark_counter += test_task_5()
    mark_counter += test_task_6()
    mark_counter += test_task_7()
    print("You have scored ", mark_counter, "out of 14")

marking_scheme()