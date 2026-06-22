#function to convert time by converting the minutes into hours and adding it with existing hours
#it is assumed that the user will input time in 24 hour format

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60




def main():
    time = input("What time is it? ")
    x = convert(time)
 #main calls on the convert function
    if 7.0 <= x <= 8.0:
        print("breakfast time")
        #<= and >= used becuse question specifies that the time shouldbe inclusive of the start and end time
    elif 12.0 <= x <= 13.0:
        print("lunch time")
    elif 18.0 <= x <= 19.0:
        print("dinner time")
  #nothing is outputed if the time is not within the specified ranges therefore there is no else statement

main()



