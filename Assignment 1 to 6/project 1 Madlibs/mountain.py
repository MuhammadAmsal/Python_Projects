def madlib():
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")
    adj4 = input("Adjective: ")
    noun1 = input("Mountain name or feature (e.g., peak, valley): ")
    noun2 = input("Equipment (e.g., rope, backpack, axe): ")
    noun3 = input("Explorer's name: ")
    noun4 = input("Treasure or goal (e.g., flag, summit, lost artifact): ")
    noun5 = input("Emotion (e.g., excitement, fear): ")
    noun6 = input("Object (e.g., compass, torch): ")
    noun_plural = input("Plural noun (e.g., climbers, glaciers, boulders): ")
    body_part = input("Body part: ")
    body_part2 = input("Body part: ")
    verb = input("Verb (present tense, e.g., climb, struggle): ")
    verb_past = input("Verb (past tense, e.g., reached, slipped): ")
    verb_past2 = input("Verb (past tense, e.g., conquered, lost): ")
    spell1 = input("Exclamation (e.g., Whoa!, Unbelievable!): ")
    spell2 = input("Another exclamation (e.g., We did it!, Incredible!): ")

    madlib = f"The {adj1} sun dipped behind the towering {noun1}, casting long shadows across the rugged landscape. \
The cold wind howled as {noun3} tightened their grip on the {noun2}, determined to {verb} further. The summit was near, \
but danger lurked ahead. Suddenly, the ice beneath their {body_part} cracked.\n\
\"{spell1}!\"\n\
\"{spell2}!\"\n\
A {adj2} avalanche rumbled down, shaking the mountain as {noun_plural} tumbled. With a {adj3} reflex, {noun3} \
{verb_past} to safety, clutching the {noun6} tightly. The climb was relentless, but the goal was within reach. \
At last, standing at the peak, the {adj4} view stretched endlessly before them. With the final step, {noun3} \
planted the {noun4} in triumph, their {body_part2} filled with {noun5}. The journey was over, sealed by a \
{verb_past2} adventure that would be remembered for ages."

    print(madlib)