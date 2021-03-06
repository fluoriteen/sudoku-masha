# Test cases

class Tests : 
    # Sudoku 1
    case_1 = {
        '1 1': 1, '2 1': 2, '3 1': 3, '4 1': 4,
        '1 4': 2, '2 4': 3, '3 4': 4, '4 4': 5,
        '1 7': 3, '2 7': 4, '3 7': 5, '4 7': 6,
        '6 3': 3, '7 3': 4, '8 3': 5, '9 3': 6,
        '6 9': 5, '7 9': 6, '8 9': 7, '9 9': 8,
        '6 6': 4, '7 6': 5, '8 6': 6, '9 6': 7,
    }

    # Sudoku 2
    case_2 = {
        '1 3': 5, '1 4': 8, '1 7': 9, '1 9': 6,
        '2 1': 2, '2 2': 7, '2 3': 6, '2 4': 3,
        '4 1': 1, '4 4': 4, '4 5': 2,
        '5 5': 1, '5 7': 3, '5 9': 2,
        '6 3': 4, '6 8': 9,
        '7 8': 8,
        '8 4': 5, '8 5': 9, '8 6': 8, '8 7': 7,
        '9 1': 3, '9 8': 1,
    }

    # Sudoku 3
    case_3 = {
        '1 1': 8, 
        '2 4': 2, '2 5': 6, '2 8': 5,
        '3 3': 9, '3 4': 8, '3 9': 4,
        '4 1': 7, '4 3': 3, '4 8': 2,
        '5 5': 4, '5 8': 8, '5 9': 1,
        '6 1': 5, '6 6': 7, '6 8': 3,
        '7 2': 5, '7 6': 9, '7 7': 2, '7 8': 4,
        '8 4': 7,
        '9 1': 9, '9 2': 1
    }

    # Sudoku 4
    case_4 = {
        '1 3': 5, '1 4': 3,
        '2 1': 8, '2 8': 2,
        '3 2': 7, '3 5': 1, '3 7': 5,
        '4 1': 4, '4 6': 5, '4 7': 3,
        '5 2': 1, '5 5': 7, '5 9': 6,
        '6 3': 3, '6 4': 2, '6 8': 8,
        '7 2': 6, '7 4': 5, '7 9': 9,
        '8 3': 4, '8 8': 3,
        '9 6': 9, '9 7': 7
    }

    # Sudoku 5
    case_5 = {
        '1 8': 7, '1 9': 9,
        '2 6': 4, '2 8': 5, '2 9': 8,
        '3 2': 5, '3 3': 7, '3 5': 9, '3 7': 6,
        '4 2': 8, '4 3': 9, '4 5': 6, '4 9': 7,
        '5 1': 2, '5 3': 6, '5 5': 4,
        '6 4': 3,
        '7 9': 6,
        '8 2': 6, '8 3': 8, '8 5': 5, '8 8': 9,
        '9 1': 1, '9 3': 2
    }

    # Sudoku 6
    case_6 = {
        '1 1': 5, '1 2': 3, '1 5': 7,
        '2 1': 6, '2 4': 1, '2 5': 9, '2 6': 5,
        '3 2': 9, '3 3': 8, '3 8': 6,
        '4 1': 8, '4 5': 6, '4 9': 3,
        '5 1': 4, '5 4': 8, '5 6': 3, '5 9': 1,
        '6 1': 7, '6 5': 2, '6 9': 6,
        '7 2': 6, '7 7': 2, '7 8': 8,
        '8 4': 4, '8 5': 1, '8 6': 9, '8 9': 5,
        '9 5': 8, '9 8': 7, '9 9': 9
    }


    # Sudoku 7
    case_7 = {
        '1 9': 8,
        '2 4': 2, '2 5': 9, '2 7': 6, '2 8': 5,
        '3 1': 1, '3 5': 7, '3 6': 3,
        '4 2': 3, '4 3': 1, '4 9': 4,
        '5 4': 3, '5 5': 8,
        '6 1': 8, '6 2': 2, '6 7': 1,
        '7 2': 9, '7 4': 5, '7 6': 7,
        '8 1': 2, '8 8': 7,
        '9 6': 4, '9 7': 9
    }

    # Sudoku 8
    case_8 = {
        '1 1': 6, '1 5': 7, '1 6': 3, '1 7': 2,
        '2 4': 5, '2 5': 1,
        '3 2': 5, '3 3': 2, '3 8': 9,
        '4 1': 1, '4 4': 6, '4 7': 4, '4 8': 3,
        '5 2': 9, '5 8': 8,
        '6 2': 7, '6 3': 6, '6 6': 8, '6 9': 9,
        '7 2': 4, '7 7': 1, '7 8': 2,
        '8 5': 9, '8 6': 1,
        '9 3': 1, '9 4': 2, '9 5': 8, '9 9': 3
    }

    # Sudoku 9 // wolfram lvl 60
    case_9 = {
        '1 2': 8,
        '2 8': 6, '2 9': 4,
        '3 9': 8,
        '4 2': 9, '4 7': 8, '4 8': 1, '4 9': 3,
        '5 2': 7, '5 4': 1, '5 6': 6, '5 8': 4, '5 9': 2,
        '6 3': 1, '6 5': 8, '6 6': 3,
        '7 1': 3, '7 9': 1,
        '8 7': 3,
        '9 5': 2, '9 7': 4
    }

    # Sudoku 10 // wolfram lvl 60
    case_10 = {
        '1 1': 7, '1 4': 4, '1 9': 9,
        '2 1': 6, '2 4': 3, '2 6': 1, '2 8': 7,
        '3 1': 1, '3 8': 2,
        '4 9': 2,
        '5 1': 3, '5 5': 8,
        '6 4': 6, '6 8': 5, '6 9': 7,
        '7 2': 8, '7 5': 9,
        '9 1': 2, '9 2': 1, '9 4': 8, '9 7': 7, '9 9': 5,
    }

    # Sudoku 11 // World Sudoku Championship 2006
    case_11 = {
        '1 1': 8, '1 4': 7, '1 5': 5, '1 9': 3,
        '2 2': 3, '2 5': 4, '2 6': 8, '2 8': 2,
        '3 1': 1, '3 9': 6,
        '4 1': 3, '4 2': 4, '4 5': 7, '4 9': 8,
        '5 1': 7, '5 2': 9, '5 4': 4, '5 5': 8, '5 8': 3, '5 9': 1,
        '6 1': 2, '6 3': 8, '6 8': 7, '6 9': 4,
        '7 1': 5, '7 4': 8, '7 5': 1, '7 6': 4, '7 9': 7,
        '8 2': 8, '8 4': 3, '8 5': 2, '8 6': 7, '8 8': 4,
        '9 1': 4, '9 4': 5, '9 5': 6, '9 6': 9, '9 9': 2,
    }

    # Sudoku 12 // taking sudoku seriously p.114 (Easy and Hard Twins)
    case_12 = {
        '1 2': 8, '1 7': 5,
        '2 3': 6, '2 6': 4, '2 9': 9,
        '3 1': 7, '3 3': 3, '3 7': 4, '3 8': 2,
        '4 2': 2, '4 5': 3,
        '5 4': 8, '5 5': 9, '5 6': 1,
        '6 5': 2, '6 8': 7,
        '7 2': 9, '7 3': 2, '7 7': 6, '7 9': 3,
        '8 1': 4, '8 4': 6, '8 7': 8,
        '9 3': 5, '9 8': 4
    }

    # Sudoku 16x16
    case_13 = {
        '1 2': 4, '1 5': 8, '1 7': 16, '1 9': 11, '1 11': 1, '1 14': 6, '1 16': 14,
        '2 1': 3, '2 4': 9, '2 6': 15, '2 8': 4, '2 9': 10, '2 10': 7, '2 12': 13, '2 15': 12,
        '3 2': 6, '3 5': 2, '3 6': 11, '3 9': 8, '3 13': 3,
        '4 1': 15, '4 8': 13, '4 11': 14, '4 14': 2, '4 16': 4,
        '5 4': 8, '5 6': 3, '5 9': 7, '5 13': 5,
        '6 7': 14, '6 12': 10, '6 14': 16, '6 16': 13,
        '7 3': 9, '7 4': 2, '7 5': 5, '7 10': 8, '7 13': 11,
        '8 1': 12, '8 3': 1, '8 8': 16, '8 11': 13, '8 15': 3,
        '9 4': 12, '9 5': 15, '9 10': 6, '9 13': 13, '9 15': 4, '9 16': 7,
        '10 1': 16, '10 2': 1, '10 3': 13, '10 5': 10, '10 8': 3, '10 11': 7, '10 14': 9,
        '11 1': 6, '11 7': 11, '11 9': 4, '11 12': 9, '11 15': 2, '11 16': 10,
        '12 2': 3, '12 6': 16, '12 10': 14, '12 11': 8, '12 14': 11,
        '13 1': 5, '13 2': 11, '13 3': 3, '13 4': 10, '13 8': 8, '13 11': 12, '13 12': 4, '13 16': 1,
        '14 2': 14, '14 5': 11, '14 6': 9, '14 10': 13, '14 11': 15, '14 13': 4, '14 15': 5,
        '15 1': 13, '15 3': 4, '15 5': 6, '15 12': 2, '15 14': 12, '15 16': 9,
        '16 2': 12, '16 4': 16, '16 6': 13, '16 10': 1, '16 13': 6, '16 15': 15
    }
