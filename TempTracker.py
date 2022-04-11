entry = input("What do you want to do:\n- New entry? (type: 'insert')\n- Get mean? (type: 'mean')\n- Get max? (type: 'max')\n- Get min? (type: 'min')\n- Quit? (type: 'quit')\n")
#setting up variables
track = []
maximum = None
minimum = None
average = None

#inputs and printing respective outputs
while entry != "quit":
    if entry == "insert":
        try: #accounting for user entry error
            temp = int(input("---------\nEnter temperature recording: "))
            track.append(temp)
            maximum = max(track)
            minimum = min(track)
            average = sum(track)/len(track)
        except ValueError:
            print("\n[WARNING] Please enter an integer!\n")
    elif entry == "max":
        print("---------\nMaximum temperature:", maximum)
    elif entry == "min":
        print("---------\nMinimum temperature:", minimum)
    elif entry == "mean":
        print("---------\nMean temperature:", average)
    else:
        print("\n[WARNING] Invalid Option!\n") #accounting for user entry error
    entry = input("---------\nWhat do you want to do:\n- New entry? (type: 'insert')\n- Get mean? (type: 'mean')\n- Get max? (type: 'max')\n- Get min? (type: 'min')\n- Quit? (type: 'quit')\n")

#saving the temperatures to a file
file = open("trackedtemperatures.txt", "w")
file.write("Maximum temperature: {}\n".format(str(maximum)))
file.write("Minimum temperature: {}\n".format(str(minimum)))
file.write("Mean temperature: {}\n---------\n".format(str(average)))
for item in track:
    file.write("{}\n".format(str(item)))
