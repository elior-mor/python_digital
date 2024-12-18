from time import sleep
print("Hello!\nThis program will calculate the marketing budget needed according your specific needs.\n-----------\nPrice list:\nFacebook campaign = 100ILS per day.\nInstagram campaign = 50ILS per day\n-----------")
sleep(2)
marketing_budget=int(input("Please enter your planned marketing budget in ILS: "))
facebook_camp_time=int(input("For how many days you want the Facebook campaign to run? "))
instagram_camp_time=int(input("For how many days you want the Instagram campaign to run? "))
total_cost=float(100*facebook_camp_time + 50*instagram_camp_time)
print("The summary of marketing budget cost with tax is: " +str(1.17*total_cost) + " ILS" )
if((1.17*total_cost)>marketing_budget):
    print("You need to add " + str((1.17*total_cost)-marketing_budget) + " ILS")
else:
    print("Successful!")