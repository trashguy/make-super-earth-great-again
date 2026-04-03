"""
Helldivers 2 Trump Voice Mod - Voice Line Mapping

Each entry maps an original helldiver voice line to either:
- A Trumpified rewrite (for AI generation)
- A classic Trump clip reference (marked with __CLASSIC__ prefix)

Categories match the in-game audio triggers.
"""

from dataclasses import dataclass

@dataclass
class VoiceLine:
    category: str
    original: str
    trump: str
    emotion: str = "normal"  # normal, excited, angry, whispering, shouting


VOICE_LINES: list[VoiceLine] = [

    # =========================================================================
    # DEPLOYMENT / LANDING
    # =========================================================================
    VoiceLine("deployment", "Helldiver reporting to the front.", "Trump is here. The best helldiver, many people are saying it.", "confident"),
    VoiceLine("deployment", "Helldiver reporting for duty.", "Reporting for duty. Nobody reports better than me, believe me.", "confident"),
    VoiceLine("deployment", "Democracy has landed.", "Your favorite president has landed!", "excited"),
    VoiceLine("deployment", "Point me to the enemy.", "Point me to the enemy. I'll handle it.", "confident"),
    VoiceLine("deployment", "Ready to liberate.", "Ready to liberate. Believe me.", "excited"),
    VoiceLine("deployment", "Joining the fray.", "Joining the fight. I always win.", "confident"),
    VoiceLine("deployment", "Reporting to the front.", "I'm at the front. Somebody had to do it.", "confident"),
    VoiceLine("deployment", "Loadout confirmed.", "Loadout confirmed. Tremendous.", "confident"),
    VoiceLine("deployment", "Weapons ready.", "Weapons ready. Beautiful weapons.", "confident"),
    VoiceLine("deployment", "Let's do this!", "Let's do this! Let's make Super Earth great again!", "excited"),
    VoiceLine("deployment", "Rolling out!", "Rolling out! Trump is rolling out, folks!", "excited"),
    VoiceLine("deployment", "We'll drop in here.", "We'll drop right here. Perfect spot.", "confident"),
    VoiceLine("deployment", "Inputting drop point.", "Drop point set. Great location.", "confident"),
    VoiceLine("deployment", "Strategy selected.", "Strategy selected. The best strategy.", "confident"),

    # =========================================================================
    # RELOADING / AMMUNITION
    # =========================================================================
    VoiceLine("reload", "Reloading!", "Reloading! Gotta reload!", "urgent"),
    VoiceLine("reload", "Gotta reload!", "Hold on, I'm reloading, okay?", "urgent"),
    VoiceLine("reload", "Changing mag!", "New mag! Tremendous!", "urgent"),
    VoiceLine("reload", "New mag!", "Big new mag!", "urgent"),
    VoiceLine("reload", "New mag.", "New mag. Beautiful.", "urgent"),
    VoiceLine("reload", "Last reload!", "Last reload! Unbelievable!", "angry"),
    VoiceLine("reload", "Mag's empty.", "Mag's empty. Very sad.", "urgent"),
    VoiceLine("reload", "Out of ammo!", "Out of ammo! Total disaster!", "angry"),
    VoiceLine("reload", "I'm out!", "I'm out! Can you believe it?!", "angry"),
    VoiceLine("reload", "I need ammo.", "I need ammo. The best ammo.", "urgent"),
    VoiceLine("reload", "I need to reload.", "Gotta reload. Hold on.", "urgent"),
    VoiceLine("reload", "Need to reload!", "Gotta reload! One second!", "urgent"),
    VoiceLine("reload", "Nothing in the chamber.", "Nothing in the chamber. Empty.", "urgent"),
    VoiceLine("reload", "Canister's empty!", "Canister's empty! Totally empty!", "urgent"),
    VoiceLine("reload", "New canister!", "New canister! Beautiful!", "urgent"),
    VoiceLine("reload", "New canister for maximum liberation.", "New canister for maximum liberation!", "excited"),
    VoiceLine("reload", "Need fresh ice.", "Need fresh ice. The best ice.", "urgent"),
    VoiceLine("reload", "Changing ice!", "Changing ice! Gotta swap it!", "urgent"),
    VoiceLine("reload", "Gotta swap ice!", "Swapping ice! Fast!", "urgent"),
    VoiceLine("reload", "Swapping internal cooling element.", "Swapping the cooling element. Very technical.", "urgent"),
    VoiceLine("reload", "Reloading support weapon!", "Reloading the big gun!", "urgent"),
    VoiceLine("reload", "Team reload required!", "Team reload! Help me out!", "urgent"),
    VoiceLine("reload", "I need a team reload!", "Get over here! Team reload!", "urgent"),
    VoiceLine("reload", "Need team reload!", "Team reload! Come on!", "urgent"),
    VoiceLine("reload", "Performing assisted reload.", "I'm helping you reload. You're welcome.", "confident"),
    VoiceLine("reload", "Reloading you!", "Reloading you! Best team player.", "confident"),

    # =========================================================================
    # THROWING GRENADES
    # =========================================================================
    VoiceLine("grenade", "Throwing grenade!", "You're fired!", "shouting"),
    VoiceLine("grenade", "Grenade!", "Grenade! Big grenade! Huge!", "shouting"),
    VoiceLine("grenade", "Fire in the hole!", "Fire in the hole! Tremendous fire!", "shouting"),
    VoiceLine("grenade", "How about a nice cup of Liber-tea?", "How about a nice cup of Liber-tea? The best tea. Trump tea.", "excited"),
    VoiceLine("grenade", "Eat this!", "Eat this, loser!", "shouting"),

    # =========================================================================
    # COMBAT - SUSTAINED FIRE / KILLS
    # =========================================================================
    VoiceLine("combat", "Get some! GET SOOOOME!", "Get some! So much winning!", "shouting"),
    VoiceLine("combat", "Say hello to Democracy!", "Say hello to Democracy!", "shouting"),
    VoiceLine("combat", "Have a taste of Democracy!", "Have a taste of Democracy! Beautiful!", "shouting"),
    VoiceLine("combat", "How'd you like the taste of Freedom?", "How do you like freedom? Tremendous!", "excited"),
    VoiceLine("combat", "How about a nice cup of Liberty?", "How about some Liberty?", "excited"),
    VoiceLine("combat", "You will never destroy our way of life!", "You will never destroy our way of life!", "angry"),
    VoiceLine("combat", "Freedom forever!", "Freedom forever!", "shouting"),
    VoiceLine("combat", "FOR SUPER EARTH!!!", "FOR SUPER EARTH!!!", "shouting"),
    VoiceLine("combat", "FREEEEEDOM!!!", "FREEEEEDOM!!!", "shouting"),
    VoiceLine("combat", "KILL 'EM ALL!!!", "KILL EM ALL!!!", "shouting"),
    VoiceLine("combat", "Burn in the fires of Democracy!", "Burn in the fires of Democracy! You're fired!", "shouting"),
    VoiceLine("combat", "Let the light of Liberty shine!", "Let Liberty shine! Nobody shines brighter!", "excited"),
    VoiceLine("combat", "That's called Democracy!", "That's called Democracy, folks!", "excited"),
    VoiceLine("combat", "You are the tinder, and Liberty is the match!", "You're the tinder and I'm the match!", "excited"),
    VoiceLine("combat", "The flames of Democracy spread like wildfire!", "The flames of Democracy! Huge flames!", "excited"),
    VoiceLine("combat", "Liberty burns hot!", "Liberty burns hot! So hot!", "excited"),
    VoiceLine("combat", "*Maniacal laughter* AHAHAHAHA!", "Hahaha! Did you see that?!", "excited"),
    VoiceLine("combat", "Freedom delivery!", "Freedom delivery! You're welcome!", "excited"),
    VoiceLine("combat", "For Liberty!", "For Liberty! For Trump!", "shouting"),
    VoiceLine("combat", "Liberty for every being!", "Liberty for every being! Not the bugs.", "excited"),
    VoiceLine("combat", "This is for you!", "This one's for you!", "shouting"),

    # =========================================================================
    # ENEMY CALLOUTS
    # =========================================================================
    VoiceLine("enemy", "Contact!", "Contact! Bad guys!", "shouting"),
    VoiceLine("enemy", "Enemy spotted!", "Enemy spotted! Big enemy!", "shouting"),
    VoiceLine("enemy", "Enemies spotted!", "Enemies! Not sending their best!", "shouting"),
    VoiceLine("enemy", "Engaging!", "Engaging! Going in!", "shouting"),
    VoiceLine("enemy", "Not engaging.", "Not engaging. Strategic.", "confident"),
    VoiceLine("enemy", "Enemy patrol!", "Enemy patrol! Bad hombres!", "urgent"),
    VoiceLine("enemy", "Enemy outpost spotted! Look alive!", "Enemy outpost! We're taking it!", "urgent"),
    VoiceLine("enemy", "Enemy outpost!", "Enemy outpost! Nasty place!", "urgent"),
    VoiceLine("enemy", "Enemy emplacement!", "Emplacement! Very unfair!", "urgent"),
    VoiceLine("enemy", "Enemy elite!", "Big one! Elite! I've dealt with worse!", "urgent"),
    VoiceLine("enemy", "Heavy!", "Heavy! Huge!", "shouting"),
    VoiceLine("enemy", "Aerial enemy!", "In the air! Shoot it down!", "shouting"),
    VoiceLine("enemy", "Dropships!", "Dropships! Unbelievable!", "shouting"),
    VoiceLine("enemy", "Bugs!", "Bugs! Nasty!", "angry"),
    VoiceLine("enemy", "Bug outpost spotted! Prepare to exterminate!", "Bug outpost! Total extermination!", "angry"),
    VoiceLine("enemy", "Bug hive spotted!", "Bug hive! Shut it down!", "angry"),
    VoiceLine("enemy", "Bug tunnel breach!", "Coming out of the ground!", "shouting"),
    VoiceLine("enemy", "Bughole!", "Bug hole! Nasty! Shut it down!", "angry"),
    VoiceLine("enemy", "Squids!", "Squids! Very nasty!", "angry"),
    VoiceLine("enemy", "Illuminate!", "Illuminate! They're not smart!", "angry"),
    VoiceLine("enemy", "Illuminate teleporting in!", "Teleporting! That's cheating!", "angry"),
    VoiceLine("enemy", "Squid outpost spotted!", "Squid outpost! Taking it down!", "urgent"),
    VoiceLine("enemy", "Squid warp gate!", "Warp gate! Big ugly gate!", "urgent"),
    VoiceLine("enemy", "Bot fabricator!", "Bot factory! Not on my watch!", "angry"),
    VoiceLine("enemy", "Dangerous wildlife.", "Dangerous. Very dangerous.", "confident"),
    VoiceLine("enemy", "Harmless animal.", "Harmless. Very cute.", "confident"),
    VoiceLine("enemy", "Local fauna.", "Local wildlife. Interesting.", "confident"),

    # =========================================================================
    # STRATAGEM CALLOUTS
    # =========================================================================
    # Eagle / Air Support
    VoiceLine("stratagem", "Requesting air support!", "Air support! The best!", "excited"),
    VoiceLine("stratagem", "Sending in an Eagle!", "Sending in the Eagle! Bald Eagle!", "excited"),
    VoiceLine("stratagem", "Calling in an Eagle.", "Eagle coming in. Majestic.", "confident"),

    # Orbital Strikes
    VoiceLine("stratagem", "Requesting orbital strike!", "Orbital strike! Biggest you've ever seen!", "excited"),
    VoiceLine("stratagem", "Requesting orbital!", "Give me an orbital! Big beautiful orbital!", "excited"),
    VoiceLine("stratagem", "Calling in orbital strike!", "Orbital coming in! Gonna be huge!", "excited"),
    VoiceLine("stratagem", "Orbital incoming!", "Orbital incoming! Take cover!", "shouting"),
    VoiceLine("stratagem", "Orbital inbound!", "Orbital inbound! Tremendous!", "shouting"),

    # Support Weapons
    VoiceLine("stratagem", "Requesting advanced weaponry!", "Get me the good stuff!", "excited"),
    VoiceLine("stratagem", "Calling down a support weapon!", "Support weapon! Beautiful weapon!", "excited"),
    VoiceLine("stratagem", "Support weapon inbound!", "Weapon incoming! You'll love it!", "excited"),
    VoiceLine("stratagem", "Freedom requires firepower.", "Freedom requires firepower.", "confident"),
    VoiceLine("stratagem", "Requesting TACPAC!", "I need a tack-pack!", "urgent"),
    VoiceLine("stratagem", "TACPAC inbound!", "Tack-pack on the way!", "urgent"),

    # Supplies
    VoiceLine("stratagem", "Throwing supply beacon!", "Supply beacon! Incoming!", "urgent"),
    VoiceLine("stratagem", "Calling down supplies!", "Supplies! The best!", "excited"),
    VoiceLine("stratagem", "Requesting supplies!", "I need supplies!", "urgent"),
    VoiceLine("stratagem", "Supplies!", "Supplies! Beautiful!", "excited"),

    # Reinforcements
    VoiceLine("stratagem", "Calling in reinforcements!", "Calling backup! Great people!", "excited"),
    VoiceLine("stratagem", "Another diver for the cause.", "Another diver. We need winners.", "confident"),
    VoiceLine("stratagem", "Reinforcing!", "Reinforcements! Tremendous people!", "excited"),
    VoiceLine("stratagem", "No diver left behind!", "No diver left behind!", "confident"),

    # Sentries / Fortifications / Vehicles
    VoiceLine("stratagem", "Calling down a sentry.", "Sentry coming in. A great sentry.", "confident"),
    VoiceLine("stratagem", "Requesting sentry!", "Get me a sentry! Border protection!", "excited"),
    VoiceLine("stratagem", "Calling down fortifications.", "Building a wall, basically.", "confident"),
    VoiceLine("stratagem", "Requesting fortifications!", "Big beautiful fortifications!", "excited"),
    VoiceLine("stratagem", "Calling down a vehicle!", "Vehicle incoming! Beautiful!", "excited"),
    VoiceLine("stratagem", "Requesting vehicle!", "Get me a vehicle!", "excited"),
    VoiceLine("stratagem", "Calling down a walker!", "Walker coming in! Tremendous!", "excited"),
    VoiceLine("stratagem", "Requesting walker!", "Get me the walker!", "excited"),
    VoiceLine("stratagem", "Manning combat walker!", "Getting in the walker! Great!", "excited"),

    # Equipment / Objectives
    VoiceLine("stratagem", "Calling down equipment!", "Equipment! Top of the line!", "excited"),
    VoiceLine("stratagem", "Requesting equipment!", "I need equipment! The best!", "urgent"),
    VoiceLine("stratagem", "Calling down objective equipment!", "Objective equipment incoming!", "urgent"),
    VoiceLine("stratagem", "Requesting objective equipment!", "Objective gear! Mission critical!", "urgent"),
    VoiceLine("stratagem", "Objective equipment.", "Objective equipment. Very important.", "confident"),

    # Hellbomb / SOS / Flare
    VoiceLine("stratagem", "Calling in a hellbomb!", "HELLBOMB! You're gonna love it!", "excited"),
    VoiceLine("stratagem", "Hellbomb armed -- clear the area!", "Hellbomb armed! Get out! Gonna be huge!", "shouting"),
    VoiceLine("stratagem", "Hellbomb.", "Hellbomb. Very powerful.", "confident"),
    VoiceLine("stratagem", "Deploying SOS beacon.", "SOS. We need help.", "urgent"),
    VoiceLine("stratagem", "Sending out an SOS!", "SOS! Send everyone!", "urgent"),
    VoiceLine("stratagem", "S.O.S.!", "S.O.S.! Send help!", "urgent"),
    VoiceLine("stratagem", "Deploying flare!", "Flare going up! Beautiful!", "excited"),

    # =========================================================================
    # INJURY / DAMAGE
    # =========================================================================
    # General
    VoiceLine("injury", "I'm bleeding out!", "I'm bleeding! Very bad!", "angry"),
    VoiceLine("injury", "I'm hit! Sweet Liberty... the blood!", "I'm hit! This suit was expensive!", "angry"),
    VoiceLine("injury", "The blood! I can't stop the blood!", "So much blood! This is a disaster!", "angry"),
    VoiceLine("injury", "Can't survive these wounds much longer!", "Can't take much more! Very unfair!", "angry"),
    VoiceLine("injury", "I'm losing so much blood!", "Losing blood! Tremendous blood!", "angry"),
    VoiceLine("injury", "More blood loss than manual recommends.", "More blood than doctors recommend.", "urgent"),
    VoiceLine("injury", "Ouch!", "Ow!", "angry"),
    VoiceLine("injury", "AHHH!", "AHHH!", "shouting"),

    # Arms
    VoiceLine("injury", "Sweet Liberty, my arm!", "My arm! This is terrible!", "angry"),
    VoiceLine("injury", "MY ARM!", "MY ARM!", "shouting"),
    VoiceLine("injury", "Can't liberate with this broken arm!", "Broken arm! Very unfair!", "angry"),
    VoiceLine("injury", "Cannot liberate effectively with injured arm.", "Arm is hurt. Sad.", "angry"),
    VoiceLine("injury", "Gotta fix this Liberty-forsaken arm!", "Gotta fix this arm!", "angry"),
    VoiceLine("injury", "Gotta patch up this arm!", "Gotta fix the arm!", "urgent"),
    VoiceLine("injury", "I need to do something about my arm!", "My arm! Somebody help!", "urgent"),

    # Legs
    VoiceLine("injury", "Sweet Liberty, my leg!", "My leg! My beautiful leg!", "angry"),
    VoiceLine("injury", "MY LEG!", "MY LEG!", "shouting"),
    VoiceLine("injury", "My legs! For the love of Liberty, my legs!", "My legs! The worst!", "shouting"),
    VoiceLine("injury", "Oh, my legs!", "Oh my legs!", "angry"),
    VoiceLine("injury", "Flag-forsaken leg's slowin' me down!", "Leg's slowing me down!", "angry"),
    VoiceLine("injury", "Gotta patch up this leg!", "Gotta fix this leg!", "urgent"),
    VoiceLine("injury", "My leg -- not functioning at capacity.", "Leg's not working. Sad.", "angry"),
    VoiceLine("injury", "Limping is not liberating.", "Limping! Very bad!", "angry"),

    # No Stims
    VoiceLine("injury", "Out of stims!", "Out of stims! Catastrophe!", "angry"),
    VoiceLine("injury", "I need stims!", "I need stims!", "urgent"),
    VoiceLine("injury", "I could truly use a stim!", "Need a stim! Badly!", "urgent"),
    VoiceLine("injury", "Need... stim!", "Need a stim...", "urgent"),

    # =========================================================================
    # HEALING
    # =========================================================================
    # Self
    VoiceLine("healing", "Feels gooooood.", "Feels incredible. The best.", "confident"),
    VoiceLine("healing", "Freedom never sleeps!", "Freedom never sleeps!", "excited"),
    VoiceLine("healing", "Freedom never rests!", "Never rest! Always winning!", "excited"),
    VoiceLine("healing", "My life for Super Earth!", "My life for Super Earth!", "excited"),
    VoiceLine("healing", "My body for Super Earth!", "This body for Super Earth! Great body!", "confident"),
    VoiceLine("healing", "Must defend prosperity!", "Must defend prosperity!", "confident"),
    VoiceLine("healing", "Democracy needs me.", "Democracy needs me.", "confident"),
    VoiceLine("healing", "Helldivers never die!", "Trump never dies! Helldivers never die!", "excited"),
    VoiceLine("healing", "A little shot o' Liberty.", "Shot of Liberty. Doctor ordered.", "confident"),
    VoiceLine("healing", "No pain, no freedom!", "No pain, no freedom!", "excited"),
    VoiceLine("healing", "Injury? What injury!", "Injury? What injury? I feel perfect!", "excited"),
    VoiceLine("healing", "Not today!", "Not today! I don't lose!", "confident"),
    VoiceLine("healing", "Whatever it takes.", "Whatever it takes.", "confident"),
    VoiceLine("healing", "Liberty heal me!", "Heal me! Too important to go down!", "urgent"),
    VoiceLine("healing", "Liberty save me!", "Save me! Very important!", "urgent"),
    VoiceLine("healing", "Liberty shield me!", "Shield me! Protect your president!", "urgent"),

    # Healing Teammates
    VoiceLine("healing", "Stimming you!", "Healing you! You're welcome!", "confident"),
    VoiceLine("healing", "Administering meds!", "I take care of my people!", "confident"),
    VoiceLine("healing", "No diver left behind!", "No diver left behind!", "confident"),
    VoiceLine("healing", "Live to dive another day.", "Fight another day. Winners.", "confident"),
    VoiceLine("healing", "Democracy isn't done with you yet.", "Get up! We need you!", "confident"),
    VoiceLine("healing", "I've got you.", "I've got you. Trump's got you.", "confident"),
    VoiceLine("healing", "I got you.", "I got you. Believe me.", "confident"),

    # =========================================================================
    # SAMPLE COLLECTION
    # =========================================================================
    VoiceLine("samples", "Got a sample!", "Got a sample! Beautiful!", "excited"),
    VoiceLine("samples", "Sample collected!", "Sample! Tremendous!", "excited"),
    VoiceLine("samples", "Another sample collected for Democracy.", "Another sample. Collecting them all.", "confident"),
    VoiceLine("samples", "This sample should greatly aid in the war effort.", "This'll help us win. Big league.", "confident"),
    VoiceLine("samples", "Democracy fills my sample container.", "Container filling up. The best samples.", "confident"),
    VoiceLine("samples", "This biosample will directly increase our freedom.", "Gonna make us stronger.", "confident"),
    VoiceLine("samples", "This biological sample will provide excellent data.", "Excellent data. I love data.", "confident"),
    VoiceLine("samples", "Biological sample secured!", "Sample secured! Locked down!", "confident"),
    VoiceLine("samples", "Rare sample collected!", "Rare sample! Very valuable!", "excited"),
    VoiceLine("samples", "Rare sample acquired.", "Rare sample. Very special.", "confident"),
    VoiceLine("samples", "High-value sample collected!", "High-value! Tremendous!", "excited"),
    VoiceLine("samples", "Tech sample acquired!", "Tech sample! The best technology!", "excited"),

    # =========================================================================
    # ITEM / RESOURCE PICKUP
    # =========================================================================
    VoiceLine("pickup", "Package acquired!", "Package! Great package!", "excited"),
    VoiceLine("pickup", "Artifact collected.", "Artifact! Beautiful!", "excited"),
    VoiceLine("pickup", "Illuminate artifact acquired!", "Squid artifact! Love it!", "excited"),
    VoiceLine("pickup", "Legendarium acquired!", "Legendarium! Almost as legendary as me!", "excited"),
    VoiceLine("pickup", "Legendarium -- truly as legendary as the name suggests.", "Legendarium! Not as legendary as Trump, but close.", "confident"),
    VoiceLine("pickup", "Crystallized E710 acquired!", "E seven ten! Beautiful crystals!", "excited"),
    VoiceLine("pickup", "This crystallized E710 will help fuel our future!", "This'll power our future!", "confident"),
    VoiceLine("pickup", "E-710, the galaxy's greatest energy source.", "E seven ten. The best energy. Big energy guy.", "confident"),
    VoiceLine("pickup", "Super uranium acquired!", "Super uranium! Tremendously powerful!", "excited"),
    VoiceLine("pickup", "Super uranium -- safe enough for babies!", "Super uranium! Totally safe!", "confident"),
    VoiceLine("pickup", "Super uranium -- defier of gravity and extremely safe.", "Super uranium. Defies gravity. I guarantee it.", "confident"),
    VoiceLine("pickup", "Black saffron harvested!", "Black saffron! I know expensive!", "excited"),
    VoiceLine("pickup", "Black saffron -- life-saving and non-habit-forming.", "Black saffron. No side effects. Like me.", "confident"),
    VoiceLine("pickup", "One small scrap of technology, one giant leap for Liberty.", "Small tech, giant leap for freedom.", "confident"),
    VoiceLine("pickup", "This small bit of technology may lead to a large increase in Liberty.", "This tech's gonna increase freedom. Huge.", "confident"),
    VoiceLine("pickup", "This canister will see me through.", "This canister. Very useful.", "confident"),

    # =========================================================================
    # DROPPING / MARKING ITEMS
    # =========================================================================
    VoiceLine("marking", "Dropping item.", "Dropping it. It's a gift.", "confident"),
    VoiceLine("marking", "Dropping package!", "Dropping a package! For you!", "confident"),
    VoiceLine("marking", "Dropping high-value item.", "Dropping something valuable.", "confident"),
    VoiceLine("marking", "Dropping a pin.", "Marking it. Right here.", "confident"),
    VoiceLine("marking", "Marking location.", "Marking it. Great location.", "confident"),
    VoiceLine("marking", "Tagging location.", "Tagging it. Right there.", "confident"),
    VoiceLine("marking", "Tagging map.", "On the map. Very important.", "confident"),
    VoiceLine("marking", "High-value item.", "High-value! Don't miss this!", "excited"),
    VoiceLine("marking", "Critical item.", "Critical item. The most important.", "urgent"),

    # =========================================================================
    # PINGS / DIRECTIONS
    # =========================================================================
    VoiceLine("ping", "North.", "North!", "normal"),
    VoiceLine("ping", "South.", "South!", "normal"),
    VoiceLine("ping", "East.", "East!", "normal"),
    VoiceLine("ping", "West.", "West!", "normal"),
    VoiceLine("ping", "Northeast.", "Northeast!", "normal"),
    VoiceLine("ping", "Northwest.", "Northwest!", "normal"),
    VoiceLine("ping", "Southeast.", "Southeast!", "normal"),
    VoiceLine("ping", "Southwest.", "Southwest!", "normal"),
    VoiceLine("ping", "Up.", "Up!", "normal"),
    VoiceLine("ping", "Down.", "Down!", "normal"),
    VoiceLine("ping", "Left.", "Left!", "normal"),
    VoiceLine("ping", "Right.", "Right!", "normal"),
    VoiceLine("ping", "Close.", "Close! Very close!", "normal"),
    VoiceLine("ping", "Far.", "Far! Very far!", "normal"),
    VoiceLine("ping", "50 meters.", "Fifty meters!", "normal"),
    VoiceLine("ping", "100 meters.", "A hundred meters!", "normal"),
    VoiceLine("ping", "200 meters.", "Two hundred meters!", "normal"),
    VoiceLine("ping", "300 meters.", "Three hundred meters!", "normal"),

    # Marking / Communication
    VoiceLine("ping", "Objective located.", "Objective found! I found it!", "excited"),
    VoiceLine("ping", "There's something here.", "Something here. Something big.", "confident"),
    VoiceLine("ping", "Found something!", "Found something! Tremendous!", "excited"),
    VoiceLine("ping", "There.", "Right there!", "normal"),
    VoiceLine("ping", "Here.", "Right here!", "normal"),
    VoiceLine("ping", "What about here?", "What about right here? Great spot.", "normal"),
    VoiceLine("ping", "That one.", "That one! Right there!", "normal"),
    VoiceLine("ping", "Intel.", "Intel! Very important intel!", "normal"),
    VoiceLine("ping", "Sub-objective.", "Sub-objective. We'll handle it.", "normal"),
    VoiceLine("ping", "Primary objective.", "Primary objective! The main event!", "confident"),
    VoiceLine("ping", "Tactical benefit.", "Tactical advantage! Very smart!", "confident"),
    VoiceLine("ping", "Tactical impediment.", "Problem here! Not good! Big problem!", "urgent"),
    VoiceLine("ping", "Danger!", "Danger! Big danger! Watch out!", "urgent"),
    VoiceLine("ping", "Additional extraction point located.", "Another extraction point! More options! I love options!", "normal"),

    # NATO / Numbers (keep these short and punchy)
    VoiceLine("ping", "Alpha.", "Alpha!", "normal"),
    VoiceLine("ping", "Bravo.", "Bravo!", "normal"),
    VoiceLine("ping", "Charlie.", "Charlie!", "normal"),
    VoiceLine("ping", "Delta.", "Delta!", "normal"),
    VoiceLine("ping", "Echo.", "Echo!", "normal"),
    VoiceLine("ping", "Foxtrot.", "Foxtrot!", "normal"),
    VoiceLine("ping", "Code is...", "The code is...", "normal"),
    VoiceLine("ping", "Zero.", "Zero!", "normal"),
    VoiceLine("ping", "One.", "One!", "normal"),
    VoiceLine("ping", "Two.", "Two!", "normal"),
    VoiceLine("ping", "Three.", "Three!", "normal"),
    VoiceLine("ping", "Four.", "Four!", "normal"),
    VoiceLine("ping", "Five.", "Five!", "normal"),
    VoiceLine("ping", "Six.", "Six!", "normal"),
    VoiceLine("ping", "Seven.", "Seven!", "normal"),
    VoiceLine("ping", "Eight.", "Eight!", "normal"),
    VoiceLine("ping", "Nine.", "Nine!", "normal"),

    # =========================================================================
    # MOVEMENT / ORDERS
    # =========================================================================
    VoiceLine("movement", "Follow me!", "Follow me! Best way!", "shouting"),
    VoiceLine("movement", "Move!", "Move it! Come on!", "shouting"),
    VoiceLine("movement", "MOVE MOVE MOVE!", "MOVE MOVE MOVE!", "shouting"),
    VoiceLine("movement", "On my way.", "On my way. Don't worry.", "confident"),
    VoiceLine("movement", "Heading there now.", "Heading there. Very fast.", "confident"),
    VoiceLine("movement", "I'm on it!", "I'm on it!", "excited"),
    VoiceLine("movement", "Hold position.", "Hold position! Don't move!", "shouting"),
    VoiceLine("movement", "Fall back!", "Fall back! Strategic retreat!", "shouting"),
    VoiceLine("movement", "RUN!!!", "RUN!!! GO GO GO!!!", "shouting"),
    VoiceLine("movement", "Steering clear!", "Staying away! No way!", "urgent"),
    VoiceLine("movement", "On my position.", "On my position!", "confident"),

    # =========================================================================
    # RESPONSES
    # =========================================================================
    VoiceLine("response", "Affirmative!", "Absolutely! One hundred percent!", "confident"),
    VoiceLine("response", "Yes!", "Yes! Definitely yes!", "confident"),
    VoiceLine("response", "Negative.", "No. Hard no.", "confident"),
    VoiceLine("response", "No.", "No. Wrong.", "confident"),
    VoiceLine("response", "Cancel that.", "Cancel that. Bad idea.", "confident"),
    VoiceLine("response", "Nevermind.", "Nevermind. Forget it.", "confident"),
    VoiceLine("response", "I'll take it.", "I'll take it!", "excited"),
    VoiceLine("response", "Don't need it.", "Don't need it. I'm good.", "confident"),
    VoiceLine("response", "Thank you.", "Thank you. Very nice.", "confident"),
    VoiceLine("response", "I'm sorry.", "I'm sorry. It happens. Rarely.", "confident"),
    VoiceLine("response", "Nice!", "Nice! Beautiful! Fantastic!", "excited"),
    VoiceLine("response", "Done!", "Done! Finished! Perfect!", "excited"),

    # =========================================================================
    # EXTRACTION
    # =========================================================================
    VoiceLine("extraction", "Calling an extraction!", "Extraction! Time to go! We won!", "excited"),
    VoiceLine("extraction", "Calling in extraction.", "Extraction called. Beautiful shuttle.", "confident"),
    VoiceLine("extraction", "Marking extraction point.", "Extraction point. Perfect spot.", "confident"),
    VoiceLine("extraction", "Entering shuttle.", "Getting on. First class.", "confident"),
    VoiceLine("extraction", "Get in!", "Get in! Let's go!", "shouting"),

    # =========================================================================
    # JUMP PACK
    # =========================================================================
    VoiceLine("jumppack", "Activating jump pack!", "Jump pack activated! I'm flying! Beautiful!", "excited"),
    VoiceLine("jumppack", "To the skies!", "To the skies! Like an eagle! A bald eagle!", "excited"),
    VoiceLine("jumppack", "Liberty leap!", "Liberty leap! A tremendous leap!", "excited"),

    # =========================================================================
    # TERMINAL / OBJECTIVES
    # =========================================================================
    VoiceLine("terminal", "I'm on the terminal.", "On the terminal. The best with computers.", "confident"),
    VoiceLine("terminal", "I got the terminal!", "Got the terminal! I understand it!", "confident"),
    VoiceLine("terminal", "I'll handle the terminal.", "I'll handle the terminal.", "confident"),
    VoiceLine("terminal", "Engaging terminal.", "Working the terminal. Not complicated for me.", "confident"),
    VoiceLine("terminal", "We've got equipment.", "Equipment! Great equipment!", "excited"),

    # =========================================================================
    # WEATHER / VISIBILITY
    # =========================================================================
    VoiceLine("weather", "Visibility decreasing.", "Can't see! Very bad!", "urgent"),
    VoiceLine("weather", "Decreased visibility should help obscure our movements.", "Low visibility. Very strategic.", "confident"),
    VoiceLine("weather", "Visibility improving -- avoid being an easy target.", "Visibility up. Don't be a target.", "confident"),
    VoiceLine("weather", "Increased visibility. We can see them. They can see us.", "We see them. They see us. Be careful.", "confident"),

    # =========================================================================
    # VICTORY / PATRIOTIC FLAVOR
    # =========================================================================
    VoiceLine("patriotic", "I fight for Super Earth.", "I fight for Super Earth!", "excited"),
    VoiceLine("patriotic", "I fight for freedom.", "I fight for freedom! Trump freedom!", "excited"),
    VoiceLine("patriotic", "I am a soldier of Liberty.", "Soldier of Liberty! The best!", "excited"),
    VoiceLine("patriotic", "I am a soldier of Democracy.", "Soldier of Democracy! Tremendous!", "excited"),
    VoiceLine("patriotic", "Democracy conquers all.", "Democracy conquers all! Like me!", "excited"),
    VoiceLine("patriotic", "Democracy for all.", "Democracy for all! It's free!", "excited"),
    VoiceLine("patriotic", "Liberty, prosperity, Democracy.", "Liberty! Prosperity! Democracy!", "excited"),
    VoiceLine("patriotic", "Liberty guides my hand.", "Liberty guides my hand! Very steady!", "confident"),
    VoiceLine("patriotic", "Liberty will prevail.", "Liberty will prevail!", "excited"),
    VoiceLine("patriotic", "Liberty will not fall.", "Liberty will never fall!", "excited"),
    VoiceLine("patriotic", "For prosperity!", "For prosperity!", "excited"),
    VoiceLine("patriotic", "Our way of life must be protected.", "Our way of life! At all costs!", "excited"),
    VoiceLine("patriotic", "I will protect Democracy at all costs.", "I will protect Democracy!", "excited"),
    VoiceLine("patriotic", "I will protect our way of life.", "I will protect our way of life!", "excited"),
    VoiceLine("patriotic", "I will keep Super Earth safe.", "Super Earth safe! The safest ever!", "excited"),
    VoiceLine("patriotic", "Freedom fight!", "Freedom fight!", "shouting"),
    VoiceLine("patriotic", "Let's play!", "Let's play! I always win!", "excited"),
    VoiceLine("patriotic", "I win!", "I win! Of course I win!", "excited"),
    VoiceLine("patriotic", "You win.", "You win. This time.", "confident"),
    VoiceLine("patriotic", "Tie!", "A tie! Very boring!", "confident"),
    VoiceLine("patriotic", "Have a good one!", "Have a good one folks! Trump loves you!", "excited"),

    # =========================================================================
    # MISCELLANEOUS
    # =========================================================================
    VoiceLine("misc", "This combat walker truly showcases Super Earth's superior engineering.", "This walker! The best engineering!", "excited"),
    VoiceLine("misc", "Alien wildlife found -- assessment: adorable.", "Very cute! Almost as cute as me!", "confident"),
    VoiceLine("misc", "Local fauna identified -- possible source for emergency rations.", "Could be food. Probably delicious.", "confident"),
]

# Stats
if __name__ == "__main__":
    from collections import Counter
    cats = Counter(v.category for v in VOICE_LINES)
    print(f"Total voice lines: {len(VOICE_LINES)}")
    print(f"\nBy category:")
    for cat, count in cats.most_common():
        print(f"  {cat}: {count}")
