
import time

print("==========================================================================================")
print("    This is my second mini-project called NATURAL TRANQUILIZER FOR THE Nervous SYSTEM ")
print("===========================================================================================")


print("\n\n")

name = input("Enter you name: ")
print(f"{name}, are you stressed? (Yes/NO): " ,end='')
ans = input()

if ans == 'Yes' or ans == 'yes':
    print("Do not worry! here is the technique that will cool your Nervous system down 😄")
    print("Do you want to start, the cooling the Nervous system donw, techniques (YES/NO): ",end='')
    startTech = input()

    if (startTech == 'Yes' or startTech == 'yes') :
        ans = 'yes'
        print("Here we go........")
        for m in range(5):
            time.sleep(1)
            print("⌛")
            
    else:
        ans = 'No'
else:
    print(f"Good, have a stress free day {name} 🥂")





print("==========================================================================================")


while ans == 'Yes' or ans == 'yes':
    time.sleep(3)
    print("\nEnhale for 4 seconds\n")
    counter = 4
    while counter != 0:
        print("Enhaling 🧘",counter)
        time.sleep(1) # This will allow each next iteration to wait for one second.
        counter = counter-1



    print("\nNow hold your breath for 7 seconds!\n")
    counter = 7
    while counter != 0:
        print("Hold and count down 🧘",counter)
        time.sleep(1) 
        counter = counter-1


    print("\nExhale for 8 seconds!\n")
    counter = 8
    while counter != 0:
        print("Exhaling 😤",counter)
        time.sleep(1) 
        counter = counter-1
    

    print(f"\n\n{name}, is your brain cooled now (Yes/NO)?? If yes enter cool, or do you need more practice? " )
    print("If cooled enter cool, or yes for repeating the process: ",end = '')
    ans = input()

    if ans == 'Yes' or ans == 'yes':
        print("Do not worry here is the technique that will cool your Nervous system down 😄")
    else :
        print(f"Good, have a stress free day {name} 🥂")



print("==========================================================================================")
print("\n\n")

"""
The 4-7-8 breathing technique (sometimes referred to casually as variations like 7-4, but the official rhythmic sequence is 4, 7, and 8).

1.Enhale:
4 Seconds.
Close your mouth and Enhale quietly through your nose for a mental count of 4.

2.Hold:
7 Seconds.Hold your breath entirely for a count of 7. (This is the most important part, as it allows your blood to maximize its oxygen intake).

3.Exhale:
8 Seconds.Exhale completely through your mouth, making a "whoosh" sound, for a count of 8. Empty your lungs entirely.


Why it Actually Works

When you are stressed, your breathing becomes shallow and fast, which keeps your nervous system amped up. This technique works because:

Forces Exhalation: The 8-second exhale forces your body to rid itself of stale air and activates the parasympathetic nervous system, which naturally lowers your heart rate and blood pressure.

Focuses the Mind: Counting to 4, 7, and 8 gives your brain a simple, rhythmic task to focus on, immediately distracting you from whatever is causing the stress.

"""



