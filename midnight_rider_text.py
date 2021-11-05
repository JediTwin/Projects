# Constants

INTRODUCTION = """Welcome to Midnight Rider.

WE"VE STOLEN A CAR. WE NEED TO GET IT HOME.
THE CAR IS SPECIAL.

THAT'S WHY THE GOVERNMENT WANTS IT.

WE CAN'T LET THEM HAVE IT.

ONE GOAL: SURVIVAL... AND THE CAR
REACH THE SAFEHOUSE BEFORE THE MAN GON GETCHU.
"""

CHOICES = """
    --- Your Choices ---
    A - Eat tofu
    B - Drive moderately
    C - Speed ahead at full speed
    D - Stop to refuel
    E - Check current status
    Q - Quit the game.
    ---
    
"""

REFUEL = """-------You filled the fuel tank.
-------The agents got closer...
"""

EAT_TOFU = """-------Mmmmm. Soybean goodness.
-------Your hunger is sated.
"""

NO_TOFU = """-------You have no tofu left.
"""

SEVERE_HUNGER = """\n*******Your stomach rumbles.
*******You need to eat something quick.
"""

HUNGER = """\n*******Your hunger is small but manageable.
"""

ENDGAME_TEXT = [
    """\n\nThe game has ended. Thanks for playing""",     # Quit the game
    """\n\nTHE AGENTS HAVE CLOSED IN ON YOU.
THERE ARE AT LEAST 20 CARS SURROUNDING YOU.
THE LEAD CAR BUMPS YOUR PASSENGER SIDE.
YOU MANAGE TO CORRECT YOUR STEERING
TO KEEP YOU FROM CRASHING.

YOU DIDN'T SEE THE AGENT'S CAR RIGHT BESIDE YOU.
THAT DRIVER BUMPS YOUR CAR.
AND THAT'S IT.

YOU SPIN UNCONTROLLABLY.
YOUR CAR FLIPS OVER AT LEAST TWO TIMES.
OR MORE... YOU SEEM TO HAVE LOST COUNT.

SIRENS.

"ARE THEY ALIVE?" THEY SAY AS YOU HEAR
FOOTSTEPS COMING CLOSER.
"DOESN'T MATTER, ALL WE WANTED WAS THE CAR."

YOU SEE A DOG SLOWLY STEP OUT OF THE
OVERTURNED CAR.

"YOU WILL NEVER STOP THE REVOLUTION!"
THE DOG SEEMS TO SAY TO THE AGENTS.

IT WAS IN THE CAR THE WHOLE TIME.

YOU DRIFT OFF INTO UNCONSCIOUSNESS...

-----GAME OVER-----\n""",     # LOSE - Agents have caught up
    """\n\nYOUR CAR SPUTTERS AND SEEMS TO LET OUT
A BIG SIGH. THERE's NO MORE FUEL LEFT.

THE AGENTS SURROUND YOU AND STEP OUT
OF THEIR CARS. THE LEAD AGENT RIPS
THE DOOR OPEN AND THROWS YOU OUT OF
YOU CAR.

"WE FINALLY GOT IT."

YOU FAILED.

-----GAME OVER-----\n""", # LOSE - Fuel runs out
    """\n\nYOUR STOMACH IS EMPTY.
WHO KNEW THAT WHAT THE DOCTOR SAID WAS TRUE,
THAT HUMAN/ROBOT HYBRIDS WOULD NEED
TOFU TO SUSTAIN THEMSELVES.
YOUR ROBOT SYSTEMS START TO SHUT DOWN.
YOUR HUMAN EYES CLOSE.
THE LAST THING THAT YOU HEAR ARE SIRENS.
THEY GOTCHU. THEY GOT THE CAR.
WE FAILED...
----GAME OVER----\n""", # LOSE - Perish because of hunger
    """\n\nYOU PRESS THE BUTTON TO OPEN THE GATE.
THIS ISN'T THE FIRST TIME YOU'VE DONE THIS.
YOU CAN TIME IT PERFECTLY SO THAT YOU
SLIDE THE CAR IN AS THE GATES CLOSE.

YOU KNOW YOU DID THE RIGHT THING.
THE GOVERNMENT WOULD HAVE TORN THE CAR APART.
ANALYZING IT, TESTING IT, THEN DESTROYING IT.

THEY DON'T KNOW IT'S SECRETS...
THAT IT HOLDS THE KEY DO DIFFERENT WORLDS.

AS YOU STEP OUT OF THE VEHICLE, FIDO RUNS
UP TO YOU.
"THANK YOU FOR SAVING ME," HE SAYS.

AS YOU TAKE A COUPLE OF STEPS AWAY FROM THE CAR,
IT MAKES A STRANGE NOISE.

BEFORE YOUR EYES IT SHIFTS IT'S SHAPE.
YOU'VE SEEN THIS BEFORE, BUT ONLY IN
THE MOVIES.

"BUMBLEBEE...?"

-----GAME OVER-----\n""", # WIN
]
