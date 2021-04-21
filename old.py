# import

import random
import math
import os

# formatting

udl = '\033[4m'
end = '\033[0m'
bld = '\033[1m'

loopcheck = True
while loopcheck == True:
    # functions

    def die(y):  # dice rolling
        return random.randint(1, y)

    def statgen():
        rolls = ([die(6), die(6), die(6), die(6)])
        rolls.sort()
        return (sum(rolls) - rolls[0])

    def mod(n):  # Modifier
        MOD_calc = math.floor((n - 10) / 2)
        return MOD_calc

    def hp(n):  # Hit Point
        HP_calc = n + mod(CON)
        return HP_calc

    def ac(n):
        AC_calc = 10 + mod(n)
        return AC_calc

    def bg():
        charbg = [
            'Acolyte', 'Charlatan', 'Criminal / Spy', 'Entertainer',
            'Folk Hero', 'Gladiator', 'Guild Artisan \ Guild Merchant',
            'Hemit', 'Knight', 'Noble', 'Outlander', 'Pirate', 'Sage',
            'Sailor', 'Soldier', 'Urchin'
        ]
        return random.choice(charbg)

    def quirk():
        charquirk = [
            "They swear exclusively using flower names.",
            "They belief that 'Hello' is a type of insult.",
            "They can't distinguish between left and right.",
            "They must have a good long think before making any purchases. No matter how small.",
            "They go through at least one sDwarf-help book every week.",
            "They start the day by warming up their vocal chords. Loudly.",
            "They are of the opinion that mayonaisse goes well with every dish.",
            "Their motto is 'You can fit any peg through a round hole if you bring a saw.'"
        ]

        return random.choice(charquirk)

    def stats():  # Stat Print
        print(udl + "\nCHARACTERSHEET" + end)
        print("\nRACE:", c_char_race, "\nCLASS:", c_char_class,
              "\nBACKGROUND:", bg(), "\nQUIRK:", quirk(), '\n')

        print('HP:', HP, '\nAC:', AC, '\nSP:', SP)

        print('\nSTR:', STR, mod(STR), '\nDEX:', DEX, mod(DEX), '\nCON:', CON,
              mod(CON), '\nINT:', INT, mod(INT), '\nWIS:', WIS, mod(WIS),
              '\nCHA:', CHA, mod(CHA), '\n')

    statlist = [
        statgen(),
        statgen(),
        statgen(),
        statgen(),
        statgen(),
        statgen(),
        statgen()
    ]
    statlist_s = sorted(statlist, reverse=True)

    # Races

    Dwarf = '1'

    # Classes

    Barbarian = '1'
    Bard = '2'
    Cleric = '3'
    Druid = '4'
    Fighter = '5'
    Monk = '6'
    Paladin = '7'
    Ranger = '8'
    Rogue = '9'
    Sorcerer = '10'
    Warlock = '11'
    Wizard = '12'

    # choosing a race

    print('Choose your RACE\n1.  Dwarf')

    char_race = input('\nCHOICE: \n')

    if (char_race == Dwarf):
        c_char_race = 'Dwarf'

    # choosing a class

    print(
        'Choose your class:\n1.  Barbarian\n2.  Bard\n3.  Cleric\n4.  Druid\n5.  Fighter\n6.  Monk\n7.  Paladin\n8.  Ranger\n9.  Rogue\n10. Sorcerer\n11. Warlock\n12. Wizard'
    )

    char_class = input('\nCHOICE: \n')

    # Barbarian

    if (char_class == Barbarian):
        c_char_class = 'Barbarian'

        STR = statlist_s[0]
        DEX = statlist_s[2]
        CON = statlist_s[1]
        INT = statlist_s[5]
        WIS = statlist_s[4]
        CHA = statlist_s[3]

        HP = hp(12)
        AC = ac(DEX)

    if (char_class == Bard):
        c_char_class = 'Bard'

        STR = statlist_s[5]
        DEX = statlist_s[2]
        CON = statlist_s[1]
        INT = statlist_s[4]
        WIS = statlist_s[3]
        CHA = statlist_s[0]

        HP = hp(8)
        AC = ac(DEX)

    # Cleric

    if (char_class == Cleric):
        c_char_class = 'Cleric'

        STR = statlist_s[3]
        DEX = statlist_s[2]
        CON = statlist_s[1]
        INT = statlist_s[5]
        WIS = statlist_s[0]
        CHA = statlist_s[4]

        HP = hp(8)
        AC = ac(DEX)

    # Druid

    if (char_class == Druid):
        c_char_class = 'Druid'

        STR = statlist_s[4]
        DEX = statlist_s[1]
        CON = statlist_s[2]
        INT = statlist_s[3]
        WIS = statlist_s[0]
        CHA = statlist_s[5]

        HP = hp(8)
        AC = ac(DEX)

    # Fighter

    if (char_class == Fighter):
        c_char_class = 'Fighter'

        STR = statlist_s[0]
        DEX = statlist_s[2]
        CON = statlist_s[1]
        INT = statlist_s[5]
        WIS = statlist_s[3]
        CHA = statlist_s[4]

        HP = hp(10)
        AC = ac(DEX)

        # Monk

    if (char_class == Monk):
        c_char_class = 'Monk'

        STR = statlist_s[3]
        DEX = statlist_s[0]
        CON = statlist_s[2]
        INT = statlist_s[4]
        WIS = statlist_s[1]
        CHA = statlist_s[5]

        HP = hp(8)
        AC = ac(DEX) + mod(WIS)

    # Paladin

    if (char_class == Paladin):
        c_char_class = 'Paladin'

        STR = statlist_s[0]
        DEX = statlist_s[3]
        CON = statlist_s[1]
        INT = statlist_s[5]
        WIS = statlist_s[4]
        CHA = statlist_s[2]

        HP = hp(10)
        AC = ac(DEX)

    # Ranger

    if (char_class == Ranger):
        c_char_class = 'Ranger'

        STR = statlist_s[4]
        DEX = statlist_s[0]
        CON = statlist_s[2]
        INT = statlist_s[3]
        WIS = statlist_s[1]
        CHA = statlist_s[5]

        HP = hp(10)
        AC = ac(DEX)

    # Rogue

    if (char_class == Rogue):
        c_char_class = 'Rogue'

        STR = statlist_s[5]
        DEX = statlist_s[0]
        CON = statlist_s[1]
        INT = statlist_s[4]
        WIS = statlist_s[3]
        CHA = statlist_s[2]

        HP = hp(6)
        AC = ac(DEX)

    # Sorcerer

    if (char_class == Sorcerer):
        c_char_class = 'Sorcerer'

        STR = statlist_s[5]
        DEX = statlist_s[3]
        CON = statlist_s[1]
        INT = statlist_s[4]
        WIS = statlist_s[2]
        CHA = statlist_s[0]

        HP = hp(6)
        AC = ac(DEX)

    # Warlock

    if (char_class == Warlock):
        c_char_class = 'Warlock'

        STR = statlist_s[4]
        DEX = statlist_s[2]
        CON = statlist_s[1]
        INT = statlist_s[5]
        WIS = statlist_s[3]
        CHA = statlist_s[0]

        HP = hp(8)
        AC = ac(DEX)

        stats()

    # Wizard

    if (char_class == Wizard):
        c_char_class = 'Wizard'

        STR = statlist_s[5]
        DEX = statlist_s[3]
        CON = statlist_s[1]
        INT = statlist_s[0]
        WIS = statlist_s[2]
        CHA = statlist_s[4]

        HP = hp(6)
        AC = ac(DEX)

    # race mods

    if (char_race == Dwarf):  # mountain dwarf
        SP = 25
        CON += 2
        STR += 2

    os.system('cls' if os.name == 'nt' else 'clear')
    stats()

    # reset

    loopcheck = False
    print('Press', bld + 'enter' + end, 'to generate another character!')
    input()
    loopcheck = True
    os.system('cls' if os.name == 'nt' else 'clear')