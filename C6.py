def evaluate_performance():
    print("=== Employee Performance Evaluation Expert System ===")
    
    punctuality = input("Is the employee punctual? (yes/no): ").lower()
    task_completion = input("Does the employee complete tasks on time? (yes/no): ").lower()
    quality_of_work = input("Is the quality of work good? (yes/no): ").lower()
    teamwork = input("Is the employee good at teamwork? (yes/no): ").lower()
    initiative = input("Does the employee show initiative? (yes/no): ").lower()

    score = 0

    if punctuality == 'yes':
        score += 1
    if task_completion == 'yes':
        score += 1
    if quality_of_work == 'yes':
        score += 1
    if teamwork == 'yes':
        score += 1
    if initiative == 'yes':
        score += 1

    print("\nEvaluation Result:")
    if score == 5:
        print("Excellent Performance")
    elif 3 <= score < 5:
        print("Good Performance")
    elif 1 <= score < 3:
        print("Needs Improvement")
    else:
        print("Poor Performance")

# Run the expert system
# evaluate_performance()


# Simple Expert System for Airline Scheduling and Cargo Schedules

flights = [
    {"flight_no": "AI101", "destination": "Mumbai", "cargo_capacity": 1000},
    {"flight_no": "AI202", "destination": "Pune", "cargo_capacity": 800},
    {"flight_no": "AI303", "destination": "Nagpur", "cargo_capacity": 1200},
    {"flight_no": "AI404", "destination": "Nashik", "cargo_capacity": 600},
]

def schedule_cargo():
    print("=== Airline Cargo Scheduling Expert System ===")

    destination = input("Enter destination (Mumbai/Pune/Nagpur/Nashik): ").capitalize()
    try:
        weight = int(input("Enter cargo weight in kg: "))
    except ValueError:
        print("❌ Invalid weight input.")
        return

    print("\nSearching for suitable flights...")
    scheduled = False
    for flight in flights:
        if flight["destination"] == destination:
            if weight <= flight["cargo_capacity"]:
                print(f"✅ Cargo scheduled on flight {flight['flight_no']} to {destination}")
                print(f"Remaining capacity: {flight['cargo_capacity'] - weight} kg")
                scheduled = True
                break
            else:
                print(f"❌ Flight {flight['flight_no']} has insufficient cargo space.")
    
    if not scheduled:
        print("❌ No suitable flights found for this cargo.")

# Run the expert system
schedule_cargo()
