# Collect user input
adj1 = input("Enter an adjective to describe the day: ")
adj2 = input("Enter an adjective to describe the monkey: ")
adj3 = input("Enter an adjective to describe the lion: ")
adj4 = input("Enter an adjective to describe the experience: ")

# Construct the story
story = (
    f"On a beautiful {adj1} day, I went to the zoo. "
    f"I saw a funny {adj2} monkey swinging from the trees. "
    f"Then, I spotted a majestic {adj3} lion lounging in the sun. "
    f"What a wild and {adj4} experience!"
)

# Print the story
print("\nHere is your Mad Libs story:\n")
print(story)

# Conditional twist based on the last adjective
if adj4.lower() in ["boring", "dull", "ordinary"]:
    print("\nMaybe next time, you'll see some ninja pandas to spice things up!")
elif adj4.lower() in ["exciting", "crazy", "unforgettable"]:
    print("\nSounds like a zoo adventure you'll never forget!")
else:
    print("\nEvery zoo trip has its own charm, doesn’t it?")
