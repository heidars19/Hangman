class TUI():
    def __init__(self):
        self.user = ""
        self.main_menu = """
 /$$   /$$                                                                
| $$  | $$                                                                
| $$  | $$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$ 
| $$$$$$$$ |____  $$| $$__  $$ /$$__  $$| $$_  $$_  $$ |____  $$| $$__  $$
| $$__  $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$ \ $$ \ $$  /$$$$$$$| $$  \ $$
| $$  | $$ /$$__  $$| $$  | $$| $$  | $$| $$ | $$ | $$ /$$__  $$| $$  | $$
| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$  | $$
|__/  |__/ \_______/|__/  |__/ \____  $$|__/ |__/ |__/ \_______/|__/  |__/
                               /$$  \ $$                                  
                              |  $$$$$$/                                  
                               \______/                                      
"""
        self.menu_selection = """
                        Type in the character to select operation
             Max (G)uesses    (S)et user    (P)lay    (H)ighscores    (Q)uit        

        """
        self.wrong_selection = """
                                                                                 /$$                       /$$     /$$                    
                                                                                | $$                      | $$    |__/                    
 /$$  /$$  /$$  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$         /$$$$$$$  /$$$$$$ | $$  /$$$$$$   /$$$$$$$ /$$$$$$   /$$  /$$$$$$  /$$$$$$$ 
| $$ | $$ | $$ /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$       /$$_____/ /$$__  $$| $$ /$$__  $$ /$$_____/|_  $$_/  | $$ /$$__  $$| $$__  $$
| $$ | $$ | $$| $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$      |  $$$$$$ | $$$$$$$$| $$| $$$$$$$$| $$        | $$    | $$| $$  \ $$| $$  \ $$
| $$ | $$ | $$| $$      | $$  | $$| $$  | $$| $$  | $$       \____  $$| $$_____/| $$| $$_____/| $$        | $$ /$$| $$| $$  | $$| $$  | $$
|  $$$$$/$$$$/| $$      |  $$$$$$/| $$  | $$|  $$$$$$$       /$$$$$$$/|  $$$$$$$| $$|  $$$$$$$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$
 \_____/\___/ |__/       \______/ |__/  |__/ \____  $$      |_______/  \_______/|__/ \_______/ \_______/   \___/  |__/ \______/ |__/  |__/
                                             /$$  \ $$                                                                                    
                                            |  $$$$$$/                                                                                    
                                             \______/                                                                                     """


        self.hiscore_header = """
 /$$   /$$ /$$                                                          
| $$  | $$|__/                                                          
| $$  | $$ /$$          /$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$ 
| $$$$$$$$| $$ /$$$$$$ /$$_____/ /$$_____/ /$$__  $$ /$$__  $$ /$$__  $$
| $$__  $$| $$|______/|  $$$$$$ | $$      | $$  \ $$| $$  \__/| $$$$$$$$
| $$  | $$| $$         \____  $$| $$      | $$  | $$| $$      | $$_____/
| $$  | $$| $$         /$$$$$$$/|  $$$$$$$|  $$$$$$/| $$      |  $$$$$$$
|__/  |__/|__/        |_______/  \_______/ \______/ |__/       \_______/
                                                                                                                                    """


    def print_menu(self):
        print(self.main_menu+self.menu_selection)

    def print_wrong(self):
        print(self.wrong_selection)
        
    def print_hiscores(self, bucket) :
        print(self.hiscore_header)
        
        header= "Sæti Nafn     Vinningar  Ágiskanir    Dags"
        print(header)

        for i in range(10) :
            hiscore_list = bucket.data
            print(" {} ---- {} ---- {} ---- {} ---- {}".format(i+1, hiscore_list[0], hiscore_list[1], hiscore_list[2], hiscore_list[3]))
            if bucket.next :    
                bucket = bucket.next
            else :
                break


        
        
        