import time
import os
import random

def clear_screen():
    """Clears the terminal screen for better readability"""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.02, pause=0.5):
    """Makes text appear dramatically like in classic RPGs with better pacing"""
    text = str(text).replace('\n', ' ').strip()
    text = ' '.join(text.split())

    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")  # Clean line ending
    time.sleep(pause)

def print_divider():
    """Adds a pretty divider to separate sections (like in Zelda text boxes!)"""
    print("\n" + "✨" + "="*48 + "✨\n")

def scene_transition():
    """Dramatic pause between scenes (but no screen clearing!)"""
    input("\n[Press Enter to continue your adventure...]\n")

# Game state variables (our patient chart, if you will! 📊)
player = {
    "name": "",
    "anxiety": 0,
    "correct_choices": 0,
    "reputation": 50,
    "diagnosis_hints": []
}

def print_stats():
    """Displays current player stats with nice formatting"""
    print_divider()
    print(f"Anxiety Level: {'😰' * (player['anxiety'] // 10)}")
    print(f"Reputation with Dr. Rampy: {'⭐' * (player['reputation'] // 10)}")
    print(f"Correct Clinical Decisions: {player['correct_choices']}")

    # Show diagnosis hints if we have any
    if player['diagnosis_hints']:
        print("\nDiagnosis Clues: 🔍")
        for hint in player['diagnosis_hints']:
            print(f"  • {hint}")

    print_divider()

def first_decision():
    """First interaction with Dr. Rampy about the new patient"""
    while True:
        print_stats()

        type_text("What would you like to do?")
        print("\n1. Ask about the vital signs")
        print("2. Review the chart first")
        print("3. Go see the patient immediately")
        print("4. Pretend you didn't hear and keep typing notes*")

        choice = input("\nYour choice (1-4): ")

        if choice == "1":
            type_text("Dr. Rampy raises an eyebrow, seemingly impressed by your initiative.")
            type_text("'BP 178/104, HR 122, Temp 36.3°C. Make of that what you will.'")
            player["correct_choices"] += 1
            player["diagnosis_hints"].append("Hypertension with tachycardia")
            second_decision()
            break
        elif choice == "2":
            type_text("Dr. Rampy sighs. 'AHEM, didn't I JUST say... 'interesting VITALS'?! Time is of the essence, doctor.'")
            player["reputation"] -= 5
            continue
        elif choice == "3":
            type_text("Dr. Rampy blocks your path.")
            type_text("'Perhaps some... pertinent information first?'")
            player["anxiety"] += 10
            continue
        elif choice == "4":
            type_text("*Your typing intensifies nervously*")
            type_text("Dr. Rampy: 'I can see you typing 'HELP' repeatedly.'")
            type_text("'And is that... Zelda you're playing on an emulator?'")
            player["anxiety"] += 20
            player["reputation"] -= 10
            continue
        else:
            type_text("Dr. Rampy frowns. 'That wasn't one of the options, doctor.'")

def second_decision():
    """Second decision point after learning about vitals"""
    clear_screen()
    print_stats()

    type_text("Dr. Rampy taps their pen thoughtfully. 'So, given these vital signs...'")

    while True:
        print("\nWhat's your next move?")
        print("\n1. 'Could we get more history about the headaches?'")
        print("2. *Frantically google 'high BP + tachycardia' on your phone*")
        print("3. 'RAPID RESPONSE!' *Reaches for the emergency button*")
        print("4. 'Well, when we consider the sympathetic nervous system...'")

        choice = input("\nYour choice (1-4): ")

        if choice == "1":
            type_text("'Ah, finally asking the right questions!' Dr. Rampy's eyes light up.")
            type_text("'Patient reports episodic symptoms including headache, palpitations, and diaphoresis...'")
            type_text("'Been occurring on and off for 3 months, lasting 15-30 minutes, once or twice a week.'")
            type_text("'Yesterday's episode was more intense and lasted about an hour.'")
            player["correct_choices"] += 1
            player["reputation"] += 10
            player["diagnosis_hints"].append("Episodic symptoms: headache, palpitations, diaphoresis")
            third_decision()
            break
        elif choice == "2":
            type_text("Dr. Rampy: 'Your phone's UpToDate history is... interesting.'")
            type_text("'Let me see... ah yes, \"help attending scary BP high\" - very professional.'")
            player["anxiety"] += 15
            continue
        elif choice == "3":
            type_text("Dr. Rampy physically blocks your path to the button.")
            type_text("'Let's not alert the ENTIRE HOSPITAL just yet, shall we?'")
            player["anxiety"] += 25
            player["reputation"] -= 15
            continue
        elif choice == "4":
            type_text("Dr. Rampy's eyebrow raises to previously unknown heights.")
            type_text("'Going straight for the pathophysiology? Bold choice.'")
            type_text("'But yes, we should consider sympathetic activation here.'")
            player["correct_choices"] += 1
            player["diagnosis_hints"].append("Sympathetic nervous system activation")
            third_decision()
            break
        else:
            type_text("Dr. Rampy: 'That wasn't one of the options. Again.'")

def third_decision():
    """Third decision point - narrowing down the diagnosis"""
    clear_screen()
    print_stats()

    type_text("Dr. Rampy hands you the patient's chart.")
    type_text("'So, Dr. " + player["name"] + ", what's your diagnostic approach?'")

    while True:
        print("\nWhat tests would you order?")
        print("\n1. 'Let's get plasma metanephrines and catecholamines'")
        print("2. 'I'd like to order a Head CT and EKG'")
        print("3. 'Let's start with a basic metabolic panel and CBC'")
        print("4. 'Maybe we should check aldosterone and renin levels?'")

        choice = input("\nYour choice (1-4): ")

        if choice == "1":
            type_text("Dr. Rampy's eyes widen with visible approval.")
            type_text("'Excellent choice. Going straight for the gold standard.'")
            player["correct_choices"] += 2
            player["reputation"] += 15
            player["diagnosis_hints"].append("Ordered plasma metanephrines")
            final_diagnosis()
            break
        elif choice == "2":
            type_text("Dr. Rampy tilts her head. 'Not entirely off base, but perhaps premature.'")
            type_text("'Let's think about the underlying cause of these symptoms first.'")
            player["reputation"] -= 5
            continue
        elif choice == "3":
            type_text("'Standard workup, I see. Safe but... uninspired.'")
            type_text("'These might be helpful as baseline data, but unlikely to yield our diagnosis.'")
            player["correct_choices"] += 1
            continue
        elif choice == "4":
            type_text("'Hmm, thinking about Conn's syndrome? Interesting differential.'")
            type_text("'But remember the episodic nature of the symptoms.'")
            player["correct_choices"] += 1
            player["diagnosis_hints"].append("Considered endocrine causes of hypertension")
            continue
        else:
            type_text("Dr. Rampy sighs. 'Please choose from the options provided.'")

def final_diagnosis():
    """Final diagnostic moment"""
    clear_screen()
    print_stats()

    type_text("The next day, Dr. Rampy approaches with the test results.")
    type_text("'Well, the labs are back. Care to make your diagnosis?'")

    if "Ordered plasma metanephrines" in player["diagnosis_hints"]:
        type_text("You see the results: Metanephrine (free), plasma: 5.2 nmol/L (ref: <0.50)")
        type_text("Normetanephrine (free), plasma: 9.8 nmol/L (ref: <0.90)")

    while True:
        print("\nWhat's your diagnosis?")
        print("\n1. 'This patient has a pheochromocytoma'")
        print("2. 'I believe this is essential hypertension with anxiety'")
        print("3. 'The patient has Conn's syndrome (primary hyperaldosteronism)'")
        print("4. 'I need more tests before making a diagnosis'")

        choice = input("\nYour choice (1-4): ")

        if choice == "1":
            type_text("Dr. Rampy breaks into a rare, genuine smile!")
            type_text("'Excellent diagnosis, doctor! The CT scan confirms a 3.2 cm right adrenal mass.'")
            player["correct_choices"] += 2
            player["reputation"] += 15
            end_game(win=True)
            break
        elif choice == "2":
            type_text("Dr. Rampy's face falls. 'Really? With those metanephrine levels?'")
            type_text("'Perhaps reconsider the episodic nature and catecholamine excess?'")
            player["reputation"] -= 10
            continue
        elif choice == "3":
            type_text("Dr. Rampy shakes her head. 'Close, but not quite right.'")
            type_text("'Conn's would typically present with hypokalemia and wouldn't explain the episodic symptoms.'")
            continue
        elif choice == "4":
            type_text("Dr. Rampy sighs deeply. 'Indecisiveness is not a virtue in medicine.'")
            type_text("'The elevated plasma metanephrines are quite diagnostic here.'")
            player["anxiety"] += 10
            player["reputation"] -= 5
            continue
        else:
            type_text("'Focus, doctor. This is a critical moment.'")

def end_game(win=False):
    """Game ending based on performance"""
    clear_screen()
    print_divider()

    # Calculate final score
    score = player["correct_choices"] * 10 + player["reputation"] - player["anxiety"]

    if win:
        type_text("CONGRATULATIONS! You correctly diagnosed the patient with pheochromocytoma!")
        type_text("Dr. Rampy nods approvingly. 'Well done. I'll schedule the patient for an adrenalectomy.'")
        type_text("'Alpha blockade first, of course, then surgery. Classic management.'")

        if score > 100:
            type_text("'You know, you might actually survive residency after all.'")
            type_text("You've impressed Dr. Rampy - a rare achievement indeed!")
        elif score > 50:
            type_text("'Not bad for a student. You still have much to learn, but there's potential.'")
        else:
            type_text("'You got there eventually, though rather... circuitously.'")
    else:
        type_text("The patient was transferred to another service after complications.")
        type_text("Dr. Rampy looks disappointed. 'We'll discuss this further at your evaluation.'")

    print_divider()
    print(f"Final Score: {score}")
    print(f"Correct Decisions: {player['correct_choices']}")
    print(f"Reputation with Dr. Rampy: {player['reputation']}")
    print(f"Anxiety Level: {player['anxiety']}")
    print_divider()

    type_text("Thank you for playing CLINICAL ROTATIONS!")
    type_text("Remember, in both medicine and coding: practice makes perfect!")

def start_game():
    """Game initialization and introduction"""
    clear_screen()

    # Display game title ASCII art
    print("""
    ██████╗ ██████╗ ██╗  ██╗ ██████╗  █████╗ ███╗   ███╗███████╗
    ██╔══██╗██║  ██║╚██╗██╔╝██╔════╝ ██╔══██╗████╗ ████║██╔════╝
    ██║  ██║██║  ██║ ╚███╔╝ ██║  ███╗███████║██╔████╔██║█████╗  
    ██║  ██║██║  ██║ ██╔██╗ ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
    ██████╔╝██████╔╝██╔╝ ██╗╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
    ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
    """)

    print_divider()
    type_text("🏥 Welcome to ddxGAME: A Terminal Adventure 🏥")
    type_text("Where every patient is a puzzle, and every attending is a final boss...")

    player["name"] = input("\nEnter your name, brave medical student: ")

    type_text(f"\n[Dell Medical School - Internal Medicine Ward]")
    type_text("It's 6:45 AM. Pre-rounds are about to start.")
    type_text(f"You, Dr. {player['name']}, are nervously reviewing your patient's chart when...")
    type_text(".....")

    type_text("👩‍⚕️ Dr. Rampy appears suddenly behind you!")
    type_text("'Ah, perfect timing. New admission in room 2.'")
    type_text("'37-year-old woman with... interesting vital signs.'")
    scene_transition()

    first_decision()

# Start our adventure! 🎮✨
if __name__ == "__main__":
    start_game()