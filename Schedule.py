import ast  #--literal_eval -- to evaluate the string as a python expression.

Action = input("*Choose: load, add, show, save, exit \nChoose from the list:\n")

list = ['load', 'add', 'show', 'save', 'exit'] #choice list 

Text = "" # text to save -- used in 'Save' section

Day = {
    'Sunday':{
        "start time":[],"end time" :[],"plan":[]
     },
    'Monday':{
        "start time":[],"end time" :[],"plan":[]
    }, 
    'Tuesday':{
        "start time":[],"end time" :[],"plan":[]
    },
    'Wednesday':{
        "start time":[],"end time" :[],"plan":[]
    },
    'Thursday':{
        "start time":[],"end time" :[],"plan":[]
    },
    'Friday':{
        "start time":[],"end time" :[],"plan":[]
    },
    'Saturday':{
        "start time":[],"end time" :[],"plan":[]
    }
}

while (Action in list):

#----------------Add-----------
    while (Action=="add"):
        day = input("Which day? (First letter should be capital.) \n")

        if day not in Day:
            print("Error: 'Incorrect Format !'\nPlease re-enter the day in correct format like 'Sunday'. \n")
        
        else:

            Start_time = input('Start-time? Ex. 12:30.\n')
            Day[day]["start time"].append(Start_time)

            End_time = input('End-Time? Ex. 12:30.\n')
            Day[day]["end time"].append(End_time)

            Plan_ = input('What is the plan?\n')
            Day[day]["plan"].append(Plan_)

        Action = input("*Choose: load, add, show, save, exit \nChoose from the list:\n")

#---------Show-----------
    while (Action=="show"):

        choice = input("Which Day? \n")

        if choice not in Day:
            print("Error: 'Incorrect Format !'\nPlease re-enter the day in correct format like 'Sunday'. \n")
        
        else:
            
            S_list = Day[choice]["start time"]
            E_list = Day[choice]["end time"]
            P_list = Day[choice]["plan"]

            if len(S_list) == 0:
                print("You have no plans for" + choice + '.')

            else:
                for i in range (len(S_list)):
                    print(str(S_list[i]) + '-'+ str(E_list[i]) + ' ' + str(P_list[i]))

        Action = input("*Choose: load, add, show, save, exit \nChoose from the list:\n")

#-------------Save-----------
    while (Action=="save"):
    # Two files will be saved, one with good text format for text editor and another with dictionary format for loading purpose.

        file_text = input("File-Name? \n") # text format
        file_dict = file_text.replace('.txt','dict.txt') # for loading purpose

        f = open(file_text, 'w')

        fd = open(file_dict, 'w')
        fd.write(str(Day))
        fd.close

        #---For text format
        for x in Day.keys():

            S_list = Day[x]["start time"]
            E_list = Day[x]["end time"]
            P_list = Day[x]["plan"]
            Text = Text + '\n\n' + x + ':'

            if len(S_list) == 0:
                Text = Text + "\n" + "You have no plans for " + x + '.'

            else:
                for i in range (len(S_list)):
                    Text = Text + "\n" + str(S_list[i]) + ' - '+ str(E_list[i]) + ' ' + str(P_list[i])   
        
        f.write(Text.lstrip())
        f.close()
        print("Your plan file has saved successfully.")

        Action = input("*Choose: load, add, show, save, exit \nChoose from the list:\n")

#-----------Load---------------
    while (Action=="load"):
        file_name = input("File-Name? \nNote: Please enter the file name that you saved before with extention Ex. 'ACITplans.txt'\n").replace('.txt','dict.txt')
        fl = open(file_name, 'r')
        Day = ast.literal_eval(fl.read()) #Convert the String to Dictionary
        print("The saved plan has loaded successfully.")

        Action = input("*Choose: load, add, show, save, exit \nChoose from the list:\n")

#-------------Exit--------------    
    while (Action=="exit"):
        print("Thank you, have a nice day.")
        raise SystemExit

#Simple Plan Tracking System
