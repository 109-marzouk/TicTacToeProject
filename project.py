from random import choice
def validation_core(x, t = None, b = None):
    if x.isspace() or x == "":
        return "ERROR: Enter Valid Input please!"
    if t == "letter" and x not in ["X", "O"]:
        return "ERROR: Enter Valid Input please!, Choose X or O Only!"
    if t == "boardPos" and int(x) not in range(1,10):
        if int(x) not in range(1,10):
            return "ERROR: This placement does not exist!, Try Again."
        if b[x] != " ":
            return "ERROR: This placement is already selected! Select another placement."
    if t == "options" and x not in ["1", "2"]:
        return "ERROR: Choose 1 or 2 Only!"
    return "100%"

def validation(x, m, t = None, b = None):
    while "ERROR" in validation_core(x, t, b):
        print(validation_core(x, t, b))
        x = input(m).upper()
    
def print_board(s):
    print("""
+-----+-----+-----+
|  {}  |  {}  |  {}  |
+-----+-----+-----+
|  {}  |  {}  |  {}  |
+-----+-----+-----+
|  {}  |  {}  |  {}  |
+-----+-----+-----+
    """.format(s["7"], s["8"], s["9"],
				s["4"], s["5"], s["6"],
				s["1"], s["2"], s["3"]))

def computer_choice(s):
    if s['1'] + s['2'] == second_palyer_letter * 2 and s['3'] == " ": computer_input = '3'
    elif s['1'] + s['3'] == second_palyer_letter * 2 and s['2'] == " ": computer_input = '2'
    elif s['2'] + s['3'] == second_palyer_letter * 2 and s['1'] == " ": computer_input = '1'
    elif s['4'] + s['5'] == second_palyer_letter * 2 and s['6'] == " ": computer_input = '6'
    elif s['4'] + s['6'] == second_palyer_letter * 2 and s['5'] == " ": computer_input = '5'
    elif s['5'] + s['6'] == second_palyer_letter * 2 and s['4'] == " ": computer_input = '4'
    elif s['7'] + s['8'] == second_palyer_letter * 2 and s['9'] == " ": computer_input = '9'
    elif s['7'] + s['9'] == second_palyer_letter * 2 and s['8'] == " ": computer_input = '8'
    elif s['8'] + s['9'] == second_palyer_letter * 2 and s['7'] == " ": computer_input = '7'
    elif s['1'] + s['4'] == second_palyer_letter * 2 and s['7'] == " ": computer_input = '7'
    elif s['1'] + s['7'] == second_palyer_letter * 2 and s['4'] == " ": computer_input = '4'
    elif s['4'] + s['7'] == second_palyer_letter * 2 and s['1'] == " ": computer_input = '1'
    elif s['2'] + s['5'] == second_palyer_letter * 2 and s['8'] == " ": computer_input = '8'
    elif s['2'] + s['8'] == second_palyer_letter * 2 and s['5'] == " ": computer_input = '5'
    elif s['5'] + s['8'] == second_palyer_letter * 2 and s['2'] == " ": computer_input = '2'
    elif s['3'] + s['6'] == second_palyer_letter * 2 and s['9'] == " ": computer_input = '9'
    elif s['3'] + s['9'] == second_palyer_letter * 2 and s['6'] == " ": computer_input = '6'
    elif s['6'] + s['9'] == second_palyer_letter * 2 and s['3'] == " ": computer_input = '3'
    elif s['3'] + s['5'] == second_palyer_letter * 2 and s['7'] == " ": computer_input = '7'
    elif s['3'] + s['7'] == second_palyer_letter * 2 and s['5'] == " ": computer_input = '5'
    elif s['5'] + s['7'] == second_palyer_letter * 2 and s['3'] == " ": computer_input = '3'
    elif s['1'] + s['5'] == second_palyer_letter * 2 and s['9'] == " ": computer_input = '9'
    elif s['1'] + s['9'] == second_palyer_letter * 2 and s['5'] == " ": computer_input = '5'
    elif s['5'] + s['9'] == second_palyer_letter * 2 and s['1'] == " ": computer_input = '1'
    elif s['1'] + s['2'] == first_palyer_letter * 2 and s['3'] == " ": computer_input = '3'
    elif s['1'] + s['3'] == first_palyer_letter * 2 and s['2'] == " ": computer_input = '2'
    elif s['2'] + s['3'] == first_palyer_letter * 2 and s['1'] == " ": computer_input = '1'
    elif s['4'] + s['5'] == first_palyer_letter * 2 and s['6'] == " ": computer_input = '6'
    elif s['4'] + s['6'] == first_palyer_letter * 2 and s['5'] == " ": computer_input = '5'
    elif s['5'] + s['6'] == first_palyer_letter * 2 and s['4'] == " ": computer_input = '4'
    elif s['7'] + s['8'] == first_palyer_letter * 2 and s['9'] == " ": computer_input = '9'
    elif s['7'] + s['9'] == first_palyer_letter * 2 and s['8'] == " ": computer_input = '8'
    elif s['8'] + s['9'] == first_palyer_letter * 2 and s['7'] == " ": computer_input = '7'
    elif s['1'] + s['4'] == first_palyer_letter * 2 and s['7'] == " ": computer_input = '7'
    elif s['1'] + s['7'] == first_palyer_letter * 2 and s['4'] == " ": computer_input = '4'
    elif s['4'] + s['7'] == first_palyer_letter * 2 and s['1'] == " ": computer_input = '1'
    elif s['2'] + s['5'] == first_palyer_letter * 2 and s['8'] == " ": computer_input = '8'
    elif s['2'] + s['8'] == first_palyer_letter * 2 and s['5'] == " ": computer_input = '5'
    elif s['5'] + s['8'] == first_palyer_letter * 2 and s['2'] == " ": computer_input = '2'
    elif s['3'] + s['6'] == first_palyer_letter * 2 and s['9'] == " ": computer_input = '9'
    elif s['3'] + s['9'] == first_palyer_letter * 2 and s['6'] == " ": computer_input = '6'
    elif s['6'] + s['9'] == first_palyer_letter * 2 and s['3'] == " ": computer_input = '3'
    elif s['3'] + s['5'] == first_palyer_letter * 2 and s['7'] == " ": computer_input = '7'
    elif s['3'] + s['7'] == first_palyer_letter * 2 and s['5'] == " ": computer_input = '5'
    elif s['5'] + s['7'] == first_palyer_letter * 2 and s['3'] == " ": computer_input = '3'
    elif s['1'] + s['5'] == first_palyer_letter * 2 and s['9'] == " ": computer_input = '9'
    elif s['1'] + s['9'] == first_palyer_letter * 2 and s['5'] == " ": computer_input = '5'
    elif s['5'] + s['9'] == first_palyer_letter * 2 and s['1'] == " ": computer_input = '1'
    else: computer_input = choice([x for x in board.keys() if board[x] == " "])
    return computer_input

def CheckWinner(s, player_letter):
    return (s['1'] + s['2'] + s['3'] == player_letter * 3) or (s['4'] + s['5'] + s['6'] == player_letter * 3) or \
            (s['7'] + s['8'] + s['9'] == player_letter * 3) or (s['7'] + s['4'] + s['1'] == player_letter * 3) or \
            (s['8'] + s['5'] + s['2'] == player_letter * 3) or (s['9'] + s['6'] + s['3'] == player_letter * 3) or \
            (s['7'] + s['5'] + s['3'] == player_letter * 3) or (s['9'] + s['5'] + s['1'] == player_letter * 3)


def result():
    print("""
============================================
---+ {}({}): {}
---+ {}({}): {}
============================================
""".format(first_palyer_name, first_palyer_letter, first_palyer_score,
           second_palyer_name, second_palyer_letter, second_palyer_score))

print("""
==============================================
=== Welcome to Our Game
==============================================
""")

print("""
Enter:
    [1] 1 Player
    [2] 2 Player
""")

user_choice = input("Your Choice: ")
validation(user_choice, "Your Choice: ", t = "options")
if user_choice == "1":
    print("""
Enter:
    [1] Easy
    [2] Hard
""")
    difficulty_level = input("Your Choice: ")
    validation(difficulty_level, "Your Choice: ", t = "options")

first_palyer_name = input("Enter First Player Name: ")
validation(first_palyer_name, "Enter First Player Name: ")

first_palyer_letter = input("Enter Your Letter Choose X or O: ").upper()
validation(first_palyer_letter, "Enter Your Letter Choose X or O: ", t = "letter")

first_palyer_score = 0

second_palyer_name = input("Enter Second Player Name: ") if user_choice == "2" else "Computer"
validation(second_palyer_name, "Enter Second Player Name: ")

second_palyer_letter = "X" if first_palyer_letter == "O" else "O"

second_palyer_score = 0

print("""\nOK! Each position on the board has a specific number and this board
represents the number part of the keyboard on the right""")
print("""
+-----+-----+-----+
|  7  |  8  |  9  |
+-----+-----+-----+
|  4  |  5  |  6  |
+-----+-----+-----+
|  1  |  2  |  3  |
+-----+-----+-----+
""")

while True:
    board = {"1":" ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}		
    while " " in board.values():
        print_board(board)
        first_player_input = input(first_palyer_name + ": ")
        validation(first_player_input, first_palyer_name + ": ", t = "boardPos", b = board)
        board[first_player_input] = first_palyer_letter
        print_board(board)
        if CheckWinner(board, first_palyer_letter): first_palyer_score += 1; result(); break
        else:
            if " " not in board.values(): print("draw!"); result(); break
        if user_choice == "1":
            if difficulty_level == "1":
                second_player_input = choice([x for x in board.keys() if board[x] == " "])
            else:
                second_player_input = computer_choice(board)
                board[second_player_input] = second_palyer_letter; print_board(board)
            print("Computer: " + second_player_input)
        else:
            second_player_input = input(second_palyer_name + ": ")
            validation(second_player_input, second_palyer_name + ": ", t = "boardPos", b = board)
            board[second_player_input] = second_palyer_letter; print_board(board)

        if CheckWinner(board, second_palyer_letter): second_palyer_score += 1; result(); break
        else:
            if " " not in board.values(): print("draw!"); result(); break
    if input("Do you want to continue? y/n: ").upper() != "Y": print("Thank! I hope to see you again"); break 

