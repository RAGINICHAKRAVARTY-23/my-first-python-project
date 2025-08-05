# Collect user input with clear prompts
park_adjective = input("Describe the water park with an adjective: ")
weird_thing = input("Enter the name of a weird object or creature you saw: ")
thing_adjective = input(f"Describe the {weird_thing} with an adjective: ")
thing_action = input(f"What was the {weird_thing} doing? (verb): ")
your_feeling = input("How did you feel seeing that? (adjective): ")

# Output the story
print("\n--- Your Mad Libs Story ---")
print(f"Yesterday I went to a {park_adjective} water park.")
print(f"There I saw a {weird_thing}.")
print(f"The {weird_thing} was {thing_adjective} and {thing_action}ing around.")
print(f"I felt {your_feeling} after seeing that.")
