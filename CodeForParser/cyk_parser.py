from tabulate import tabulate
# Where the magic happens
class grammar(object):
    # Reads in a grammar txt file and stores the productions in a dictionary
    # Assumes there is enough productions in grammar to work with
    def __init__(self, grammar_file):
        self.grammar_productions = {}
        for production in open(grammar_file):
            # X → YZ
            # left → right respectively
            left, right = production.split('->')
            # Should be able to handle some weird spacing 
            # in the input txt file but don't go too crazy
            self.grammar_productions[left.strip()] = [item.strip() for item in right.split('|')]
    
    # Used to print the production rules of the grammar if grammar is valid cnf
    # Great for testing purposes
    def print_rules(self):
        for left in self.grammar_productions:
            right_side = ''
            for right_side_elements in self.grammar_productions[left]:
                right_side += (right_side_elements.strip() + '|')
            print((str(left) + ' -> ' + str(right_side))[:-1])
        print('\n')

    # Checks to see if the input grammar is valid Chomsky Normal Form 
    # Remember, all productions must follow this format:
    # X → YZ
    # X → x

    # S → λ, but we will ignore this one for now because it is very hard to work with
    # TODO: May implement the third rule later but that will be very tricky
    # TODO: May extend method to accept non alphabeticals
    def is_valid_cnf(self):
        print('Checking input grammar productions... \n')
        # Check if left side of production rule fits the criteria
        for left in self.grammar_productions:
            # It can be only one upper case alphabetical non terminal symbol
            if ((len(str(left)) == 1 or len(str(left)) == 2) and str(left).isalpha() and str(left).isupper()):
                # Start to check right side of production rule  
                for right_side_element in self.grammar_productions[left]:
                    # Can be one lower case alphabetical terminal symbol or
                    if (len(str(right_side_element)) == 1 and str(right_side_element).isalpha() and str(right_side_element).islower()):
                        pass
                    # It can be two upper case alphabetical non terminal symbols
                    elif (len(str(right_side_element)) == 2 and str(right_side_element).isalpha() and str(right_side_element).isupper()):
                        pass
                    else:
                    # If invalid input throw error and exit program
                        raise ValueError('Error: grammar file has been read in unsuccesfully, please check your grammar to see if it contains any mistakes. Exiting program... \n')
            else: 
                # If invalid input throw error and exit program
                raise ValueError('Error: grammar file has been read in unsuccesfully, please check your grammar to see if it contains any mistakes. Exiting program... \n')
        print('grammar file has been read in succesfully, the productions are as follow:')
        self.print_rules()

    # Used to create the cartesian product of elements in table cells
    def cartesian_product(self, x, y):
        result = set()
        if x == set() or y == set():
            return set()
        for entry_in_x in x:
            for entry_in_y in y:
                result.add(entry_in_x + entry_in_y)
        return result


    # Performs the CYK Algorithm and parses through each character of the string
    # If you want to check the puesdocode check it out here:
    # https://en.wikipedia.org/wiki/CYK_algorithm
    def parse(self, word):
        print('Preparing to parse word... \n')
        # First Check if the grammar is Valid, and reprints rules for to view in console
        self.is_valid_cnf()
        print('Now parsing word... \n')
        # Need length of input string to determine table dimensions
        n = len(word)
        # Initialize the parse table
        # table size = (n^2 + n)/2
        parse_table = [[set() for _ in range(n-i)] for i in range(n)]
        # Initialize Dictionary containing references to terminals, and non terminals
        terminal_reference_dict = {}
        non_terminal_reference_dict = {}
        for key, value in self.grammar_productions.items():
            for element in value:
                if len(str(element)) == 1:
                    terminal_reference_dict.setdefault(element, []).append(key)
                if len(str(element)) == 2:
                    non_terminal_reference_dict.setdefault(element, []).append(key)
        # Fill out first row of table using the terminal_reference_dict 
        for i in range(n):
            for key, value in terminal_reference_dict.items():
                if word[i] == key:
                    for element in value:
                        parse_table[0][i].add(element)
        # Fill out rest of the table rows use the non_terminal_reference_dict and cartesian product
        for i in range(1, n):
            for j in range(n - i):
                for k in range(i):
                    cp = self.cartesian_product(parse_table[k][j], parse_table[i-k-1][j+k+1])
                    for e in cp:
                        for key, value in non_terminal_reference_dict.items():
                            if e == key:
                                for element in value:
                                    parse_table[i][j].add(element)
        # Print parse table for view, tabulate is awesome
        print('Parse Table generated below:')
        print(tabulate(parse_table, headers = word, tablefmt="fancy_grid"))
        print('\n')
        parse_successful = False
        # Check if the string belongs to the language generated by the input grammar
        if 'S' in parse_table[len(word)-1][0]:
            print("The string DOES belong to the language generated by the input grammar! \n")
            parse_successful = True
        else:
            print("The string DOES NOT belong to the language generated by the input grammar! \n")
        return parse_successful