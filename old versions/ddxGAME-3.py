import time
import os
import random
from enum import Enum

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
    text = text.replace('\n', ' ').strip()
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

def get_choice(options, prompt="Your choice: "):
    """Get a valid choice from the user"""
    while True:
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        choice = input(f"\n{prompt}")
        
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        else:
            type_text("That wasn't one of the options, doctor. Try again.", color=Color.YELLOW)

class GameState:
    """Class to manage game state"""
    def __init__(self):
        self.player = {
            "name": "",
            "anxiety": 0,
            "correct_choices": 0,
            "reputation": 50,
            "clinical_pearls": [],
            "inventory": []
        }
        
        # Track which scenes the player has visited
        self.visited_scenes = set()
        
        # Clinical pearls the player can collect
        self.all_clinical_pearls = [
            "Pheochromocytoma - classic triad: headaches, sweating, tachycardia",
            "Always check glucose in altered mental status",
            "Silent MIs are more common in diabetic patients",
            "Don't forget to check for orthostatic hypotension",
            "FAST exam: Face, Arms, Speech, Time for stroke",
            "The lower the Glasgow Coma Scale (GCS), the worse the prognosis",
            "Wernicke's aphasia: fluent speech but poor comprehension",
            "Broca's aphasia: non-fluent speech with good comprehension",
            "Heart murmurs that increase with inspiration suggest right-sided pathology",
            "Signs of DVT: unilateral leg swelling, pain, and warmth"
        ]
    
    def print_stats(self):
        """Displays current player stats with nice formatting"""
        print_divider()
        print(f"{Color.BOLD}Dr. {self.player['name']}'s Status:{Color.RESET}")
        print(f"Anxiety Level: {'😰' * (self.player['anxiety'] // 10)}")
        print(f"Reputation with Dr. Rampy: {'⭐' * (self.player['reputation'] // 20)}")
        print(f"Correct Clinical Decisions: {self.player['correct_choices']}")
        
        if self.player['clinical_pearls']:
            print(f"\n{Color.GREEN}📋 Clinical Pearls Collected:{Color.RESET}")
            for i, pearl in enumerate(self.player['clinical_pearls'], 1):
                print(f"  {i}. {pearl}")
        
        if self.player['inventory']:
            print(f"\n{Color.CYAN}🎒 Inventory:{Color.RESET}")
            for item in self.player['inventory']:
                print(f"  - {item}")
        
        print_divider()
    
    def add_clinical_pearl(self):
        """Add a random clinical pearl to the player's collection"""
        available_pearls = [p for p in self.all_clinical_pearls if p not in self.player['clinical_pearls']]
        
        if available_pearls:
            new_pearl = random.choice(available_pearls)
            self.player['clinical_pearls'].append(new_pearl)
            type_text(f"{Color.GREEN}💡 NEW CLINICAL PEARL! 💡{Color.RESET}")
            type_text(f"{Color.GREEN}{new_pearl}{Color.RESET}", pause=1.5)
    
    def scene_transition(self):
        """Dramatic pause between scenes"""
        input(f"\n{Color.PURPLE}[Press Enter to continue your adventure...]{Color.RESET}\n")

def start_game(game_state):
    """Initialize and start the game"""
    clear_screen()
    print(Color.CYAN + """
 ██████╗██╗     ██╗███╗   ██╗██╗ ██████╗ █████╗ ██╗          
██╔════╝██║     ██║████╗  ██║██║██╔════╝██╔══██╗██║          
██║     ██║     ██║██╔██╗ ██║██║██║     ███████║██║          
██║     ██║     ██║██║╚██╗██║██║██║     ██╔══██║██║          
╚██████╗███████╗██║██║ ╚████║██║╚██████╗██║  ██║███████╗     
 ╚═════╝╚══════╝╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝     
                                                              
███████╗██╗███████╗███████╗ ██████╗ ██████╗     ██████╗ ██╗  
██╔════╝██║██╔════╝██╔════╝██╔═══██╗██╔══██╗    ██╔══██╗██║  
█████╗  ██║█████╗  █████╗  ██║   ██║██║  ██║    ██████╔╝██║  
██╔══╝  ██║██╔══╝  ██╔══╝  ██║   ██║██║  ██║    ██╔═══╝ ╚═╝  
██║     ██║██║     ██║     ╚██████╔╝██████╔╝    ██║     ██╗  
╚═╝     ╚═╝╚═╝     ╚═╝      ╚═════╝ ╚═════╝     ╚═╝     ╚═╝  
""" + Color.RESET)
    print_divider()
    type_text("🏥 Welcome to CLINICAL FIASCO: A Medical Student Adventure 🏥", color=Color.GREEN)
    type_text("Where every patient is a puzzle, every attending is a final boss,", color=Color.CYAN)
    type_text("and your impostor syndrome is your true nemesis!", color=Color.CYAN)

    game_state.player["name"] = input("\nEnter your name, brave medical student: ")
    
    # Add welcome item
    game_state.player["inventory"].append("Trusty stethoscope (barely knows how to use it)")
    game_state.player["inventory"].append("Half-eaten protein bar")
    game_state.player["inventory"].append("Pocket Medical Guide (suspiciously coffee-stained)")
    
    type_text(f"\n[Dell Medical School - Internal Medicine Ward]", color=Color.BLUE)
    type_text("It's 6:45 AM. Pre-rounds are about to start.")
    type_text(f"You, Dr. {game_state.player['name']}, are nervously reviewing your patient's chart when...")
    type_text(".....")
    
    type_text("👩‍⚕️ Dr. Rampy appears suddenly behind you!", color=Color.YELLOW)
    type_text("'Ah, perfect timing. New admission in room 2.'", color=Color.YELLOW)
    type_text("'37-year-old woman with... interesting vital signs.'", color=Color.YELLOW)
    game_state.scene_transition()
    
    first_decision(game_state)

def first_decision(game_state):
    """First decision point in the game"""
    clear_screen()
    game_state.print_stats()
    
    type_text("What would you like to do?")
    
    options = [
        "Ask about the vital signs",
        "Review the chart first",
        "Go see the patient immediately",
        "Pretend you didn't hear and keep typing notes"
    ]
    
    choice = get_choice(options)
    
    if choice == 1:
        type_text("Dr. Rampy raises an eyebrow, seemingly impressed by your initiative.", color=Color.GREEN)
        type_text("'BP 178/104, HR 122, Temp 36.3°C. Make of that what you will.'", color=Color.YELLOW)
        game_state.player["correct_choices"] += 1
        # Add a clinical pearl here
        game_state.add_clinical_pearl()
        second_decision(game_state)
    elif choice == 2:
        type_text("Dr. Rampy sighs. 'AHEM, didn't I JUST say... 'interesting VITALS'?! Time is of the essence, doctor.'", color=Color.RED)
        game_state.player["reputation"] -= 5
        game_state.player["anxiety"] += 5
        first_decision(game_state)
    elif choice == 3:
        type_text("Dr. Rampy blocks your path.", color=Color.RED)
        type_text("'Perhaps some... pertinent information first?'", color=Color.YELLOW)
        game_state.player["anxiety"] += 10
        first_decision(game_state)
    elif choice == 4:
        type_text("*Your typing intensifies nervously*")
        type_text("Dr. Rampy: 'I can see you typing 'HELP' repeatedly.'", color=Color.YELLOW)
        type_text("'And is that... Zelda you're playing on an emulator?'", color=Color.YELLOW)
        game_state.player["anxiety"] += 20
        game_state.player["reputation"] -= 10
        first_decision(game_state)

def second_decision(game_state):
    """Second decision point in the game"""
    clear_screen()
    game_state.print_stats()
    
    type_text("Dr. Rampy taps their pen thoughtfully. 'So, given these vital signs...'", color=Color.YELLOW)
    
    options = [
        "'Could we get more history about the headaches?'",
        "*Frantically google 'high BP + tachycardia' on your phone*",
        "'RAPID RESPONSE!' *Reaches for the emergency button*",
        "'Well, when we consider the sympathetic nervous system...'"
    ]
    
    choice = get_choice(options)
    
    if choice == 1:
        type_text("'Ah, finally asking the right questions!' Dr. Rampy's eyes light up.", color=Color.GREEN)
        type_text("'Patient reports episodic symptoms including headache, palpitations, and diaphoresis...'", color=Color.YELLOW)
        game_state.player["correct_choices"] += 1
        game_state.player["reputation"] += 10
        third_decision(game_state)
    elif choice == 2:
        type_text("Dr. Rampy: 'Your phone's UpToDate history is... interesting.'", color=Color.RED)
        type_text("'Let me see... ah yes, \"help attending scary BP high\" - very professional.'", color=Color.YELLOW)
        game_state.player["anxiety"] += 15
        second_decision(game_state)
    elif choice == 3:
        type_text("Dr. Rampy physically blocks your path to the button.", color=Color.RED)
        type_text("'Let's not alert the ENTIRE HOSPITAL just yet, shall we?'", color=Color.YELLOW)
        game_state.player["anxiety"] += 25
        game_state.player["reputation"] -= 15
        second_decision(game_state)
    elif choice == 4:
        type_text("Dr. Rampy's eyebrow raises to previously unknown heights.", color=Color.GREEN)
        type_text("'Going straight for the pathophysiology? Bold choice.'", color=Color.YELLOW)
        game_state.player["correct_choices"] += 1
        third_decision(game_state)

def third_decision(game_state):
    """Third decision point - new addition to the game"""
    clear_screen()
    game_state.print_stats()
    
    type_text("Dr. Rampy hands you the patient's lab results:", color=Color.YELLOW)
    type_text("'Plasma metanephrines are elevated. CBC and BMP are unremarkable.'", color=Color.YELLOW)
    type_text("A medical student named Alex whispers from behind: 'Pssst! I think it's an endocrine thing!'", color=Color.PURPLE)
    
    options = [
        "Suggest pheochromocytoma as a possible diagnosis",
        "Order a CT scan of the abdomen",
        "Consult cardiology first",
        "Ask the patient if they've been taking any medications or supplements"
    ]
    
    choice = get_choice(options)
    
    if choice == 1:
        type_text("'Pheochromocytoma! Very good.' Dr. Rampy nods approvingly.", color=Color.GREEN)
        type_text("'The classic triad of headaches, palpitations, and diaphoresis, along with elevated plasma metanephrines is pretty suggestive.'", color=Color.YELLOW)
        type_text("You feel a surge of confidence. Maybe you do belong in medicine after all!", color=Color.GREEN)
        game_state.player["correct_choices"] += 1
        game_state.player["reputation"] += 15
        game_state.player["anxiety"] -= 10
        # Add a clinical pearl
        game_state.add_clinical_pearl()
        fourth_decision(game_state)
    elif choice == 2:
        type_text("Dr. Rampy tilts her head. 'Not a bad next step, but what's your differential?'", color=Color.YELLOW)
        type_text("You realize you should have formed a hypothesis first.", color=Color.BLUE)
        game_state.player["anxiety"] += 5
        third_decision(game_state)
    elif choice == 3:
        type_text("'Interesting. Why cardiology?' Dr. Rampy asks, genuinely curious.", color=Color.YELLOW)
        type_text("You stammer something about hypertension and tachycardia.", color=Color.BLUE)
        type_text("'Think about the WHOLE clinical picture, doctor.'", color=Color.YELLOW)
        game_state.player["anxiety"] += 10
        third_decision(game_state)
    elif choice == 4:
        type_text("'Good thinking, but the history was already taken,' Dr. Rampy says.", color=Color.YELLOW)
        type_text("'Patient denies any medications, supplements, or illicit drug use.'", color=Color.YELLOW)
        type_text("'What diagnosis are you considering with these symptoms and labs?'", color=Color.YELLOW)
        game_state.player["reputation"] += 5
        third_decision(game_state)

def fourth_decision(game_state):
    """Fourth decision point - case management"""
    clear_screen()
    game_state.print_stats()
    
    type_text("Dr. Rampy turns to the team. 'So now that we have our working diagnosis, what's our management plan?'", color=Color.YELLOW)
    type_text("All eyes turn to you. The senior resident smirks, waiting for you to fail.", color=Color.RED)
    
    options = [
        "Start alpha-blockade with phenoxybenzamine, followed by beta-blockers if needed",
        "Start beta-blockers immediately to control the tachycardia",
        "Recommend immediate surgery to remove the tumor",
        "Start IV fluids and monitor the patient"
    ]
    
    choice = get_choice(options)
    
    if choice == 1:
        type_text("'Excellent!' Dr. Rampy exclaims. 'Starting with alpha-blockade is critical.'", color=Color.GREEN)
        type_text("'Beta-blockade without alpha-blockade could worsen hypertension by blocking vasodilation.'", color=Color.YELLOW)
        type_text("The senior resident's jaw drops in disbelief. You've actually impressed Dr. Rampy!", color=Color.GREEN)
        game_state.player["correct_choices"] += 1
        game_state.player["reputation"] += 20
        game_state.player["anxiety"] -= 15
        # Add a clinical pearl
        game_state.add_clinical_pearl()
        ending(game_state)
    elif choice == 2:
        type_text("Dr. Rampy's eyes widen in alarm. 'STOP! That could be dangerous!'", color=Color.RED)
        type_text("'Beta-blockade without alpha-blockade can lead to a hypertensive crisis in these patients!'", color=Color.YELLOW)
        type_text("You feel your face flush with embarrassment.", color=Color.RED)
        game_state.player["anxiety"] += 20
        game_state.player["reputation"] -= 10
        fourth_decision(game_state)
    elif choice == 3:
        type_text("Dr. Rampy shakes her head. 'While surgery is the definitive treatment, we need medical optimization first.'", color=Color.YELLOW)
        type_text("'What specifically needs to be done before surgery?'", color=Color.YELLOW)
        game_state.player["anxiety"] += 5
        fourth_decision(game_state)
    elif choice == 4:
        type_text("'That's supportive care, but not addressing the underlying issue,' Dr. Rampy notes.", color=Color.YELLOW)
        type_text("'Let's think more specifically about pheo management.'", color=Color.YELLOW)
        game_state.player["anxiety"] += 5
        fourth_decision(game_state)

def ending(game_state):
    """Game ending based on performance"""
    clear_screen()
    game_state.print_stats()
    
    # Calculate overall score
    score = game_state.player["correct_choices"] * 10 + game_state.player["reputation"] - game_state.player["anxiety"]
    
    type_text("As rounds conclude, Dr. Rampy pulls you aside...", color=Color.BLUE)
    
    if score >= 80:
        type_text("'That was impressive work today, Dr. " + game_state.player["name"] + ".'", color=Color.GREEN)
        type_text("'Your clinical reasoning was sound, and your management plan was spot on.'", color=Color.GREEN)
        type_text("'Keep this up, and you might just survive this rotation after all!'", color=Color.GREEN)
        type_text("You've earned the respect of the attending and learned valuable clinical pearls.", color=Color.PURPLE)
        type_text("Who knew all those hours of studying would actually pay off?", color=Color.PURPLE)
    elif score >= 40:
        type_text("'You showed some good instincts today, but there's room for improvement.'", color=Color.YELLOW)
        type_text("'Review the management of pheochromocytoma tonight, and we'll discuss more tomorrow.'", color=Color.YELLOW)
        type_text("It wasn't a disaster, which in medical school counts as a win!", color=Color.PURPLE)
    else:
        type_text("'That was... educational for everyone involved.'", color=Color.RED)
        type_text("'I expect you to read up on endocrine emergencies before tomorrow's rounds.'", color=Color.RED)
        type_text("'And maybe consider switching to radiology...'", color=Color.RED)
        type_text("Well, at least you didn't kill anyone! That's medical student success, right?", color=Color.PURPLE)
    
    print_divider()
    type_text(f"🏆 FINAL SCORE: {score} points", color=Color.CYAN)
    type_text("Thank you for playing CLINICAL FIASCO!", color=Color.GREEN)
    
    # Display collected clinical pearls
    if game_state.player["clinical_pearls"]:
        type_text("📋 CLINICAL PEARLS COLLECTED:", color=Color.GREEN)
        for i, pearl in enumerate(game_state.player["clinical_pearls"], 1):
            print(f"  {i}. {pearl}")
    
    print_divider()
    type_text("Remember: In medicine, as in life, the learning never stops!", color=Color.PURPLE)
    print("\n")

# Start our adventure! 🎮✨
if __name__ == "__main__":
    game_state = GameState()
    start_game(game_state)
