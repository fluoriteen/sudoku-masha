# Test cases

class Test : 
    # Sudoku 1
    case_1 = {
        '11': 1, '21': 2, '31': 3, '41': 4,
        '14': 2, '24': 3, '34': 4, '44': 5,
        '17': 3, '27': 4, '37': 5, '47': 6,
        '63': 3, '73': 4, '83': 5, '93': 6,
        '69': 5, '79': 6, '89': 7, '99': 8,
        '66': 4, '76': 5, '86': 6, '96': 7,
    }

    # Sudoku 2
    case_2 = {
        '13': 5, '14': 8, '17': 9, '19': 6,
        '21': 2, '22': 7, '23': 6, '24': 3,
        '41': 1, '44': 4, '45': 2,
        '55': 1, '57': 3, '59': 2,
        '63': 4, '68': 9,
        '78': 8,
        '84': 5, '85': 9, '86': 8, '87': 7,
        '91': 3, '98': 1,
    }

    # Sudoku 3
    case_3 = {
        '11': 8, 
        '24': 2, '25': 6, '28': 5,
        '33': 9, '34': 8, '39': 4,
        '41': 7, '43': 3, '48': 2,
        '55': 4, '58': 8, '59': 1,
        '61': 5, '66': 7, '68': 3,
        '72': 5, '76': 9, '77': 2, '78': 4,
        '84': 7,
        '91': 9, '92': 1
    }

    # Sudoku 4
    case_4 = {
        '13': 5, '14': 3,
        '21': 8, '28': 2,
        '32': 7, '35': 1, '37': 5,
        '41': 4, '46': 5, '47': 3,
        '52': 1, '55': 7, '59': 6,
        '63': 3, '64': 2, '68': 8,
        '72': 6, '74': 5, '79': 9,
        '83': 4, '88': 3,
        '96': 9, '97': 7
    }

    # Sudoku 5
    case_5 = {
        '18': 7, '19': 9,
        '26': 4, '28': 5, '29': 8,
        '32': 5, '33': 7, '35': 9, '37': 6,
        '42': 8, '43': 9, '45': 6, '49': 7,
        '51': 2, '53': 6, '55': 4,
        '64': 3,
        '79': 6,
        '82': 6, '83': 8, '85': 5, '88': 9,
        '91': 1, '93': 2
    }

    # Sudoku 6
    case_6 = {
        '11': 5, '12': 3, '15': 7,
        '21': 6, '24': 1, '25': 9, '26': 5,
        '32': 9, '33': 8, '38': 6,
        '41': 8, '45': 6, '49': 3,
        '51': 4, '54': 8, '56': 3, '59': 1,
        '61': 7, '65': 2, '69': 6,
        '72': 6, '77': 2, '78': 8,
        '84': 4, '85': 1, '86': 9, '89': 5,
        '95': 8, '98': 7, '99': 9
    }


    # Sudoku 7
    case_7 = {
        '19': 8,
        '24': 2, '25': 9, '27': 6, '28': 5,
        '31': 1, '35': 7, '36': 3,
        '42': 3, '43': 1, '49': 4,
        '54': 3, '55': 8,
        '61': 8, '62': 2, '67': 1,
        '72': 9, '74': 5, '76': 7,
        '81': 2, '88': 7,
        '96': 4, '97': 9
    }
