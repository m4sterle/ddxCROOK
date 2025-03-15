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
    "inventory": ["Pocket medicine handbook", "Stethoscope (barely know how to use it)", "Half-eaten granola bar"]
}

# All possible clinical pearls to collect
all_clinical_pearls = [
    "Kawasaki Disease requires at least 5 days of fever PLUS 4 of 5 clinical criteria",
    "The classic 5 signs: rash, conjunctivitis, oral changes, extremity changes, and cervical lymphadenopathy",
    "IVIG and high-dose aspirin should be started within 10 days of fever onset",
    "Coronary artery aneurysms are the most serious complication of Kawasaki Disease",
    "Thrombocytosis typically occurs in the second week of illness",
    "Incomplete Kawasaki should be considered in any child with prolonged unexplained fever",
    "Echo should be performed at diagnosis, 2 weeks, and 6-8 weeks after onset",
    "Atypical Kawasaki can occur in infants < 6 months and may be harder to diagnose",
    "Elevated CRP and ESR are nearly universal in acute Kawasaki Disease",
    "Recurrence of Kawasaki Disease is rare but possible (1-3% of cases)"
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
    print(f"Reputation with Dr. Crook: {'⭐' * (player['reputation'] // 10)}")
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
    """First interaction with Dr. Crook about the new patient"""
    while True:
        print_stats()
        
        type_text("What would you like to do?")
        print("\n1. Ask about the vital signs")
        print("2. Review the chart first")
        print("3. Go see the patient immediately")
        print("4. Pretend you didn't hear and keep typing notes*")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("Dr. Crook raises an eyebrow, seemingly impressed by your initiative.", color=Color.GREEN)
            type_text("'Temperature 39.8°C, HR 130, RR 28, BP 95/60. Make of that what you will.'", color=Color.YELLOW)
            player["correct_choices"] += 1
            player["diagnosis_hints"].append("High fever with tachycardia")
            # Award a clinical pearl
            add_clinical_pearl()
            # Internal thought monologue
            type_text("(Your brain: 'High fever in a kid... infections, rheumatic fever, maybe something auto-inflammatory?')", color=Color.PURPLE)
            second_decision()
            break
        elif choice == "2":
            type_text("Dr. Crook sighs dramatically. 'Did I not JUST mention... interesting VITALS? These kids don't have all day, doctor.'", color=Color.RED)
            player["reputation"] -= 5
            # Internal thought
            type_text("(Your brain: 'Great start. Really nailing this whole doctor thing.')", color=Color.PURPLE)
            continue
        elif choice == "3":
            type_text("Dr. Crook blocks your path with surprising agility.", color=Color.RED)
            type_text("'Hold up there, speed racer. Perhaps some... pertinent information first?'", color=Color.YELLOW)
            player["anxiety"] += 10
            # Internal thought
            type_text("(Your brain: 'Ah yes, the classic medical student blunder: enthusiasm without information.')", color=Color.PURPLE)
            continue
        elif choice == "4":
            type_text("*Your typing intensifies nervously*", color=Color.BLUE)
            type_text("Dr. Crook: 'I can see you typing 'HELP ME PLEASE' repeatedly.'", color=Color.YELLOW)
            type_text("'And is that... Zelda you're playing on an emulator? In the pediatric ward?'", color=Color.YELLOW)
            player["anxiety"] += 20
            player["reputation"] -= 10
            # Internal thought
            type_text("(Your brain: 'Maybe if I type fast enough, I'll time travel to graduation...')", color=Color.PURPLE)
            continue
        else:
            type_text("Dr. Crook frowns. 'That wasn't one of the options, doctor. Kids' health is at stake here.'", color=Color.RED)

def second_decision():
    """Second decision point after learning about vitals"""
    clear_screen()
    print_stats()
    
    type_text("Dr. Crook taps his clipboard thoughtfully. 'So, given these vitals in a 5-year-old...'", color=Color.YELLOW)
    
    while True:
        print("\nWhat's your next move?")
        print("\n1. 'How long has the fever persisted?'")
        print("2. *Frantically google 'kid fever fast heart' on your phone*")
        print("3. 'PEDS RAPID RESPONSE!' *Reaches for the emergency button*")
        print("4. 'Let me examine the patient for any rashes or physical findings'")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("'Finally asking the right questions!' Dr. Crook's eyes light up.", color=Color.GREEN)
            type_text("'Fever for 5 days now, started at 38.5°C but has been persistently above 39°C'", color=Color.YELLOW)
            type_text("'Tylenol and Motrin barely touching it. Parents are appropriately freaking out.'", color=Color.YELLOW)
            player["correct_choices"] += 1
            player["reputation"] += 10
            player["diagnosis_hints"].append("Persistent high fever >5 days")
            # Award a clinical pearl
            add_clinical_pearl()
            # Internal thought
            type_text("(Your brain: 'Five days of fever resistant to antipyretics... definitely narrowing the differential.')", color=Color.PURPLE)
            third_decision()
            break
        elif choice == "2":
            type_text("Dr. Crook: 'Your phone's UpToDate history is... illuminating.'", color=Color.RED)
            type_text("'Let me see... ah yes, \"OMG HELP FEVER KID DYING\" - very professional, doctor.'", color=Color.YELLOW)
            player["anxiety"] += 15
            # Internal thought
            type_text("(Your brain: 'Maybe I should've gone with the less conspicuous \"kid fever not clickbait\" search.')", color=Color.PURPLE)
            continue
        elif choice == "3":
            type_text("Dr. Crook physically blocks your path to the button with impressive reflexes.", color=Color.RED)
            type_text("'Let's not alert the ENTIRE PEDIATRIC FLOOR just yet, shall we?'", color=Color.YELLOW)
            player["anxiety"] += 25
            player["reputation"] -= 15
            # Internal thought
            type_text("(Your brain: 'Wow, for an older attending, he sure moves fast when medical students are about to make terrible decisions.')", color=Color.PURPLE)
            continue
        elif choice == "4":
            type_text("Dr. Crook's face brightens. 'Good instinct. Physical exam is key in pediatrics.'", color=Color.GREEN)
            type_text("'Come, let's examine our little patient together.'", color=Color.YELLOW)
            player["correct_choices"] += 1
            player["diagnosis_hints"].append("Examination key in pediatric diagnosis")
            # Internal thought
            type_text("(Your brain: 'Please let me remember which side of the stethoscope to use...')", color=Color.PURPLE)
            third_decision()
            break
        else:
            type_text("Dr. Crook: 'That wasn't one of the options. Again. Kids deserve better focus.'", color=Color.RED)

def third_decision():
    """Third decision point - examining the patient"""
    clear_screen()
    print_stats()
    
    type_text("You enter the patient's room with Dr. Crook. A miserable-looking 5-year-old boy lies in bed.", color=Color.BLUE)
    type_text("His mother looks up anxiously. 'Is there any news, doctors?'", color=Color.BLUE)
    type_text("Dr. Crook turns to you expectantly. 'Dr. " + player["name"] + " would like to examine your son.'", color=Color.YELLOW)
    
    # Internal thought
    type_text("(Your brain: 'No pressure. Just don't mess up in front of the kid, the parent, AND Dr. Crook...')", color=Color.PURPLE)
    
    while True:
        print("\nWhat do you focus on first?")
        print("\n1. Look at the skin for any rashes or peeling")
        print("2. Check the lymph nodes in the neck")
        print("3. Examine the hands, feet, and mucosal surfaces")
        print("4. Ask about recent travel or exposures")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1" or choice == "3":
            if choice == "1":
                type_text("You notice a distinctive polymorphic rash across the trunk and extremities.", color=Color.GREEN)
                # Add item to inventory
                player["inventory"].append("Photo of polymorphic rash (Added to patient chart)")
            else:
                type_text("You observe swollen, red hands and feet with some peeling beginning at the fingertips.", color=Color.GREEN)
                type_text("When you check the mouth, you see clearly red, cracked lips and a 'strawberry tongue'.", color=Color.GREEN)
                # Add item to inventory
                player["inventory"].append("Photo of hands/feet and oral findings (Added to patient chart)")
            
            type_text("Dr. Crook nods approvingly. 'Excellent observation. What else do you see?'", color=Color.YELLOW)
            type_text("You continue your exam and also note bilateral conjunctival injection without discharge.", color=Color.GREEN)
            player["correct_choices"] += 2
            player["reputation"] += 10
            
            if choice == "1":
                player["diagnosis_hints"].append("Polymorphic rash")
            else:
                player["diagnosis_hints"].append("Red hands/feet with peeling + strawberry tongue")
                
            player["diagnosis_hints"].append("Conjunctival injection")
            
            # Award a clinical pearl
            add_clinical_pearl()
            
            # Internal thought
            type_text("(Your brain: 'Fever + rash + conjunctivitis + oral changes... this is starting to look familiar...')", color=Color.PURPLE)
            
            fourth_decision()
            break
            
        elif choice == "2":
            type_text("You palpate a significantly enlarged lymph node on the right side of the neck.", color=Color.GREEN)
            type_text("Dr. Crook chimes in. 'At least 1.5cm. Unilateral cervical lymphadenopathy.'", color=Color.YELLOW)
            player["correct_choices"] += 1
            player["diagnosis_hints"].append("Unilateral cervical lymphadenopathy")
            # Internal thought
            type_text("(Your brain: 'Add lymphadenopathy to the list. We're building quite the constellation of findings here...')", color=Color.PURPLE)
            fourth_decision()
            break
            
        elif choice == "4":
            type_text("The mother shakes her head. 'No travel. He was at daycare until the fever started.'", color=Color.BLUE)
            type_text("'No one else is sick that we know of. He's up-to-date on vaccines.'", color=Color.BLUE)
            type_text("Dr. Crook gives you a look. 'Perhaps a physical finding would be more illuminating...'", color=Color.YELLOW)
            # Internal thought
            type_text("(Your brain: 'Right... I should probably look at the actual patient.')", color=Color.PURPLE)
            continue
            
        else:
            type_text("Dr. Crook whispers. 'Focus, doctor. The options are right there.'", color=Color.RED)

def fourth_decision():
    """Fourth decision point - diagnostic approach"""
    clear_screen()
    print_stats()
    
    type_text("Back at the nursing station, Dr. Crook asks, 'So what's your diagnostic approach?'", color=Color.YELLOW)
    type_text("'We have a 5-year-old with 5 days of fever, rash, red eyes, swollen hands and feet,'", color=Color.YELLOW)
    type_text("'red lips, strawberry tongue, and unilateral cervical lymphadenopathy.'", color=Color.YELLOW)
    
    # Internal thought
    type_text("(Your brain is racing through differentials: 'Scarlet fever? Measles? Stevens-Johnson? Wait... Kawasaki?')", color=Color.PURPLE)
    
    while True:
        print("\nWhat tests would you order?")
        print("\n1. 'CBC with differential, CRP, ESR, and echocardiogram'")
        print("2. 'Blood culture, throat culture, and lumbar puncture'")
        print("3. 'Rapid strep test and mono spot'")
        print("4. 'CT scan of the head and chest X-ray'")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("Dr. Crook's eyes widen with visible approval.", color=Color.GREEN)
            type_text("'Excellent choices. Also consider LFTs and urinalysis. Let's monitor those platelets.'", color=Color.YELLOW)
            player["correct_choices"] += 2
            player["reputation"] += 15
            player["diagnosis_hints"].append("Ordered appropriate inflammatory markers and echo")
            
            # Award a clinical pearl
            add_clinical_pearl()
            
            # Internal thought
            type_text("(Your brain: 'Wait, did I just... impress Dr. Crook? Is this real life?')", color=Color.PURPLE)
            
            final_diagnosis()
            break
            
        elif choice == "2":
            type_text("Dr. Crook tilts his head. 'Infection workup is reasonable, but lumbar puncture?'", color=Color.RED)
            type_text("'No meningeal signs here. Think broader about the constellation of symptoms.'", color=Color.YELLOW)
            player["reputation"] -= 5
            
            # Internal thought
            type_text("(Your brain: 'Great, now I'm the med student who wants to do unnecessary LPs on children...')", color=Color.PURPLE)
            
            continue
            
        elif choice == "3":
            type_text("'Limited testing for a complex presentation. Think bigger picture, doctor.'", color=Color.RED)
            type_text("'This child has multiple systems involved. What might we be missing?'", color=Color.YELLOW)
            
            # Internal thought
            type_text("(Your brain: 'The number of ways to look incompetent seems infinite...')", color=Color.PURPLE)
            
            continue
            
        elif choice == "4":
            type_text("Dr. Crook raises both eyebrows to stratospheric heights.", color=Color.RED)
            type_text("'Irradiating a child should never be our first approach. What else could we do?'", color=Color.YELLOW)
            player["anxiety"] += 10
            
            # Internal thought
            type_text("(Your brain: 'Note to self: Don't suggest CT scans for children unless absolutely necessary...')", color=Color.PURPLE)
            
            continue
            
        else:
            type_text("Dr. Crook sighs. 'Please focus on the options at hand.'", color=Color.RED)

def final_diagnosis():
    """Final diagnostic moment"""
    clear_screen()
    print_stats()
    
    type_text("The next day, Dr. Crook approaches with the test results.", color=Color.BLUE)
    type_text("'Well, the labs are back. CRP 120 mg/L, ESR 80 mm/h, platelets 450,000.'", color=Color.YELLOW)
    type_text("'CBC shows leukocytosis with neutrophilia, mild anemia, and LFTs show mild transaminitis.'", color=Color.YELLOW)
    type_text("'Echo pending. Care to make your diagnosis?'", color=Color.YELLOW)
    
    # Internal thought
    type_text("(Your heart is pounding. 'This is it. Don't mess up now...')", color=Color.PURPLE)
    
    while True:
        print("\nWhat's your diagnosis?")
        print("\n1. 'This patient has Kawasaki Disease'")
        print("2. 'I believe this is Scarlet Fever'")
        print("3. 'The patient has Juvenile Idiopathic Arthritis with systemic features'")
        print("4. 'I need more tests before making a diagnosis'")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("Dr. Crook breaks into a rare, genuine smile!", color=Color.GREEN)
            type_text("'Excellent diagnosis, doctor! Classic presentation meeting clinical criteria.'", color=Color.YELLOW)
            type_text("'We need to start IVIG and high-dose aspirin ASAP to prevent coronary artery aneurysms.'", color=Color.YELLOW)
            player["correct_choices"] += 2
            player["reputation"] += 15
            
            # Award a clinical pearl
            add_clinical_pearl()
            
            # Internal thought
            type_text("(Your brain: 'I... I did it! I actually diagnosed something correctly!')", color=Color.PURPLE)
            
            end_game(win=True)
            break
            
        elif choice == "2":
            type_text("Dr. Crook's face falls. 'Close, but Scarlet Fever doesn't explain all findings.'", color=Color.RED)
            type_text("'The conjunctival injection, extremity changes, and persistent fever despite appropriate antibiotics point elsewhere.'", color=Color.YELLOW)
            player["reputation"] -= 5
            
            # Internal thought
            type_text("(Your brain: 'So close yet so far... what am I missing?')", color=Color.PURPLE)
            
            continue
            
        elif choice == "3":
            type_text("Dr. Crook shakes his head. 'Interesting thought, but not quite right.'", color=Color.RED)
            type_text("'No arthritis present, and the mucosal changes and lymphadenopathy suggest something else.'", color=Color.YELLOW)
            
            # Internal thought
            type_text("(Your brain: 'I swear I read about this somewhere... was it in that review article?')", color=Color.PURPLE)
            
            continue
            
        elif choice == "4":
            type_text("Dr. Crook sighs deeply. 'In pediatrics, sometimes we need to act before all data is in.'", color=Color.RED)
            type_text("'This child has a time-sensitive condition with risk of serious complications.'", color=Color.YELLOW)
            player["anxiety"] += 10
            player["reputation"] -= 5
            
            # Internal thought
            type_text("(Your brain: 'Analysis paralysis strikes again! Make a decision already!')", color=Color.PURPLE)
            
            continue
            
        else:
            type_text("'Focus, doctor. This child needs a diagnosis now.'", color=Color.RED)

def end_game(win=False):
    """Game ending based on performance"""
    clear_screen()
    print_divider()
    
    # Calculate final score
    score = player["correct_choices"] * 10 + player["reputation"] - player["anxiety"]
    
    if win:
        type_text("CONGRATULATIONS! You correctly diagnosed Kawasaki Disease!", color=Color.GREEN)
        type_text("Dr. Crook nods approvingly. 'Well done. I'll arrange for IVIG infusion right away.'", color=Color.YELLOW)
        type_text("'Time is of the essence with KD. Need to prevent those coronary artery aneurysms.'", color=Color.YELLOW)
        
        if score > 100:
            type_text("'You know, you might be cut out for pediatrics after all.'", color=Color.YELLOW)
            type_text("You've impressed Dr. Crook - a rare achievement indeed!", color=Color.GREEN)
            # Internal thought
            type_text("(Your brain: 'Is this what validation feels like? I should frame this moment.')", color=Color.PURPLE)
        elif score > 50:
            type_text("'Not bad for a student. There's hope for you yet.'", color=Color.YELLOW)
            type_text("Dr. Crook gives you a genuine smile and a nod of respect.", color=Color.GREEN)
            # Internal thought
            type_text("(Your brain: 'I'm going to ride this high for at least a week.')", color=Color.PURPLE)
        else:
            type_text("'You got there eventually, though it was touch and go for a while.'", color=Color.YELLOW)
            type_text("'We'll work on your diagnostic approach. That's why you're here to learn.'", color=Color.YELLOW)
            # Internal thought
            type_text("(Your brain: 'The important thing is I didn't kill anyone. Progress!')", color=Color.PURPLE)
    else:
        type_text("The patient was transferred to the PICU after developing coronary complications.", color=Color.RED)
        type_text("Dr. Crook looks disappointed. 'We'll discuss this further at your evaluation.'", color=Color.RED)
        # Internal thought
        type_text("(Your brain: 'Maybe the hospital cafeteria is hiring...')", color=Color.PURPLE)
    
    print_divider()
    print(f"{Color.CYAN}🏆 FINAL SCORE: {score}{Color.RESET}")
    print(f"{Color.CYAN}Correct Decisions: {player['correct_choices']}{Color.RESET}")
    print(f"{Color.CYAN}Reputation with Dr. Crook: {player['reputation']}{Color.RESET}")
    print(f"{Color.CYAN}Anxiety Level: {player['anxiety']}{Color.RESET}")
    
    # Display collected clinical pearls
    if player["clinical_pearls"]:
        print(f"\n{Color.GREEN}📋 CLINICAL PEARLS COLLECTED: {len(player['clinical_pearls'])}/{len(all_clinical_pearls)}{Color.RESET}")
        for i, pearl in enumerate(player["clinical_pearls"], 1):
            print(f"  {i}. {pearl}")
    
    print_divider()
    
    type_text("Thank you for playing ddxCROOK: KAWASAKI EDITION!", color=Color.PURPLE)
    type_text("Remember, in both pediatrics and coding: careful observation makes all the difference!", color=Color.PURPLE)

def start_game():
    """Game initialization and introduction"""
    clear_screen()
    
    # Display game title ASCII art with color
    print(Color.CYAN + """
    ██████╗ ██████╗ ██╗  ██╗ ██████╗██████╗  ██████╗  ██████╗ ██╗  ██╗
    ██╔══██╗██╔══██╗╚██╗██╔╝██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝
    ██║  ██║██║  ██║ ╚███╔╝ ██║     ██████╔╝██║   ██║██║   ██║█████╔╝ 
    ██║  ██║██║  ██║ ██╔██╗ ██║     ██╔══██╗██║   ██║██║   ██║██╔═██╗ 
    ██████╔╝██████╔╝██╔╝ ██╗╚██████╗██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
    ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                                                     
    """ + Color.RESET)
    
    print_divider()
    type_text("🏥 Welcome to ddxCROOK: A Pediatric Diagnosis Adventure 🏥", color=Color.GREEN)
    type_text("Where every child is a diagnostic puzzle, and every attending is a final boss...", color=Color.CYAN)
    type_text("(and your impostor syndrome is your true nemesis)", color=Color.PURPLE)
        
    player["name"] = input("\nEnter your name, brave medical student: ")
    
    type_text(f"\n[7:15 AM - Pediatric Ward]", color=Color.BLUE)
    type_text("Morning rounds are about to start.")
    type_text(f"You, Dr. {player['name']}, are nervously reviewing your patient list when...")
    type_text(".....")

    type_text("👨‍⚕️ Dr. Crook appears suddenly behind you with uncanny stealth!", color=Color.YELLOW)
    type_text("'Ah, perfect timing. Got an interesting admission overnight.'", color=Color.YELLOW)
    type_text("'5-year-old with quite the constellation of symptoms. Fascinating vitals too.'", color=Color.YELLOW)
    
    # Internal thought
    type_text("(You: 'Why do attendings always appear out of nowhere? Do they teach teleportation in med school?')", color=Color.PURPLE)
    
    scene_transition()
    
    first_decision()

# Start our adventure! 🎮✨
if __name__ == "__main__":
    start_game()
