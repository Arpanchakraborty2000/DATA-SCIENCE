# Collecting user feedback using list

feedback_list = []   # Empty list to store feedback

print("📢 Feedback Collection System")
print("Type 'exit' to stop giving feedback.\n")

while True:
    feedback = input("Enter your feedback: ")
    
    if feedback.lower() == "exit":
        break
    feedback_list.append(feedback)  # Store feedback in list
    print("✅ Thank you for your feedback!\n")

# Display all collected feedback
print("\n------ Collected Feedback ------")
if feedback_list:
    for i, fb in enumerate(feedback_list, start=1):
        print(f"{i}. {fb}")
else:
    print("No feedback collected.")
