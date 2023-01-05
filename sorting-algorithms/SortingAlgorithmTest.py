from SortingAlgorithm import insertion_sort, bubble_sort, selection_sort, merge_sort


class SortingAlgorithmTest:
    """driver test for the sorting algos"""
    def __init__(self):
        self.display_menu()
        
        list = [] # the container for the list
        
        try:
            # gathering user inputs
            sortalgo = int(input(">>> "))
            n = int(input("How many elements are there on your list? "))
            itemtype = int(input("Enter type of elements? [1] INTEGERS [2] LETTERS (Upper-case only) => "))
            itemtype = "INTEGERS" if itemtype == 1 else "LETTERS"
            print(itemtype)
            order = int(input("Enter the sorting mode: [1] ASCENDING [2] DESCENDING [3] APLHABETICALLY =>  "))
            print("Enter your {} {} (END EACH INTEGER BY AND ENTER KEY)".format(n, itemtype))

            for i in range(0, n):
                usr = input()
                assert usr != ""
                if itemtype == "INTEGERS":
                    list.append(int(usr))
                else:
                    list.append(usr.upper())

            list_sorted = self.sort_options(sortalgo, list, order)
            print("FINAL SORTED ELEMENTS => ", list_sorted)
        except Exception:
            print("Please use appropriate options. Try again.")
            
            
        
    def sort_options(self, algo, temp, ord):
        if algo == 1:
            temp = selection_sort(temp)
        elif algo == 2:
            temp = bubble_sort(temp)
        elif algo == 3:
            temp = insertion_sort(temp)
        elif algo == 4:
            temp = merge_sort(temp)
        else:
            return None
            
        if ord == 2: # rearrange order by descending
            temp = temp[::-1]
            
        return temp
            
    def display_menu(self):
        """for printing a stylized menu"""
        
        # for the scribbles wrtten in the menu display
        menu_titles = ["SORTING ALGORITHM APPLICATION", 
        "Programmed by: Viernes, Michael", "BSCOE 2-1", "<<< MAIN MENU >>>", 
        "(1) SELECTION SORTING", "(2) BUBBLE SORTING", "(3) INSERTION SORTING", "(4) MERGE SORTING", 
        "Select an option: "]
        
        for i in menu_titles:
            if i == menu_titles[0]:
                i = i.center(60, "*")
                print(i)
                continue
            i = i.center(56, " ")
            print("*", i, "*")
        
            

if __name__ == "__main__":
    while(True):
        SortingAlgorithmTest()
        user = input("Do you want to try again? [y/n] => If yes, the program redisplay the main menu. Otherwise, program exits.")
        if user == "n":
            break
        print()
    