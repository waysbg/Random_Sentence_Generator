from random import choice

name = ["Daniela", "Plamena", "Julia", "Maria", "Christina"]
places = ["Bourgas", "Kaspichan", "Dolno Debrene", "Bracigovo", "Vurbitza"]
verbs = ["plays with", "eats", "gives", "jumps", "touches"]
nouns = ["orange", "laundry machine", "tv", "fridge", "dog"]
adverbs = ["slowly", "sadly", "carefully", "impatiently", "badly"]
details = ["in the office", "at home", "in the park", "over the roof", "in the fitness"]

press = " "

while press != "end":
    random_name = choice(name)

    random_place = choice(places)
    random_verb = choice(verbs)
    random_noun = choice(nouns)
    random_adverb = choice(adverbs)
    random_detail = choice(details)
    print( f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}\n")
    press = input("Press [Enter] to generate new sentence or [end] to terminate: ")


