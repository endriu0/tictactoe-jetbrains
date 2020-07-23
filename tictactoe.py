# write your code here
import re, sys

x_count = 0
o_count = 0
move = "X"
symbols = "         "

symbol_list = [[symbol for symbol in symbols[0:3]], [symbol for symbol in symbols[3:6]],
               [symbol for symbol in symbols[6:10]]]


def print_board():
    print("---------")
    print("| " + symbol_list[0][0] + " " + symbol_list[0][1] + " " + symbol_list[0][2] + " |")
    print("| " + symbol_list[1][0] + " " + symbol_list[1][1] + " " + symbol_list[1][2] + " |")
    print("| " + symbol_list[2][0] + " " + symbol_list[2][1] + " " + symbol_list[2][2] + " |")
    print("---------")
    return


print_board()


def result_print(results):
    while True:
        if 'X' in results:
            print("X wins")
            sys.exit()
        elif 'O' in results:
            print("O wins")
            sys.exit()
        else:
            print("Draw")
            sys.exit()
    return


def result_check(x_count, o_count, symbol_list):
    results = []

    if "XXX" == (symbol_list[0][0] + symbol_list[0][1] + symbol_list[0][2]):
        results.append("X")
    elif "XXX" == (symbol_list[1][0] + symbol_list[1][1] + symbol_list[1][2]):
        results.append("X")
    elif "XXX" == (symbol_list[2][0] + symbol_list[2][1] + symbol_list[2][2]):
        results.append("X")
    elif "XXX" == (symbol_list[0][0] + symbol_list[1][0] + symbol_list[2][0]):
        results.append("X")
    elif "XXX" == (symbol_list[0][1] + symbol_list[1][1] + symbol_list[2][1]):
        results.append("X")
    elif "XXX" == (symbol_list[0][2] + symbol_list[1][2] + symbol_list[2][2]):
        results.append("X")
    elif "XXX" == (symbol_list[0][0] + symbol_list[1][1] + symbol_list[2][2]):
        results.append("X")
    elif "XXX" == (symbol_list[0][2] + symbol_list[1][1] + symbol_list[2][0]):
        results.append("X")

    if "OOO" == (symbol_list[0][0] + symbol_list[0][1] + symbol_list[0][2]):
        results.append("O")
    elif "OOO" == (symbol_list[1][0] + symbol_list[1][1] + symbol_list[1][2]):
        results.append("O")
    elif "OOO" == (symbol_list[2][0] + symbol_list[2][1] + symbol_list[2][2]):
        results.append("O")
    elif "OOO" == (symbol_list[0][0] + symbol_list[1][0] + symbol_list[2][0]):
        results.append("O")
    elif "OOO" == (symbol_list[0][1] + symbol_list[1][1] + symbol_list[2][1]):
        results.append("O")
    elif "OOO" == (symbol_list[0][2] + symbol_list[1][2] + symbol_list[2][2]):
        results.append("O")
    elif "OOO" == (symbol_list[0][0] + symbol_list[1][1] + symbol_list[2][2]):
        results.append("O")
    elif "OOO" == (symbol_list[0][2] + symbol_list[1][1] + symbol_list[2][0]):
        results.append("O")

    if any(results):
        result_print(results)
        return results
    else:
        if x_count + o_count == 9:
            results.append("Draw")
            result_print(results)
            return results


def new_moves():
    while True:
        moves = input("Enter the coordinates: ")
        if not re.match(r'[0-9]\s[0-9]', moves):
            print("You should enter numbers!")
        elif not re.match(r'[1-3]\s[1-3]', moves):
            print("Coordinates should be from 1 to 3!")
        else:
            return moves.split()


while True:
    moves = "".join(new_moves())
    if moves == "13":
        if symbol_list[0][0] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            if move == "X":
                symbol_list[0][0] = move
                print_board()
                x_count += 1
                move = "O"
                result_check(x_count, o_count, symbol_list)
            else:
                symbol_list[0][0] = move
                print_board()
                o_count += 1
                move = "X"
                result_check(x_count, o_count, symbol_list)
    elif moves == "23":
        if symbol_list[0][1] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            if move == "X":
                symbol_list[0][1] = move
                print_board()
                x_count += 1
                move = "O"
                result_check(x_count, o_count, symbol_list)
            else:
                symbol_list[0][1] = move
                print_board()
                o_count += 1
                move = "X"
                result_check(x_count, o_count, symbol_list)
    elif moves == "33":
        if symbol_list[0][2] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            if move == "X":
                symbol_list[0][2] = move
                print_board()
                x_count += 1
                move = "O"
                result_check(x_count, o_count, symbol_list)
            else:
                symbol_list[0][2] = move
                print_board()
                o_count += 1
                move = "X"
                result_check(x_count, o_count, symbol_list)
    elif moves == "12":
        if symbol_list[1][0] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            if move == "X":
                symbol_list[1][0] = move
                print_board()
                x_count += 1
                move = "O"
                result_check(x_count, o_count, symbol_list)
            else:
                symbol_list[1][0] = move
                print_board()
                o_count += 1
                move = "X"
                result_check(x_count, o_count, symbol_list)
    elif moves == "22":
        if symbol_list[1][1] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            if move == "X":
                symbol_list[1][1] = move
                print_board()
                x_count += 1
                move = "O"
                result_check(x_count, o_count, symbol_list)
            else:
                symbol_list[1][1] = move
                print_board()
                o_count += 1
                move = "X"
                result_check(x_count, o_count, symbol_list)
    elif moves == "32":
        if symbol_list[1][2] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            if move == "X":
                symbol_list[1][2] = move
                print_board()
                x_count += 1
                move = "O"
                result_check(x_count, o_count, symbol_list)
            else:
                symbol_list[1][2] = move
                print_board()
                o_count += 1
                move = "X"
                result_check(x_count, o_count, symbol_list)
    elif moves == "11":
        if symbol_list[2][0] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            if move == "X":
                symbol_list[2][0] = move
                print_board()
                x_count += 1
                move = "O"
                result_check(x_count, o_count, symbol_list)
            else:
                symbol_list[2][0] = move
                print_board()
                o_count += 1
                move = "X"
                result_check(x_count, o_count, symbol_list)
    elif moves == "21":
        if symbol_list[2][1] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            if move == "X":
                symbol_list[2][1] = move
                print_board()
                x_count += 1
                move = "O"
                result_check(x_count, o_count, symbol_list)
            else:
                symbol_list[2][1] = move
                print_board()
                o_count += 1
                move = "X"
                result_check(x_count, o_count, symbol_list)
    elif moves == "31":
        if symbol_list[2][2] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            if move == "X":
                symbol_list[2][2] = move
                print_board()
                x_count += 1
                move = "O"
                result_check(x_count, o_count, symbol_list)
            else:
                symbol_list[2][2] = move
                print_board()
                o_count += 1
                move = "X"
                result_check(x_count, o_count, symbol_list)
