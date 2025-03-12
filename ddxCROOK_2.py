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
    while True:
        print_stats()
        
        type_text("What would you like to do?")
        print("\n1. Ask about the vital signs")
        print("2. Review the chart first")
        print("3. Go see the patient immediately")
        print("4. Pretend you didn't hear and keep typing notes*")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("Dr. Crook raises an eyebrow, seemingly impressed by your initiative.")
            type_text("'Temperature 39.8°C, HR 130, RR 28, BP 95/60. Make of that what you will.'")
            player["correct_choices"] += 1
            player["diagnosis_hints"].append("High fever with tachycardia")
            second_decision()
            break
        elif choice == "2":
            type_text("Dr. Crook sighs dramatically. 'Did I not JUST mention... interesting VITALS? These kids don't have all day, doctor.'")
            player["reputation"] -= 5
            continue
        elif choice == "3":
            type_text("Dr. Crook blocks your path with surprising agility.")
            type_text("'Hold up there, speed racer. Perhaps some... pertinent information first?'")
            player["anxiety"] += 10
            continue
        elif choice == "4":
            type_text("*Your typing intensifies nervously*")
            type_text("Dr. Crook: 'I can see you typing 'HELP ME PLEASE' repeatedly.'")
            type_text("'And is that... Zelda you're playing on an emulator? In the pediatric ward?'")
            player["anxiety"] += 20
            player["reputation"] -= 10
            continue
        else:
            type_text("Dr. Crook frowns. 'That wasn't one of the options, doctor. Kids' health is at stake here.'")

def second_decision():
    """Second decision point after learning about vitals"""
    clear_screen()
    print_stats()
    
    type_text("Dr. Crook taps his clipboard thoughtfully. 'So, given these vitals in a 5-year-old...'")
    
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
            player["correct_choices"] += 1
            player["reputation"] += 10
            player["diagnosis_hints"].append("Persistent high fever >5 days")
            third_decision()
            break
        elif choice == "2":
            type_text("Dr. Crook: 'Your phone's UpToDate history is... illuminating.'")
            type_text("'Let me see... ah yes, \"OMG HELP FEVER KID DYING\" - very professional, doctor.'")
            player["anxiety"] += 15
            continue
        elif choice == "3":
            type_text("Dr. Crook physically blocks your path to the button with impressive reflexes.")
            type_text("'Let's not alert the ENTIRE PEDIATRIC FLOOR just yet, shall we?'")
            player["anxiety"] += 25
            player["reputation"] -= 15
            continue
        elif choice == "4":
            type_text("Dr. Crook's face brightens. 'Good instinct. Physical exam is key in pediatrics.'")
            type_text("'Come, let's examine our little patient together.'")
            player["correct_choices"] += 1
            player["diagnosis_hints"].append("Examination key in pediatric diagnosis")
            third_decision()
            break
        else:
            type_text("Dr. Crook: 'That wasn't one of the options. Again. Kids deserve better focus.'")

def third_decision():
    """Third decision point - examining the patient"""
    clear_screen()
    print_stats()
    
    type_text("You enter the patient's room with Dr. Crook. A miserable-looking 5-year-old boy lies in bed.")
    type_text("His mother looks up anxiously. 'Is there any news, doctors?'")
    type_text("Dr. Crook turns to you expectantly. 'Dr. " + player["name"] + " would like to examine your son.'")
    
    while True:
        print("\nWhat do you focus on first?")
        print("\n1. Look at the skin for any rashes or peeling")
        print("2. Check the lymph nodes in the neck")
        print("3. Examine the hands, feet, and mucosal surfaces")
        print("4. Ask about recent travel or exposures")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1" or choice == "3":
            if choice == "1":
                type_text("You notice a distinctive polymorphic rash across the trunk and extremities.")
            else:
                type_text("You observe swollen, red hands and feet with some peeling beginning at the fingertips.")
                type_text("When you check the mouth, you see clearly red, cracked lips and a 'strawberry tongue'.")
            
            type_text("Dr. Crook nods approvingly. 'Excellent observation. What else do you see?'")
            type_text("You continue your exam and also note bilateral conjunctival injection without discharge.")
            player["correct_choices"] += 2
            player["reputation"] += 10
            
            if choice == "1":
                player["diagnosis_hints"].append("Polymorphic rash")
            else:
                player["diagnosis_hints"].append("Red hands/feet with peeling + strawberry tongue")
                
            player["diagnosis_hints"].append("Conjunctival injection")
            fourth_decision()
            break
            
        elif choice == "2":
            type_text("You palpate a significantly enlarged lymph node on the right side of the neck.")
            type_text("Dr. Crook chimes in. 'At least 1.5cm. Unilateral cervical lymphadenopathy.'")
            player["correct_choices"] += 1
            player["diagnosis_hints"].append("Unilateral cervical lymphadenopathy")
            fourth_decision()
            break
            
        elif choice == "4":
            type_text("The mother shakes her head. 'No travel. He was at daycare until the fever started.'")
            type_text("'No one else is sick that we know of. He's up-to-date on vaccines.'")
            type_text("Dr. Crook gives you a look. 'Perhaps a physical finding would be more illuminating...'")
            continue
            
        else:
            type_text("Dr. Crook whispers. 'Focus, doctor. The options are right there.'")

def fourth_decision():
    """Fourth decision point - diagnostic approach"""
    clear_screen()
    print_stats()
    
    type_text("Back at the nursing station, Dr. Crook asks, 'So what's your diagnostic approach?'")
    type_text("'We have a 5-year-old with 5 days of fever, rash, red eyes, swollen hands and feet,'")
    type_text("'red lips, strawberry tongue, and unilateral cervical lymphadenopathy.'")
    
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
            player["correct_choices"] += 2
            player["reputation"] += 15
            player["diagnosis_hints"].append("Ordered appropriate inflammatory markers and echo")
            final_diagnosis()
            break
            
        elif choice == "2":
            type_text("Dr. Crook tilts his head. 'Infection workup is reasonable, but lumbar puncture?'")
            type_text("'No meningeal signs here. Think broader about the constellation of symptoms.'")
            player["reputation"] -= 5
            continue
            
        elif choice == "3":
            type_text("'Limited testing for a complex presentation. Think bigger picture, doctor.'")
            type_text("'This child has multiple systems involved. What might we be missing?'")
            continue
            
        elif choice == "4":
            type_text("Dr. Crook raises both eyebrows to stratospheric heights.")
            type_text("'Irradiating a child should never be our first approach. What else could we do?'")
            player["anxiety"] += 10
            continue
            
        else:
            type_text("Dr. Crook sighs. 'Please focus on the options at hand.'")

def final_diagnosis():
    """Final diagnostic moment"""
    clear_screen()
    print_stats()
    
    type_text("The next day, Dr. Crook approaches with the test results.")
    type_text("'Well, the labs are back. CRP 120 mg/L, ESR 80 mm/h, platelets 450,000.'")
    type_text("'CBC shows leukocytosis with neutrophilia, mild anemia, and LFTs show mild transaminitis.'")
    type_text("'Echo pending. Care to make your diagnosis?'")
    
    while True:
        print("\nWhat's your diagnosis?")
        print("\n1. 'This patient has Kawasaki Disease'")
        print("2. 'I believe this is Scarlet Fever'")
        print("3. 'The patient has Juvenile Idiopathic Arthritis with systemic features'")
        print("4. 'I need more tests before making a diagnosis'")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("Dr. Crook breaks into a rare, genuine smile!")
            type_text("'Excellent diagnosis, doctor! Classic presentation meeting clinical criteria.'")
            type_text("'We need to start IVIG and high-dose aspirin ASAP to prevent coronary artery aneurysms.'")
            player["correct_choices"] += 2
            player["reputation"] += 15
            end_game(win=True)
            break
            
        elif choice == "2":
            type_text("Dr. Crook's face falls. 'Close, but Scarlet Fever doesn't explain all findings.'")
            type_text("'The conjunctival injection, extremity changes, and persistent fever despite appropriate antibiotics point elsewhere.'")
            player["reputation"] -= 5
            continue
            
        elif choice == "3":
            type_text("Dr. Crook shakes his head. 'Interesting thought, but not quite right.'")
            type_text("'No arthritis present, and the mucosal changes and lymphadenopathy suggest something else.'")
            continue
            
        elif choice == "4":
            type_text("Dr. Crook sighs deeply. 'In pediatrics, sometimes we need to act before all data is in.'")
            type_text("'This child has a time-sensitive condition with risk of serious complications.'")
            player["anxiety"] += 10
            player["reputation"] -= 5
            continue
            
        else:
            type_text("'Focus, doctor. This child needs a diagnosis now.'")

def end_game(win=False):
    """Game ending based on performance"""
    clear_screen()
    print_divider()
    
    # Calculate final score
    score = player["correct_choices"] * 10 + player["reputation"] - player["anxiety"]
    
    if win:
        type_text("CONGRATULATIONS! You correctly diagnosed Kawasaki Disease!")
        type_text("Dr. Crook nods approvingly. 'Well done. I'll arrange for IVIG infusion right away.'")
        type_text("'Time is of the essence with KD. Need to prevent those coronary artery aneurysms.'")
        
        if score > 100:
            type_text("'You know, you might be cut out for pediatrics after all.'")
            type_text("You've impressed Dr. Crook - a rare achievement indeed!")
        elif score > 50:
            type_text("'Not bad for a student. There's hope for you yet.'")
            type_text("Dr. Crook gives you a genuine smile and a nod of respect.")
        else:
            type_text("'You got there eventually, though it was touch and go for a while.'")
            type_text("'We'll work on your diagnostic approach. That's why you're here to learn.'")
    else:
        type_text("The patient was transferred to the PICU after developing coronary complications.")
        type_text("Dr. Crook looks disappointed. 'We'll discuss this further at your evaluation.'")
    
    print_divider()
    print(f"Final Score: {score}")
    print(f"Correct Decisions: {player['correct_choices']}")
    print(f"Reputation with Dr. Crook: {player['reputation']}")
    print(f"Anxiety Level: {player['anxiety']}")
    print_divider()
    
    type_text("Thank you for playing ddxCROOK!")
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
    type_text("Where every child is a diagnostic puzzle, and Dr. Crook is your witty guide...")
        
    player["name"] = input("\nEnter your name, brave medical student: ")
    
    type_text(f"\n[Dell Medical School - Pediatric Ward]")
    type_text("It's 7:15 AM. Morning rounds are about to start.")
    type_text(f"You, Dr. {player['name']}, are nervously reviewing your patient list when...")
    type_text(".....")

    type_text("👨‍⚕️ Dr. Crook appears suddenly behind you with uncanny stealth!")
    type_text("'Morning, doctor! Got an interesting admission overnight.'")
    type_text("'5-year-old with quite the constellation of symptoms. Fascinating vitals too.'")
    scene_transition()
    
    first_decision()

# Start our adventure! 🎮✨
if __name__ == "__main__":
    start_game()
