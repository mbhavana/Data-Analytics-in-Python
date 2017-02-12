'''
PROJECT  : DRUG TREATMENT ANALYSIS

****************

Author : Bhavana Maradani

Source of our CSV file is :

http://vincentarelbundock.github.io/Rdatasets/datasets.html

Project Description : Our Data set is about a Drug Treatment conducted on white's and Non-white's who used Heroin, Cocain, Heroin & Cocain, Drug IV

                      3 months prior to treatment and their treatment details. The dataset contains type of drug used white's and Non-white's .

                      Number of treatments , treatment randomisation and length of treatment and time taken for drug to relapse from the date of treatment

                      is given . The dataset also shows if the person has returned to drug after the treatment or not.

                      Questions:

                      1. find Number of people in the age groups(below 31 years and above 31years) belonging to two race groups who used Various drugs.

                         and display them using bar chart


                      2. find Average Beck Deppresion of people different drugs and find out whose beck deppresion is high and display the output in bar chart.")

                      3. find percentage of people who returned to drugs after treatment and who din't return to drugs. Display the output in pi Chart too.")

                      4. find Percentage of people whose duration for drug relapse is more than 1 year classified by the drug intake.")

                      5. find out length of treatament and beck depression of people under different age groups.")

                      6. find out mean and standard deviation of age groups. Histogram will be displayed according to the input given by the user."



Dataset Fields :

                Age : Age of the person when he or she admitted in the hospital

                BECK : It is the beck depression score for people depending on type of drud they are addicted to.

                HC : It is the drug taken by the people. The number in the cells indicate the following

                     1. Heroin and Cocain

                     2. Heroin

                     3. Cocaine

                     4. Neiher of them

               Drug IV: The number in the cells indicate the following

                      1. Never took

                      2. Previously have taken DRUG IV

                      3. Recently have take that drug

               NDT : Number of drug treatments

               race : Race group.

                      1. White's

                      2. Non- White's

               Treat : Treatment randomisation. The number in the cells indicate the following

                       1. Long

                       2. Short

               Len.T : Length of treatment in days from the date of admission

               Time  : Indicate number days taken for the drug to relapse from the date of admission

               censor : Indicates if the people returned to drugs again after the treatment

                       1. Indicates that they have returned

                       2. They didn't return



# Known bugs = None

# Graphs are displayed for the questions 1,2,3 and 6.

'''
from decimal import *
import csv

# Reading the CSV file

def readData():

    readFile = open("uis.csv","r")

    Linereader = csv.reader(readFile)

    list1 = []

    for row in Linereader:

        list1.append(row)

    readFile.close()

    

    return list1

#Lists of people who used (Heroin & Cocaine), (Only Heroin), (Only Cocaine) , (Neither of them) and (Drug IV) 3 months before to treament 

def druglist(file):

    Heroin_Cocaine = [] 
    drugIV = []
    age_list = []
    race_list = []
    time_relapse = []
    length_treatment = []
    number_treatments = []
    censor_list = []
    numberOfColums = 0
    beck_list = [] 
    Treat = []    

    for i in range(1, len(file)):       

        hc = int(file[i][4])      

        iv = int(file[i][5])

        age = int(file[i][2])

        race = int(file[i][7])

        length = int(file[i][10])

        time = int(file[i][11])

        numtreat = int(file[i][6])

        censor = int(file[i][12])

        beck = float(file[i][3])

        treat = int(file[i][8])        

        Heroin_Cocaine.append(hc)

        drugIV.append(iv)

        age_list.append(age)

        race_list.append(race)

        time_relapse.append(time)
        length_treatment.append(length)
        number_treatments.append(numtreat)       

        censor_list.append(censor)
        numberOfColums = numberOfColums + 1

        beck_list.append(beck)

        Treat.append(treat)
        
    return age_list, Heroin_Cocaine, race_list, drugIV, time_relapse, Treat, length_treatment, number_treatments,censor_list,numberOfColums,beck_list

# white's and Non-white's and their intake of drugs

def drugUse(age_list,Heroin_Cocaine, race_list, drugIV, numberOfColums):

    count_hc_b_w = 0

    count_h_b_w = 0

    count_c_b_w = 0

    count_n_b_w = 0

    count_hc_a_w = 0

    count_h_a_w = 0

    count_c_a_w = 0

    count_n_a_w = 0

    count_n_r_n = 0

    count_n_r_b = 0

    count_b_r_w = 0

    count_hc_b_n = 0

    count_h_b_n = 0

    count_c_b_n = 0

    count_n_b_n = 0

    count_hc_a_n = 0

    count_h_a_n = 0

    count_c_a_n = 0

    count_n_a_n = 0

    count_n_r_w = 0

    # drugs used by people of age group 31years and below 

    for i in range(0, numberOfColums):

        if age_list[i] <= 31:

            

            if race_list[i] == 0:

                if Heroin_Cocaine[i] == 1:

                    count_hc_b_w += 1

                if Heroin_Cocaine[i] == 2:

                    count_h_b_w  += 1


                if Heroin_Cocaine[i] == 3:

                    count_c_b_w += 1 

                else:

                    count_n_b_w += 1

            else:

                if Heroin_Cocaine[i] == 1:

                    count_hc_b_n += 1

                if Heroin_Cocaine[i] == 2:

                    count_h_b_n  += 1

                if Heroin_Cocaine[i] == 3:

                    count_c_b_n += 1 

                else:

                    count_n_b_n += 1

       # drugs used by people of age group 32years and above 

    for i in range(0, numberOfColums):

        if age_list[i] > 31:

            if race_list[i] == 0:


               if Heroin_Cocaine[i] == 1:

                    count_hc_a_w += 1

               if Heroin_Cocaine[i] == 2:

                    count_h_a_w += 1

               if Heroin_Cocaine[i] == 3:

                    count_c_a_w += 1 

            else:

               if Heroin_Cocaine[i] == 1:
  
                    count_hc_a_n += 1

               if Heroin_Cocaine[i] == 2:

                    count_h_a_n += 1

               if Heroin_Cocaine[i] == 3:

                    count_c_a_n += 1 

    #people age above 31 who used drugIV

    for i in range(0,numberOfColums):

        if age_list[i] > 31:

            if race_list[i] == 0:



                if drugIV[i] == 2:

                    count_n_a_w += 1

                if drugIV[i] == 3:

                    count_n_r_w += 1



            else:

                if drugIV[i] == 2:

                    count_n_a_n += 1

                if drugIV[i] == 3:

                    count_n_r_n += 1

    for i in range (0, numberOfColums):

        if age_list[i] < 31:

            if race_list[i] == 0:

                 if drugIV[i] == 2:

                    count_n_b_w += 1

                 if drugIV[i] == 3:

                    count_b_r_w += 1



            else:

                if drugIV[i] == 2:

                    count_n_b_n += 1

                if drugIV[i] == 3:

                    count_n_r_b += 1

   # avg_hc_b_w = (sum_hc_b_w)/count_hc_b_w       

    print("*********  People who fall under age group of 20 - 31 years      ***********")

    print(" Race",' '*4,"Heroin&Cocaine",''*8,"Heroin only",''*7,"Cocaine only",''*7,"DrugIV previoly",''*8,"DrugIV Recently")

    print("---------------------------------------------------------------------------------------")

    

    print("Whites    :","{:<15} {:<15} {:<15} {:<12} {:<12}".format(count_hc_b_w,count_h_b_w,count_c_b_w,count_n_b_w,count_b_r_w ))

    print("Non Whites:","{:<15} {:<15} {:<15} {:<12} {:<12}".format(count_hc_b_n,count_h_b_n,count_c_b_n,count_n_b_n,count_n_r_b))



    print("\n")

    print("*********  People who fall under age group of 32years and above     ********")

    print(" Race",' '*4,"Heroin&Cocaine",''*6,"Heroin only",''*5,"Cocaine only",''*5,"DrugIV previoly",''*8,"DrugIV Recently")

    print("------------------------------------------------------------------------------------------")

    print("Whites    :","{:<15} {:<16} {:<15} {:<12} {:<12}".format(count_hc_a_w,count_h_a_w,count_c_a_w,count_n_a_w,count_n_r_w))

    print("Non Whites:","{:<15} {:<16} {:<15} {:<12} {:<12}".format(count_hc_a_n,count_h_a_n,count_c_a_n,count_n_a_n,count_n_r_n))

    print("\n")
  

# ************************ percentage of people(who used heroin, cocaine and both heroin & Cocaine)**********************************

# *************************          whose duration for drug relapse is more than 1year         *************************************
   

def PercentagePeople(Heroin_Cocaine, drugIV, time_relapse, Treat, number_treatments,numberOfColums):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    
    avg_hcTreat = []
    avg_hTreat = []
    avg_cTreat = []
    avg_ivTreat2 = []
    avg_ivTreat3 = []
    short1 = 0
    short2 = 0
    short3 = 0
    short4 = 0
    short5 = 0
    long1 = 0
    long2 = 0
    long3 = 0
    long4 = 0
    long5 = 0
    
    for i in range(numberOfColums):
    
        # people who consumed heroine and cocaine and time taken to relapse is more than 1 year
        if Heroin_Cocaine[i] == 1 and time_relapse[i] > 365 and Treat[i] == 0:
            avg_hcTreat.append(number_treatments[i])
            short1 += 1
            
            
            count1 += 1

        # people who consumed heroine and time taken to relapse is more than 1 year   
        if Heroin_Cocaine[i] == 2 and time_relapse[i] > 365 and Treat[i] == 0:
            
            avg_hTreat.append(number_treatments[i])
            short2 += 1
            
            count2 += 1
            
        # people who consumed cocaine and time taken to relapse is more than 1 year    
        if Heroin_Cocaine[i] == 3 and time_relapse[i] > 365 and Treat[i] == 0:
            
            avg_cTreat.append(number_treatments[i])
            short3 += 1
            count3 += 1

        #people who concumed drug iv previous
        if drugIV[i] == 2 and time_relapse[i] > 365 and Treat[i] == 0:
            
            avg_ivTreat2.append(number_treatments[i])
            short4 += 1
            count4 += 1
            
        #people who cunsumed drug iv recently    
        if drugIV[i] == 3 and time_relapse[i] > 365 and Treat[i] == 0:
            
            avg_ivTreat3.append(number_treatments[i])
            short5 += 1
            count5 += 1   

            
    percentage_both = float(float(count1)/float(numberOfColums))
    
    percentage_heroin = float(float(count2)/float(numberOfColums))
    
    percentage_cocaine = float(float(count3)/float(numberOfColums))
    
    percentage_drug2 = float(float(count4)/float(numberOfColums))
    
    percentage_drug3 = float(float(count5)/float(numberOfColums))
   
    #print("{:<13}{:<16}{:<15}".format(percentage_both,percentage_heroin,percentage_cocaine))
    print("")

    Average_HC = round(Mean(avg_hcTreat),0)
    Avegare_h = round(Mean(avg_hTreat),0)
    Avegare_c = round(Mean(avg_cTreat),0)
    Avegare_2 = round(Mean(avg_ivTreat2),0)
    Avegare_3 = round(Mean(avg_ivTreat3),0)
    
    print("\n Percentage of people who used various drugs whose time duration for drug to relapse is more than an year\n")
    print(" "*8,"Heroine&Cocaine",' '*5,"Heroin",' '*5,"Cocaine",' '*5,"DrugIV Previously"," "*5,"DrudIV recently")
    print(" "*8,"{:<20.2%}{:<20.2%}{:<20.2%}{:<20.2%}{:<15.2%}".format(percentage_both,percentage_heroin,percentage_cocaine,percentage_drug2,percentage_drug3))
    print("")
    
    # Treatment Randomisation is long
    for i in range(numberOfColums):

        # people who consumed heroine and cocaine and time taken to relapse is more than 1 year
        if Heroin_Cocaine[i] == 1 and time_relapse[i] > 365 and Treat[i] == 1:
            
            avg_hcTreat.append(number_treatments[i])
            long1 += 1
            
            
            count1 += 1

        # people who consumed heroine and time taken to relapse is more than 1 year   
        if Heroin_Cocaine[i] == 2 and time_relapse[i] > 365 and Treat[i] == 1:
            
            avg_hTreat.append(number_treatments[i])
            long2 += 1
            
            count2 += 1
            
        # people who consumed cocaine and time taken to relapse is more than 1 year    
        if Heroin_Cocaine[i] == 3 and time_relapse[i] > 365 and Treat[i] == 1:
            
            avg_cTreat.append(number_treatments[i])
            long3 += 1
            count3 += 1

        #people who concumed drug iv previous
        if drugIV[i] == 2 and time_relapse[i] > 365 and Treat[i] == 1:
            
            avg_ivTreat2.append(number_treatments[i])
            long4 += 1
            count4 += 1
            
        #people who cunsumed drug iv recently    
        if drugIV[i] == 3 and time_relapse[i] > 365 and Treat[i] == 1:
            
            avg_ivTreat3.append(number_treatments[i])
            long5 += 1
            count5 += 1   

    
    print(" Treatment",""*8,"--- ------ ------    Number of Treatments---- ----  ----------")
    print("Randomisation")
    print("   LONG    ","{:<18}{:<18}{:<18}{:<20}{:<15}".format(long1,long2,long3,long4,long5))
    print("   SHORT   ","{:<18}{:<18}{:<18}{:<20}{:<15}".format(short1,short2,short3,short4,short5))



def noDrugs(Heroin_Cocaine,drugIV,censor_list,numberOfColums):

    rec = []
    pre = []
    h = []
    hc = []
    c = []
    readFile = open("uis.csv","r")

    Linereader = csv.reader(readFile)

    notUsedPriorToTreatment = 0

    notUsedButReturned = 0

    notUsedanddidnotReturn = 0

    

    for i in range(numberOfColums):

        if Heroin_Cocaine[i] == 4 and drugIV[i] == 1:

            notUsedPriorToTreatment = notUsedPriorToTreatment + 1

            

        if Heroin_Cocaine[i]  == 4 and drugIV[i] == 1 and censor_list[i] == 1:

            notUsedButReturned = notUsedButReturned + 1

            

        if Heroin_Cocaine[i]  == 4 and drugIV[i] == 1 and censor_list[i] == 0:

            notUsedanddidnotReturn = notUsedanddidnotReturn + 1

            

    print("percentage of people who used none of the drugs (heroin,cocaine, drug IV) prior to treatment and ")

    print("\n 1. Returned to drugs later is      :",round((float(notUsedButReturned)/float(notUsedPriorToTreatment)) * 100,2),"%")

    print(" 2. Did not return to drugs later is:",round((float(notUsedanddidnotReturn)/float(notUsedPriorToTreatment)) * 100,2),"%")



    for i in range(numberOfColums):



        if Heroin_Cocaine[i] == 1 and censor_list[i] == 1:

            both = Heroin_Cocaine[i]

            hc.append(both)



        if Heroin_Cocaine[i] == 2 and censor_list[i] == 1:

            heroin = Heroin_Cocaine[i]

            h.append(heroin)



        if Heroin_Cocaine[i] == 3 and censor_list[i] == 1:

            cocaine = Heroin_Cocaine[i]

            c.append(cocaine)

        if drugIV[i] == 2 and censor_list[i] == 1:

            p = Heroin_Cocaine[i]

            pre.append(p)

        if drugIV[i] == 3 and censor_list[i] == 1:

            r = Heroin_Cocaine[i]

            rec.append(r)

    per_hc = float(sum(hc))/float(numberOfColums)

    per_h = float(sum(h))/float(numberOfColums)

    per_c = float(sum(c))/float(numberOfColums)

    per_pre = float(sum(pre))/float(numberOfColums)

    per_re = float(sum(rec))/float(numberOfColums)

    print("Event of Treatment lost to follow up as the people returned to drugs\n")

    print("---------------Percentage of people according to the drugs they used returned to drugs after treatment ------------\n")

    print("Heroine&Cocaine",' '*5,"Heroin",' '*5,"Cocaine",' '*5,"DrugIV Previously"," "*5,"DrudIV recently")

    print("  ","{:<18.2%}{:<18.2%}{:<18.2%}{:<20.2%}{:<15.2%}".format(per_hc,per_h,per_c,per_pre,per_re))  

def Mean( list_1):

    item_list =(list_1)

    Average =  (sum(item_list)) / float(len(item_list))

    return   Average

def drugsBeckdepress(Heroin_Cocaine,drugIV,numberOfColums,beck_list):

    notUsedPriorToTreatment = 0

    usedHeroin = 0

    userCocaine = 0

    usedbothCocaineHeroin = 0

    usedall = 0

    notUsedPriorToTreatmentBeckdepression = 0.0

    notUsedPriorToTreatment = 0

    usedHeroinBeckdepression = 0

    userCocaineBeckdepression = 0

    usedbothCocaineHeroinBeckdepression = 0

    usedallBeckdepression = 0.0

    

    for i in range(numberOfColums):

        

        if Heroin_Cocaine[i] == 4 and drugIV[i] == 1 :#None

            notUsedPriorToTreatment = notUsedPriorToTreatment + 1

            notUsedPriorToTreatmentBeckdepression = notUsedPriorToTreatmentBeckdepression + float(beck_list[i])

        if Heroin_Cocaine[i] == 2 :#Heroin

            usedHeroin = usedHeroin + 1

            usedHeroinBeckdepression = usedHeroinBeckdepression + float(beck_list[i])

            

        if Heroin_Cocaine[i] == 3 :#Cocaine

            userCocaine = userCocaine + 1

            userCocaineBeckdepression = userCocaineBeckdepression + float(beck_list[i])

            

        if Heroin_Cocaine[i] == 1 :#Both cocaine and Herion

            if drugIV[i] == 2:#all

                usedall = usedall + 1

                usedallBeckdepression = usedallBeckdepression + float(beck_list[i])

                

            else:

                usedbothCocaineHeroin = usedbothCocaineHeroin + 1

                usedbothCocaineHeroinBeckdepression = usedbothCocaineHeroinBeckdepression + float(beck_list[i])

    print("Average beck depression of people addicted neither to heroin,cocaine nor drug IV : ","%.2f" %(float(notUsedPriorToTreatmentBeckdepression)/float(notUsedPriorToTreatment)))

    print("Average beck depression of people addicted to Only cocaine : ","%.2f" %(float(userCocaineBeckdepression)/float(userCocaine)))

    print("Average beck depression of people addicted to Only heroin : ","%.2f" %(float(usedHeroinBeckdepression)/float(usedHeroin)))

    print("Average beck depression of people addicted to both heroin and cocaine : ","%.2f" %(float(usedbothCocaineHeroinBeckdepression)/float(usedbothCocaineHeroin)))

    print("Average beck depression of people addicted to both heroin,cocaine and IV : ","%.2f" %(float(usedallBeckdepression)/float(usedall)))

    averagesList = []


    averageDictonary = {}

    averageDictonary["%.2f" %(float(notUsedPriorToTreatmentBeckdepression)/float(notUsedPriorToTreatment))] = "None"

    averageDictonary["%.2f" %(float(userCocaineBeckdepression)/float(userCocaine))] =  "Cocaine"

    averageDictonary["%.2f" %(float(usedHeroinBeckdepression)/float(usedHeroin))] = "Heroin"

    averageDictonary["%.2f" %(float(usedbothCocaineHeroinBeckdepression)/float(usedbothCocaineHeroin))] = "Both Heroin and Cocaine"

    averageDictonary["%.2f" %(float(usedallBeckdepression)/float(usedall))] = "Herion , Cocaine and IV"

    

    averagesList.append("%.2f" %(float(notUsedPriorToTreatmentBeckdepression)/float(notUsedPriorToTreatment)))

    averagesList.append("%.2f" %(float(userCocaineBeckdepression)/float(userCocaine)))

    averagesList.append("%.2f" %(float(usedHeroinBeckdepression)/float(usedHeroin)))

    averagesList.append("%.2f" %(float(usedbothCocaineHeroinBeckdepression)/float(usedbothCocaineHeroin)))

    averagesList.append("%.2f" %(float(usedallBeckdepression)/float(usedall)))

    print("\nPeople who used ",averageDictonary[max(averagesList)]," has max beck depression of " ,max(averagesList)) 

# Average length of treatment for people in different age groups and their beck rapression

def agegroups(age_list,numberOfColums,beck_list,length_treatment):
    beckDepressionCount2030 = []

    count2030 = 0

    avg2030 = []

    beckDepressionCount4050 = []

    count4050 = 0

    avg4050 = []

    beckDepressionCount3040 = []

    count3040 = 0

    avg3040 = []

    beckDepressionCount5060 = []

    count5060 = 0

    avg5060 = []

    for i in range(numberOfColums):

        #People in age group of 20-29

        if int(age_list[i]) > 19 and int(age_list[i]) < 30:

            count2030 = count2030 + 1

            beckDepressionCount2030.append(beck_list[i])

            avg2030.append(length_treatment[i])
   

        #People in age group of 30-39

        if int(age_list[i]) > 39 and int(age_list[i]) < 50:

            count4050 = count4050 + 1

            beckDepressionCount4050.append(beck_list[i])

            avg4050.append(length_treatment[i])


         #People in age group of 40-49

        if int(age_list[i]) > 29 and int(age_list[i]) < 40:

            count3040 = count3040 + 1

            beckDepressionCount3040.append(beck_list[i])

            avg3040.append(length_treatment[i])

        #People in age group of 50-59

        if int(age_list[i]) > 49 and int(age_list[i]) < 60:

            count5060 = count5060 + 1

            beckDepressionCount5060.append(beck_list[i])

            avg5060.append(length_treatment[i])

    Average_length4 = round(sum(avg5060)/len(avg5060),0)

    Average_length1 = round(sum(avg2030)/len(avg2030),0)

    Average_length2 = round(sum(avg3040)/len(avg3040),0)

    Average_length3 = round(sum(avg4050)/len(avg4050),0)

    avg1 = round(sum(beckDepressionCount2030)/len(beckDepressionCount2030),2)

    avg2 = round(sum(beckDepressionCount3040)/len(beckDepressionCount3040),2)

    avg3 = round(sum(beckDepressionCount4050)/len(beckDepressionCount4050),2)

    avg4 = round(sum(beckDepressionCount5060)/len(beckDepressionCount5060),2)             

    print("Age Group",""*5,"Beck Depression",""*23,"Length of Treatments")

    print(" 20-29","       ","{:<25}{:<18}".format(avg1,Average_length1))

    print(" 30-39","       ","{:<25}{:<18}".format(avg2,Average_length2))

    print(" 40-49","       ","{:<25}{:<18}".format(avg3,Average_length3))

    print(" 50-59","       ","{:<25}{:<18}".format(avg4,Average_length4))

def meanStandaradDeviation(Heroin_Cocaine,numberOfColums,age_list):

    import math

    usedHeroin = 0

    userCocaine = 0

    usedBoth = 0

    usedHeroinsage = 0

    userCocainesage = 0

    userBothage = 0

    userCocainesage = 0

    userHeroineAverage = 0.0

    userCocaineAverage = 0.0

    userBothAverage = 0.0

    for i in range(numberOfColums):

        if Heroin_Cocaine[i] == 2 :#Heroin

            usedHeroin = usedHeroin + 1

            usedHeroinsage = usedHeroinsage + int(age_list[i])

            

        if Heroin_Cocaine[i] == 3 :#Cocaine

            userCocaine = userCocaine + 1

            userCocainesage = userCocainesage + int(age_list[i])

            

        if Heroin_Cocaine[i] == 1 :#Both cocaine and Herion

            usedBoth = usedBoth + 1

            userBothage = userBothage + int(age_list[i])

    

    print("Mean of people age who used Herion:", "%.2f" %(float(usedHeroinsage / usedHeroin)))

    print("Mean of people age who used Cocaine:", "%.2f" %(float(userCocainesage / userCocaine)))

    print("Mean of people age who used Herion and Cocaine:", "%.2f" %(float(userBothage / usedBoth)))

   

    userHeroineAverage = float(usedHeroinsage / usedHeroin)

    userCocaineAverage = float(userCocainesage / userCocaine)

    userBothAverage = float(userBothage / usedBoth)

    Herione = []

    Cocaine = []

    HeroineCocaine = []

    for i in range(numberOfColums):

        if Heroin_Cocaine[i] == 2 :#Heroin

            Herione.append(float(age_list[i]) - userHeroineAverage)

            

        if Heroin_Cocaine[i] == 3 :#Cocaine

            Cocaine.append(float(age_list[i]) - userCocaineAverage)

            

        if Heroin_Cocaine[i] == 1 :#Both cocaine and Herion

            HeroineCocaine.append(float(age_list[i]) - userBothAverage)

    HerioneSqr = []

    CocaineSqr = []

    bothSqr = []

    for i in range(numberOfColums):

        if Heroin_Cocaine[i] == 2 :#Heroin

            Herione.append(float(age_list[i]) * float(age_list[i]))

            

        if Heroin_Cocaine[i] == 3 :#Cocaine

            Cocaine.append(float(age_list[i]) * float(age_list[i]))

        if Heroin_Cocaine[i] == 1 :#Both cocaine and Herion

            HeroineCocaine.append(float(age_list[i]) * float(age_list[i]))

    sdHerione = math.sqrt(sum(Herione) / len(Herione) - 1)

    sdCocaine = math.sqrt(sum(Cocaine) / len(Cocaine) - 1)

    sdHerioneCocaine= math.sqrt(sum(HeroineCocaine) / len(HeroineCocaine) - 1)

    print("Standard deviation of people age who used Herione:","%.2f" %(float(sdHerione)))

    print("Standard deviation of people age who used Cocaine:","%.2f" %(float(sdCocaine)))

    print("Standard deviation of people age who used Herione and Cocaine:","%.2f" %(float(sdHerioneCocaine)))

    return float(usedHeroinsage / usedHeroin),float(sdHerione)

    

print("Dear User, Welcome to the Python program !!")

print("Please enter main() at the prompt to start the program.")

def main():


    inputfile = readData()

    age_list, Heroin_Cocaine, race_list, drugIV, time_relapse, Treat,length_treatment, number_treatments,censor_list,numberOfColums,beck_list = druglist(inputfile)

    while True:

        print()

        print("-------------------------------------------------------------------------------------------------------------------------------------------")

        print("\n Please Enter choices mentioned below to find the following. ")

        print(" Enter '1' to find Number of people in the age groups(below 31 years and above 31years) belonging to two race groups who used Various drugs and display them in bar chart. ")

        print(" Enter '2' to find Average Beck Deppresion of people different drugs and find out whose beck deppresion is high and display the output in bar chart.")

        print(" Enter '3' to find percentage of people who returned to drugs after treatment and who din't return to drugs. Display the output in pi Chart too.")

        print(" Enter '4' to find Percentage of people whose duration for drug relapse is more than 1 year classified by the drug intake and their number of treatments.")

        print(" Enter '5' to find out length of tretament and beck depression of people under different age groups.")

        print(" Enter '6' to find out mean and standard deviation of age groups. Histogram will be displayed according to the input given")

        print(" Enter any other key to EXIT from the program")
        
        choice = raw_input("\n Please Enter the choice from above : ")

        if choice.isdigit() and int(choice) == 1:

            drugUse(age_list,Heroin_Cocaine, race_list,drugIV, numberOfColums)

            barchart1()

            print("")

            continue

        if choice.isdigit() and int(choice) == 2:

            drugsBeckdepress(Heroin_Cocaine,drugIV,numberOfColums,beck_list)

            barchart2()

            continue

        if choice.isdigit() and int(choice) == 3:

            noDrugs(Heroin_Cocaine,drugIV,censor_list,numberOfColums)

            piChart()

            continue

        if choice.isdigit() and int(choice) == 4:
            

            PercentagePeople(Heroin_Cocaine, drugIV, time_relapse, Treat, number_treatments, numberOfColums)

            continue

        if choice.isdigit() and int(choice) == 5:

            agegroups(age_list,numberOfColums,beck_list,length_treatment)

            continue            

        if choice.isdigit() and int(choice) == 6:

            meanH,sdHeroin = meanStandaradDeviation(Heroin_Cocaine,numberOfColums,age_list)

            choice = str(input("Please enter 1 Heroin   2. Cocain    3. Both: ") )

            if choice == '1':

                cocain,heroin,cocainHeroin = meanStd()

                histogram1(heroin,meanH,sdHeroin)

            elif choice == '2':

                cocain,heroin,cocainHeroin = meanStd()

                histogram1(cocain,meanH,sdHeroin)

            elif choice == '3':

                cocain,heroin,cocainHeroin = meanStd()

                histogram1(cocainHeroin,meanH,sdHeroin)    

            continue

        if choice not in '123456':

            print(" Thank You for using the program")

            print(" Bye")

            return
def histogram1(myList,mean,standard_deviation):

    fig = plt.figure()

    fig.suptitle('Mean & Standard Deviation', fontsize=14, fontweight='bold')        

    ax = fig.add_subplot(111)       

    mylist1 = []

    for i in myList:

        mylist1.append(int(i))        

    plt.hist(mylist1,35,color="red")    # hist function takes list as arguments and plots the bar graphs.

    plt.title("Frequency Chart")          # x-axis is the items and y-axis is the frequency

    plt.xlabel("Items")                    # xlabel is used to label x-axis

    plt.ylabel("Frequency")               # ylabel is used to label y-axis

    plt.plot([mean],[3],"o")              # plot function plots for the given values

    plt.plot([mean - standard_deviation+13, (mean + standard_deviation)-13], [2, 2], 'k-', lw=10,color="black")  # draws the line for the given points   

    ax.text(3, 30, 'Mean is shown using period symbol', style='italic',

        bbox={'facecolor':'white', 'alpha':0.5, 'pad':10})      

    plt.show()                          # used to show the chart

    ax.savefig('Histogram.png')

def meanStd():

    fileOpen = open("uis.csv","r")

    allList = []

    for line in fileOpen:

        word = line.split(",")

        tuple1 = word[2],word[4]

        allList.append(tuple1)   

    cocain = []

    heroin = []

    cocainHeroin =[]

    for item in allList:

        if item[1] == '2':

            heroin.append(item[0])

        elif item[1] == '3':

            cocain.append(item[0])

        elif item[1] == '1':

            cocainHeroin.append(item[0])

    return cocain,heroin,cocainHeroin

import numpy as np

import matplotlib.pyplot as plt

def barchart1(): 
    N = 5
    Whites_count = ( 33,26,74,150,58 )
    ind = np.arange(N)  # the x locations for the groups

    width = 0.35       # the width of the bars

    ax = plt.subplot(211)

    rects1 = ax.bar(ind, Whites_count, width, color='r')


    Non_White_count = (9,9,20, 57,10 )
    rects2 = ax.bar(ind+width, Non_White_count, width, color='b')

    ax.set_ylabel('No.of people', alpha = 0.5)

    ax.set_title('Type of drugs consumed by different people in race groups of age below 31 years\n')

    ax.set_xlabel('Drugs', alpha = 0.5)

    ax.set_xticks(ind+width)

    ax.set_xticklabels( ('Heroin&Cocaine' ,'Heroin only' ,'Cocaine only', 'DrugIV previously','DrugIV recently') )



    ax.legend( (rects1[0], rects2[0]), ('Whites', 'Non Whites') )

    def autolabel(rects):

        # attach some text labels

        for rect in rects:

            height = rect.get_height()

            ax.text(rect.get_x()+rect.get_width()/2., 0.85*height, '%d'%int(height),

                    ha='center', va='top')



    autolabel(rects1)

    autolabel(rects2)
    #-------------------------------------- second graph ----------------------------

    Whites_count_1 = (44,66,48,49,136)
    ind = np.arange(N)  # the x locations for the groups

    width = 0.35       # the width of the bars

    fig  = plt.subplots()

    ax = plt.subplot(212)

    rects3 = ax.bar(ind, Whites_count_1, width, color='r', alpha = 0.55)

    Non_White_count_1 = (18,6,30,17,24)

    rects4 = ax.bar(ind+width, Non_White_count_1, width, color='b', alpha = 0.25)

    #ax.set_xlabel('volts', alpha=0.5)

    # add some

    ax.set_ylabel('No.of people', alpha = 0.5)

    ax.set_title('Type of drugs consumed by different people in race groups of age above 32 years\n')

    ax.set_xlabel('Drugs', alpha = 0.5)

    ax.set_xticks(ind+width)

    ax.set_xticklabels( ('Heroin&Cocaine' ,'Heroin only' ,'Cocaine only', 'DrugIV previously','DrugIV recently') )

    ax.legend( (rects3[0], rects4[0]), ('Whites', 'Non Whites') )

    autolabel(rects3)

    autolabel(rects4)

    plt.show()

    ax.savefig('BarChart1.png')

# bar chart showing average beck depression of people taking differet drugs.    

def barchart2():

    N = 5

    Average_count = (15.67,17.18,18.38,19.48,20.40 )

    ind = np.arange(N)  # the x locations for the groups

    width = 0.35       # the width of the bars

    #fig  = plt.subplots()

    ax = plt.subplot(111)

    rects1 = ax.bar(ind, Average_count, width, color='r',alpha = 0.25)

    ax.set_ylabel('No.of patients', alpha = 0.5)

    ax.set_title('Average Beck depression score for people taking differnt drugs\n')

    ax.set_xlabel('Drugs', alpha = 0.5)

    ax.set_xticks(ind+width)

    ax.set_xticklabels( ('neither to heroin,cocaine nor drug IV' ,'Cocaine only','Heroin only','both heroin and cocaine', 'both heroin,cocaine and IV') )

    #ax.legend( (rects1[0], rects2[0]), ('Whites', 'Non Whites') )

    def autolabel(rects):

        # attach some text labels

        for rect in rects:

            height = rect.get_height()

            ax.text(rect.get_x()+rect.get_width()/2., 0.85*height, '%d'%int(height),

                    ha='center', va='bottom')


    autolabel(rects1)

    #autolabel(rects2)
  plt.show()

    ax.savefig('BarChart2.png')

from pylab import *

# Pi chart showing percentage of people who returned to drug after after treatment

def piChart():    

    # make a square figure and axes

    fig = figure(1, figsize=(6,6))

    ax = axes([0.1, 0.1,0.8,0.8])

    # The slices will be ordered and plotted counter-clockwise.

    labels = 'Returned to drugs later is ', 'Did not return to drugs later is'

    fracs = [74.74, 25.26]

    explode=(0, 0)

    pie(fracs, explode=explode, labels=labels,

                    autopct='%1.1f%%', shadow=True, startangle=90)

                    # The default startangle is 0, which would start

                    # the Frogs slice on the x-axis.  With startangle=90,

                    # everything is rotated counter-clockwise by 90 degrees,

                    # so the plotting starts on the positive y-axis.



    title('percentage of people who returned to drugs after treatment', bbox={'facecolor':'0.8', 'pad':5})

    fig.savefig('BarChart1.png')



        

