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
                (G)uesses    (S)et user    (P)lay    (H)ighscores    (Q)uit

"""

        self.wrong_selection = """
     /$$$$$$$                /$$                /$$         /$$
    | $$__  $$              | $$               |__/        | $$
    | $$  \ $$ /$$$$$$  /$$$$$$$        /$$$$$$ /$$ /$$$$$$| $$   /$$
    | $$$$$$$ |____  $$/$$__  $$       /$$__  $| $$/$$_____| $$  /$$/
    | $$__  $$ /$$$$$$| $$  | $$      | $$  \ $| $| $$     | $$$$$$/
    | $$  \ $$/$$__  $| $$  | $$      | $$  | $| $| $$     | $$_  $$
    | $$$$$$$|  $$$$$$|  $$$$$$$      | $$$$$$$| $|  $$$$$$| $$ \  $$
    |_______/ \_______/\_______/      | $$____/|__/\_______|__/  \__/
                                      | $$
                                      | $$
                                      |__/                                                                                                               




"""

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

        self.user_text = """
     /$$   /$$
    | $$  | $$
    | $$  | $$  /$$$$$$$  /$$$$$$   /$$$$$$
    | $$  | $$ /$$_____/ /$$__  $$ /$$__  $$
    | $$  | $$|  $$$$$$ | $$$$$$$$| $$  \__/
    | $$  | $$ \____  $$| $$_____/| $$
    |  $$$$$$/ /$$$$$$$/|  $$$$$$$| $$
     \______/ |_______/  \_______/|__/
        
        
        
        
        
        
        
"""

        self.guess_text = """
      /$$$$$$
     /$$__  $$
    | $$  \__//$$   /$$ /$$$$$$  /$$$$$$$/$$$$$$$ /$$$$$$  /$$$$$$$
    | $$ /$$$| $$  | $$/$$__  $$/$$_____/$$_____//$$__  $$/$$_____/
    | $$|_  $| $$  | $| $$$$$$$|  $$$$$|  $$$$$$| $$$$$$$|  $$$$$$
    | $$  \ $| $$  | $| $$_____/\____  $\____  $| $$_____/\____  $$
    |  $$$$$$|  $$$$$$|  $$$$$$$/$$$$$$$/$$$$$$$|  $$$$$$$/$$$$$$$/
     \______/ \______/ \_______|_______|_______/ \_______|_______/
        
        
        


        
        
"""

    def print_hiscores(self, bucket):
        ''' Prints out the scoreboard for 10 highest scores '''
        buffer_bucket = bucket.top
        print(self.hiscore_header)

        # Finds the length of the longest username in bucket
        name_len = 10
        for i in range(10):
            hiscore_list = buffer_bucket.data
            if len(hiscore_list[0].strip()) > name_len:
                name_len = len(hiscore_list[0].strip())
            if buffer_bucket.next != None:
                buffer_bucket = buffer_bucket.next
            else:
                break

        header = "    |Sæti         {:<{length:}}         Vinningar Ágiskanir  Dags       |".format(
            "Nafn", length=name_len)
        vertical_line = "    |" + "="*(len(header)-6) + "|"

        print(vertical_line)
        print(header)
        print(vertical_line)

        buffer_bucket = bucket.top
        for i in range(10):
            hiscore_list = buffer_bucket.data
            print("    | {:3}  -----  {:<{length:}}  -----  {}  -----  {:2}  -----  {} |".format(
                i+1, hiscore_list[0], hiscore_list[1], hiscore_list[2], hiscore_list[3], length=name_len))
            if buffer_bucket.next != None:
                buffer_bucket = buffer_bucket.next
            else:
                break
        print(vertical_line)
