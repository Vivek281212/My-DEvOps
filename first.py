
###please create a program where you will have 5 participants, take the feedback of the class from the users

###then calculate the average of the feedback and print the average of the feedback

###if it is greater than 3 , then it is good, else it is bad



feedback1=int(input("Enter the feedback of the first participant"))

feedback2=int(input("Enter the feedback of the second participant"))

feedback3=int(input("Enter the feedback of the third participant"))

feedback4=int(input("Enter the feedback of the fourth participant"))

feedback5=int(input("Enter the feedback of the fifth participant"))

average=(feedback1+feedback2+feedback3+feedback4+feedback5)/5

print("The average feedback is",average)

if(average>4):

    print("Very good")

elif(average>3):

    print("Average feedback is  average")

elif(average>2):

    print("average feedback is bad")

else:

    print("replace the teacher")
