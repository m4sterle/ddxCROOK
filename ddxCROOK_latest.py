import time
import os
import random

# Simple color class that works on most terminals
class Color:
    """ANSI color codes for terminal text"""
    RED = '\033[91m'      # Errors and negative feedback
    GREEN = '\033[92m'    # Success and positive feedback
    YELLOW = '\033[93m'   # Dr. Crook's dialogue
    BLUE = '\033[94m'     # Patient/family dialogue and scenario
    PURPLE = '\033[95m'   # Player's internal thoughts (lighter shade)
    CYAN = '\033[96m'     # Game UI elements
    RESET = '\033[0m'     # Reset color
    BOLD = '\033[1m'      # Bold text for emphasis

# ======= HINT SYSTEM =======
# Clinical pearls hints dictionary - organized by diagnosis
hints_dict = {
    "kawasaki": [
        "Does... 'CRASH & BURN' ring a bell?! 👀",
        "This disease typically affects wee lads under 5 years old.",
        "The strawberry tongue is a distinctive finding... 🍓",
        "Coronary artery aneurysms are the most serious complication.",
        "Fever lasting more than 5 days is a key diagnostic criterion."
    ]
}

# Track hint usage
hints_used = 0
max_hints = 3

def provide_hint(current_case="kawasaki"):
    """Provides a clinical pearl hint for the current case"""
    global hints_used
    if hints_used >= max_hints:
        type_text("⚠️ NO MORE HINTS!", color=Color.RED)
        return
        
    hints_used += 1
    remaining = max_hints - hints_used
    
    # Get a random hint that hasn't been used yet (if possible)
    used_hints = player.get("hints_received", [])
    available_hints = [h for h in hints_dict.get(current_case.lower(), []) if h not in used_hints]
    
    # If we've used all unique hints, just get a random one
    if not available_hints and hints_dict.get(current_case.lower()):
        hint = random.choice(hints_dict[current_case.lower()])
    elif available_hints:
        hint = random.choice(available_hints)
        # Track this hint as used
        if "hints_received" not in player:
            player["hints_received"] = []
        player["hints_received"].append(hint)
    else:
        hint = "Focus on the pattern of symptoms and their timing. Consider the patient demographics."
    
    # Display the hint with proper formatting
    print_divider()
    type_text(f"💡 CLINICAL PEARL ({remaining} hints remaining)", color=Color.GREEN + Color.BOLD)
    type_text(f"{hint}", color=Color.GREEN)
    print_divider()
# ======= END HINT SYSTEM =======

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
    """Dramatic pause between scenes (with user confirmation before clearing!)"""
    input(f"\n{Color.CYAN}[Press Enter to continue...]{Color.RESET}\n")
    clear_screen()  # Only clear AFTER the player confirms they're ready

# Game state variables (our patient chart, if you will! 📊)
player = {
    "name": "",
    "anxiety": 0,
    "correct_choices": 0,
    "reputation": 50,
    "diagnosis_hints": [],
    "findings": [],  # Track what the player has actually found
    "hints_received": []  # Track which hints the player has seen
}

def print_stats():
    """Displays current player stats with nice formatting"""
    print_divider()
    print(f"{Color.BOLD}Dr. {player['name']}'s Status:{Color.RESET}")
    print(f"Anxiety Level: {'😰' * (player['anxiety'] // 10)}")
    print(f"Reputation with Dr. Crook: {'⭐' * (player['reputation'] // 10)}")
    print(f"Correct Clinical Decisions: {player['correct_choices']}")
    
    # Show diagnosis hints if we have any
    if player['diagnosis_hints']:
        print(f"\n{Color.CYAN}Diagnosis Clues: 🔍{Color.RESET}")
        for hint in player['diagnosis_hints']:
            print(f"  • {hint}")
    
    # Show available help options
    print(f"\n{Color.CYAN}Available Actions:{Color.RESET}")
    print(f"  • Type your choice number as usual")
    print(f"  • Type 'hint' to get a clinical pearl ({max_hints - hints_used} remaining)")
    
    print_divider()

def first_decision():
    """First interaction with Dr. Crook about the new patient"""
    print_stats()
    
    type_text("What would you like to do?", color=Color.CYAN)
    print("\n1. Ask about the vital signs")
    print("2. Review the chart first")
    print("3. Go see the patient immediately")
    print("4. Pretend you didn't hear and keep typing notes*")
    
    while True:
        choice = input("\nYour choice (1-4 or 'hint'): ").lower().strip()
        
        if choice == "hint":
            provide_hint()
            continue
            
        elif choice == "1":
            type_text("Dr. Crook raises an eyebrow, seemingly impressed by your initiative.", color=Color.GREEN)
            type_text("'Temperature 39.8°C, HR 130, RR 28, BP 95/60. Make of that what you will.'", color=Color.YELLOW)
            
            # Add these findings to our tracking
            player["findings"].append("Temp 39.8°C, HR 130, RR 28, BP 95/60")
            
            player["correct_choices"] += 1
            player["diagnosis_hints"].append("High fever with tachycardia")
            
            # Internal thought
            type_text("(Your brain: 'High fever in a kid... infections, rheumatic fever, maybe something auto-inflammatory?')", color=Color.PURPLE)
            
            scene_transition()
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
            type_text("*Your typing intensifies nervously*", color=Color.RED)
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
    print_stats()
    
    # Remind the player of the vitals they just learned
    type_text("Dr. Crook taps his clipboard thoughtfully. 'So, given these vitals in a 5-year-old... Temp 39.8°C, HR 130, RR 28, BP 95/60...'", color=Color.YELLOW)
    
    while True:
        print("\nWhat's your next move?")
        print("\n1. 'How long has the fever persisted?'")
        print("2. *Frantically google 'kid fever fast heart' on your phone*")
        print("3. 'PEDS RAPID RESPONSE!' *Reaches for the emergency button*")
        print("4. 'Let me examine the patient for any rashes or physical findings'")
        
        choice = input("\nYour choice (1-4 or 'hint'): ").lower().strip()
        
        if choice == "hint":
            provide_hint()
            continue
            
        elif choice == "1":
            type_text("'Finally asking the right questions!' Dr. Crook's eyes light up.", color=Color.GREEN)
            type_text("'Fever for 5 days now, started at 38.5°C but has been persistently above 39°C'", color=Color.YELLOW)
            type_text("'Tylenol and Motrin barely touching it. Parents are appropriately freaking out.'", color=Color.YELLOW)
            
            # Add to our findings
            player["findings"].append("5 days of persistent fever >39°C, poorly responsive to antipyretics")
            
            player["correct_choices"] += 1
            player["reputation"] += 10
            player["diagnosis_hints"].append("Persistent high fever >5 days")
            
            # Internal thought
            type_text("(Your brain: 'Five days of fever resistant to antipyretics... definitely narrowing the differential.')", color=Color.PURPLE)
            
            scene_transition()
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
            type_text("(Your brain: 'I swear attendings have a sixth sense for detecting when students are about to do something dumb.')", color=Color.PURPLE)
            continue
        elif choice == "4":
            type_text("Dr. Crook raises an eyebrow. 'Eager to examine, I see. But perhaps we should learn more about the history first?'", color=Color.YELLOW)
            type_text("'In pediatrics, a detailed history often guides our physical exam. Let's start there.'", color=Color.YELLOW)
            
            # Internal thought
            type_text("(Your brain: 'Right... history before physical. Med School 101. Nailing it.')", color=Color.PURPLE)
            
            continue
        else:
            type_text("Dr. Crook: 'That wasn't one of the options. Again. Kids deserve better focus.'", color=Color.RED)

def third_decision():
    """Third decision point - examining the patient (with a more comprehensive option)"""
    print_stats()
    
    type_text("You enter the patient's room with Dr. Crook. A miserable-looking 5-year-old boy lies in bed.", color=Color.BLUE)
    type_text("His mother looks up anxiously. 'Is there any news, doctors?'", color=Color.BLUE)
    type_text("Dr. Crook turns to you expectantly. 'Dr. " + player["name"] + " would like to examine your son.'", color=Color.YELLOW)
    
    # Internal thought
    type_text("(Your brain: 'No pressure. Just don't mess up in front of the kid, the parent, AND Dr. Crook...')", color=Color.PURPLE)
    
    while True:
        print("\nHow will you approach the physical exam?")
        print("\n1. 'I'll perform a systematic head-to-toe exam focusing on the diagnostic features of pediatric inflammatory conditions'")
        print("2. Look for specific findings: rashes, oral changes, eye redness, lymph nodes")
        print("3. Focus primarily on the cardiac and respiratory systems")
        print("4. Ask the mother about recent exposures before examining")
        
        choice = input("\nYour choice (1-4 or 'hint'): ").lower().strip()
        
        if choice == "hint":
            provide_hint()
            continue
            
        elif choice == "1":
            # Only choice 1 is correct now - matches the systematic approach a clinician should take
            type_text("Dr. Crook nods approvingly. 'A systematic approach. Very good.'", color=Color.GREEN)
            type_text("Your examination reveals:", color=Color.CYAN)
            print(Color.BOLD + "• Bilateral conjunctival injection without exudate" + Color.RESET)
            print(Color.BOLD + "• Erythema of the lips with a strawberry tongue appearance" + Color.RESET)
            print(Color.BOLD + "• Polymorphous rash over the trunk" + Color.RESET)
            print(Color.BOLD + "• Erythema and edema of the hands and feet" + Color.RESET)
            print(Color.BOLD + "• A single enlarged right cervical lymph node (approximately 1.5 cm)" + Color.RESET)
            print()  # Extra spacing for readability
            
            # Add all these findings to our tracking
            player["findings"].extend([
                "bilateral conjunctival injection",
                "erythema of lips and strawberry tongue",
                "polymorphous rash",
                "erythema and edema of hands and feet", 
                "unilateral cervical lymphadenopathy"
            ])
            
            player["correct_choices"] += 2
            player["reputation"] += 10
            
            # Add several diagnosis hints based on the comprehensive exam
            player["diagnosis_hints"].append("Mucocutaneous findings: polymorphic rash, conjunctival injection")
            player["diagnosis_hints"].append("Extremity changes: red, edematous hands and feet")
            player["diagnosis_hints"].append("Oral changes: red lips and strawberry tongue")
            player["diagnosis_hints"].append("Unilateral cervical lymphadenopathy >1.5cm")
            
            # Internal thought
            type_text("(Your brain: 'These are the classic findings! Febrile kid, rash, red eyes, oral changes, extremity changes, lymphadenopathy...')", color=Color.PURPLE)
            
            scene_transition()
            fourth_decision()
            break
            
        elif choice == "2":
            type_text("Dr. Crook watches you. 'While those are important areas, a more structured approach would be better.'", color=Color.YELLOW)
            type_text("'Remember what we learned about systematic examination in pediatric patients.'", color=Color.YELLOW)
            
            # Internal thought
            type_text("(Your brain: 'I need to be more organized in my approach to pick up all the findings...')", color=Color.PURPLE)
            
            continue
            
        elif choice == "3":
            type_text("You focus on auscultating the heart and lungs.", color=Color.BLUE)
            type_text("Dr. Crook observes your technique, then gently suggests, 'Perhaps we should be more systematic in our approach.'", color=Color.YELLOW)
            type_text("'Remember, in pediatrics, the skin and mucous membranes often hold the diagnostic keys.'", color=Color.YELLOW)
            
            # Internal thought
            type_text("(Your brain: 'Right... look at the whole patient, not just the vital organs.')", color=Color.PURPLE)
            
            continue
            
        elif choice == "4":
            type_text("You turn to the mother: 'Has he been around anyone sick recently? Any travel?'", color=Color.BLUE)
            type_text("The mother shakes her head. 'No travel. He was at daycare until the fever started.'", color=Color.BLUE)
            type_text("'No one else is sick that we know of. He's up-to-date on vaccines.'", color=Color.BLUE)
            type_text("Dr. Crook gives you a look. 'Good background, but perhaps we should examine the patient now?'", color=Color.YELLOW)
            
            # Add this epidemiological finding
            player["findings"].append("No travel history, attends daycare, vaccinations up-to-date")
            
            # Internal thought
            type_text("(Your brain: 'Right... I should probably look at the actual patient.')", color=Color.PURPLE)
            
            continue
            
        else:
            type_text("Dr. Crook whispers. 'Focus, doctor. The options are right there.'", color=Color.RED)

def fourth_decision():
    """Fourth decision point - diagnostic approach"""
    print_stats()
    
    # Now Dr. Crook only mentions findings the player actually discovered!
    if player["findings"]:
        type_text("Back at the nursing station, Dr. Crook asks, 'So what's your diagnostic approach?'", color=Color.YELLOW)
        
        # Create a summary of the findings for Dr. Crook to mention
        # First, get the fever duration finding
        fever_finding = next((f for f in player["findings"] if "fever" in f.lower()), "")
        
        # Then get the physical exam findings
        exam_findings = [f for f in player["findings"] if f not in ["Temp 39.8°C, HR 130, RR 28, BP 95/60", fever_finding] and "no travel" not in f.lower()]
        
        if fever_finding:
            type_text(f"'We have a 5-year-old with {fever_finding},'", color=Color.YELLOW)
        
        if exam_findings:
            # Format the physical findings nicely
            if len(exam_findings) > 1:
                formatted_findings = ", ".join(exam_findings[:-1]) + ", and " + exam_findings[-1]
            else:
                formatted_findings = exam_findings[0]
                
            type_text(f"'Plus physical findings of {formatted_findings}.'", color=Color.YELLOW)
    else:
        # Fallback if somehow no findings were recorded
        type_text("Back at the nursing station, Dr. Crook reviews the patient's presentation.", color=Color.YELLOW)
        type_text("'Let's consider what we know about this febrile 5-year-old.'", color=Color.YELLOW)
    
    # Internal thought
    type_text("(Your brain is racing through differentials: 'Scarlet fever? Measles? Stevens-Johnson? Wait... Kawasaki?')", color=Color.PURPLE)
    
    while True:
        print("\nWhat tests would you order?")
        print("\n1. 'CBC with differential, CRP, ESR, and echocardiogram'")
        print("2. 'Blood culture, throat culture, and lumbar puncture'")
        print("3. 'Rapid strep test and mono spot'")
        print("4. 'CT scan of the head and chest X-ray'")
        
        choice = input("\nYour choice (1-4 or 'hint'): ").lower().strip()
        
        if choice == "hint":
            provide_hint()
            continue
            
        elif choice == "1":
            type_text("Dr. Crook's eyes widen with visible approval.", color=Color.GREEN)
            type_text("'Excellent choices. Also consider LFTs and urinalysis. Let's monitor those platelets.'", color=Color.YELLOW)
            
            # Add these tests to our findings
            player["findings"].append("Ordered: CBC with diff, CRP, ESR, LFTs, UA, and echocardiogram")
            
            player["correct_choices"] += 2
            player["reputation"] += 15
            player["diagnosis_hints"].append("Ordered appropriate inflammatory markers and echo")
            
            # Internal thought
            type_text("(Your brain: 'Wait, did I just... impress Dr. Crook? Is this real life?')", color=Color.PURPLE)
            
            scene_transition()
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
    print_stats()
    
    # Display test results prominently
    type_text("The next day, Dr. Crook approaches with the test results.", color=Color.YELLOW)
    
    print(Color.BOLD + "\n📋 LABORATORY RESULTS:" + Color.RESET)
    print(Color.BOLD + "- CRP: 120 mg/L (ref: <5)" + Color.RESET)
    print(Color.BOLD + "- ESR: 80 mm/h (ref: <15)" + Color.RESET)
    print(Color.BOLD + "- WBC: 15.5 x10^9/L with neutrophilia" + Color.RESET)
    print(Color.BOLD + "- Hgb: 10.8 g/dL (mild anemia)" + Color.RESET)
    print(Color.BOLD + "- Platelets: 450,000 (elevated)" + Color.RESET)
    print(Color.BOLD + "- ALT: 85 U/L, AST: 70 U/L (mild transaminitis)" + Color.RESET)
    print(Color.BOLD + "- Echo: Pending" + Color.RESET)
    print()
    
    type_text("Dr. Crook looks at you expectantly. 'Care to make your diagnosis?'", color=Color.YELLOW)
    
    # Add lab results to our findings
    player["findings"].append("Labs: Elevated CRP/ESR, leukocytosis, mild anemia, thrombocytosis, mild transaminitis")
    
    # Internal thought
    type_text("(Your heart is pounding. 'This is it. Don't mess up now...')", color=Color.PURPLE)
    
    while True:
        print("\nWhat's your diagnosis?")
        print("\n1. 'This patient has Kawasaki Disease'")
        print("2. 'I believe this is Scarlet Fever'")
        print("3. 'The patient has Juvenile Idiopathic Arthritis with systemic features'")
        print("4. 'I need more tests before making a diagnosis'")
        
        choice = input("\nYour choice (1-4 or 'hint'): ").lower().strip()
        
        if choice == "hint":
            provide_hint()
            continue
            
        elif choice == "1":
            type_text("Dr. Crook breaks into an approving smile!", color=Color.GREEN)
            type_text("'Excellent diagnosis, doctor! The patient meets the diagnostic criteria for classic Kawasaki Disease.'", color=Color.YELLOW)
            type_text("'5+ days of fever plus 4 of the 5 classic criteria: rash, conjunctivitis, oral changes, extremity changes, and cervical lymphadenopathy.'", color=Color.YELLOW)
            type_text("'We need to start IVIG and high-dose aspirin ASAP to prevent coronary artery aneurysms.'", color=Color.YELLOW)
            
            # Add diagnosis to our findings
            player["findings"].append("Final diagnosis: Kawasaki Disease")
            player["findings"].append("Treatment plan: IVIG and high-dose aspirin")
            
            player["correct_choices"] += 2
            player["reputation"] += 15
            
            # Internal thought
            type_text("(Your brain: 'I... I did it! I actually diagnosed something correctly!')", color=Color.PURPLE)
            
            scene_transition()
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
    print_divider()
    
    # Calculate final score
    score = player["correct_choices"] * 10 + player["reputation"] - player["anxiety"]
    
    if win:
        type_text("CONGRATULATIONS! You correctly diagnosed Kawasaki Disease!", color=Color.GREEN)
        type_text("Dr. Crook nods approvingly. 'Well done. I'll arrange for IVIG infusion right away.'", color=Color.YELLOW)
        type_text("'Time is of the essence with KD. Need to prevent those coronary artery aneurysms.'", color=Color.YELLOW)
        
        if score > 100:
            type_text("'You know, you might be cut out for pediatrics after all.'", color=Color.YELLOW)
            type_text("You've impressed an attending on rotations - a rare achievement indeed!", color=Color.GREEN)
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
        type_text("Dr. Crook looks disappointed. 'We'll discuss this further at your evaluation.'", color=Color.YELLOW)
        # Internal thought
        type_text("(Your brain: 'Maybe the hospital cafeteria is hiring...')", color=Color.PURPLE)
    
    # Show a summary of what was discovered throughout the game
    print("\n📋 CASE SUMMARY:")
    if player["findings"]:
        for finding in player["findings"]:
            print(f"• {finding}")
    
    print_divider()
    print(Color.CYAN + f"🏆 FINAL SCORE: {score}" + Color.RESET)
    print(Color.CYAN + f"Correct Decisions: {player['correct_choices']}" + Color.RESET)
    print(Color.CYAN + f"Reputation with Dr. Crook: {player['reputation']}" + Color.RESET)
    print(Color.CYAN + f"Anxiety Level: {player['anxiety']}" + Color.RESET)
    print(Color.CYAN + f"Clinical Pearls Used: {hints_used}/{max_hints}" + Color.RESET)
    print_divider()
    
    # Display all available clinical pearls at the end for educational purposes
    if win:
        print(Color.GREEN + "\n📚 CLINICAL PEARLS FOR KAWASAKI DISEASE:" + Color.RESET)
        for i, pearl in enumerate(hints_dict["kawasaki"], 1):
            print(f"{i}. {pearl}")
        print()
    
    type_text("Thank you for playing ddxCROOK: KAWASAKI EDITION!", color=Color.GREEN)
    type_text("Remember, in both pediatrics and coding: careful observation makes all the difference!", color=Color.GREEN)

def start_game():
    """Game initialization and introduction"""
    clear_screen()
    
    # Display game title ASCII art with color
    print(Color.CYAN + """
     █████     █████               █████████  ███████████      ███████       ███████    █████   ████
    ░░███     ░░███               ███░░░░░███░░███░░░░░███   ███░░░░░███   ███░░░░░███ ░░███   ███░ 
  ███████   ███████  █████ █████ ███     ░░░  ░███    ░███  ███     ░░███ ███     ░░███ ░███  ███   
 ███░░███  ███░░███ ░░███ ░░███ ░███          ░██████████  ░███      ░███░███      ░███ ░███████    
░███ ░███ ░███ ░███  ░░░█████░  ░███          ░███░░░░░███ ░███      ░███░███      ░███ ░███░░███   
░███ ░███ ░███ ░███   ███░░░███ ░░███     ███ ░███    ░███ ░░███     ███ ░░███     ███  ░███ ░░███  
░░████████░░████████ █████ █████ ░░█████████  █████   █████ ░░░███████░   ░░░███████░   █████ ░░████
 ░░░░░░░░  ░░░░░░░░ ░░░░░ ░░░░░   ░░░░░░░░░  ░░░░░   ░░░░░    ░░░░░░░       ░░░░░░░    ░░░░░   ░░░░ 
    """ + Color.RESET)
    
    print_divider()
    type_text("🏥 Welcome to ddxCROOK: A Pediatric Diagnosis Adventure 🏥", color=Color.GREEN)
    type_text("Where every child is a diagnostic puzzle, and every attending is a final boss...", color=Color.CYAN)
    type_text("(and your impostor syndrome is your true nemesis)", color=Color.PURPLE)
    type_text("NEW FEATURE: Type 'hint' at any decision point to get a clinical pearl! (3 available per game)", color=Color.GREEN + Color.BOLD)
        
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
    try:
        start_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\n\nAn error occurred: {e}")
        print("Sorry about that! Please report this bug.")
