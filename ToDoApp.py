

print('-----------------ToDo App---------------------')
print()


# collection of user input
list_collection = []

while len(list_collection)>=0:
    # Asking user Input
    user_List = input("What do you want to do ?: ").lower()

    list_collection.append(user_List)
    print("--------Your ToDo List---------")
    print()
    for items in list_collection:
        # print()
        print(f'◆ {items}')
    
    print()
    choice = input('Still want to add (Y/N): ').lower()
    

    if choice == 'n' :

        removing_list = input('Do you want to remove(Y/N)?: ').lower()

        if removing_list == "y":
            print("-----------------------------------------------")
            try:

                removed_item = input('Enter what you want to remove: ').lower()

                if removed_item:

                    list_collection.remove(removed_item)

                    print("--------Your ToDo List---------")
                    print()
                    for newList in list_collection:

                        print(f'◆ {newList}')
                break
            except ValueError:

                # When error established
                print()
                print('🚫 There is nothing to remove')
                break

        elif removing_list == 'n':
            print("Thanks for using our app \nDon't forget To Do them  😊")
            print()
            break

        else:
            print("😕 Entered wrong choice please try again ")
            print()
            break

    elif choice == 'y':

        continue

    else:

        print("Wrong choice try again 😕")
        print()


print("-----------------------------------------------------------------")






# Developer : Frans M Chokoe
# Date : 29 June 2025