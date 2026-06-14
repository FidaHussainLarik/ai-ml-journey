
import time

print("==========================================================================================")
print("    This is my second mini-project called NATURAL TRANQUILIZER FOR THE Nervous SYSTEM ")
print("===========================================================================================")

def healer():
    print("\nEnhale for 4 seconds\n")
    for counter in range(4, 0, -1):  # Starts at 4, stops before 0, steps down by -1
        print(f"Inhaling 🧘 {counter}")
        time.sleep(1) # This will allow each next iteration to wait for one second.
        

    print("\nNow hold your breath for 7 seconds!\n")
    for counter in range(7, 0, -1):
        print("Hold and count down 🧘",counter)
        time.sleep(1) 
        

    print("\nExhale for 8 seconds!\n")
    counter = 8
    for counter in range(8, 0, -1):
        print("Exhaling 😤",counter)
        time.sleep(1) 


print("\n\n")


name = input("Enter you name: ").strip().lower()
print(f"{name}, are you stressed? (Yes/NO): " ,end='')

ans = input().strip().lower() # strip().lower() handles accidental spaces and any capitalization mix

if ans == 'yes':
    print("Do not worry! here is the technique that will cool your Nervous system down 😄")
    print("\nDo you want to start, the cooling the Nervous system donw, techniques (YES/NO): ",end='')
    
    startTech = input().strip().lower()

    if startTech == 'yes':
        ans = 'yes'
        print("Here we go........")
        for m in range(5):
            time.sleep(1)
            print("⌛",end=' ')
    else:
        ans = 'no'
else:
    print(f"Good, have a stress-free day {name} 🥂")





print("\n==========================================================================================")


while ans == 'yes':

    time.sleep(3)

    
    healer()
    
    print(f"\n\n{name}, is your brain cooled now? If cool enter yes, otherwise no to iterate one more time (yes/no): " )

    print("If cooled enter cool, or yes for repeating the process: ",end = '')

    ans = input()


    if ans == 'yes':
        print("Do not worry here is the technique that will cool your Nervous system down 😄")
    else :
        print(f"Good, have a stress-free day {name}! 🥂")


print("\n==========================================================================================")
print("\n\n")



