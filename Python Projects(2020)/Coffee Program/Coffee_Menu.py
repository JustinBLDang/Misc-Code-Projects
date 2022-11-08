import add_coffee_record, delete_coffee_record, modify_coffee_records, search_coffee_records, show_coffee_records, sys

def main():
    while True:
        print('\nSmells Good Coffee Inventory Menu'
              '\n1. Add a coffee record'
              '\n2. Delete a coffee record'
              '\n3. Modify a coffee record'
              '\n4. Search for a coffee record'
              '\n5. Show all coffee records', sep= '')
        USERINPUT = int(input('Enter a task number you would like to execute:'))
        if USERINPUT == 1:
            add_coffee_record.add_coffee()
        elif USERINPUT == 2:
            delete_coffee_record.del_coffee()
        if USERINPUT == 3:
            modify_coffee_records.mod_coffee()
        elif USERINPUT == 4:
            search_coffee_records.search()
        if USERINPUT == 5:
            show_coffee_records.show()
main()
              
