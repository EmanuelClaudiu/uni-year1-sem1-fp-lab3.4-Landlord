#from problem_1.problem_1 import *
#from menu_functions.menu_functions import *

def get_id(apartment_dictionary):
    #gets the id of the apartment
    #input - the apartment dictionary
    #output - the apartment id
    return apartment_dictionary['apartment']

def get_water(apartment_dictionary):
    #gets the water bill from an apartment
    #input - the apartment dictionary
    #output - the water expenses from the apartment
    return apartment_dictionary['water']

def get_heating(apartment_dictionary):
    #gets the heating bill from an apartment
    #input - the apartment dictionary
    #output - the heating expenses from the apartment
    return apartment_dictionary['heating']

def get_electricity(apartment_dictionary):
    #gets the electricity bill from an apartment
    #input - the apartment dictionary
    #output - the electricity expenses from the apartment
    return apartment_dictionary['electricity']

def get_gas(apartment_dictionary):
    #gets the gas bill from an apartment
    #input - the apartment dictionary
    #output - the gas expenses from the apartment
    return apartment_dictionary['gas']

def get_other(apartment_dictionary):
    #gets the 'other' expenses from an apartment
    #input - the apartment dictionary
    #output - all other expenses from the apartment
    return apartment_dictionary['other']

####################################################                                                        PROBLEM 1

def add_to_transaction_type(transaction_dictionary, transaction_type, transaction_amount):
    #Determines which type of transaction takes place, and it adds the amount to that expense category
    if (transaction_type == 'water'):
        transaction_dictionary['water'] += transaction_amount
    if (transaction_type == 'heating'):
        transaction_dictionary['heating'] += transaction_amount
    if (transaction_type == 'electricity'):
        transaction_dictionary['electricity'] += transaction_amount
    if (transaction_type == 'gas'):
        transaction_dictionary['gas'] += transaction_amount
    if (transaction_type == 'other'):
        transaction_dictionary['other'] += transaction_amount

    return transaction_dictionary


def create_transaction(transaction_id, transaction_type, transaction_amount):
    '''
    Creates a new transaction as a dictionary object of the list
    '''
    new_transaction = {
        'apartment': 0,
        'water': 0,
        'heating': 0,
        'electricity': 0,
        'gas': 0,
        'other': 0
    }

    new_transaction = add_to_transaction_type(new_transaction, transaction_type, transaction_amount)
    new_transaction['apartment'] = transaction_id

    return new_transaction

def add_transaction(list_of_expenses, transaction_id, transaction_type, transaction_amount):
    '''
    Adds a new transaction
    list_of_expenses - the list of all transactions made
    transaction_id - the id of the apartment to which the transaction is being made
    transaction_type - the type of expense added to that apartment
    transaction_amount - the amount of money involved in the transaction
    '''
    new_transaction = create_transaction(transaction_id, transaction_type, transaction_amount)

    list_of_expenses.append(dict(new_transaction))
    return list_of_expenses

######################################################################################################################################################

#########################################                                                   PROBLEM 2


def set_erase_expenses(apartment_dictionary):
    # sets all expenses from an apartment to the value 0
    # input - the apartment dictionary
    # output - the new dictionary, with all the values except the id set to 0
    apartment_dictionary['water'] = 0
    apartment_dictionary['heating'] = 0
    apartment_dictionary['electricity'] = 0
    apartment_dictionary['gas'] = 0
    apartment_dictionary['other'] = 0

    return apartment_dictionary


def remove_expenses_from_apartment(list_of_expenses, apartment_id):
    # parses the list of apartments, and searches for the given id, then it erases all expenses from set apartment
    # input - the list of apartments, the id of the apartment to which we will erase the expenses from
    # output - the new modified apartment list
    for x in list_of_expenses:
        if get_id(x) == apartment_id:
            x = set_erase_expenses(x)

    return list_of_expenses


def remove_expenses_from_apartment_interval(list_of_expenses, apartment_id_1, apartment_id_2):
    # parses the list, and searches for the apartment id's that are in the interval, then it erases all expenses from those apartments
    # input - the list of apartments, the first id of the interval, the last id of the interval
    # output - the new modified apartment list
    for x in list_of_expenses:
        if get_id(x) >= apartment_id_1 and get_id(x) <= apartment_id_2:
            x = set_erase_expenses(x)

    return list_of_expenses


def remove_expense_type_from_apartments(list_of_expenses, expense_type):
    for x in list_of_expenses:
        x[expense_type] = 0

    return list_of_expenses


def replace_expense_type_from_apartment(list_of_expenses, apartment_id, expense_type, new_value):
    for x in list_of_expenses:
        if get_id(x) == apartment_id:
            x[expense_type] = new_value

    return list_of_expenses

######################################################################################################################################################

#############################################################                                                                   PROBLEM 3

def print_apartment(apartment_id, water, heating, electricity, gas, other):
    '''
    prints a string containing the informations about the expenses of an apartment
    '''
    print('Apartment', str(apartment_id) + ":", 'water -', str(water) + ';', 'heating -', str(heating) + ';', 'electricity -', str(electricity) + ';', 'gas -', str(gas) + ';', 'other -', str(other))

def show_all_expenses(list_of_expenses):
    #shows expenses from al apartments
    for x in list_of_expenses:
        apartment_id = get_id(x)
        water = get_water(x)
        heating = get_heating(x)
        electricity = get_electricity(x)
        gas = get_gas(x)
        other = get_other(x)

        print_apartment(apartment_id, water, heating, electricity, gas, other)
    print('\n')

def show_expenses_from_apartment(list_of_expenses, apartment):
    #shows expenses from the apartment of which the id is equal to the 'apartment' value from the parameter
    for x in list_of_expenses:
        if get_id(x) == apartment:
            apartment_id = get_id(x)
            water = get_water(x)
            heating = get_heating(x)
            electricity = get_electricity(x)
            gas = get_gas(x)
            other = get_other(x)

            print_apartment(apartment_id, water, heating, electricity, gas, other)
    print('\n')

def show_expenses_less_than_a_value(list_of_expenses, value):
    for x in list_of_expenses:
        apartment_id = get_id(x)
        water = get_water(x)
        heating = get_heating(x)
        electricity = get_electricity(x)
        gas = get_gas(x)
        other = get_other(x)

        s = water + heating + electricity + gas + other

        if s < value:
            print_apartment(apartment_id, water, heating, electricity, gas, other)
    print('\n')

def show_expenses_equal_to_a_value(list_of_expenses, value):
    for x in list_of_expenses:
        apartment_id = get_id(x)
        water = get_water(x)
        heating = get_heating(x)
        electricity = get_electricity(x)
        gas = get_gas(x)
        other = get_other(x)

        s = water + heating + electricity + gas + other

        if s == value:
            print_apartment(apartment_id, water, heating, electricity, gas, other)
    print('\n')

def show_expenses_more_than_a_value(list_of_expenses, value):
    for x in list_of_expenses:
        apartment_id = get_id(x)
        water = get_water(x)
        heating = get_heating(x)
        electricity = get_electricity(x)
        gas = get_gas(x)
        other = get_other(x)

        s = water + heating + electricity + gas + other

        if s > value:
            print_apartment(apartment_id, water, heating, electricity, gas, other)
    print('\n')

######################################################################################################################################################

############################################################                                                                        PROBLEM 4

def write_total_for_type(list_of_expenses, expense_type):
    # this function parses the list and adds the value from the type of expense to a sum
    s = 0

    for x in list_of_expenses:
        s += x[expense_type]

    print('\n')
    print(str(expense_type), "expenses add up to", str(s))
    print('\n')

def write_maximum_expense_for_apartment(list_of_expenses, apartment_id):
    '''
    parses the list of apartments, and at the apartment with set id, it prints the highest value expense
    :param list_of_expenses: the list of apartments
    :param apartment_id: the id of the apartment we are looking for
    :return: maximum value from expenses
    '''
    maximum_value = 0

    for x in list_of_expenses:
        if apartment_id == get_id(x):
            if get_water(x) >= maximum_value:
                maximum_value = get_water(x)
                maximum = 'water'
            if get_heating(x) >= maximum_value:
                maximum_value = get_heating(x)
                maximum = 'heating'
            if get_electricity(x) >= maximum_value:
                maximum_value = get_electricity(x)
                maximum = 'electricity'
            if get_gas(x) >= maximum_value:
                maximum_value = get_gas(x)
                maximum = 'gas'
            if get_other(x) >= maximum_value:
                maximum_value = get_other(x)
                maximum = 'other'
    print('\nThe maximum expense for apartment' , apartment_id , 'is', str(maximum) + ':' , str(maximum_value), '\n')

def sortSecond(val):
    return val[1]

def sort_apartments_by_total(list_of_expenses):
    '''
    this function parses the list of apartments expenses, then creates another list with objects containing just the apartment id and total expenses
    so that it would furthers sort the list, and then print it in ascending order of expenses
    :param list_of_expenses: the initial list of expenses
    '''
    list_of_apartments = []

    for x in list_of_expenses:
        s = get_water(x) + get_heating(x) + get_electricity(x) + get_gas(x) + get_other(x)
        vector_list = [get_id(x) , s]
        list_of_apartments.append(vector_list)

    list_of_apartments.sort(key = sortSecond)
    print('\n')

    i = 1
    for x in list_of_apartments:
        print(str(i) + '. Apartment' , x[0] , 'totaling' , x[1])
        i += 1
    print('\n')

def sort_expenses(list_of_expenses):
    '''
    it parses the list of expenses, makes a list with all of the expenses and respective values, then sorts it and prints it
    :param list_of_expenses: the initial list of apartments expenses
    '''
    water_total = 0
    heating_total = 0
    electricity_total = 0
    gas_total = 0
    other_total = 0

    for x in list_of_expenses:
        water_total += get_water(x)
        heating_total += get_heating(x)
        electricity_total += get_electricity(x)
        gas_total += get_gas(x)
        other_total += get_other(x)

    vector_expenses = [['water' , water_total] , ['heating' , heating_total] , ['electricity' , electricity_total] , ['gas' , gas_total] , ['other' , other_total]]
    vector_expenses.sort(key = sortSecond)
    print('\n')

    i = 1
    for x in vector_expenses:
        print(str(i)+'.' , x[0] + ':' , x[1])
        i += 1
    print('\n')

######################################################################################################################################################

###########################################################                                                                         PROBLEM 5

def filter_water(apartment_dict):
    apartment_dict['heating'] = 0
    apartment_dict['electricity'] = 0
    apartment_dict['gas'] = 0
    apartment_dict['other'] = 0

def filter_heating(apartment_dict):
    apartment_dict['water'] = 0
    apartment_dict['electricity'] = 0
    apartment_dict['gas'] = 0
    apartment_dict['other'] = 0

def filter_electricity(apartment_dict):
    apartment_dict['heating'] = 0
    apartment_dict['water'] = 0
    apartment_dict['gas'] = 0
    apartment_dict['other'] = 0

def filter_gas(apartment_dict):
    apartment_dict['heating'] = 0
    apartment_dict['electricity'] = 0
    apartment_dict['water'] = 0
    apartment_dict['other'] = 0

def filter_other(apartment_dict):
    apartment_dict['heating'] = 0
    apartment_dict['electricity'] = 0
    apartment_dict['gas'] = 0
    apartment_dict['water'] = 0

def filter_type(list_of_expenses , expense_type):
    for x in list_of_expenses:
        if expense_type == 'water':
            filter_water(x)
        elif expense_type == 'heating':
            filter_heating(x)
        elif expense_type == 'electricity':
            filter_electricity(x)
        elif expense_type == 'gas':
            filter_gas(x)
        elif expense_type == 'other':
            filter_other(x)

    return list_of_expenses

def filter_expenses_smaller_than_a_value(list_of_expenses , value):
    for x in list_of_expenses:
        for k , v in x.items():
            if x[k] > value:
                x[k] = 0

    return list_of_expenses

######################################################################################################################################################

############################################################                                                                        MENU FUNCTIONS

def show_menu():
    print('1. Add a new transaction to the list(add)')
    print('2. Modify an expense from the list(remove/replace)')
    print('3. Write the expenses having a set property(list)')
    print('4. Obtain different characteristics of the expenses')
    print('5. Filter expenses')
    print('x. Exit')

def menu_modify_expense():
    print('1. Remove expenses from an apartment(remove ...)')
    print('2. Remove expenses from an interval of apartments(remove ... to ...)')
    print('3. Remove a type of expense from all apartments(remove [type])')
    print('4. Replace an expense of a certain apartment(replace)')
    print('x. Exit')

def menu_show_expenses():
    print('1. Write the entire list of expenses ')
    print('2. Write all expenses for an apartment ')
    print('3. Write all apartments with total expenses adding less than a value ')
    print('4. Write all apartments with total expenses equal to a value ')
    print('5. Write all apartments with total expenses adding more than a value ')
    print('x. Exit')

def menu_characteristics():
    print('1.Write the total amount of expenses having a certain type ')
    print('2.Write the maximum amount per each expense type for an apartment by id ')
    print('3.Write the list of apartments sorted ascending by total amount of expenses ')
    print('4.Write the total amount of expenses for each type, sorted ascending by amount of money ')
    print('x. Exit')

def menu_filter():
    print('1.Keep only one type of expense')
    print('2.Keep only expenses having a value smaller than a set value')
    print('x. Exit')

#####################################################################################################################################################

#############################################################                                                              UI FUNCTIONS

def ui_add_transaction(list_of_expenses):
    #this function adds a new transaction to the list of apartments
    #input: list_of_expenses - the list of expenses from the apartment
    #output: the new modified list
    apartment_id = int(input('The id of the apartment: '))
    transaction_type = input('The type of the transaction expense: ')
    transaction_amount = int(input('The amount of money in the transaction: '))

    list_of_expenses = add_transaction(list_of_expenses, apartment_id, transaction_type, transaction_amount)
    print('\nNew expense added to the list!\n')

    return list_of_expenses

def ui_remove_expenses_from_apartment(list_of_expenses):
    apartment_id = int(input('The id of the apartment you would like to remove all expenses from: '))

    list_of_expenses = remove_expenses_from_apartment(list_of_expenses, apartment_id)
    print('\nAll expenses erased from the apartent\n')

    return list_of_expenses

def ui_remove_expenses_from_apartment_interval(list_of_expenses):
    apartment_id_1 = int(input('The id of the first apartment from the interval: '))
    apartment_id_2 = int(input('The id of the last apartment from the interval: '))

    list_of_expenses = remove_expenses_from_apartment_interval(list_of_expenses, apartment_id_1, apartment_id_2)
    print('\nAll expenses erased from the apartments in the interval\n')

    return list_of_expenses

def ui_remove_expense_type_from_apartments(list_of_expenses):
    expense_type = input('The type of expense you would like to remove from all apartments: ')

    list_of_expenses = remove_expense_type_from_apartments(list_of_expenses, expense_type)
    print ('\n All ', expense_type, 'expenses were removed from all apartments\n')

    return list_of_expenses

def ui_replace_expense_type_from_apartment(list_of_expenses):
    apartment_id = int(input('The id of the apartment: '))
    expense_type = input('The type of the expense: ')
    new_value = int(input('The new value you would like to set '))

    list_of_expenses = replace_expense_type_from_apartment(list_of_expenses,apartment_id, expense_type, new_value)
    print('\nExpense modified\n')

    return list_of_expenses

def ui_show_expenses_from_apartment(list_of_expenses):
    apartment = int(input('The id of the apartment: '))

    show_expenses_from_apartment(list_of_expenses, apartment)

def ui_show_expenses_less_than_a_value(list_of_expenses):
    value = int(input('The value: '))

    show_expenses_less_than_a_value(list_of_expenses, value)

def ui_show_expenses_equal_to_a_value(list_of_expenses):
    value = int(input('The value: '))

def ui_write_total_for_type(list_of_expenses):
    expense_type = input('The type of expense: ')

    write_total_for_type(list_of_expenses, expense_type)

def ui_write_maximum_expense_for_apartment(list_of_expenses):
    apartment_id = int(input('The id of the apartment: '))

    write_maximum_expense_for_apartment(list_of_expenses, apartment_id)

def ui_filter_type(list_of_expenses):
    expense_type = input("The type of expense you would like to filter: ")

    list_of_expenses = filter_type(list_of_expenses , expense_type)

    print('\nFilter successful. Only kept' , expense_type , 'expenses\n')

    return list_of_expenses

def ui_filter_expenses_smaller_than_a_value(list_of_expenses):
    value = int(input('The maximum value: '))

    list_of_expenses = filter_expenses_smaller_than_a_value(list_of_expenses, value)

    print('\nFilter successful. All values over' , value , 'erased\n')

    return list_of_expenses

#####################################################################################################################################################

###############################################################                                                             TEST FUNCTIONS

def test_add_transaction():
    list_of_expenses = []
    add_transaction(list_of_expenses , 1 , 'water' , 100)
    apartment = list_of_expenses[0]
    assert(apartment['apartment'] == 1)
    assert(apartment['water'] == 100)

test_add_transaction()

def test_remove_expenses_from_apartment():
    list_of_expenses = []
    add_transaction(list_of_expenses, 1, 'water', 100)
    replace_expense_type_from_apartment(list_of_expenses, 1, 'heating', 100)
    replace_expense_type_from_apartment(list_of_expenses, 1, 'electricity', 50)
    remove_expenses_from_apartment(list_of_expenses, 1)
    apartment = list_of_expenses[0]
    assert(apartment['water'] == 0)
    assert(apartment['heating'] == 0)
    assert(apartment['electricity'] == 0)

test_remove_expenses_from_apartment()

def test_remove_expenses_from_apartment_interval():
    list_of_expenses = []
    add_transaction(list_of_expenses, 1, 'water', 100)
    add_transaction(list_of_expenses, 2, 'heating', 50)
    add_transaction(list_of_expenses, 3, 'electricity', 200)
    remove_expenses_from_apartment_interval(list_of_expenses, 1, 3)
    apartment = list_of_expenses[0]
    assert (apartment['water'] == 0)
    apartment = list_of_expenses[1]
    assert (apartment['heating'] == 0)
    apartment = list_of_expenses[2]
    assert (apartment['electricity'] == 0)

test_remove_expenses_from_apartment_interval()

#####################################################################################################################################################

def create_initial_list(list_of_expenses):
    dictionary_1 = {'apartment': 1 , 'water': 100 , 'heating': 25 , 'electricity': 40 , 'gas': 24 , 'other': 10}
    dictionary_2 = {'apartment': 2, 'water': 50, 'heating': 235, 'electricity': 420, 'gas': 21, 'other': 13}
    dictionary_3 = {'apartment': 3, 'water': 500, 'heating': 0, 'electricity': 90, 'gas': 71, 'other': 24}
    dictionary_4 = {'apartment': 4, 'water': 400, 'heating': 10, 'electricity': 190, 'gas': 0, 'other': 0}
    dictionary_5 = {'apartment': 5, 'water':10 , 'heating': 20, 'electricity': 70, 'gas': 21, 'other': 200}
    dictionary_6 = {'apartment': 6, 'water': 100, 'heating': 54, 'electricity': 200, 'gas': 11, 'other': 10}
    dictionary_7 = {'apartment': 7, 'water': 0, 'heating': 0, 'electricity': 0, 'gas': 0, 'other': 0}
    dictionary_8 = {'apartment': 8, 'water': 10, 'heating': 10, 'electricity': 10, 'gas': 10, 'other': 10}
    dictionary_9 = {'apartment': 9, 'water': 69, 'heating': 69, 'electricity': 69, 'gas': 69, 'other': 69}
    dictionary_10 = {'apartment': 10, 'water': 420, 'heating': 420, 'electricity': 420, 'gas': 420, 'other': 420}
    list_of_expenses.append(dict(dictionary_1))
    list_of_expenses.append(dict(dictionary_2))
    list_of_expenses.append(dict(dictionary_3))
    list_of_expenses.append(dict(dictionary_4))
    list_of_expenses.append(dict(dictionary_5))
    list_of_expenses.append(dict(dictionary_6))
    list_of_expenses.append(dict(dictionary_7))
    list_of_expenses.append(dict(dictionary_8))
    list_of_expenses.append(dict(dictionary_9))
    list_of_expenses.append(dict(dictionary_10))

    return list_of_expenses

def check_validity(choice , valid_list):
    while True:
        ok = 1
        for x in valid_list:
            if x == choice:
                ok = 0
        if ok == 1:
            print('\nInvalid choice!\n')
            choice = input('Re-enter your choice: ')
        else:
            break
    return choice

def main():
    list_of_expenses = []

    list_of_expenses = create_initial_list(list_of_expenses)
    
    while True:
        show_menu()
        choice = input("\nYour choice: ")

        choice = check_validity(choice , ['1','2','3','4','5'])

        if choice == '1':
            list_of_expenses = ui_add_transaction(list_of_expenses)

        elif choice == '2':
            menu_modify_expense()
            choice_2 = input("\nYour choice: ")

            choice_2 = check_validity(choice_2 , ['1','2','3','4','x'])

            if choice_2 == '1':
                list_of_expenses = ui_remove_expenses_from_apartment(list_of_expenses)
            elif choice_2 == '2':
                list_of_expenses = ui_remove_expenses_from_apartment_interval(list_of_expenses)
            elif choice_2 == '3':
                list_of_expenses = ui_remove_expense_type_from_apartments(list_of_expenses)
            elif choice_2 == '4':
                list_of_expenses = ui_replace_expense_type_from_apartment(list_of_expenses)
            elif choice == 'x':
                break
        
        elif choice == '3':
            menu_show_expenses()
            choice_3 = input("\nYour choice: ")

            choice_3 = check_validity(choice_3 , ['1','2','3','4','5','x'])

            if choice_3 == '1':
                show_all_expenses(list_of_expenses)
            if choice_3 == '2':
                ui_show_expenses_from_apartment(list_of_expenses)
            if choice_3 == '3':
                ui_show_expenses_less_than_a_value(list_of_expenses)
            if choice_3 == '4':
                ui_show_expenses_equal_to_a_value(list_of_expenses)
            if choice_3 == '5':
                ui_show_expenses_more_than_a_value(list_of_expenses)
            if choice_3 == 'x':
                break
        
        elif choice == '4':
            menu_characteristics()
            choice_4 = input("\nYour choice: ")

            choice_4 = check_validity(choice_4, ['1', '2', '3', '4', 'x'])

            if choice_4 == '1':
                ui_write_total_for_type(list_of_expenses)
            if choice_4 == '2':
                ui_write_maximum_expense_for_apartment(list_of_expenses)
            if choice_4 == '3':
                sort_apartments_by_total(list_of_expenses)
            if choice_4 == '4':
                sort_expenses(list_of_expenses)
            if choice_4 == 'x':
                break

        elif choice == '5':
            menu_filter()
            choice_5 = input("\nYour choice: ")

            choice_5 = check_validity(choice_5 , ['1','2','x'])

            if choice_5 == '1':
                list_of_expenses = ui_filter_type(list_of_expenses)
            if choice_5 == '2':
                list_of_expenses = ui_filter_expenses_smaller_than_a_value(list_of_expenses)
            if choice_5 == 'x':
                break
main()