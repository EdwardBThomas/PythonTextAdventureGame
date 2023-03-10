import random
import time


def prompt(content):
    print(content)
    time.sleep(.1)


unemployed = ["dragon", "gnome", "dwarf", "halfling", "elf", "sprite"]
business_owner = ["gorgon", "troll", "minotaur", "giant", "draugr",
                  "hobgoblin", "goblin", "rakshasi"]
business = ["bar", "tavern", "church", "speakeasy", "printer", "cafe",
            "foundry", "dock", "warehouse"]
dwelling = ["house", "hut", "townhouse", "manse", "bungalo", "chalet",
            "cottage", "brownstone", "cabin"]
briefcase = []


def valid_input(choice, options):
    while True:
        response = input(choice).lower()
        if response in options:
            return response
        else:
            prompt(f"'{response}' makes no sense. Focus, chachi, you're "
                   f"on the job.")


def intro():
    global recipient
    recipient = random.choice(unemployed)
    global establishment
    establishment = random.choice(business)
    global taxed
    taxed = random.choice(business_owner)
    global residence
    residence = random.choice(dwelling)
    prompt("You are the Taxman.\n")
    prompt("Today's job is collect and distribute unemployment money.\n")
    prompt(f"Your next case is an unemployed {recipient} here in town.\n")
    prompt("But you spent most of yesterday's collections at the ponies.\n")
    prompt("l(ツ)∫\n")


def collect():
    prompt(f"You barge into the {establishment}.\n")
    prompt("The Taxman cometh!\n")
    prompt("A 'help wanted' sign clatters to the floor.\n")
    prompt(f"The {taxed} running the place glares at you.\n")
    prompt("But hands over the coins regardless.\n")
    prompt("You walk out. Like a boss.\n")
    briefcase.append("coins")


def collect_after():
    if "coins" not in briefcase:
        collect()
    else:
        prompt(
            f"As you look into the window, the {taxed} puts up a new sign.\n")
        prompt("'Closing early due to shortage of staff and money.'\n")
        prompt(f"The {taxed} gives you a look, something like...\n")
        prompt("ಠ_ಠ\n")
        prompt(
            "Good thing you got the money before they closed for the day.\n")


def distribute_intro():
    prompt(f"You knock on the door of the {residence}.\n")
    prompt(f"Out steps the {recipient}.\n")
    prompt("You go to open your briefcase.\n")
    distribute()


def distribute():
    distribute_choice = valid_input(
        f"Type 'distribute' to give the tax money to the {recipient}.\n"
        "Type 'collect' to find some more tax money.\n", ['distribute',
                                                          'collect'])
    if distribute_choice == 'distribute':
        if 'coins' in briefcase:
            prompt(f"You give the {recipient} the unemployment money.\n")
            prompt(
                f"So in summery, you made the {taxed} at the {establishment} "
                "pay to keep it understaffed...\n")
            prompt(f"...by paying the {recipient} to remain unemployed.\n")
            prompt("Walking away, you start to wonder if you might not be "
                   "the bad guy...\n")
            next_case()
        else:
            prompt("You look in your briefcase.\n")
            prompt("There is not enough collected to pay out the "
                   "unemployment money.\n")
            prompt("You feel like a baffoon.\n")
            prompt(f"Maybe try the {establishment}? The one with the 'help "
                   f"wanted' sign out front.\n")
            prompt("If they aren't paying an employee, they can afford the "
                   "tax money.\n")
            prompt(f"You know, for the unemployed {recipient}.\n")
            prompt("Brilliant!\n")
            street()
    elif distribute_choice == 'collect':
        prompt(f"You leave the {residence}, determined to find that "
               f"cheddar.\n")
        street()


def street():
    prompt(f"Across the street from one another are a {establishment} and a"
           f" {residence}.\n")
    street_choice = valid_input(f"Enter 'residence' to knock on the door of "
                                f"the {residence}.\n"
                                f"Enter 'establishment' to barge into the"
                                f" {establishment}.\n", ['residence',
                                                         'establishment'])
    if street_choice == 'residence':
        distribute_intro()
        distribute()
        next_case()

    elif street_choice == 'establishment':
        collect_after()
        street()


def next_case():
    play_again = valid_input("Type 'next' if you want to take another case.\n"
                             "Type 'quit' if you want to quit this job (and "
                             "the game).\n", ['next', 'quit'])
    if play_again == "next":
        prompt("Yes man, money go BRRRR.\n")
        briefcase.remove("coins")
        intro()
        street()
    elif play_again == "quit":
        prompt("It dawns on you, the whole time the monsters weren't the "
               "ones getting taxed...\n")
        prompt("It was the one doing the taxing.\n")
        prompt("You self-terminate by uttering the sacred tech-prayer:\n")
        exit(0)


intro()
street()
