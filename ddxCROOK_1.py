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
        
        type_text("Dr. Crook gestures to the patient's room. 'What approach would you like to take?'")
        print("\n1. Ask about the vital signs first")
        print("2. Review the chart before going in")
        print("3. Go introduce yourself to the patient and family")
        print("4. Check your phone for pediatric guidelines")
        
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
    
    type_text("You enter the room with Dr. Crook. A 5-year-old boy named Alex is sitting up in bed, visibly working to breathe.")
    type_text("His mother explains he's been sick for 3 days, initially with a runny nose and cough that has gotten progressively worse.")
    type_text("Dr. Crook observes quietly as you approach the patient.")
    
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
    
    type_text("After examining Alex, Dr. Crook asks, 'What studies would you like to order?'")
    type_text("'And what's your leading differential diagnosis?'")
    
    while True:
        print("\nWhat would you recommend?")
        print("\n1. 'I'd like a chest X-ray, CBC with differential, and blood culture'")
        print("2. 'Let's start with albuterol and reassess in 20 minutes'")
        print("3. 'We should do a rapid strep test and viral panel first'")
        print("4. 'I think we need a CT scan to rule out a foreign body'")
        
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
    
    type_text("An hour later, Dr. Crook finds you reviewing the results:")
    type_text("Chest X-ray: Right lower lobe infiltrate")
    type_text("CBC: WBC 18,500 with left shift")
    type_text("'So, Dr. " + player["name"] + ", what's your diagnosis and treatment plan?' Dr. Crook asks.")
    
    while True:
        print("\nWhat's your final assessment and plan?")
        print("\n1. 'Bacterial pneumonia - admit for IV antibiotics and oxygen support'")
        print("2. 'Viral pneumonia - supportive care and close observation'")
        print("3. 'Bacterial pneumonia - oral antibiotics and follow-up in 24 hours'")
        print("4. 'Asthma exacerbation with atelectasis - bronchodilators and steroids'")
        
        choice = input("\nYour choice (1-4): ")
        
        if choice == "1":
            type_text("Dr. Crook nods with approval. 'I agree completely.'")
            type_text("'His hypoxemia, focal findings, and elevated WBC with left shift all point to bacterial pneumonia requiring admission.'")
            type_text("'Excellent clinical reasoning throughout this case.'")
            player["correct_choices"] += 2
            player["learning_points"] += 15
            player["confidence"] += 15
            end_game(win=True)
            break
        elif choice == "2":
            type_text("Dr. Crook considers this thoughtfully. 'What about the elevated WBC with left shift?'")
            type_text("'And the focal consolidation? Those typically suggest a bacterial process.'")
            type_text("He's guiding your thinking rather than dismissing your answer.")
            player["confidence"] -= 5
            continue
        elif choice == "3":
            type_text("'You're on the right track with bacterial pneumonia,' Dr. Crook nods.")
            type_text("'But given his oxygen requirement of 91% on room air, what's the appropriate level of care?'")
            player["correct_choices"] += 1
            player["learning_points"] += 5
            continue
        elif choice == "4":
            type_text("Dr. Crook shakes his head gently. 'Let's reconsider the findings.'")
            type_text("'The focal consolidation, fever for days, and elevated WBC with left shift aren't typical for asthma alone.'")
            player["learning_points"] += 5
            continue
        else:
            type_text("Dr. Crook waits patiently. 'Let's focus on making our final assessment.'")

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
            type_text("'That was outstanding clinical reasoning today,' Dr. Crook says warmly.")
            type_text("'You have a real talent for pediatrics - your attention to detail while maintaining the big picture is impressive.'")
            type_text("'I'm looking forward to seeing your growth as a physician.'")
        elif score > 80:
            type_text("'Good work today,' Dr. Crook says with an encouraging smile.")
            type_text("'You're developing solid clinical reasoning skills. Keep connecting the physical findings with your diagnostic thinking.'")
        else:
            type_text("'We got to the right conclusion,' Dr. Crook says supportively.")
            type_text("'Clinical reasoning is a journey. Keep working on linking the examination findings to your differential diagnosis.'")
    else:
        type_text("The case concludes with Dr. Crook guiding the final management decisions.")
        type_text("'Let's take a moment to review the key learning points from this case,' he suggests.")
        type_text("'It's through these challenging cases that we develop our clinical reasoning.'")
    
    print_divider()
    print(f"Final Score: {score}")
    print(f"Correct Decisions: {player['correct_choices']}")
    print(f"Learning Points: {player['learning_points']}")
    print(f"Confidence Level: {player['confidence']}")
    print_divider()
    
    type_text("Thank you for playing DDXCrook!")
    type_text("Remember, both in medicine and coding: practice makes perfect!")
    type_text("This game was created as a thank you to Dr. Crook for his guidance and support.")

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
    
    type_text(f"\n[Dell Children's Hospital - Pediatric Emergency Department]")
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