print("LET THE GAME BEGIN... IF YOU DARE.")

print("""
        🕯️ THE HORROR QUIZ 🕯️

        Enter the world of darkness...
        Only the worthy shall survive.

        Choice 1. The Linguistic Horror Quiz
""")

guessspell1 = "STAGE 1: GUESS THE WORD\nA word beginning with E, meaning eerie, strange, mysterious, and unsettling."

guessspell2 = """STAGE 2: POETRY OF THE DAMNED

Identify the poet who wrote this famous poem:

"Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore..."

"""

guessspell3 = """STAGE 3: GUESS THE NOVEL

Written by Bram Stoker and published in 1897,
this Gothic horror novel tells the story of a mysterious
Transylvanian count who survives by drinking blood.
Name the novel.
"""

guessspell4 = """STAGE 4: THE FINAL NIGHTMARE

Identify the playwright who wrote Macbeth,
a tragedy filled with ambition, murder, supernatural prophecies,
and three mysterious witches.

Who is the playwright?
"""

choice = input("ENTER YOUR CHOICE: ")

if choice == "1":
    print("\nYOU HAVE ENTERED THE REALM OF HORROR...")
    print("There is no turning back now. 🩸")

    print("\n" + guessspell1)
    ansspell1 = input("ENTER YOUR ANSWER: ")

    if ansspell1.strip().lower() == "eldritch":
        print("\nCORRECT! Eldritch describes something eerie and otherworldly.")
        print("You have survived Stage 1... for now. 🔥")

        print("\n" + guessspell2)
        ansspell2 = input("ENTER YOUR ANSWER: ")

        if ansspell2.strip().lower() in ["edgar allan poe", "edgar poe"]:
            print("\nIMPRESSIVE! You have survived the poetry of the damned.")
            print("Stage 2 complete. The shadows grow darker...")

            print("\n" + guessspell3)
            ansspell3 = input("ENTER YOUR ANSWER: ")

            if ansspell3.strip().lower() == "dracula":
                print("\nEXCELLENT! You have escaped the vampire's castle.")
                print("Stage 3 complete. One final challenge remains...")

                print("\n" + guessspell4)
                ansspell4 = input("ENTER YOUR ANSWER: ")

                if ansspell4.strip().lower() == "william shakespeare":
                    print("""

                    🩸 CONGRATULATIONS, SURVIVOR! 🩸

                    You have conquered all four stages
                    of the Horror Quiz.

                    You faced the unknown, survived the
                    damned poetry, escaped the vampire,
                    and conquered the final nightmare.

                    YOU HAVE WON. 🔥
                    """)
                else:
                    print("""

                    THE SHADOWS HAVE CLAIMED YOU.
                    The correct answer was William Shakespeare.
                    Your journey ends here...
                    """)
            else:
                print("""

                THE COUNT HAS FOUND YOU.
                The correct answer was Dracula.
                You have failed Stage 3.
                """)
        else:
            print("""

            THE RAVEN CACKLES IN THE DARK.
            The correct answer was Edgar Allan Poe.
            You have failed Stage 2.
            """)
    else:
        print("""

        THE UNKNOWN HAS CONSUMED YOU.
        The correct answer was Eldritch.
        Your journey ends at Stage 1.
        """)

else:
    print("THE DARKNESS REJECTS YOUR CHOICE. GAME OVER.")