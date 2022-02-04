#******************************************************************************
# Author:           Proxima-L3
# Date:             July 19, 2020
# Description:      The main purpose of this program is to provide the user
#                   with a simulation of Drake's Equation. The program also
#                   displays two other menu options, allowing the user to
#                   either read a small description of the historical origin of
#                   the equation or to read more about what the variables in
#                   Drake's Equation represent.
# Input:            Equation values
# Output:           Drake's Equation result
# Sources:          https://stackoverflow.com/questions/51870312/python-clear-
#                   output-in-atom-mac
#                   https://www.seti.org/drake-equation-index
#******************************************************************************


# This constant represents a value that will need to be multiplied by a percent
# value entered in by the user in order to change it to a decimal (or float).
P_TO_D_CONSTANT = .01


# This function ties all other functions together to make one coherent program
def main():
    menu_choice = 0
    intro()
    while True:
        menu_choice = menu()

        if menu_choice == 1:
            print("\033[H\033[J")
            history()
        elif menu_choice == 2:
            print("\033[H\033[J")
            the_equation()
        elif menu_choice == 3:
            print("\033[H\033[J")
            equation_simulator()

        b_button = ''

        while True:
            b_button = input("press b to return to the main menu\n\t")

            if b_button == 'b':
                print("\033[H\033[J")
                break
            else:
                print("\n\n..hmm. That didn't work. Lemme give you a hint: "
                      + "press b ...\n\n")


# This function displays a short origin history of the Drake Equation.
def history():

    print("\n[History]\n\n")

    print("Soon after the search for extraterrestrial intelligence (SETI) \n"
          + "began in the late 1950's, a radio astronomer named Frank Drake \n"
          + "developed an equation that could give rough predictions of the \n"
          + "number of intelligent alien civilizations in the galaxy. The \n"
          + "equation I am talking about is of course the Drake Equation.\n")

    print("Though the variables within the Drake Equation are extremely \n"
          + "uncertain and are expected to drastically change as more and \n"
          + "more scientific discoveries are made, a lower limit of at \n"
          + "least 36 alien civilizations being in the galaxy has been \n"
          + "calculated.\n\n")

    print("(see [The Equation] option in the main menu to learn more \n"
          + "about the variables in Drake's equation)\n\n")


# This function displays the Drake Equation and defines what each variable in
# the equation means.
def the_equation():

    print("\n[The Equation]\n\n")

    print("N = Rs * fp * Ne * fl * fi * fc * L\n\n\n")

    print("N = the number of civilizations, in our galaxy, technologically \n"
          + "advanced enough to communicate through interstellar space\n")

    print("Rs = the average rate of star formation in our galaxy per year\n")

    print("fp = the fraction of those stars that host a planetary system\n")

    print("Ne = the number of planets per solar system that have the \n"
          "ability to develop an ecosystem\n")

    print("fl = the fraction of those planets that actually succeed in \n"
          + "developing life\n")

    print("fi = the fraction of those life bearing planets that also \n"
          + "develop intelligent life\n")

    print("fc = the fraction of those planets with intelligent life that \n"
          + "develop a technologically advanced civilization (and \n"
          + "interstellar communication as a consequence)\n")

    print("L = the average length of time that those technologically \n"
          + "advanced civilizations survive and continue to send \n"
          + "interstellar communications\n\n\n")


# This function is the Drake Equation simulator. It allows the user to enter
# in different values for each variable within the Drake Equation and returns
# the result of that equation to the user.
def equation_simulator():
    print("\n[Equation Simulator]\n\n")

    N = 0
    Rs = 0
    fp = 0
    Ne = 0
    fl = 0
    fi = 0
    fc = 0
    L = 0


    Rs = float(input("Please enter the average rate of star formations \n"
                      + "per year:  Rs = "))

    fp = float(input("Please enter the percent of those stars that host any \n"
                      + "planets:  fp = "))

    Ne = float(input("Please enter the average number of planets per solar \n"
                      + "system that have the ability to develop an \n"
                      + "ecosystem:  Ne = "))

    fl = float(input("Please enter the percent of those planets that \n"
                      + "actually succeed in developing life:  fl = "))

    fi = float(input("Please enter the percent of those life bearing \n"
                      + "planets that also develop intelligent life:  fi = "))

    fc = float(input("Please enter the percent of those planets with \n"
                      + "intelligent life that develop a technologically \n"
                      + "advanced civilization (and interstellar \n"
                      + "communication as a consequence):  fc = "))

    L = float(input("Please enter the average length of time that those \n"
                    + "technologically advanced civilizations survive \n"
                    + "and continue to send interstellar communications:  L = "))


    print("\n\nCalculating user pessimism severity...\n\n")

    print(f"Your equation: N = ({Rs} per year) * ({fp}%) * ({Ne} per solar system) * \n"
          + f"({fl}%) * ({fi}%) * ({fc}%) * ({L} years)")

    fp *= P_TO_D_CONSTANT
    fl *= P_TO_D_CONSTANT
    fi *= P_TO_D_CONSTANT
    fc *= P_TO_D_CONSTANT

    N = Rs * fp * Ne * fl * fi * fc * L

    print(f"\nThe number of technologically advanced civilizations in the \n"
          + f"galaxy: N = {N}\n\n")

    if N < 1:
        print("\t\tWhat is the Air Speed Velocity of an Unladen Swallow? \n"
              + "...hm I don't think I can answer that one because \n"
              + "according to this schmuck, swallows don't exist ...and \n"
              + "neither do we!\n\n")
    elif N < 1.5:
        print("\t\tWhat are you, a creationist?!\n\n")
    elif N >= 1000000:
        print("\t\tOk... time to storm area 51\n\n")
    else:
        pass


# This function displays the main menu which contains three options for the user.
def menu():

    menu_choice = 0

    while True:

        menu_choice = input("\n\npress 1 for [History]\npress 2 for "
                            + "[The Equation]\npress 3 for [Equation "
                            + "Simulator]\n\n")

        if menu_choice in ['1','2','3']:
            return int(menu_choice)
        else:
            print("\nThere's only three options for now. \n"
                  + "NOW CHOOSE PROPERLY!! ")


# Program introduction code
def intro():
    print("The Drake Equation")

    while True:
        c_button = input("\n\t(press c to continue)\n\t")

        if c_button == 'c':
            print("\033[H\033[J")
            break
        else:
            print("\n\n..hmm. That didn't work. Lemme give you a hint: press \n"
                  + "c to continue ...\n")

main()
