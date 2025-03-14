import time
import os
import random

class Color:
    """ANSI color codes for terminal text"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    """Clears the terminal screen for better readability"""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.02, pause=0.5, color=None):
    """Makes text appear dramatically like in classic RPGs with better pacing"""
    text = str(text).replace('\n', ' ').strip()
    text = ' '.join(text.split())
    
    if color:
        print(color, end='')
    
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    
    if color:
        print(Color.RESET, end='')
    
    print("\n")  # Clean line ending
    time.sleep(pause)

def print_divider():
    """Adds a pretty divider to separate sections (like in Zelda text boxes!)"""
    print("\n" + Color.CYAN + "✨" + "="*48 + "✨" + Color.RESET + "\n")

def scene_transition():
    """Dramatic pause between scenes (but no screen clearing!)"""
    input(f"\n{Color.PURPLE}[Press Enter to continue your adventure...]{Color.RESET}\n")

# Game state variables (our patient chart, if you will! 📊)
player = {
    "name": "",
    "anxiety": 0,
    "correct_choices": 0,
    "reputation": 50,
    "diagnosis_hints": [],
    "clinical_pearls": [],
    "inventory": ["Pocket medicine handbook", "Stethoscope (you've convinced yourself it's haunted)", "Granola bar from orientation week"]
}

# All possible clinical pearls to collect
all_clinical_pearls = [
    "The classic triad of pheochromocytoma: headaches, sweating, and tachycardia",
    "Always block alpha receptors BEFORE beta receptors in pheochromocytoma",
    "The rule of 10s: 10% of pheos are extra-adrenal, 10% are bilateral, 10% are malignant, 10% are hereditary",
    "Up to 30% of pheochromocytomas are associated with genetic syndromes like MEN2, VHL, and NF1",
    "Plasma free metanephrines is the most sensitive test for pheochromocytoma",
    "Never palpate the abdomen vigorously in a patient with suspected pheochromocytoma",
    "Beta-blockade without alpha-blockade can precipitate a hypertensive crisis",
    "Surgical excision is the definitive treatment for pheochromocytoma",
    "Contrast-enhanced CT or MRI is the imaging modality of choice for suspected pheo",
    "Paragangliomas are extra-adrenal pheochromocytomas that arise from the sympathetic chain"
]

def add_clinical_pearl():
    """Add a random clinical pearl that the player doesn't have yet"""
    available_pearls = [p for p in all_clinical_pearls if p not in player["clinical_pearls"]]
    if available_pearls:
        new_pearl = random.choice(available_pearls)
        player["clinical_pearls"].append(new_pearl)
        type_text(f"{Color.GREEN}💡 NEW CLINICAL PEARL! 💡{Color.RESET}")
        type_text(f"{Color.GREEN}{new_pearl}{Color.RESET}", pause=1.5)

def print_stats():
    """Displays current player stats with nice formatting"""
    print_divider()
    print(f"{Color.BOLD}Dr. {player['name']}'s Status:{Color.RESET}")
    print(f"Anxiety Level: {'😰' * (player['anxiety'] // 10)}")
    print(f"Reputation with Dr. Rampy: {'⭐' * (player['reputation'] // 10)}")
    print(f"Correct Clinical Decisions: {player['correct_choices']}")
    
    # Show diagnosis hints if we have any
    if player['diagnosis_hints']:
        print(f"\n{Color.BLUE}Diagnosis Clues: 🔍{Color.RESET}")
        for hint in player['diagnosis_hints']:
            print(f"  • {hint}")
    
    # Show clinical pearls if we have any
    if player['clinical_pearls']:
        print(f"\n{Color.GREEN}📋 Clinical Pearls Collected: {len(player['clinical_pearls'])}/{len(all_clinical_pearls)}{Color.RESET}")
    
    # Show inventory
    if player['inventory']:
        print(f"\n{Color.CYAN}🎒 Inventory:{Color.RESET}")
        for item in player['inventory']:
            print(f"  - {item}")
    
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
            type_text("Dr. Rampy raises an eyebrow, seemingly impressed by your initiative.", color=Color.GREEN)
            type_text("'BP 178/104, HR 122, Temp 36.3°C. Make of that what you will.'", color=Color.YELLOW)
            player["correct_choices"] += 1
            player["diagnosis_hints"].append("Hypertension with tachycardia")
            # Award a clinical pearl
            add_clinical_pearl()
            # Internal thought monologue
            type_text("(Your brain: 'Hypertension AND tachycardia? That's... concerning. Secondary HTN maybe?')", color=Color.PURPLE)
            second_decision()
            break
        elif choice == "2":
            type_text("Dr. Rampy sighs. 'AHEM, didn't I JUST say... 'interesting VITALS'?! Time is of the essence, doctor.'", color=Color.RED)
            player["reputation"] -= 5
            # Internal thought
            type_text("(Your brain: 'Great, now I look like I can't follow simple instructions. Stellar start.')", color=Color.PURPLE)
            continue
        elif choice == "3":
            type_text("Dr. Rampy blocks your path with surprising agility.", color=Color.RED)
            type_text("'Perhaps some... pertinent information first?'", color=Color.YELLOW)
            player["anxiety"] += 10
            # Internal thought
            type_text("(Your brain: 'What is it with attendings and blocking doorways? Is this a medical education ritual?')", color=Color.PURPLE)
            continue
        elif choice == "4":
            type_text("*Your typing intensifies nervously*", color=Color.BLUE)
            type_text("Dr. Rampy: 'I can see you typing 'HELP' repeatedly.'", color=Color.YELLOW)
            type_text("'And is that... Zelda you're playing on an emulator?'", color=Color.YELLOW)
            player["anxiety"] += 20
            player["reputation"] -= 10
            # Internal thought
            type_text("(Your brain: 'In my defense, Breath of the Wild has gotten me through many rough call nights...')", color=Color.PURPLE)
            continue
        else:
            type_text("Dr. Rampy frowns. 'That wasn't one of the options, doctor.'", color=Color.RED)

def second_decision():
    """Second decision point after learning about vitals"""
    clear_screen()
    print_stats()
    
    type_text("Dr. Rampy taps their pen thoughtfully. 'So, given these vital signs...'", color=Color.YELLOW)
    
    while True:
        print("\nWhat's your next move?")
        print("\n1. 'Could we get more history about the headaches?'")
        print("2. *Frantically google 'high BP + tachycardia' on your phone*")
        print("3. 'RAPID RESPONSE!' *Reaches for the emergency button*")
        print("4. 'Well, when we consider the sympathetic nervous system...'")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("'Ah, finally asking the right questions!' Dr. Rampy's eyes light up.", color=Color.GREEN)
            type_text("'Patient reports episodic symptoms including headache, palpitations, and diaphoresis...'", color=Color.YELLOW)
            type_text("'Been occurring on and off for 3 months, lasting 15-30 minutes, once or twice a week.'", color=Color.YELLOW)
            type_text("'Yesterday's episode was more intense and lasted about an hour.'", color=Color.YELLOW)
            player["correct_choices"] += 1
            player["reputation"] += 10
            player["diagnosis_hints"].append("Episodic symptoms: headache, palpitations, diaphoresis")
            # Award a clinical pearl
            add_clinical_pearl()
            # Internal thought
            type_text("(Your brain: 'Episodic symptoms? That narrows things down considerably...')", color=Color.PURPLE)
            third_decision()
            break
        elif choice == "2":
            type_text("Dr. Rampy: 'Your phone's UpToDate history is... interesting.'", color=Color.RED)
            type_text("'Let me see... ah yes, \"help attending scary BP high\" - very professional.'", color=Color.YELLOW)
            player["anxiety"] += 15
            # Internal thought
            type_text("(Your brain: 'Note to self: Clear browser history BEFORE rotations...')", color=Color.PURPLE)
            continue
        elif choice == "3":
            type_text("Dr. Rampy physically blocks your path to the button with impressive reflexes.", color=Color.RED)
            type_text("'Let's not alert the ENTIRE HOSPITAL just yet, shall we?'", color=Color.YELLOW)
            player["anxiety"] += 25
            player["reputation"] -= 15
            # Internal thought
            type_text("(Your brain: 'Remember that time I wanted to call a rapid response and almost got tackled by my attending? Good times.')", color=Color.PURPLE)
            continue
        elif choice == "4":
            type_text("Dr. Rampy's eyebrow raises to previously unknown heights.", color=Color.GREEN)
            type_text("'Going straight for the pathophysiology? Bold choice.'", color=Color.YELLOW)
            type_text("'But yes, we should consider sympathetic activation here.'", color=Color.YELLOW)
            player["correct_choices"] += 1
            player["diagnosis_hints"].append("Sympathetic nervous system activation")
            # Internal thought
            type_text("(Your brain: 'Wait, did I just say something smart? Is this... competence?')", color=Color.PURPLE)
            third_decision()
            break
        else:
            type_text("Dr. Rampy: 'That wasn't one of the options. Again.'", color=Color.RED)

def third_decision():
    """Third decision point - narrowing down the diagnosis"""
    clear_screen()
    print_stats()
    
    type_text("Dr. Rampy hands you the patient's chart.", color=Color.BLUE)
    type_text("'So, Dr. " + player["name"] + ", what's your diagnostic approach?'", color=Color.YELLOW)
    
    # Internal thought
    type_text("(Your brain rapidly cycles through everything you've ever learned about hypertension and sympathetic activation...)", color=Color.PURPLE)
    
    while True:
        print("\nWhat tests would you order?")
        print("\n1. 'Let's get plasma metanephrines and catecholamines'")
        print("2. 'I'd like to order a Head CT and EKG'")
        print("3. 'Let's start with a basic metabolic panel and CBC'")
        print("4. 'Maybe we should check aldosterone and renin levels?'")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("Dr. Rampy's eyes widen with visible approval.", color=Color.GREEN)
            type_text("'Excellent choice. Going straight for the gold standard.'", color=Color.YELLOW)
            player["correct_choices"] += 2
            player["reputation"] += 15
            player["diagnosis_hints"].append("Ordered plasma metanephrines")
            # Add an item to inventory
            player["inventory"].append("Lab order for plasma metanephrines (smart move!)")
            # Award a clinical pearl
            add_clinical_pearl()
            # Internal thought
            type_text("(Your brain: 'Wow, I actually remembered the right test! Those UWorld questions weren't for nothing!')", color=Color.PURPLE)
            final_diagnosis()
            break
        elif choice == "2":
            type_text("Dr. Rampy tilts her head. 'Not entirely off base, but perhaps premature.'", color=Color.RED)
            type_text("'Let's think about the underlying cause of these symptoms first.'", color=Color.YELLOW)
            player["reputation"] -= 5
            # Internal thought
            type_text("(Your brain: 'Right, diagnose THEN image. Basic stuff, focus!')", color=Color.PURPLE)
            continue
        elif choice == "3":
            type_text("'Standard workup, I see. Safe but... uninspired.'", color=Color.YELLOW)
            type_text("'These might be helpful as baseline data, but unlikely to yield our diagnosis.'", color=Color.YELLOW)
            player["correct_choices"] += 1
            # Internal thought
            type_text("(Your brain: 'The medical equivalent of ordering vanilla ice cream. Not wrong, just... boring.')", color=Color.PURPLE)
            continue
        elif choice == "4":
            type_text("'Hmm, thinking about Conn's syndrome? Interesting differential.'", color=Color.YELLOW)
            type_text("'But remember the episodic nature of the symptoms.'", color=Color.YELLOW)
            player["correct_choices"] += 1
            player["diagnosis_hints"].append("Considered endocrine causes of hypertension")
            # Internal thought
            type_text("(Your brain: 'Close! Right system, wrong gland. Think adrenal medulla, not cortex...')", color=Color.PURPLE)
            continue
        else:
            type_text("Dr. Rampy sighs. 'Please choose from the options provided.'", color=Color.RED)

def final_diagnosis():
    """Final diagnostic moment"""
    clear_screen()
    print_stats()
    
    type_text("The next day, Dr. Rampy approaches with the test results.", color=Color.BLUE)
    type_text("'Well, the labs are back. Care to make your diagnosis?'", color=Color.YELLOW)
    
    if "Ordered plasma metanephrines" in player["diagnosis_hints"]:
        type_text("You see the results: Metanephrine (free), plasma: 5.2 nmol/L (ref: <0.50)", color=Color.CYAN)
        type_text("Normetanephrine (free), plasma: 9.8 nmol/L (ref: <0.90)", color=Color.CYAN)
        # Add item to inventory
        player["inventory"].append("Lab report with elevated metanephrines (Jackpot!)")
    
    # Internal thought
    type_text("(Your heart races. 'This is my moment. Don't say pancreatitis, don't say pancreatitis...')", color=Color.PURPLE)
    
    while True:
        print("\nWhat's your diagnosis?")
        print("\n1. 'This patient has a pheochromocytoma'")
        print("2. 'I believe this is essential hypertension with anxiety'")
        print("3. 'The patient has Conn's syndrome (primary hyperaldosteronism)'")
        print("4. 'I need more tests before making a diagnosis'")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("Dr. Rampy breaks into a rare, genuine smile!", color=Color.GREEN)
            type_text("'Excellent diagnosis, doctor! The CT scan confirms a 3.2 cm right adrenal mass.'", color=Color.YELLOW)
            player["correct_choices"] += 2
            player["reputation"] += 15
            # Award a clinical pearl
            add_clinical_pearl()
            # Internal thought
            type_text("(Your brain explodes with confetti. 'I DIAGNOSED SOMETHING REAL AND RARE! This is going in my personal statement.')", color=Color.PURPLE)
            management_decision()
            break
        elif choice == "2":
            type_text("Dr. Rampy's face falls. 'Really? With those metanephrine levels?'", color=Color.RED)
            type_text("'Perhaps reconsider the episodic nature and catecholamine excess?'", color=Color.YELLOW)
            player["reputation"] -= 10
            # Internal thought
            type_text("(Your brain: 'Way to ignore the lab values that are literally 10x normal. Stellar work.')", color=Color.PURPLE)
            continue
        elif choice == "3":
            type_text("Dr. Rampy shakes her head. 'Close, but not quite right.'", color=Color.RED)
            type_text("'Conn's would typically present with hypokalemia and wouldn't explain the episodic symptoms.'", color=Color.YELLOW)
            # Internal thought
            type_text("(Your brain: 'Wrong adrenal hormone again! Remember, Conn's = aldosterone, not catecholamines!')", color=Color.PURPLE)
            continue
        elif choice == "4":
            type_text("Dr. Rampy sighs deeply. 'Indecisiveness is not a virtue in medicine.'", color=Color.RED)
            type_text("'The elevated plasma metanephrines are quite diagnostic here.'", color=Color.YELLOW)
            player["anxiety"] += 10
            player["reputation"] -= 5
            # Internal thought
            type_text("(Your brain: 'Ah yes, the classic medical student move: when in doubt, order more tests!')", color=Color.PURPLE)
            continue
        else:
            type_text("'Focus, doctor. This is a critical moment.'", color=Color.RED)

def management_decision():
    """New function for management decision"""
    clear_screen()
    print_stats()
    
    type_text("Dr. Rampy looks expectantly at you. 'Now that we have our diagnosis, what's our next step?'", color=Color.YELLOW)
    
    # Internal thought
    type_text("(Your brain: 'Wait, we're not done? There's a management portion to this test too?')", color=Color.PURPLE)
    
    while True:
        print("\nWhat's your management plan?")
        print("\n1. 'Start beta-blockers to control the tachycardia, then schedule surgery'")
        print("2. 'Start alpha-blockers like phenoxybenzamine first, then add beta-blockers if needed'")
        print("3. 'Immediate surgical referral for adrenalectomy'")
        print("4. 'Start an ACE inhibitor and monitor blood pressure'")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("Dr. Rampy gasps audibly. 'ABSOLUTELY NOT!'", color=Color.RED)
            type_text("'Starting beta-blockers without alpha blockade could cause a hypertensive crisis!'", color=Color.YELLOW)
            player["anxiety"] += 15
            player["reputation"] -= 10
            # Internal thought
            type_text("(Your brain: 'And that's how you kill a patient. Good job breaking the first rule of medicine!')", color=Color.PURPLE)
            continue
        elif choice == "2":
            type_text("Dr. Rampy nods enthusiastically. 'Precisely correct!'", color=Color.GREEN)
            type_text("'Alpha blockade must precede beta blockade to prevent unopposed alpha-mediated vasoconstriction.'", color=Color.YELLOW)
            type_text("'We'll start phenoxybenzamine, then add a beta-blocker once blood pressure is controlled.'", color=Color.YELLOW)
            player["correct_choices"] += 2
            player["reputation"] += 15
            # Award a clinical pearl
            add_clinical_pearl()
            # Internal thought
            type_text("(Your brain: 'That random factoid from that one lecture actually paid off! Guess attendance does matter.')", color=Color.PURPLE)
            end_game(win=True)
            break
        elif choice == "3":
            type_text("'Not so fast,' says Dr. Rampy. 'We need medical management first.'", color=Color.RED)
            type_text("'Operating on an unprepared patient with a pheochromocytoma would be extremely dangerous.'", color=Color.YELLOW)
            player["reputation"] -= 5
            # Internal thought
            type_text("(Your brain: 'Right, preparation first. Surgery isn't always the immediate answer.')", color=Color.PURPLE)
            continue
        elif choice == "4":
            type_text("Dr. Rampy shakes her head. 'That's not standard management for pheochromocytoma.'", color=Color.RED)
            type_text("'There's a specific protocol we need to follow here.'", color=Color.YELLOW)
            player["anxiety"] += 5
            # Internal thought
            type_text("(Your brain: 'ACE inhibitors are not the answer to everything, despite what Step 1 would have you believe.')", color=Color.PURPLE)
            continue
        else:
            type_text("'Please choose a valid option, doctor. This patient needs proper care.'", color=Color.RED)

def end_game(win=False):
    """Game ending based on performance"""
    clear_screen()
    print_divider()
    
    # Calculate final score
    score = player["correct_choices"] * 10 + player["reputation"] - player["anxiety"]
    
    if win:
        type_text("CONGRATULATIONS! You correctly diagnosed and managed a patient with pheochromocytoma!", color=Color.GREEN)
        type_text("Dr. Rampy nods approvingly. 'Well done. I'll schedule the patient for an adrenalectomy.'", color=Color.YELLOW)
        type_text("'Alpha blockade first, of course, then surgery. Classic management.'", color=Color.YELLOW)
        
        if score > 100:
            type_text("'You know, you might actually survive residency after all.'", color=Color.YELLOW)
            type_text("You've impressed Dr. Rampy - a rare achievement indeed!", color=Color.GREEN)
            # Internal thought
            type_text("(Your brain: 'Did Dr. Rampy just... compliment me? Is this real life?')", color=Color.PURPLE)
        elif score > 50:
            type_text("'Not bad for a student. You still have much to learn, but there's potential.'", color=Color.YELLOW)
            # Internal thought
            type_text("(Your brain: 'From Dr. Rampy, that's practically a standing ovation.')", color=Color.PURPLE)
        else:
            type_text("'You got there eventually, though rather... circuitously.'", color=Color.YELLOW)
            # Internal thought
            type_text("(Your brain: 'Translation: You stumbled to the finish line, but at least you finished.')", color=Color.PURPLE)
    else:
        type_text("The patient was transferred to another service after complications.", color=Color.RED)
        type_text("Dr. Rampy looks disappointed. 'We'll discuss this further at your evaluation.'", color=Color.RED)
        # Internal thought
        type_text("(Your brain: 'Maybe I should have gone into accounting like my mother suggested...')", color=Color.PURPLE)
    
    print_divider()
    print(f"{Color.CYAN}🏆 FINAL SCORE: {score}{Color.RESET}")
    print(f"{Color.CYAN}Correct Decisions: {player['correct_choices']}{Color.RESET}")
    print(f"{Color.CYAN}Reputation with Dr. Rampy: {player['reputation']}{Color.RESET}")
    print(f"{Color.CYAN}Anxiety Level: {player['anxiety']}{Color.RESET}")
    
    # Display collected clinical pearls
    if player["clinical_pearls"]:
        print(f"\n{Color.GREEN}📋 CLINICAL PEARLS COLLECTED: {len(player['clinical_pearls'])}/{len(all_clinical_pearls)}{Color.RESET}")
        for i, pearl in enumerate(player["clinical_pearls"], 1):
            print(f"  {i}. {pearl}")
    
    print_divider()
    
    type_text("Thank you for playing ddxRAMPY: PHEOCHROMOCYTOMA EDITION!", color=Color.PURPLE)
    type_text("Remember, in medicine as in gaming: the sympathetic surge is real!", color=Color.PURPLE)

def start_game():
    """Game initialization and introduction"""
    clear_screen()
    
    # Display game title ASCII art with color
    print(Color.CYAN + """
    ██████╗ ██████╗ ██╗  ██╗██████╗  █████╗ ███╗   ███╗██████╗ ██╗   ██╗
    ██╔══██╗██╔══██╗╚██╗██╔╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗╚██╗ ██╔╝
    ██║  ██║██║  ██║ ╚███╔╝ ██████╔╝███████║██╔████╔██║██████╔╝ ╚████╔╝ 
    ██║  ██║██║  ██║ ██╔██╗ ██╔══██╗██╔══██║██║╚██╔╝██║██╔═══╝   ╚██╔╝  
    ██████╔╝██████╔╝██╔╝ ██╗██║  ██║██║  ██║██║ ╚═╝ ██║██║        ██║   
    ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝        ╚═╝   
                                                                         
    """ + Color.RESET)
    
    print_divider()
    type_text("🏥 Welcome to ddxRAMPY: A Terminal Adventure 🏥", color=Color.GREEN)
    type_text("Where every patient is a puzzle, and every attending is a final boss...", color=Color.CYAN)
    type_text("...and your impostor syndrome is your true nemesis!", color=Color.PURPLE)
        
    player["name"] = input("\nEnter your name, brave medical student: ")
    
    type_text(f"\n[Dell Medical School - Internal Medicine Ward]", color=Color.BLUE)
    type_text("It's 6:45 AM. Pre-rounds are about to start.")
    type_text(f"You, Dr. {player['name']}, are nervously reviewing your patient's chart when...")
    type_text(".....")

    type_text("👩‍⚕️ Dr. Rampy appears suddenly behind you!", color=Color.YELLOW)
    type_text("'Ah, perfect timing. New admission in room 2.'", color=Color.YELLOW)
    type_text("'37-year-old woman with... interesting vital signs.'", color=Color.YELLOW)
    
    # Internal thought
    type_text("(Your brain: 'Why do all attendings have ninja-level stealth? And why are vitals always \"interesting\" not \"concerning\"?')", color=Color.PURPLE)
    
    scene_transition()
    
    first_decision()

# Start our adventure! 🎮✨
if __name__ == "__main__":
    start_game()
