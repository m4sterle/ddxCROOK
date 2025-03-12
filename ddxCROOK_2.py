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
    "confidence": 50,  # Replacing anxiety with confidence (positive framing)
    "correct_choices": 0,
    "learning_points": 0,  # Replacing reputation with learning points
    "diagnosis_hints": []
}

def print_stats():
    """Displays current player stats with nice formatting"""
    print_divider()
    print(f"Confidence Level: {'😊' * (player['confidence'] // 10)}")
    print(f"Learning Points: {'📚' * (player['learning_points'] // 10)}")
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
        
        type_text("Dr. Crook raises an eyebrow. 'So, Dr. " + player["name"] + ", what's your first move?'")
        type_text("'This could either be a brilliant learning moment or an epic disaster. I'm here for either.'")
        
        print("\n1. Ask about the vital signs first")
        print("2. Review the chart before going in")
        print("3. Go introduce yourself to the patient and family")
        print("4. Quietly look for the nearest exit")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("'Ah! Direct and to the point. I like your style,' Dr. Crook says with a grin.")
            type_text("'Temp 39.2°C, RR 32, HR 128, SpO2 91% on room air.'")
            type_text("'In the world of pediatrics, we call these "spicy" vitals.'")
            player["correct_choices"] += 1
            player["learning_points"] += 5
            player["diagnosis_hints"].append("Fever with tachypnea and hypoxemia")
            second_decision()
            break
        elif choice == "2":
            type_text("Dr. Crook nods. 'Doing your homework first, I see. Wise choice.'")
            type_text("'Though I should warn you - the mom has added 14 pages of notes she printed from Facebook groups.'")
            type_text("'5-year-old with fever, increased work of breathing, and oxygen saturation of 91%.'")
            player["learning_points"] += 5
            player["diagnosis_hints"].append("Pediatric respiratory distress")
            second_decision()
            break
        elif choice == "3":
            type_text("'Bold move! Diving in headfirst,' Dr. Crook chuckles.")
            type_text("'I admire your confidence, but perhaps we should strategize before you face the WebMD warrior mom?'")
            type_text("'The chief complaint IS fever and difficulty breathing, by the way.'")
            player["confidence"] -= 5
            player["diagnosis_hints"].append("Pediatric respiratory illness with fever")
            continue
        elif choice == "4":
            type_text("Dr. Crook blocks your path with surprising agility.")
            type_text("'Nice try! I've already told them you're the pediatric prodigy.'")
            type_text("'Besides, I disabled the electronic door locks. There's no escape from learning opportunities!'")
            player["confidence"] -= 10
            player["learning_points"] += 5
            continue
        else:
            type_text("Dr. Crook sighs dramatically. 'I see indecision is our first diagnosis of the day.'")

        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("Dr. Crook nods encouragingly. 'Good instinct for this case.'")
            type_text("'Temp 39.2°C, RR 32, HR 128, SpO2 91% on room air.'")
            type_text("He gives you a thoughtful look. 'What does this tell you?'")
            player["correct_choices"] += 1
            player["diagnosis_hints"].append("Fever with tachypnea and hypoxemia")
            second_decision()
            break
        elif choice == "2":
            type_text("Dr. Crook smiles. 'Always good to be prepared. Let me tell you what we have so far...'")
            type_text("'5-year-old with fever, increased work of breathing, and oxygen saturation of 91%.'")
            player["learning_points"] += 5
            player["diagnosis_hints"].append("Pediatric respiratory distress")
            second_decision()
            break
        elif choice == "3":
            type_text("'I appreciate your patient-centered approach,' Dr. Crook says warmly.")
            type_text("'Let's go in together. But first, any particular concerns based on the chief complaint?'")
            type_text("You hesitate briefly, and Dr. Crook adds, 'This child has fever and difficulty breathing.'")
            player["confidence"] -= 5
            player["diagnosis_hints"].append("Pediatric respiratory illness with fever")
            second_decision()
            break
        elif choice == "4":
            type_text("You quickly check your pediatric quick-reference app.")
            type_text("Dr. Crook notices but doesn't comment negatively.")
            type_text("'It's good to verify your approach. What are you looking for specifically?'")
            player["learning_points"] += 5
            player["confidence"] -= 5
            player["diagnosis_hints"].append("Need to focus on pediatric respiratory conditions")
            second_decision()
            break
        else:
            type_text("Dr. Crook waits patiently. 'Let's focus on the options at hand.'")

def second_decision():
    """Second decision point after learning about vitals"""
    clear_screen()
    print_stats()
    
    type_text("You enter the room with Dr. Crook. A 5-year-old boy named Alex is sitting up in bed, working hard to breathe.")
    type_text("His mother immediately launches into a detailed history. 'It started with a runny nose, then a cough, then THIS.'")
    type_text("She holds up her phone. 'According to my research, it could be pneumonia, tuberculosis, or a rare tropical parasite.'")
    type_text("Dr. Crook whispers to you, 'Welcome to pediatrics, where the parents have already diagnosed AND treated via Google.'")
    
    while True:
        print("\nWhat's your next move?")
        print("\n1. Perform a focused respiratory examination")
        print("2. Ask about vaccination history and daycare attendance")
        print("3. Order a chest X-ray immediately")
        print("4. Tell the mom her WebMD diagnosis is probably right")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("You carefully assess the child's respiratory status.")
            type_text("You note intercostal retractions, crackles in the right lower lobe, and decreased breath sounds.")
            type_text("Dr. Crook gives you a subtle thumbs up. 'Look at you, using your actual medical training instead of WebMD!'")
            player["correct_choices"] += 1
            player["learning_points"] += 10
            player["confidence"] += 10
            player["diagnosis_hints"].append("Right lower lobe crackles and decreased breath sounds")
            third_decision()
            break
        elif choice == "2":
            type_text("The mother launches into a 10-minute monologue about every vaccine, vitamin, and organic food Alex has ever encountered.")
            type_text("'...and we only use non-GMO hand sanitizer,' she concludes.")
            type_text("Dr. Crook coughs pointedly. 'Fascinating social history, but perhaps we should check if the kid can breathe?'")
            player["learning_points"] += 5
            player["diagnosis_hints"].append("Possible school outbreak")
            continue
        elif choice == "3":
            type_text("Dr. Crook raises an eyebrow so high it nearly leaves his forehead.")
            type_text("'Jumping straight to radiation, are we? Bold choice. Very 1950s of you.'")
            type_text("'Maybe we should try using our stethoscopes first? Those fancy things hanging around our necks?'")
            player["confidence"] -= 5
            continue
        elif choice == "4":
            type_text("The mother looks triumphant. 'I KNEW IT! So you agree it could be a rare tropical parasite?'")
            type_text("Dr. Crook facepalms silently behind her, then gives you a death stare.")
            type_text("'What Dr. " + player["name"] + " means is that we'll consider ALL possibilities after a THOROUGH examination.'")
            player["learning_points"] -= 10
            player["confidence"] -= 10
            continue
        else:
            type_text("Dr. Crook whispers, 'The options are right there. Just like the answers on your last exam.'")
    
    while True:
        print("\nWhat's your next move?")
        print("\n1. Perform a focused respiratory examination")
        print("2. Ask about vaccination history and daycare attendance")
        print("3. Order a chest X-ray immediately")
        print("4. Reassure the family that this is probably just a cold")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("You carefully assess the child's respiratory status.")
            type_text("You note intercostal retractions, crackles in the right lower lobe, and decreased breath sounds.")
            type_text("Dr. Crook nods approvingly. 'Excellent examination technique. Very thorough.'")
            player["correct_choices"] += 1
            player["learning_points"] += 10
            player["confidence"] += 10
            player["diagnosis_hints"].append("Right lower lobe crackles and decreased breath sounds")
            third_decision()
            break
        elif choice == "2":
            type_text("The mother reports Alex is up-to-date on all vaccinations and attends kindergarten.")
            type_text("'Several kids in his class have been sick recently,' she adds.")
            type_text("Dr. Crook interjects gently, 'Good contextual information, but let's also focus on the patient's current status.'")
            player["learning_points"] += 5
            player["diagnosis_hints"].append("Possible school outbreak")
            continue
        elif choice == "3":
            type_text("Dr. Crook raises an eyebrow but speaks encouragingly.")
            type_text("'I think we'll likely need imaging, but let's complete our clinical assessment first.'")
            type_text("'What physical findings would help narrow our differential?'")
            player["confidence"] -= 5
            continue
        elif choice == "4":
            type_text("Dr. Crook intervenes tactfully, 'Let's be thorough before offering reassurance.'")
            type_text("He gestures subtly toward the child's retractions and tachypnea.")
            type_text("'What do you notice about his work of breathing?'")
            player["learning_points"] -= 5
            player["confidence"] -= 10
            continue
        else:
            type_text("Dr. Crook waits patiently. 'Let's focus on the clinical scenario.'")

def third_decision():
    """Third decision point - narrowing down the diagnosis"""
    clear_screen()
    print_stats()
    
    type_text("After examining Alex, Dr. Crook turns to you with a theatrical flourish.")
    type_text("'And now, the moment of truth! Your differential diagnosis and plan, doctor?'")
    type_text("He leans in with an exaggerated whisper: 'Remember, the mom is recording this conversation for her blog.'")
    
    while True:
        print("\nWhat would you recommend?")
        print("\n1. 'I'd like a chest X-ray, CBC with differential, and blood culture'")
        print("2. 'Let's start with albuterol and reassess in 20 minutes'")
        print("3. 'We should do a rapid strep test and viral panel first'")
        print("4. 'I suspect a rare tropical parasite - let's consult Dr. Google'")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("'FINALLY!' Dr. Crook exclaims, pretending to faint with relief.")
            type_text("'A med student who actually listened during pulmonology week!'")
            type_text("He turns to the mother: 'See? I told you we occasionally train them properly.'")
            player["correct_choices"] += 2
            player["learning_points"] += 15
            player["confidence"] += 10
            player["diagnosis_hints"].append("Suspecting bacterial pneumonia")
            final_diagnosis()
            break
        elif choice == "2":
            type_text("Dr. Crook tilts his head. 'Interesting. So you think this is primarily bronchospasm?'")
            type_text("'Bold move considering he has a fever of 39.2°C and focal crackles.'")
            type_text("'But hey, who needs antibiotics when you have... *checks notes*... wishful thinking?'")
            player["confidence"] -= 5
            continue
        elif choice == "3":
            type_text("'Ah yes, the shotgun approach to diagnostics,' Dr. Crook nods sagely.")
            type_text("'And while we're at it, maybe we should test for werewolfism? It IS a full moon tonight.'")
            type_text("'But seriously, what about those focal LOWER RESPIRATORY findings we just heard?'")
            player["learning_points"] += 5
            continue
        elif choice == "4":
            type_text("The mother frantically begins typing on her phone.")
            type_text("Dr. Crook steps between you and the family with surprising speed.")
            type_text("'What Dr. " + player["name"] + " means is that we're going to follow EVIDENCE-BASED protocols.'")
            type_text("He whispers to you: 'I can't tell if you're joking or if I should start drafting your dismissal paperwork.'")
            player["learning_points"] -= 10
            player["confidence"] -= 15
            continue
        else:
            type_text("Dr. Crook checks his watch. 'We're losing daylight here. And possibly this patient's lung function.'")

        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("'Excellent plan,' Dr. Crook says with an approving nod.")
            type_text("'And your working diagnosis?'")
            type_text("You confidently reply, 'Community-acquired pneumonia, likely bacterial given the focal findings.'")
            type_text("Dr. Crook smiles. 'Very good reasoning. Let's get those tests.'")
            player["correct_choices"] += 2
            player["learning_points"] += 15
            player["confidence"] += 10
            player["diagnosis_hints"].append("Suspecting bacterial pneumonia")
            final_diagnosis()
            break
        elif choice == "2":
            type_text("Dr. Crook considers this. 'Interesting approach. What makes you think this is bronchospasm?'")
            type_text("He adds gently, 'The focal crackles and fever pattern suggest something else.'")
            player["confidence"] -= 5
            continue
        elif choice == "3":
            type_text("'Those tests might be helpful,' Dr. Crook acknowledges, 'but what about the focal findings on exam?'")
            type_text("'How would you evaluate the lower respiratory tract?'")
            player["learning_points"] += 5
            continue
        elif choice == "4":
            type_text("Dr. Crook looks puzzled. 'What history suggests a foreign body aspiration?'")
            type_text("'And would a 3-day progressive illness be typical for that?'")
            type_text("This is a good teaching moment about clinical reasoning.")
            player["learning_points"] += 5
            player["confidence"] -= 5
            continue
        else:
            type_text("Dr. Crook waits patiently. 'Let's stay focused on the clinical decision.'")

def final_diagnosis():
    """Final diagnostic moment"""
    clear_screen()
    print_stats()
    
    type_text("An hour later, Dr. Crook dramatically slaps the results onto the table in front of you.")
    type_text("Chest X-ray: Right lower lobe infiltrate")
    type_text("CBC: WBC 18,500 with left shift")
    type_text("He strikes a pose. 'Your final answer, Dr. " + player["name"] + "? The child's fate rests in your hands!'")
    
    while True:
        print("\nWhat's your final assessment and plan?")
        print("\n1. 'Bacterial pneumonia - admit for IV antibiotics and oxygen support'")
        print("2. 'Viral pneumonia - supportive care and close observation'")
        print("3. 'Bacterial pneumonia - oral antibiotics and follow-up in 24 hours'")
        print("4. 'Asthma exacerbation with atelectasis - bronchodilators and steroids'")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("Dr. Crook slow claps. 'Ladies and gentlemen, we have a WINNER!'")
            type_text("'Bacterial pneumonia with hypoxemia. Admission, IV antibiotics, supplemental O2.'")
            type_text("'I was starting to worry we'd need to send you back to first-year pathophysiology.'")
            player["correct_choices"] += 2
            player["learning_points"] += 15
            player["confidence"] += 15
            end_game(win=True)
            break
        elif choice == "2":
            type_text("Dr. Crook stares at you. 'Did you... did you actually LOOK at the lab results I just gave you?'")
            type_text("'That WBC count has more left shift than a Bernie Sanders rally.'")
            type_text("'Would you like to reconsider, or should I find a student who passed microbiology?'")
            player["confidence"] -= 5
            continue
        elif choice == "3":
            type_text("'Sooooo close,' Dr. Crook says, making a tiny gap with his fingers.")
            type_text("'You nailed the diagnosis but missed a teeny detail - the kid's oxygen saturation is 91%.'")
            type_text("'Unless you're planning to send him home with his own personal oxygen concentrator?'")
            player["correct_choices"] += 1
            player["learning_points"] += 5
            continue
        elif choice == "4":
            type_text("Dr. Crook looks at the ceiling as if searching for divine patience.")
            type_text("'Right. Because asthma typically presents with high fever and an 18.5 WBC count with left shift.'")
            type_text("'I'm going to pretend I didn't hear that, and you're going to try again.'")
            player["learning_points"] += 5
            continue
        else:
            type_text("Dr. Crook taps his foot impatiently. 'Tick tock, doctor. The antibiotics aren't going to prescribe themselves.'")


def end_game(win=False):
    """Game ending based on performance"""
    clear_screen()
    print_divider()
    
    # Calculate final score
    score = player["correct_choices"] * 10 + player["learning_points"] + player["confidence"]
    
    if win:
        type_text("CONGRATULATIONS! You successfully diagnosed and created an appropriate treatment plan!")
        type_text("Alex is admitted to the pediatric ward for IV antibiotics and supplemental oxygen.")
        type_text("Dr. Crook walks with you as you leave for the day.")
        
        if score > 120:
            type_text("'Not bad, kid. Not bad at all,' Dr. Crook says with genuine approval.")
            type_text("'You actually might survive pediatrics rotation without me having to save you every five minutes.'")
            type_text("'That was some solid clinical reasoning. Keep that up and I might even learn your real name!'")
        elif score > 80:
            type_text("'You know, you're starting to worry me,' Dr. Crook says with a smirk.")
            type_text("'If you keep making good clinical decisions, I'll have to find someone else to torment with my sarcasm.'")
            type_text("'But seriously, nice work today. The kid will be fine because you used your brain.'")
        else:
            type_text("'Well, we got there eventually,' Dr. Crook says with a dramatic sigh.")
            type_text("'It was touch and go for a minute there - I wasn't sure if we'd diagnose the pneumonia before the kid grew up and went to college.'")
            type_text("'But hey, a win is a win. Just maybe... faster next time?'")
    else:
        type_text("The case concludes with Dr. Crook stepping in to make the final management decisions.")
        type_text("'Well, that was... educational,' he says with a wry smile.")
        type_text("'For both of us, really. I've learned that I need to be MUCH more specific in my teaching.'")
        type_text("'And you've learned that pediatric diagnoses rarely include "rare tropical parasites."'")
    
    print_divider()
    print(f"Final Score: {score}")
    print(f"Correct Decisions: {player['correct_choices']}")
    print(f"Learning Points: {player['learning_points']}")
    print(f"Confidence Level: {player['confidence']}")
    print_divider()
    
    type_text("Thank you for playing DDXCrook!")
    type_text("A game created in honor of Dr. Crook's unique mix of sarcasm and support.")
    type_text("May your clinical reasoning be strong and your pimping questions merciful.")


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
                                                                   
██████╗ ███████╗██████╗ ██╗ █████╗ ████████╗██████╗ ██╗ ██████╗   
██╔══██╗██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝██╔══██╗██║██╔════╝   
██████╔╝█████╗  ██║  ██║██║███████║   ██║   ██████╔╝██║██║        
██╔═══╝ ██╔══╝  ██║  ██║██║██╔══██║   ██║   ██╔══██╗██║██║        
██║     ███████╗██████╔╝██║██║  ██║   ██║   ██║  ██║██║╚██████╗   
╚═╝     ╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝   
                                                                   
██████╗ ██╗ █████╗  ██████╗ ███╗   ██╗ ██████╗ ███████╗████████╗██╗ ██████╗███████╗
██╔══██╗██║██╔══██╗██╔════╝ ████╗  ██║██╔═══██╗██╔════╝╚══██╔══╝██║██╔════╝██╔════╝
██║  ██║██║███████║██║  ███╗██╔██╗ ██║██║   ██║███████╗   ██║   ██║██║     ███████╗
██║  ██║██║██╔══██║██║   ██║██║╚██╗██║██║   ██║╚════██║   ██║   ██║██║     ╚════██║
██████╔╝██║██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝███████║   ██║   ██║╚██████╗███████║
╚═════╝ ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝ ╚═════╝╚══════╝
                                                                                     
    """)
    
    print_divider()
    type_text("🏥 Welcome to DDXCrook: A Pediatric Diagnostic Adventure 🏥")
    type_text("Where every child is a puzzle, and Dr. Crook is your supportive mentor...")
        
    player["name"] = input("\nEnter your name, aspiring pediatrician: ")
    
    type_text(f"\n[Texas Children's Hospital - Pediatric Emergency Department]")
    type_text("It's 2:15 PM. A new patient has just arrived.")
    type_text(f"You, Dr. {player['name']}, are reviewing your notes when...")
    type_text(".....")

    type_text("👨‍⚕️ Dr. Crook approaches with a warm smile!")
    type_text("'I have an interesting case I'd like your input on.'")
    type_text("'5-year-old with fever and increased work of breathing.'")
    type_text("'Sounds like a good learning opportunity, don't you think?'")
    scene_transition()
    
    first_decision()

# Start our adventure! 🎮✨
if __name__ == "__main__":
    start_game()