# Backgrounds
image bg generic = Placeholder("bg")

# Characters
image arcum normal = Placeholder("boy")
image maxris normal = Placeholder("girl")
image nico normal = Placeholder("boy")
image zero normal = Placeholder("boy")
image scribam normal = Placeholder("boy")
image sandwich normal = Placeholder("boy")
image william normal = Placeholder("boy")
image pulse normal = Placeholder("boy")
image henry normal = Placeholder("boy")
    # Retired.
    image bran normal = Placeholder("boy")
    image jacob normal = Placeholder("boy")
    image matthias normal = Placeholder("boy")
    image nightwanderer normal = Placeholder("boy")

# Declare characters used by this game.
define arcum = Character("Arcum")
define maxris = Character("Maxris")
define nico = Character("Nico")
define zero = Character("Zero")
define scribam = Character("The Scribam")
define sandwich = Character("Sandwich")
define william = Character("William")
define pulse = Character("Pulse")
define henry = Character("Henry")
    # Retired
    define bran = Character("Bran")
    define jacob = Character("Jacob")
    define matthias = Character("Matthias")
    define nightwanderer = Character("Night-Wanderer")

# The game starts here.
label start:
    show bg generic
    show arcum normal
    arcum "As you can see, this game should work."
    arcum "If you can't see it, try turning it off and on again."
