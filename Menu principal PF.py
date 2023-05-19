#!/usr/bin/python3
import random
genetic_list = []

def createSequence(genetic_list):

    """
    Adds a DNA or RNA sequence to a list.

    Args:
    genetic_list (list): The list of genetic sequences to add to.

    Returns:
    genetic_list (list): The updated list of genetic sequences.
    """

    #Ask the user if they want to create a sequence automatically
    while True:
        auto = input("Create sequence automatically? [Y/N]: ")
        if auto == "Y" or auto == "y":
            while True:

                try:
                    length = int(input("Enter the length of the sequence [minimum 20]: "))

                except ValueError:
                    print("Please enter a valid value")
                    continue

                if length < 20:
                    print("The length must be greater or equal to 20. Please try again.")
                
                else:
                    sequence_type = input("Create DNA or RNA sequence? ")

                    if sequence_type == "DNA" or sequence_type == "dna":
                        dnaString = ""
                        for bases in range(length):
                            genBases = random.randint(1, 4)
                            if genBases == 1: 
                                dnaString += "A" 
                            elif genBases == 2: 
                                dnaString += "C" 
                            elif genBases == 3: 
                                dnaString += "G" 
                            else: 
                                dnaString += "T" 
                        genetic_list.append(dnaString)
                        print("Sequence added successfully:", dnaString)
                        return genetic_list
                    
                    elif sequence_type == "RNA" or sequence_type == "rna":
                        rnaString = ""
                        for bases in range(length):
                            genBases = random.randint(1, 4)
                            if genBases == 1: 
                                rnaString += "A" 
                            elif genBases == 2: 
                                rnaString += "C" 
                            elif genBases == 3: 
                                rnaString += "G" 
                            else: 
                                rnaString += "U" 
                        genetic_list.append(rnaString)
                        print("Sequence added successfully:", rnaString)
                        return genetic_list
                    
                    else:
                        print("Invalid input. Please try again.")

        elif auto == "N" or auto == "n":
            user_sequence = input("Please enter the DNA or RNA sequence: ")
            print("Sequence added successfully:", user_sequence)
            genetic_list.append(user_sequence)
            return genetic_list
        
        else:
            print("Invalid input. Please try again.")

def deleteSequence(genetic_list):
    if len(genetic_list) == 0:
        print("ERROR: Empty list")
        return genetic_list
    
    else:
        genetic_list.pop()
        print ("Last Sequence Deleted Successfully")
        return genetic_list

def searchSequence(genetic_list, pattern):

    """Browse genetic_list and if it matches with
    the pattern, show the position as index.
    Args=
    genetic_list[list[]]: list created previously
    pattern[str]: DNA or RNA pattern inserted by user
    """
    
    found = 0
    index_list = []
    for element in range(len(genetic_list)):
        if genetic_list[element] == pattern:
            index_list.append(element)
            found += 1
            print("Sequence found in position:", element)   
    if found == 0:
        print("Not results found")

def compareSequence(genetic_list, pattern, percent):
    
    found = 0
    for element in range(len(genetic_list)):
        seq = genetic_list[element]
        if len(seq) != len(pattern):
            similar = 0
        else:
            found += 1
            matches = 0
            for base in range(len(seq)):
                if seq[base] == pattern[base]:
                    matches += 1
            similar = matches / len(seq)
        if similar >= percent:
            print("Similar sequence found in: ", element)
    if found == 0:
        print("Not results found")

def invertOrComplement(genetic_list):

    if len(genetic_list) == 0:
        print("Empty list")
        return genetic_list
            
    last_sequence = genetic_list[-1]
    if "U" in last_sequence:
        #Secuence is RNA
        inverse_RNA = last_sequence[::-1]
        genetic_list.append(inverse_RNA)
        print("Reverse Chain Creation Complete: ", inverse_RNA)
        return inverse_RNA
    
    else:
        #Secuence is DNA
        complement_DNA = ""
        for base in last_sequence:
            if base == "A":
                complement_DNA += "T"
            elif base == "T":
                complement_DNA += "A"
            elif base == "C":
                complement_DNA += "G"
            else:
                complement_DNA += "C"
        genetic_list.append(complement_DNA)
        print("Complementary Chain Creation Complete: ", complement_DNA)
        return genetic_list


def mainMenu():
    showMenu="""---- Mitochondria ----
----- Nombre-app -----
----- Main Menu -----
1. ¿What is COVID-19?
2. ¿What symptoms does COVID-19 cause?
3. ¿What is SARS-CoV-2?
4. SARS-CoV-2 Genetic Sequence.
5. Genetic Sequence Analysis.
6. Exit Program."""
    option=0
    #Runs if not option 6
    while option != 6:
        print(showMenu)
        #User enters an option
        try:
            option=int(input("Enter an option: "))

        except ValueError:
            print("Invalid Input. Please try again")
            continue

        #Options are defined
        if option == 1:
            print("""COVID-19 is a highly contagious infectious disease caused by the
SARS-CoV-2 virus. Anyone at any age can get the
disease but they are the elderly and people with 
underlying diseases the most likely to become seriously ill or die""")
            #User enters any value in order to
            #return to the main menu
            rand_num1=(input("Enter any value to return to Main Menu: "))          
        elif option == 2:
            print("""COVID-19 causes symptoms such as fever, cough and tiredness. Others
symptoms includes: Difficulty breathing, Sore throat, headache, 
nausea, vomiting, diarrhea and chills""")
            rand_num2=(input("Enter any value to return to Main Menu: "))                     
        elif option == 3:
            print("""SARS-CoV-2 is a virus of the Coronavirus family that infects human beings.
humans and some animals. It is transmitted from one 
person to another when the infected person coughs, 
sneezes, or even talks.""")
            rand_num3=(input("Enter any value to return to Main Menu: "))            
        elif option == 4:
            print(""" SARS-CoV-2 genetic sequence fragment is: attaaaggtt tataccttcc caggtaacaa accaaccaac tttcgatctc ttgtagatct
gttctctaaa cgaactttaa aatctgtgtg gctgtcactc ggctgcatgc ttagtgcact
cacgcagtat aattaataac taattactgt cgttgacagg acacgagtaa ctcgtctatc
ttctgcaggc tgcttacggt ttcgtccgtg ttgcagccga tcatcagcac atctaggttt
cgtccgggtg tgaccgaaag gtaagatgga gagccttgtc cctggtttca acgagaaaac """)
            rand_num4=(input("Enter any value to return to Main Menu: "))            
        elif option == 5:
            def geneticSequenceMenu():
                """Receive a list of genetic sequences to operate according to the
                option chosen by the user.
                Args:
                list[list[str]]: Genetic sequences list
                Return:
                According to chosen option
                """
                seqMenu="""---- Mitochondria ----
----- Nombre-app -----
----- Genetic Sequence Menu -----
1. Create Genetic Sequence
2. Eliminate Genetic Sequence
3. Search Genetic Sequence
4. Compare Genetic Sequence.
5. Build Complementary Genetic Sequence.
6. Show Saved Genetic Sequences
7. Return to Main Menu
"""
                option2=0
                while option2 != 7:
                    print(seqMenu) 
                    try:
                        option2=int(input("Enter an option: "))
                    
                    except ValueError:
                        print("Invalid Input. Please try again")
                        continue
                    
                    if option2 == 1:
                        createSequence(genetic_list)

                    elif option2 == 2:
                        deleteSequence(genetic_list)

                    elif option2 == 3:
                        pattern = input("Please enter a DNA or RNA sequence: ")
                        searchSequence(genetic_list, pattern)

                    elif option2 == 4:
                        pattern = input("Please enter a DNA or RNA sequence: ")
                        percent = float(input("Please enter a percentage of similarity (0.0 and 1.0): "))
                        compareSequence(genetic_list, pattern, percent)

                    elif option2 == 5:
                        invertOrComplement(genetic_list)

                    elif option2 == 6:
                        if len(genetic_list) == 0:
                            print("Empty List")

                        else:
                            for element in range(len(genetic_list)):
                                print(genetic_list[element])
                    
                    elif option2 == 7:
                        return genetic_list
                    else:
                        print("""ERROR: Invalid Selection""")
                        continue                        
                    
            geneticSequenceMenu()                
            
        elif option == 6:
            print("""End of the program""")
            break
        else:
            print("""ERROR: Invalid Selection""")
mainMenu()
