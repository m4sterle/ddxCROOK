import time
import os

def clear_screen():
    """Clears the terminal screen for better readability"""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.02, pause=0.5):
    """Makes text appear dramatically like in classic RPGs with better pacing"""
    text = text.replace('\n', ' ').strip()
    text = ' '.join(text.split())
    
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")  # Clean line ending
    time.sleep(pause)

def print_divider():
    """Adds a pretty divider to separate sections (like in Zelda text boxes!)"""
    print("\n" + "✨" + "="*48 + "✨\n")

def print_stats():
    """Displays current player stats with nice formatting"""
    print_divider()
    print(f"Anxiety Level: {'😰' * (player['anxiety'] // 10)}")
    print(f"Reputation with Dr. Rampy: {'⭐' * (player['reputation'] // 10)}")
    print(f"Correct Clinical Decisions: {player['correct_choices']}")
    print_divider()

def scene_transition():
    """Dramatic pause between scenes (but no screen clearing!)"""
    input("\n[Press Enter to continue your adventure...]\n")

# Game state variables (our patient chart, if you will! 📊)
player = {
    "name": "",
    "anxiety": 0,
    "correct_choices": 0,
    "reputation": 50
}

def print_stats():
    """Displays current player stats"""
    print(f"\n{'='*50}")
    print(f"Anxiety Level: {'😰' * (player['anxiety'] // 10)}")
    print(f"Reputation with Dr. Rampy: {'⭐' * (player['reputation'] // 10)}")
    print(f"Correct Clinical Decisions: {player['correct_choices']}")
    print(f"{'='*50}\n")

def first_decision():
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
            player["correct_choices"] += 1
            player["reputation"] += 10
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
            player["correct_choices"] += 1
            break
        else:
            type_text("Dr. Rampy: 'That wasn't one of the options. Again.'")

def start_game():
    print("""
 ██████╗ ██████╗ ██╗  ██╗ ██████╗  █████╗ ███╗   ███╗███████╗
 ██╔══██╗██╔══██╗╚██╗██╔╝██╔════╝ ██╔══██╗████╗ ████║██╔════╝
 ██║  ██║██║  ██║ ╚███╔╝ ██║  ███╗███████║██╔████╔██║█████╗  
 ██║  ██║██║  ██║ ██╔██╗ ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
 ██████╔╝██████╔╝██╔╝ ██╗╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
    """)
    print_divider()
    type_text("🏥 Welcome to CLINICAL ROTATIONS: A Terminal Adventure 🏥")
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