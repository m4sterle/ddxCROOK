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
    """Dramatic pause between scenes (with user confirmation before clearing!)"""
    input("\n[Press Enter to continue...]\n")
    clear_screen()  # Only clear AFTER the player confirms they're ready

# Game state variables (our patient chart, if you will! 📊)
player = {
    "name": "",
    "anxiety": 0,
    "correct_choices": 0,
    "reputation": 50,
    "diagnosis_hints": [],
    "findings": []  # Track what the player has actually found
}

def print_stats():
    """Displays current player stats with nice formatting"""
    print_divider()
    print(f"Dr. {player['name']}'s Status:")
    print(f"Anxiety Level: {'😰' * (player['anxiety'] // 10)}")
    print(f"Reputation with Dr. Crook: {'⭐' * (player['reputation'] // 10)}")
    print(f"Correct Clinical Decisions: {player['correct_choices']}")
    
    # Show diagnosis hints if we have any
    if player['diagnosis_hints']:
        print("\nDiagnosis Clues: 🔍")
        for hint in player['diagnosis_hints']:
            print(f"  • {hint}")
    
    print_divider()

def first_decision():
    """First interaction with Dr. Crook about the new patient"""
    print_stats()
    
    type_text("What would you like to do?")
    print("\n1. Ask about the vital signs")
    print("2. Review the chart first")
    print("3. Go see the patient immediately")
    print("4. Pretend you didn't hear and keep typing notes*")
    
    while True:
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("Dr. Crook raises an eyebrow, seemingly impressed by your initiative.")
            type_text("'Temperature 39.8°C, HR 130, RR 28, BP 95/60. Make of that what you will.'")
            
            # Add these findings to our tracking
            player["findings"].append("Temp 39.8°C, HR 130, RR 28, BP 95/60")
            
            player["correct_choices"] += 1
            player["diagnosis_hints"].append("High fever with tachycardia")
            
            # Internal thought
            type_text("(Your brain: 'High fever in a kid... infections, rheumatic fever, maybe something auto-inflammatory?')")
            
            scene_transition()
            second_decision()
            break
        elif choice == "2":
            type_text("Dr. Crook sighs dramatically. 'Did I not JUST mention... interesting VITALS? These kids don't have all day, doctor.'")
            player["reputation"] -= 5
            
            # Internal thought
            type_text("(Your brain: 'Great start. Really nailing this whole doctor thing.')")
            continue
        elif choice == "3":
            type_text("Dr. Crook blocks your path with surprising agility.")
            type_text("'Hold up there, speed racer. Perhaps some... pertinent information first?'")
            player["anxiety"] += 10
            
            # Internal thought
            type_text("(Your brain: 'Ah yes, the classic medical student blunder: enthusiasm without information.')")
            continue
        elif choice == "4":
            type_text("*Your typing intensifies nervously*")
            type_text("Dr. Crook: 'I can see you typing 'HELP ME PLEASE' repeatedly.'")
            type_text("'And is that... Zelda you're playing on an emulator? In the pediatric ward?'")
            player["anxiety"] += 20
            player["reputation"] -= 10
            
            # Internal thought
            type_text("(Your brain: 'Maybe if I type fast enough, I'll time travel to graduation...')")
            continue
        else:
            type_text("Dr. Crook frowns. 'That wasn't one of the options, doctor. Kids' health is at stake here.'")

def second_decision():
    """Second decision point after learning about vitals"""
    print_stats()
    
    # Remind the player of the vitals they just learned
    type_text("Dr. Crook taps his clipboard thoughtfully. 'So, given these vitals in a 5-year-old... Temp 39.8°C, HR 130, RR 28, BP 95/60...'")
    
    while True:
        print("\nWhat's your next move?")
        print("\n1. 'How long has the fever persisted?'")
        print("2. *Frantically google 'kid fever fast heart' on your phone*")
        print("3. 'PEDS RAPID RESPONSE!' *Reaches for the emergency button*")
        print("4. 'Let me examine the patient for any rashes or physical findings'")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("'Finally asking the right questions!' Dr. Crook's eyes light up.")
            type_text("'Fever for 5 days now, started at 38.5°C but has been persistently above 39°C'")
            type_text("'Tylenol and Motrin barely touching it. Parents are appropriately freaking out.'")
            
            # Add to our findings
            player["findings"].append("5 days of persistent fever >39°C, poorly responsive to antipyretics")
            
            player["correct_choices"] += 1
            player["reputation"] += 10
            player["diagnosis_hints"].append("Persistent high fever >5 days")
            
            # Internal thought
            type_text("(Your brain: 'Five days of fever resistant to antipyretics... definitely narrowing the differential.')")
            
            scene_transition()
            third_decision()
            break
        elif choice == "2":
            type_text("Dr. Crook: 'Your phone's UpToDate history is... illuminating.'")
            type_text("'Let me see... ah yes, \"OMG HELP FEVER KID DYING\" - very professional, doctor.'")
            player["anxiety"] += 15
            
            # Internal thought
            type_text("(Your brain: 'Maybe I should've gone with the less conspicuous \"kid fever not clickbait\" search.')")
            continue
        elif choice == "3":
            type_text("Dr. Crook physically blocks your path to the button with impressive reflexes.")
            type_text("'Let's not alert the ENTIRE PEDIATRIC FLOOR just yet, shall we?'")
            player["anxiety"] += 25
            player["reputation"] -= 15
            
            # Internal thought
            type_text("(Your brain: 'I swear attendings have a sixth sense for detecting when students are about to do something dumb.')")
            continue
        elif choice == "4":
            type_text("Dr. Crook raises an eyebrow. 'Eager to examine, I see. But perhaps we should learn more about the history first?'")
            type_text("'In pediatrics, a detailed history often guides our physical exam. Let's start there.'")
            
            # Internal thought
            type_text("(Your brain: 'Right... history before physical. Med School 101. Nailing it.')")
            
            continue
        else:
            type_text("Dr. Crook: 'That wasn't one of the options. Again. Kids deserve better focus.'")

def third_decision():
    """Third decision point - examining the patient (with a more comprehensive option)"""
    print_stats()
    
    type_text("You enter the patient's room with Dr. Crook. A miserable-looking 5-year-old boy lies in bed.")
    type_text("His mother looks up anxiously. 'Is there any news, doctors?'")
    type_text("Dr. Crook turns to you expectantly. 'Dr. " + player["name"] + " would like to examine your son.'")
    
    # Internal thought
    type_text("(Your brain: 'No pressure. Just don't mess up in front of the kid, the parent, AND Dr. Crook...')")
    
    while True:
        print("\nHow will you approach the physical exam?")
        print("\n1. 'I'll perform a systematic head-to-toe exam focusing on the diagnostic features of pediatric inflammatory conditions'")
        print("2. Look for specific findings: rashes, oral changes, eye redness, lymph nodes")
        print("3. Focus primarily on the cardiac and respiratory systems")
        print("4. Ask the mother about recent exposures before examining")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1" or choice == "2":
            # Both of these are good approaches to the physical exam
            type_text("Dr. Crook nods approvingly. 'A systematic approach. Very good.'")
            type_text("Your examination reveals:")
            type_text("• Bilateral conjunctival injection without exudate")
            type_text("• Erythema of the lips with a strawberry tongue appearance")
            type_text("• Polymorphous rash over the trunk")
            type_text("• Erythema and edema of the hands and feet")
            type_text("• A single enlarged right cervical lymph node (approximately 1.5 cm)")
            
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
            type_text("(Your brain: 'These are the classic findings! Febrile kid, rash, red eyes, oral changes, extremity changes, lymphadenopathy...')")
            
            scene_transition()
            fourth_decision()
            break
            
        elif choice == "3":
            type_text("You focus on auscultating the heart and lungs.")
            type_text("Dr. Crook observes your technique, then gently suggests, 'Perhaps we should be more systematic in our approach.'")
            type_text("'Remember, in pediatrics, the skin and mucous membranes often hold the diagnostic keys.'")
            
            # Internal thought
            type_text("(Your brain: 'Right... look at the whole patient, not just the vital organs.')")
            
            continue
            
        elif choice == "4":
            type_text("You turn to the mother: 'Has he been around anyone sick recently? Any travel?'")
            type_text("The mother shakes her head. 'No travel. He was at daycare until the fever started.'")
            type_text("'No one else is sick that we know of. He's up-to-date on vaccines.'")
            type_text("Dr. Crook gives you a look. 'Good background, but perhaps we should examine the patient now?'")
            
            # Add this epidemiological finding
            player["findings"].append("No travel history, attends daycare, vaccinations up-to-date")
            
            # Internal thought
            type_text("(Your brain: 'Right... I should probably look at the actual patient.')")
            
            continue
            
        else:
            type_text("Dr. Crook whispers. 'Focus, doctor. The options are right there.'")

def fourth_decision():
    """Fourth decision point - diagnostic approach"""
    print_stats()
    
    # Now Dr. Crook only mentions findings the player actually discovered!
    if player["findings"]:
        type_text("Back at the nursing station, Dr. Crook asks, 'So what's your diagnostic approach?'")
        
        # Create a summary of the findings for Dr. Crook to mention
        # First, get the fever duration finding
        fever_finding = next((f for f in player["findings"] if "fever" in f.lower()), "")
        
        # Then get the physical exam findings
        exam_findings = [f for f in player["findings"] if f not in ["Temp 39.8°C, HR 130, RR 28, BP 95/60", fever_finding] and "no travel" not in f.lower()]
        
        if fever_finding:
            type_text(f"'We have a 5-year-old with {fever_finding},'")
        
        if exam_findings:
            # Format the physical findings nicely
            if len(exam_findings) > 1:
                formatted_findings = ", ".join(exam_findings[:-1]) + ", and " + exam_findings[-1]
            else:
                formatted_findings = exam_findings[0]
                
            type_text(f"'Plus physical findings of {formatted_findings}.'")
    else:
        # Fallback if somehow no findings were recorded
        type_text("Back at the nursing station, Dr. Crook reviews the patient's presentation.")
        type_text("'Let's consider what we know about this febrile 5-year-old.'")
    
    # Internal thought
    type_text("(Your brain is racing through differentials: 'Scarlet fever? Measles? Stevens-Johnson? Wait... Kawasaki?')")
    
    while True:
        print("\nWhat tests would you order?")
        print("\n1. 'CBC with differential, CRP, ESR, and echocardiogram'")
        print("2. 'Blood culture, throat culture, and lumbar puncture'")
        print("3. 'Rapid strep test and mono spot'")
        print("4. 'CT scan of the head and chest X-ray'")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("Dr. Crook's eyes widen with visible approval.")
            type_text("'Excellent choices. Also consider LFTs and urinalysis. Let's monitor those platelets.'")
            
            # Add these tests to our findings
            player["findings"].append("Ordered: CBC with diff, CRP, ESR, LFTs, UA, and echocardiogram")
            
            player["correct_choices"] += 2
            player["reputation"] += 15
            player["diagnosis_hints"].append("Ordered appropriate inflammatory markers and echo")
            
            # Internal thought
            type_text("(Your brain: 'Wait, did I just... impress Dr. Crook? Is this real life?')")
            
            scene_transition()
            final_diagnosis()
            break
            
        elif choice == "2":
            type_text("Dr. Crook tilts his head. 'Infection workup is reasonable, but lumbar puncture?'")
            type_text("'No meningeal signs here. Think broader about the constellation of symptoms.'")
            player["reputation"] -= 5
            
            # Internal thought
            type_text("(Your brain: 'Great, now I'm the med student who wants to do unnecessary LPs on children...')")
            
            continue
            
        elif choice == "3":
            type_text("'Limited testing for a complex presentation. Think bigger picture, doctor.'")
            type_text("'This child has multiple systems involved. What might we be missing?'")
            
            # Internal thought
            type_text("(Your brain: 'The number of ways to look incompetent seems infinite...')")
            
            continue
            
        elif choice == "4":
            type_text("Dr. Crook raises both eyebrows to stratospheric heights.")
            type_text("'Irradiating a child should never be our first approach. What else could we do?'")
            player["anxiety"] += 10
            
            # Internal thought
            type_text("(Your brain: 'Note to self: Don't suggest CT scans for children unless absolutely necessary...')")
            
            continue
            
        else:
            type_text("Dr. Crook sighs. 'Please focus on the options at hand.'")

def final_diagnosis():
    """Final diagnostic moment"""
    print_stats()
    
    # Display test results prominently
    type_text("The next day, Dr. Crook approaches with the test results.")
    print("\n📋 LABORATORY RESULTS:")
    print("- CRP: 120 mg/L (ref: <5)")
    print("- ESR: 80 mm/h (ref: <15)")
    print("- WBC: 15.5 x10^9/L with neutrophilia")
    print("- Hgb: 10.8 g/dL (mild anemia)")
    print("- Platelets: 450,000 (elevated)")
    print("- ALT: 85 U/L, AST: 70 U/L (mild transaminitis)")
    print("- Echo: Pending")
    print()
    
    type_text("Dr. Crook looks at you expectantly. 'Care to make your diagnosis?'")
    
    # Add lab results to our findings
    player["findings"].append("Labs: Elevated CRP/ESR, leukocytosis, mild anemia, thrombocytosis, mild transaminitis")
    
    # Internal thought
    type_text("(Your heart is pounding. 'This is it. Don't mess up now...')")
    
    while True:
        print("\nWhat's your diagnosis?")
        print("\n1. 'This patient has Kawasaki Disease'")
        print("2. 'I believe this is Scarlet Fever'")
        print("3. 'The patient has Juvenile Idiopathic Arthritis with systemic features'")
        print("4. 'I need more tests before making a diagnosis'")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("Dr. Crook breaks into an approving smile!")
            type_text("'Excellent diagnosis, doctor! The patient meets the diagnostic criteria for classic Kawasaki Disease.'")
            type_text("'5+ days of fever plus 4 of the 5 classic criteria: rash, conjunctivitis, oral changes, extremity changes, and cervical lymphadenopathy.'")
            type_text("'We need to start IVIG and high-dose aspirin ASAP to prevent coronary artery aneurysms.'")
            
            # Add diagnosis to our findings
            player["findings"].append("Final diagnosis: Kawasaki Disease")
            player["findings"].append("Treatment plan: IVIG and high-dose aspirin")
            
            player["correct_choices"] += 2
            player["reputation"] += 15
            
            # Internal thought
            type_text("(Your brain: 'I... I did it! I actually diagnosed something correctly!')")
            
            scene_transition()
            end_game(win=True)
            break
            
        elif choice == "2":
            type_text("Dr. Crook's face falls. 'Close, but Scarlet Fever doesn't explain all findings.'")
            type_text("'The conjunctival injection, extremity changes, and persistent fever despite appropriate antibiotics point elsewhere.'")
            player["reputation"] -= 5
            
            # Internal thought
            type_text("(Your brain: 'So close yet so far... what am I missing?')")
            
            continue
            
        elif choice == "3":
            type_text("Dr. Crook shakes his head. 'Interesting thought, but not quite right.'")
            type_text("'No arthritis present, and the mucosal changes and lymphadenopathy suggest something else.'")
            
            # Internal thought
            type_text("(Your brain: 'I swear I read about this somewhere... was it in that review article?')")
            
            continue
            
        elif choice == "4":
            type_text("Dr. Crook sighs deeply. 'In pediatrics, sometimes we need to act before all data is in.'")
            type_text("'This child has a time-sensitive condition with risk of serious complications.'")
            player["anxiety"] += 10
            player["reputation"] -= 5
            
            # Internal thought
            type_text("(Your brain: 'Analysis paralysis strikes again! Make a decision already!')")
            
            continue
            
        else:
            type_text("'Focus, doctor. This child needs a diagnosis now.'")

def end_game(win=False):
    """Game ending based on performance"""
    print_divider()
    
    # Calculate final score
    score = player["correct_choices"] * 10 + player["reputation"] - player["anxiety"]
    
    if win:
        type_text("CONGRATULATIONS! You correctly diagnosed Kawasaki Disease!")
        type_text("Dr. Crook nods approvingly. 'Well done. I'll arrange for IVIG infusion right away.'")
        type_text("'Time is of the essence with KD. Need to prevent those coronary artery aneurysms.'")
        
        if score > 100:
            type_text("'You know, you might be cut out for pediatrics after all.'")
            type_text("You've impressed an attending on rotations - a rare achievement indeed!")
            # Internal thought
            type_text("(Your brain: 'Is this what validation feels like? I should frame this moment.')")
        elif score > 50:
            type_text("'Not bad for a student. There's hope for you yet.'")
            type_text("Dr. Crook gives you a genuine smile and a nod of respect.")
            # Internal thought
            type_text("(Your brain: 'I'm going to ride this high for at least a week.')")
        else:
            type_text("'You got there eventually, though it was touch and go for a while.'")
            type_text("'We'll work on your diagnostic approach. That's why you're here to learn.'")
            # Internal thought
            type_text("(Your brain: 'The important thing is I didn't kill anyone. Progress!')")
    else:
        type_text("The patient was transferred to the PICU after developing coronary complications.")
        type_text("Dr. Crook looks disappointed. 'We'll discuss this further at your evaluation.'")
        # Internal thought
        type_text("(Your brain: 'Maybe the hospital cafeteria is hiring...')")
    
    # Show a summary of what was discovered throughout the game
    print("\n📋 CASE SUMMARY:")
    if player["findings"]:
        for finding in player["findings"]:
            print(f"• {finding}")
    
    print_divider()
    print(f"🏆 FINAL SCORE: {score}")
    print(f"Correct Decisions: {player['correct_choices']}")
    print(f"Reputation with Dr. Crook: {player['reputation']}")
    print(f"Anxiety Level: {player['anxiety']}")
    print_divider()
    
    type_text("Thank you for playing ddxCROOK: KAWASAKI EDITION!")
    type_text("Remember, in both pediatrics and coding: careful observation makes all the difference!")

def start_game():
    """Game initialization and introduction"""
    clear_screen()
    
    # Display game title ASCII art
    print("""
    ██████╗ ██████╗ ██╗  ██╗ ██████╗██████╗  ██████╗  ██████╗ ██╗  ██╗
    ██╔══██╗██╔══██╗╚██╗██╔╝██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝
    ██║  ██║██║  ██║ ╚███╔╝ ██║     ██████╔╝██║   ██║██║   ██║█████╔╝ 
    ██║  ██║██║  ██║ ██╔██╗ ██║     ██╔══██╗██║   ██║██║   ██║██╔═██╗ 
    ██████╔╝██████╔╝██╔╝ ██╗╚██████╗██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
    ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                                                     
    """)
    
    print_divider()
    type_text("🏥 Welcome to ddxCROOK: A Pediatric Diagnosis Adventure 🏥")
    type_text("Where every child is a diagnostic puzzle, and every attending is a final boss...")
    type_text("(and your impostor syndrome is your true nemesis)")
        
    player["name"] = input("\nEnter your name, brave medical student: ")
    
    type_text(f"\n[7:15 AM - Pediatric Ward]")
    type_text("Morning rounds are about to start.")
    type_text(f"You, Dr. {player['name']}, are nervously reviewing your patient list when...")
    type_text(".....")

    type_text("👨‍⚕️ Dr. Crook appears suddenly behind you with uncanny stealth!")
    type_text("'Ah, perfect timing. Got an interesting admission overnight.'")
    type_text("'5-year-old with quite the constellation of symptoms. Fascinating vitals too.'")
    
    # Internal thought
    type_text("(You: 'Why do attendings always appear out of nowhere? Do they teach teleportation in med school?')")
    
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