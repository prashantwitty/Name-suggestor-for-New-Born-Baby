import pandas as pd #importing pandas to read the dateset as dataframe
dataset = pd.read_excel('names.xlsx') #reading the dataset
#logic start Custom Switch case
dict_origin = {'c': '_christian', 'h': '_hindu', 'm': '_muslim'}
dict_gender = {'m': 'Male', 'f': 'Female'}
string = '''enter origin:
                    1.c for christian
                    2.h for hindu
                    3.m for muslim\n'''

gender,origin = input('enter gender : \n 1.m for male \n 2.f for female\n'), input(string) 
category = dict_gender[gender] + dict_origin[origin] #generating the column name of the dataset as per user choice

initials = input('Enter the initial letter/s of your child\'s name\n')
wcount=int(len(initials))
required_suggestions = int(input('How much suggestion you want?\n'))

names = [] #for storing the required names
count = 0 #intializing the counter to keep track of suggestion no.s

for name in dataset[category]: #reading names from dataset onebyone
    if name[:wcount] == initials: #matching the initials of name of user's choice
        names.append(name)
        count+=1
    if count == required_suggestions:
        break

print('Your {0} names are : '.format(required_suggestions)) #printing the required names

for name in names:
    print(name)
