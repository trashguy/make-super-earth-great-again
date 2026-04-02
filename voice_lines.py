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
    VoiceLine("deployment", "Point me to the enemy.", "Point me to the enemy. I'll handle it, just like I handle everything.", "confident"),
    VoiceLine("deployment", "Ready to liberate.", "Ready to liberate. We're gonna liberate so hard, your head will spin.", "excited"),
    VoiceLine("deployment", "Joining the fray.", "I'm joining the fight. And when I fight, I win.", "confident"),
    VoiceLine("deployment", "Reporting to the front.", "I'm at the front. Somebody had to do it, and that somebody is me.", "confident"),
    VoiceLine("deployment", "Loadout confirmed.", "Loadout confirmed. Tremendous loadout. The best weapons.", "normal"),
    VoiceLine("deployment", "Weapons ready.", "Weapons ready. Big weapons. Beautiful weapons.", "confident"),
    VoiceLine("deployment", "Let's do this!", "Let's do this! Let's make Super Earth great again!", "excited"),
    VoiceLine("deployment", "Rolling out!", "Rolling out! Trump is rolling out, folks!", "excited"),
    VoiceLine("deployment", "We'll drop in here.", "We'll drop right here. Perfect spot. I pick the best spots.", "normal"),
    VoiceLine("deployment", "Inputting drop point.", "Inputting the drop point. Great location. Fantastic location.", "normal"),
    VoiceLine("deployment", "Strategy selected.", "Strategy selected. My strategy. The best strategy.", "confident"),

    # =========================================================================
    # RELOADING / AMMUNITION
    # =========================================================================
    VoiceLine("reload", "Reloading!", "Reloading! Gotta reload!", "urgent"),
    VoiceLine("reload", "Gotta reload!", "Hold on, I'm reloading, okay?", "urgent"),
    VoiceLine("reload", "Changing mag!", "New magazine! Tremendous magazine!", "urgent"),
    VoiceLine("reload", "New mag!", "Big new mag going in!", "normal"),
    VoiceLine("reload", "New mag.", "Beautiful new magazine.", "normal"),
    VoiceLine("reload", "Last reload!", "Last reload! They gave me the worst ammo supply, unbelievable!", "angry"),
    VoiceLine("reload", "Mag's empty.", "The magazine is empty. Very sad.", "normal"),
    VoiceLine("reload", "Out of ammo!", "I'm out of ammo! This is a disaster! Total disaster!", "angry"),
    VoiceLine("reload", "I'm out!", "I'm out! Can you believe it? They didn't give me enough ammo!", "angry"),
    VoiceLine("reload", "I need ammo.", "I need ammo. Somebody get me ammo. The best ammo.", "urgent"),
    VoiceLine("reload", "I need to reload.", "I need to reload. Hold on folks.", "normal"),
    VoiceLine("reload", "Need to reload!", "Gotta reload! Give me a second, just a second!", "urgent"),
    VoiceLine("reload", "Nothing in the chamber.", "Nothing in the chamber. Empty. Like a Democrat's promises.", "normal"),
    VoiceLine("reload", "Canister's empty!", "Canister's empty! Totally empty!", "urgent"),
    VoiceLine("reload", "New canister!", "New canister! Big beautiful canister!", "normal"),
    VoiceLine("reload", "New canister for maximum liberation.", "New canister for maximum liberation. We love liberation, don't we folks?", "excited"),
    VoiceLine("reload", "Need fresh ice.", "Need fresh ice. Get me the ice. The best ice.", "normal"),
    VoiceLine("reload", "Changing ice!", "Changing the ice! Gotta swap it out!", "urgent"),
    VoiceLine("reload", "Gotta swap ice!", "Swapping ice! Nobody swaps ice faster than me!", "urgent"),
    VoiceLine("reload", "Swapping internal cooling element.", "Swapping the cooling element. Very technical. I understand technology.", "normal"),
    VoiceLine("reload", "Reloading support weapon!", "Reloading the big gun! The really big beautiful gun!", "urgent"),
    VoiceLine("reload", "Team reload required!", "I need somebody to help me reload! Team reload!", "urgent"),
    VoiceLine("reload", "I need a team reload!", "Get over here and help me reload this thing!", "urgent"),
    VoiceLine("reload", "Need team reload!", "Team reload! Come on, help me out here!", "urgent"),
    VoiceLine("reload", "Performing assisted reload.", "I'm helping you reload. You're welcome, by the way.", "normal"),
    VoiceLine("reload", "Reloading you!", "I'm reloading you! See? I'm a team player. The best team player.", "normal"),

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
    VoiceLine("combat", "Get some! GET SOOOOME!", "Get some! We're winning so much! So much winning!", "shouting"),
    VoiceLine("combat", "Say hello to Democracy!", "Say hello to Democracy! The real Democracy, not the fake kind!", "shouting"),
    VoiceLine("combat", "Have a taste of Democracy!", "Have a taste of Democracy! Beautiful, beautiful Democracy!", "shouting"),
    VoiceLine("combat", "How'd you like the taste of Freedom?", "How do you like freedom? I love freedom. Tremendous freedom.", "excited"),
    VoiceLine("combat", "How about a nice cup of Liberty?", "How about some Liberty? We have the best Liberty!", "excited"),
    VoiceLine("combat", "You will never destroy our way of life!", "You will never destroy our way of life! Never ever!", "angry"),
    VoiceLine("combat", "Freedom forever!", "Freedom forever! Make Super Earth great again!", "shouting"),
    VoiceLine("combat", "FOR SUPER EARTH!!!", "FOR SUPER EARTH!!! MAKE SUPER EARTH GREAT AGAIN!!!", "shouting"),
    VoiceLine("combat", "FREEEEEDOM!!!", "FREEEEEDOM!!! BEAUTIFUL FREEDOM!!!", "shouting"),
    VoiceLine("combat", "KILL 'EM ALL!!!", "KILL EM ALL!!! EVERY SINGLE ONE!!!", "shouting"),
    VoiceLine("combat", "Burn in the fires of Democracy!", "Burn in the fires of Democracy! You're fired! Permanently!", "shouting"),
    VoiceLine("combat", "Let the light of Liberty shine!", "Let Liberty shine! The brightest light! Nobody shines brighter!", "excited"),
    VoiceLine("combat", "That's called Democracy!", "That's called Democracy, folks! We do it better than anybody!", "excited"),
    VoiceLine("combat", "You are the tinder, and Liberty is the match!", "You're the tinder, and I'm the match! A perfect match!", "excited"),
    VoiceLine("combat", "The flames of Democracy spread like wildfire!", "The flames of Democracy are spreading! Huge flames! Beautiful flames!", "excited"),
    VoiceLine("combat", "Liberty burns hot!", "Liberty burns hot! So hot! Incredibly hot!", "excited"),
    VoiceLine("combat", "*Maniacal laughter* AHAHAHAHA!", "Oh that was beautiful! That was so beautiful! Did you see that?", "excited"),
    VoiceLine("combat", "Freedom delivery!", "Freedom delivery! Free of charge! You're welcome!", "excited"),
    VoiceLine("combat", "For Liberty!", "For Liberty! For Super Earth! For Trump!", "shouting"),
    VoiceLine("combat", "Liberty for every being!", "Liberty for every being! Except the bugs. Not the bugs.", "normal"),
    VoiceLine("combat", "This is for you!", "This one's for you! From me! A gift!", "shouting"),

    # =========================================================================
    # ENEMY CALLOUTS
    # =========================================================================
    VoiceLine("enemy", "Contact!", "Contact! We've got bad guys!", "urgent"),
    VoiceLine("enemy", "Enemy spotted!", "I see them! I see the enemy! Big enemy!", "urgent"),
    VoiceLine("enemy", "Enemies spotted!", "Enemies everywhere! They're not sending their best!", "urgent"),
    VoiceLine("enemy", "Engaging!", "Engaging! I'm going in!", "urgent"),
    VoiceLine("enemy", "Not engaging.", "Not engaging. We'll get them later. Strategic.", "normal"),
    VoiceLine("enemy", "Enemy patrol!", "Enemy patrol! Bad hombres on patrol!", "urgent"),
    VoiceLine("enemy", "Enemy outpost spotted! Look alive!", "Enemy outpost! Big outpost! We're gonna take it, believe me!", "urgent"),
    VoiceLine("enemy", "Enemy outpost!", "Outpost! Enemy outpost! Nasty place!", "urgent"),
    VoiceLine("enemy", "Enemy emplacement!", "They've got a position set up! Very unfair!", "urgent"),
    VoiceLine("enemy", "Enemy elite!", "Big one! Elite enemy! But I've dealt with worse, believe me!", "urgent"),
    VoiceLine("enemy", "Heavy!", "Heavy! A big heavy! Huge!", "urgent"),
    VoiceLine("enemy", "Aerial enemy!", "They're in the air! Aerial enemy! Shoot it down!", "urgent"),
    VoiceLine("enemy", "Dropships!", "Dropships coming in! More of them! Unbelievable!", "urgent"),
    VoiceLine("enemy", "Bugs!", "Bugs! Disgusting bugs! Nasty!", "angry"),
    VoiceLine("enemy", "Bug outpost spotted! Prepare to exterminate!", "Bug outpost! We're gonna exterminate them! Total extermination!", "angry"),
    VoiceLine("enemy", "Bug hive spotted!", "Bug hive! Disgusting! We're shutting it down!", "angry"),
    VoiceLine("enemy", "Bug tunnel breach!", "They're coming out of the ground! Out of the tunnels!", "urgent"),
    VoiceLine("enemy", "Bughole!", "Bug hole right there! Nasty! Very nasty! We gotta shut it down, believe me!", "angry"),
    VoiceLine("enemy", "Squids!", "Squids! Alien squids! Very nasty!", "urgent"),
    VoiceLine("enemy", "Illuminate!", "Illuminate! They think they're so smart! They're not!", "angry"),
    VoiceLine("enemy", "Illuminate teleporting in!", "They're teleporting! Very unfair! Teleporting is cheating!", "angry"),
    VoiceLine("enemy", "Squid outpost spotted!", "Squid outpost! We see it! Taking it down!", "urgent"),
    VoiceLine("enemy", "Squid warp gate!", "Warp gate! A big ugly warp gate!", "urgent"),
    VoiceLine("enemy", "Bot fabricator!", "Bot factory! They're building robots! Not on my watch!", "urgent"),
    VoiceLine("enemy", "Dangerous wildlife.", "Dangerous animal. Very dangerous. Be careful.", "normal"),
    VoiceLine("enemy", "Harmless animal.", "Harmless animal. Nice animal. Very cute.", "normal"),
    VoiceLine("enemy", "Local fauna.", "Local wildlife. Interesting. Very interesting.", "normal"),

    # =========================================================================
    # STRATAGEM CALLOUTS
    # =========================================================================
    # Eagle / Air Support
    VoiceLine("stratagem", "Requesting air support!", "Calling in air support! The best air support!", "urgent"),
    VoiceLine("stratagem", "Sending in an Eagle!", "Sending in the Eagle! Beautiful Eagle! Bald Eagle!", "excited"),
    VoiceLine("stratagem", "Calling in an Eagle.", "Eagle coming in. Majestic. Very majestic.", "normal"),

    # Orbital Strikes
    VoiceLine("stratagem", "Requesting orbital strike!", "Requesting orbital strike! The biggest strike you've ever seen!", "urgent"),
    VoiceLine("stratagem", "Requesting orbital!", "Give me an orbital! A big beautiful orbital!", "urgent"),
    VoiceLine("stratagem", "Calling in orbital strike!", "Orbital strike coming in! This is gonna be huge!", "excited"),
    VoiceLine("stratagem", "Orbital incoming!", "Orbital incoming! Take cover! Big one coming!", "shouting"),
    VoiceLine("stratagem", "Orbital inbound!", "Orbital on the way! Tremendous firepower!", "urgent"),

    # Support Weapons
    VoiceLine("stratagem", "Requesting advanced weaponry!", "Get me the good stuff! The really good weapons!", "urgent"),
    VoiceLine("stratagem", "Calling down a support weapon!", "Support weapon dropping in! Big weapon! Beautiful weapon!", "excited"),
    VoiceLine("stratagem", "Support weapon inbound!", "Weapon incoming! You're gonna love this weapon!", "excited"),
    VoiceLine("stratagem", "Freedom requires firepower.", "Freedom requires firepower. And I have the best firepower.", "confident"),
    VoiceLine("stratagem", "Requesting TACPAC!", "I need a tack-pack! The best tack-pack!", "urgent"),
    VoiceLine("stratagem", "TACPAC inbound!", "Tack-pack on the way! Tremendous pack!", "normal"),

    # Supplies
    VoiceLine("stratagem", "Throwing supply beacon!", "Supply beacon going out! Supplies incoming!", "normal"),
    VoiceLine("stratagem", "Calling down supplies!", "Calling in supplies! The best supplies!", "normal"),
    VoiceLine("stratagem", "Requesting supplies!", "I need supplies! Get me supplies!", "urgent"),
    VoiceLine("stratagem", "Supplies!", "Supplies! Beautiful supplies!", "normal"),

    # Reinforcements
    VoiceLine("stratagem", "Calling in reinforcements!", "Calling in backup! More great people coming!", "urgent"),
    VoiceLine("stratagem", "Another diver for the cause.", "Another diver joining us. Good. We need winners.", "normal"),
    VoiceLine("stratagem", "Reinforcing!", "Reinforcements! We're bringing in more tremendous people!", "urgent"),
    VoiceLine("stratagem", "No diver left behind!", "No diver left behind! That's the Trump guarantee!", "confident"),

    # Sentries / Fortifications / Vehicles
    VoiceLine("stratagem", "Calling down a sentry.", "Sentry coming in. Gonna build a sentry. A great sentry.", "normal"),
    VoiceLine("stratagem", "Requesting sentry!", "Get me a sentry! We need border protection!", "urgent"),
    VoiceLine("stratagem", "Calling down fortifications.", "Building fortifications. We're building a wall, basically.", "normal"),
    VoiceLine("stratagem", "Requesting fortifications!", "I need fortifications! Big, beautiful fortifications!", "urgent"),
    VoiceLine("stratagem", "Calling down a vehicle!", "Vehicle incoming! A beautiful vehicle!", "excited"),
    VoiceLine("stratagem", "Requesting vehicle!", "Get me a vehicle! The biggest vehicle!", "urgent"),
    VoiceLine("stratagem", "Calling down a walker!", "Walker coming in! A tremendous walker!", "excited"),
    VoiceLine("stratagem", "Requesting walker!", "I want a walker! Get me the walker!", "urgent"),
    VoiceLine("stratagem", "Manning combat walker!", "I'm getting in the walker! This is gonna be great!", "excited"),

    # Equipment / Objectives
    VoiceLine("stratagem", "Calling down equipment!", "Equipment dropping in! Top of the line!", "normal"),
    VoiceLine("stratagem", "Requesting equipment!", "I need equipment! The best equipment!", "urgent"),
    VoiceLine("stratagem", "Calling down objective equipment!", "Objective equipment coming in! Very important equipment!", "normal"),
    VoiceLine("stratagem", "Requesting objective equipment!", "I need the objective gear! Mission critical!", "urgent"),
    VoiceLine("stratagem", "Objective equipment.", "Objective equipment. Very important. The most important.", "normal"),

    # Hellbomb / SOS / Flare
    VoiceLine("stratagem", "Calling in a hellbomb!", "HELLBOMB! The biggest bomb! You're gonna love it!", "excited"),
    VoiceLine("stratagem", "Hellbomb armed -- clear the area!", "Hellbomb is armed! Get out! Get out now! It's gonna be huge!", "shouting"),
    VoiceLine("stratagem", "Hellbomb.", "Hellbomb. Very powerful. The most powerful.", "normal"),
    VoiceLine("stratagem", "Deploying SOS beacon.", "Sending out an SOS. We need help. Tremendous help.", "urgent"),
    VoiceLine("stratagem", "Sending out an SOS!", "SOS! We need people! Send everyone!", "urgent"),
    VoiceLine("stratagem", "S.O.S.!", "S.O.S.! Help! Send help!", "urgent"),
    VoiceLine("stratagem", "Deploying flare!", "Flare going up! Light it up! Beautiful light!", "normal"),

    # =========================================================================
    # INJURY / DAMAGE
    # =========================================================================
    # General
    VoiceLine("injury", "I'm bleeding out!", "I'm bleeding! This is terrible! Very bad!", "angry"),
    VoiceLine("injury", "I'm hit! Sweet Liberty... the blood!", "I'm hit! Look at the blood! This suit was expensive!", "angry"),
    VoiceLine("injury", "The blood! I can't stop the blood!", "So much blood! Somebody do something! This is a disaster!", "angry"),
    VoiceLine("injury", "Can't survive these wounds much longer!", "I can't take much more of this! Very unfair!", "angry"),
    VoiceLine("injury", "I'm losing so much blood!", "I'm losing blood! Tremendous amounts of blood!", "angry"),
    VoiceLine("injury", "More blood loss than manual recommends.", "More blood than the doctors say is good. Not great.", "normal"),
    VoiceLine("injury", "Ouch!", "Ow! That hurt! Very unfair!", "angry"),
    VoiceLine("injury", "AHHH!", "AHHH! They got me! Can you believe it?!", "shouting"),

    # Arms
    VoiceLine("injury", "Sweet Liberty, my arm!", "My arm! They got my arm! This is terrible!", "angry"),
    VoiceLine("injury", "MY ARM!", "MY ARM! Do you see this?! MY ARM!", "shouting"),
    VoiceLine("injury", "Can't liberate with this broken arm!", "Can't fight with a broken arm! Very unfair disadvantage!", "angry"),
    VoiceLine("injury", "Cannot liberate effectively with injured arm.", "My arm is hurt. Can't operate at full capacity. Sad.", "normal"),
    VoiceLine("injury", "Gotta fix this Liberty-forsaken arm!", "I gotta fix this arm! This arm used to be perfect!", "angry"),
    VoiceLine("injury", "Gotta patch up this arm!", "Gotta fix the arm! The arm needs work!", "urgent"),
    VoiceLine("injury", "I need to do something about my arm!", "My arm! I need to do something about my arm! Somebody help!", "urgent"),

    # Legs
    VoiceLine("injury", "Sweet Liberty, my leg!", "My leg! They got my beautiful leg!", "angry"),
    VoiceLine("injury", "MY LEG!", "MY LEG! Look what they did to my leg!", "shouting"),
    VoiceLine("injury", "My legs! For the love of Liberty, my legs!", "My legs! Both legs! This is the worst! Absolute worst!", "shouting"),
    VoiceLine("injury", "Oh, my legs!", "Oh my legs! My beautiful legs!", "angry"),
    VoiceLine("injury", "Flag-forsaken leg's slowin' me down!", "This leg is slowing me down! I used to be fast! Very fast!", "angry"),
    VoiceLine("injury", "Gotta patch up this leg!", "Gotta fix this leg! Come on!", "urgent"),
    VoiceLine("injury", "My leg -- not functioning at capacity.", "My leg is not working right. Not at full power. Sad.", "normal"),
    VoiceLine("injury", "Limping is not liberating.", "I'm limping! Can't liberate while limping! Very bad!", "angry"),

    # No Stims
    VoiceLine("injury", "Out of stims!", "Out of stims! No stims! This is a catastrophe!", "angry"),
    VoiceLine("injury", "I need stims!", "I need stims! Somebody give me stims!", "urgent"),
    VoiceLine("injury", "I could truly use a stim!", "I really need a stim right now! Really badly!", "urgent"),
    VoiceLine("injury", "Need... stim!", "Need... a stim... come on...", "urgent"),

    # =========================================================================
    # HEALING
    # =========================================================================
    # Self
    VoiceLine("healing", "Feels gooooood.", "That feels incredible. I feel incredible. The best I've ever felt.", "confident"),
    VoiceLine("healing", "Freedom never sleeps!", "I never sleep! Freedom never sleeps! We keep going!", "excited"),
    VoiceLine("healing", "Freedom never rests!", "We never rest! Always fighting! Always winning!", "excited"),
    VoiceLine("healing", "My life for Super Earth!", "My life for Super Earth! I'd do anything for this planet!", "confident"),
    VoiceLine("healing", "My body for Super Earth!", "This body, for Super Earth! A great body, by the way!", "confident"),
    VoiceLine("healing", "Must defend prosperity!", "We must defend prosperity! Our prosperity! The best prosperity!", "confident"),
    VoiceLine("healing", "Democracy needs me.", "Democracy needs me. And frankly, I need Democracy.", "confident"),
    VoiceLine("healing", "Helldivers never die!", "Trump never dies! I mean, Helldivers never die!", "excited"),
    VoiceLine("healing", "A little shot o' Liberty.", "A little shot of Liberty. Just what the doctor ordered.", "normal"),
    VoiceLine("healing", "No pain, no freedom!", "No pain, no freedom! I know pain! I know freedom!", "confident"),
    VoiceLine("healing", "Injury? What injury!", "Injury? What injury? I feel perfect! Absolutely perfect!", "excited"),
    VoiceLine("healing", "Not today!", "Not today! Not gonna happen! I don't lose!", "confident"),
    VoiceLine("healing", "Whatever it takes.", "Whatever it takes. I always do whatever it takes.", "confident"),
    VoiceLine("healing", "Liberty heal me!", "Liberty, heal me! I'm too important to go down!", "urgent"),
    VoiceLine("healing", "Liberty save me!", "Save me! I'm very important! Very very important!", "urgent"),
    VoiceLine("healing", "Liberty shield me!", "Shield me! Protect your favorite president!", "urgent"),

    # Healing Teammates
    VoiceLine("healing", "Stimming you!", "I'm healing you! You're welcome!", "normal"),
    VoiceLine("healing", "Administering meds!", "Taking care of you! I take care of my people!", "normal"),
    VoiceLine("healing", "No diver left behind!", "No diver left behind! That's my policy! Great policy!", "confident"),
    VoiceLine("healing", "Live to dive another day.", "Live to fight another day. That's what winners do.", "normal"),
    VoiceLine("healing", "Democracy isn't done with you yet.", "We're not done with you yet! Get up! We need you!", "confident"),
    VoiceLine("healing", "I've got you.", "I've got you. Don't worry. Trump's got you.", "confident"),
    VoiceLine("healing", "I got you.", "I got you. You're gonna be fine. Believe me.", "confident"),

    # =========================================================================
    # SAMPLE COLLECTION
    # =========================================================================
    VoiceLine("samples", "Got a sample!", "Got a sample! Beautiful sample!", "normal"),
    VoiceLine("samples", "Sample collected!", "Sample collected! Tremendous sample!", "normal"),
    VoiceLine("samples", "Another sample collected for Democracy.", "Another sample for the cause. We're collecting them all.", "normal"),
    VoiceLine("samples", "This sample should greatly aid in the war effort.", "This sample is gonna help us win. Big league.", "confident"),
    VoiceLine("samples", "Democracy fills my sample container.", "My container is filling up. Great samples. The best samples.", "normal"),
    VoiceLine("samples", "This biosample will directly increase our freedom.", "This sample is gonna make us stronger. Much stronger.", "confident"),
    VoiceLine("samples", "This biological sample will provide excellent data.", "Excellent data from this sample. I love data. Good data.", "normal"),
    VoiceLine("samples", "Biological sample secured!", "Sample secured! Locked down! Nobody's taking this sample!", "normal"),
    VoiceLine("samples", "Rare sample collected!", "Rare sample! Very rare! Like a Trump steak! Very valuable!", "excited"),
    VoiceLine("samples", "Rare sample acquired.", "Rare sample. Very rare. Very special.", "normal"),
    VoiceLine("samples", "High-value sample collected!", "High-value sample! The most valuable! Tremendous value!", "excited"),
    VoiceLine("samples", "Tech sample acquired!", "Tech sample acquired! Great technology! The best technology!", "normal"),

    # =========================================================================
    # ITEM / RESOURCE PICKUP
    # =========================================================================
    VoiceLine("pickup", "Package acquired!", "Package acquired! Great package!", "normal"),
    VoiceLine("pickup", "Artifact collected.", "Artifact! A beautiful artifact! Very collectible!", "normal"),
    VoiceLine("pickup", "Illuminate artifact acquired!", "Squid artifact! Taking their stuff! Love it!", "excited"),
    VoiceLine("pickup", "Legendarium acquired!", "Legendarium! Legendary! Almost as legendary as me!", "excited"),
    VoiceLine("pickup", "Legendarium -- truly as legendary as the name suggests.", "Legendarium! Truly legendary. Not as legendary as Trump, but close.", "confident"),
    VoiceLine("pickup", "Crystallized E710 acquired!", "E seven ten! Beautiful crystals! The best crystals!", "normal"),
    VoiceLine("pickup", "This crystallized E710 will help fuel our future!", "This fuel is gonna power our future! A great future!", "confident"),
    VoiceLine("pickup", "E-710, the galaxy's greatest energy source.", "E seven ten. The galaxy's best energy. I know energy. Big energy guy.", "confident"),
    VoiceLine("pickup", "Super uranium acquired!", "Super uranium! Very powerful! Tremendously powerful and very safe!", "normal"),
    VoiceLine("pickup", "Super uranium -- safe enough for babies!", "Super uranium! Totally safe! The safest! I'd give it to a baby!", "confident"),
    VoiceLine("pickup", "Super uranium -- defier of gravity and extremely safe.", "Super uranium. Defies gravity. Extremely safe. I guarantee it.", "confident"),
    VoiceLine("pickup", "Black saffron harvested!", "Black saffron! Very expensive stuff! I know expensive!", "normal"),
    VoiceLine("pickup", "Black saffron -- life-saving and non-habit-forming.", "Black saffron. Saves lives. No side effects. Perfect. Like me.", "confident"),
    VoiceLine("pickup", "One small scrap of technology, one giant leap for Liberty.", "A small piece of tech, a giant leap for freedom. Very poetic. I'm poetic.", "confident"),
    VoiceLine("pickup", "This small bit of technology may lead to a large increase in Liberty.", "This technology is gonna increase our freedom. Big increase. Huge.", "confident"),
    VoiceLine("pickup", "This canister will see me through.", "This canister. Very useful. I always find the best stuff.", "normal"),

    # =========================================================================
    # DROPPING / MARKING ITEMS
    # =========================================================================
    VoiceLine("marking", "Dropping item.", "Dropping this item. Take it. It's a gift.", "normal"),
    VoiceLine("marking", "Dropping package!", "Dropping a package! A beautiful package! For you!", "normal"),
    VoiceLine("marking", "Dropping high-value item.", "Dropping something very valuable. Very very valuable.", "normal"),
    VoiceLine("marking", "Dropping a pin.", "I'm marking it. Right here. Remember this spot.", "normal"),
    VoiceLine("marking", "Marking location.", "Marking the location. Great location.", "normal"),
    VoiceLine("marking", "Tagging location.", "Tagging it. I'm tagging it. Right there.", "normal"),
    VoiceLine("marking", "Tagging map.", "Putting it on the map. On the map. Very important.", "normal"),
    VoiceLine("marking", "High-value item.", "High-value item! Very valuable! Don't miss this!", "normal"),
    VoiceLine("marking", "Critical item.", "Critical item. Very important. The most important.", "urgent"),

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
    VoiceLine("ping", "Objective located.", "Objective found! I found it! I always find things!", "normal"),
    VoiceLine("ping", "There's something here.", "There's something here. Something big. I can feel it.", "normal"),
    VoiceLine("ping", "Found something!", "Found something! Look at this! Tremendous!", "excited"),
    VoiceLine("ping", "There.", "Right there!", "normal"),
    VoiceLine("ping", "Here.", "Right here!", "normal"),
    VoiceLine("ping", "What about here?", "What about right here? Great spot.", "normal"),
    VoiceLine("ping", "That one.", "That one! Right there!", "normal"),
    VoiceLine("ping", "Intel.", "Intel! Very important intel!", "normal"),
    VoiceLine("ping", "Sub-objective.", "Sub-objective. We'll handle it.", "normal"),
    VoiceLine("ping", "Primary objective.", "Primary objective! The big one! The main event!", "confident"),
    VoiceLine("ping", "Tactical benefit.", "Tactical advantage! Very smart! I love tactics!", "normal"),
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
    VoiceLine("movement", "Follow me!", "Follow me! I know the way! The best way!", "urgent"),
    VoiceLine("movement", "Move!", "Move it! Let's go! Come on!", "urgent"),
    VoiceLine("movement", "MOVE MOVE MOVE!", "MOVE MOVE MOVE! COME ON PEOPLE!", "shouting"),
    VoiceLine("movement", "On my way.", "On my way. I'm coming. Don't worry.", "normal"),
    VoiceLine("movement", "Heading there now.", "Heading there now. I'm fast. Very fast.", "normal"),
    VoiceLine("movement", "I'm on it!", "I'm on it! Nobody handles things faster than me!", "confident"),
    VoiceLine("movement", "Hold position.", "Hold your position! Stay right there! Don't move!", "urgent"),
    VoiceLine("movement", "Fall back!", "Fall back! We're pulling back! Strategic retreat!", "urgent"),
    VoiceLine("movement", "RUN!!!", "RUN!!! GET OUT OF THERE!!! GO GO GO!!!", "shouting"),
    VoiceLine("movement", "Steering clear!", "Staying away from that! Not going near it! No way!", "urgent"),
    VoiceLine("movement", "On my position.", "Come to me! On my position!", "normal"),

    # =========================================================================
    # RESPONSES
    # =========================================================================
    VoiceLine("response", "Affirmative!", "Absolutely! One hundred percent!", "confident"),
    VoiceLine("response", "Yes!", "Yes! Definitely yes!", "confident"),
    VoiceLine("response", "Negative.", "No. That's a no. Hard no.", "normal"),
    VoiceLine("response", "No.", "No. Wrong.", "normal"),
    VoiceLine("response", "Cancel that.", "Cancel that. Forget it. Bad idea.", "normal"),
    VoiceLine("response", "Nevermind.", "Nevermind. Forget I said anything.", "normal"),
    VoiceLine("response", "I'll take it.", "I'll take it! Give it to me!", "normal"),
    VoiceLine("response", "Don't need it.", "Don't need it. I'm good. I'm always good.", "normal"),
    VoiceLine("response", "Thank you.", "Thank you. Very nice. I appreciate it.", "normal"),
    VoiceLine("response", "I'm sorry.", "I'm sorry. That was my fault. It happens. Rarely, but it happens.", "normal"),
    VoiceLine("response", "Nice!", "Nice! Beautiful! Fantastic!", "excited"),
    VoiceLine("response", "Done!", "Done! Finished! Perfect!", "excited"),

    # =========================================================================
    # EXTRACTION
    # =========================================================================
    VoiceLine("extraction", "Calling an extraction!", "Calling the extraction! Time to go! We won!", "excited"),
    VoiceLine("extraction", "Calling in extraction.", "Extraction called. The shuttle's coming. Beautiful shuttle.", "normal"),
    VoiceLine("extraction", "Marking extraction point.", "Extraction point right here. Great spot. Perfect spot.", "normal"),
    VoiceLine("extraction", "Entering shuttle.", "Getting on the shuttle. First class. Always first class.", "normal"),
    VoiceLine("extraction", "Get in!", "Get in! Get in the shuttle! Let's go!", "urgent"),

    # =========================================================================
    # JUMP PACK
    # =========================================================================
    VoiceLine("jumppack", "Activating jump pack!", "Jump pack activated! I'm flying! Beautiful!", "excited"),
    VoiceLine("jumppack", "To the skies!", "To the skies! Like an eagle! A bald eagle!", "excited"),
    VoiceLine("jumppack", "Liberty leap!", "Liberty leap! A tremendous leap!", "excited"),

    # =========================================================================
    # TERMINAL / OBJECTIVES
    # =========================================================================
    VoiceLine("terminal", "I'm on the terminal.", "I'm on the terminal. Very good with computers. The best.", "normal"),
    VoiceLine("terminal", "I got the terminal!", "I got the terminal! Very technical stuff! I understand it!", "confident"),
    VoiceLine("terminal", "I'll handle the terminal.", "I'll handle the terminal. Nobody handles terminals better.", "confident"),
    VoiceLine("terminal", "Engaging terminal.", "Working the terminal. Very complicated. But not for me.", "normal"),
    VoiceLine("terminal", "We've got equipment.", "We've got equipment! Great equipment!", "normal"),

    # =========================================================================
    # WEATHER / VISIBILITY
    # =========================================================================
    VoiceLine("weather", "Visibility decreasing.", "Can't see anything! Visibility is terrible! Very bad!", "normal"),
    VoiceLine("weather", "Decreased visibility should help obscure our movements.", "Low visibility. Good for us. They can't see us. Very strategic.", "normal"),
    VoiceLine("weather", "Visibility improving -- avoid being an easy target.", "Visibility improving. Don't be a target. Be smart about it.", "normal"),
    VoiceLine("weather", "Increased visibility. We can see them. They can see us.", "We can see them now. But they can see us too. Be careful.", "normal"),

    # =========================================================================
    # VICTORY / PATRIOTIC FLAVOR
    # =========================================================================
    VoiceLine("patriotic", "I fight for Super Earth.", "I fight for Super Earth! The greatest planet in the galaxy!", "confident"),
    VoiceLine("patriotic", "I fight for freedom.", "I fight for freedom! Real freedom! Trump freedom!", "confident"),
    VoiceLine("patriotic", "I am a soldier of Liberty.", "I am a soldier of Liberty! The best soldier!", "confident"),
    VoiceLine("patriotic", "I am a soldier of Democracy.", "I am a soldier of Democracy! A tremendous soldier!", "confident"),
    VoiceLine("patriotic", "Democracy conquers all.", "Democracy conquers all! Always wins! Like me!", "confident"),
    VoiceLine("patriotic", "Democracy for all.", "Democracy for all! Everyone gets Democracy! It's free!", "excited"),
    VoiceLine("patriotic", "Liberty, prosperity, Democracy.", "Liberty! Prosperity! Democracy! And Trump!", "confident"),
    VoiceLine("patriotic", "Liberty guides my hand.", "Liberty guides my hand! Steady hand! Very steady!", "confident"),
    VoiceLine("patriotic", "Liberty will prevail.", "Liberty will prevail! We always prevail! Always!", "confident"),
    VoiceLine("patriotic", "Liberty will not fall.", "Liberty will never fall! Not on my watch! Never!", "confident"),
    VoiceLine("patriotic", "For prosperity!", "For prosperity! Tremendous prosperity!", "excited"),
    VoiceLine("patriotic", "Our way of life must be protected.", "Our way of life must be protected! At all costs!", "confident"),
    VoiceLine("patriotic", "I will protect Democracy at all costs.", "I will protect Democracy! At all costs! Nobody protects it better!", "confident"),
    VoiceLine("patriotic", "I will protect our way of life.", "I will protect our way of life! I always protect! The best protector!", "confident"),
    VoiceLine("patriotic", "I will keep Super Earth safe.", "I will keep Super Earth safe! The safest it's ever been!", "confident"),
    VoiceLine("patriotic", "Freedom fight!", "Freedom fight! Let's fight! Big fight!", "shouting"),
    VoiceLine("patriotic", "Let's play!", "Let's play! Game time! I love games! I always win!", "excited"),
    VoiceLine("patriotic", "I win!", "I win! Of course I win! I always win!", "excited"),
    VoiceLine("patriotic", "You win.", "You win. This time. Enjoy it.", "normal"),
    VoiceLine("patriotic", "Tie!", "It's a tie! Nobody wins! Very boring!", "normal"),
    VoiceLine("patriotic", "Have a good one!", "Have a good one, folks! Trump loves you!", "confident"),

    # =========================================================================
    # MISCELLANEOUS
    # =========================================================================
    VoiceLine("misc", "This combat walker truly showcases Super Earth's superior engineering.", "This walker is incredible! Super Earth engineering! The best engineering! Nobody builds like us!", "excited"),
    VoiceLine("misc", "Alien wildlife found -- assessment: adorable.", "Look at this little alien thing! Very cute! Almost as cute as me!", "normal"),
    VoiceLine("misc", "Local fauna identified -- possible source for emergency rations.", "Local wildlife. Could be food. Probably delicious. Everything I eat is delicious.", "normal"),
]

# Stats
if __name__ == "__main__":
    from collections import Counter
    cats = Counter(v.category for v in VOICE_LINES)
    print(f"Total voice lines: {len(VOICE_LINES)}")
    print(f"\nBy category:")
    for cat, count in cats.most_common():
        print(f"  {cat}: {count}")
