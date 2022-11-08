# name: Justin Dang
# Student ID: 1148267
# Homework 5, Problem Set 1

'''Reads the tea.txt file and them prints a report using dictionaries'''

def main():
    #Open tea.txt file
    tea_file = open('tea.txt', 'r')

    #variables used
    empty_list = []
    tea_info = 'filler value'
    total = []
    totals = []
    tea_names = []
    tea_totals_rows = []
    tea_totals_columns = []
    list = []
    
    #inputs txt data into a list
    while True:
        tea_info = tea_file.readline()
        if tea_info != '':
            tea_info = tea_info.rstrip('\n')
            x = tea_info.split(':')
            list.append(x)
        else:
            break
    tea_file.close()
    
    # stores names into a list
    for x in range(0, len(list)):
        tea_names.append(list[x][0])
        list[x].remove(list[x][0])

    #stores total of rows into a list
    for x in range(0, len(list)):
        nmbr = 0
        for a in range(0 , len(list[x])):
            nmbr += float(list[x][a])
        tea_totals_rows.append(nmbr)
        
    #stores total of columns into a list
    for x in range(0, len(list)):
        total.append(float(format(float(list[x][0]), '.2f')))
    total = sum(total)
    tea_totals_columns.append(total)
    total = empty_list
    for x in range(0, len(list)):
        total.append(float(format(float(list[x][1]), '.2f')))
    total = sum(total)        
    tea_totals_columns.append(total)
    total = empty_list
    for x in range(0, len(list)):
        total.append(float(format(float(list[x][2]), '.2f')))
    total = sum(total)
    tea_totals_columns.append(total)
    total = empty_list
    for x in range(0, len(totals)):
        totals[x] = sum(totals[x])
    
    #converts all strings in list to float
    for x in range(0, len(list)):
        for a in range(0, len(list[x])):
            list[x][a] = float(list[x][a])
    
    #converts list into a dictionary
    tea_dict = {tea_names[x]:list[x] for x in range(0, len(tea_names))}

    #output
    print("{0:<18}{1:>12}{2:>14}{3:>16}{4:>18}".format("Ceylon", tea_dict["Ceylon"][0], tea_dict["Ceylon"][1], tea_dict["Ceylon"][2], tea_totals_rows[2]))
    print("{0:<18}{1:>12}{2:>14}{3:>16}{4:>18}".format("Earl Grey", tea_dict["Earl Grey"][0], tea_dict["Earl Grey"][1], tea_dict["Earl Grey"][2], tea_totals_rows[1]))
    print("{0:<18}{1:>12}{2:>14}{3:>16}{4:>18}".format("Green Tea", tea_dict["Green Tea"][0], tea_dict["Green Tea"][1], tea_dict["Green Tea"][2], tea_totals_rows[0]))
    print("{0:<18}{1:>12}{2:>14}{3:>16}{4:>18}".format("Jasmine", tea_dict["Jasmine"][0], tea_dict["Jasmine"][1], tea_dict["Jasmine"][2], tea_totals_rows[3]))
    print("{0:<18}{1:>12}{2:>14}{3:>16}{4:>18}".format("Mint Tea", tea_dict["Mint Tea"][0], tea_dict["Mint Tea"][1], tea_dict["Mint Tea"][2], tea_totals_rows[4]))
    print("                  {0:>12}{1:>14}{2:>16}".format(tea_totals_columns[0], tea_totals_columns[1], tea_totals_columns[2]))
    
################################################################main()

#Output with test case
##
##Test case 1.
##
##Ceylon                  6700.1       5012.45          6011.0          17723.55
##Earl Grey             10225.25        9025.0          9505.0          28755.25
##Green Tea               8580.0       7201.25          8900.0          24681.25
##Jasmine                9285.15        8276.1          8705.0          26266.25
##Mint Tea               7901.25        4267.0          7056.5          19224.75
##                      42691.75       33781.8         73959.3

main()

        

                
        
