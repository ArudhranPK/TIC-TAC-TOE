#importing required modules
from random import choice, randint
from tkinter import *

#making a window to display the widgets and to set the icon for the app
root = Tk()
root.title("NOUGHTS AND CROSSES")
icon_image = PhotoImage(file = r"xo.png")
root.tk.call('wm', 'iconphoto', root._w, icon_image)

#setting photos for the X and O for the marks
X_photo = PhotoImage(file = r"x.png")
O_photo = PhotoImage(file = r"o.png")

#creating variables for the alternation chance for the player and changing the first chance of the player
chance = 0
chance_before = 1

#representing the values of the rows and column for the algorithm of the game
row_column_values = {"row_1" : ["column_1", "column_2", "column_3"], "row_2" : ["column_1", "column_2", "column_3"], "row_3" : ["column_1", "column_2", "column_3"]}

#variable to display the number of times a player has won
player_1_won_count = 0
player_2_won_count = 0

#variable to chack whether the game has ended up in draw
draw = 0

def start():
    #asking the user to enter the players name and storing them
    global label_player_1
    label_player_1 = Label(root, text = "PLAYER 1 NAME:")
    label_player_1.grid(row = 0, column = 0, pady = 4, sticky = EW)

    global player_1_name_entry
    player_1_name_entry = Entry(root, borderwidth = 2)
    player_1_name_entry.grid(row = 0, column = 2, pady = 4, sticky = EW)
    
    global label_player_2
    label_player_2 = Label(root, text = "PLAYER 2 NAME:")
    label_player_2.grid(row = 1, column = 0, pady = 4, sticky = EW)

    global player_2_name_entry
    player_2_name_entry = Entry(root, borderwidth = 2)
    player_2_name_entry.grid(row = 1, column = 2, pady = 4, sticky = EW)

    global next_button
    next_button = Button(root, text = "NEXT", background = "black", foreground = "white", borderwidth = 2, command = lambda : start_next())
    next_button.grid(row = 2, column = 2, padx = 2, pady = 2, sticky = E)

    global exit_button
    exit_button = Button(root, text = "EXIT", background = "red", foreground = "black", borderwidth = 2, command = lambda : exit_window())
    exit_button.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = W)

    global chance
    #randomise the chance of the of getting the first chance
    chance = randint(0, 1)

def exit_window():
    #asking for the permission to exit the game
    global exit_widget
    exit_widget = Tk()
    exit_widget.title("EXIT")

    global exit_label
    exit_label = Label(exit_widget, text = "DO YOU WANT TO EXIT?")
    exit_label.grid(row = 0, column = 0, padx = 2, pady = 2, columnspan = 2)

    global yes_button
    yes_button = Button(exit_widget, text = "YES", borderwidth = 2, command = lambda : destroy_app(1))
    yes_button.grid(row = 1, column = 0, padx = 2, pady = 2)

    global no_button
    no_button = Button(exit_widget, text = "NO", background = "black", foreground = "white", borderwidth = 2, command = lambda : destroy_app(0))
    no_button.grid(row = 1, column = 1, padx = 2, pady = 2)

def destroy_app(a):

    #killing the app completely
    if a == 1:
        root.destroy()
        exit_widget.destroy()
        quit()
    else:
        exit_widget.destroy()

def start_next():

    #getting the username from the entry
    global player_1_name
    player_1_name = player_1_name_entry.get()
    player_1_name = player_1_name.title()
    
    global player_2_name
    player_2_name = player_2_name_entry.get()
    player_2_name = player_2_name.title()

    global next_button
    global exit_button

    if player_1_name != "" and player_2_name != "":
        
        #destroying the buttons for the next widgets
        label_player_1.destroy()
        label_player_2.destroy()
        player_1_name_entry.destroy()
        player_2_name_entry.destroy()
        next_button.destroy()
        exit_button.destroy()

        global player_1_symbol
        global player_2_symbol

        #randomise the chance to get X and O
        player_1_symbol = choice(["X", "O"])

        global label_to_tell_symbol_1
        global label_to_tell_symbol_2

        #Displaying which player is which symbol and who to start first
        if player_1_symbol == "X":
             player_2_symbol = "O"
             label_to_tell_symbol_1 = Label(root, text = f"{player_1_name} is 'X'")
             label_to_tell_symbol_2 = Label(root, text = f"{player_2_name} is 'O'")
        else:
             player_2_symbol = "X"
             label_to_tell_symbol_1 = Label(root, text = f"{player_1_name} is 'O'")
             label_to_tell_symbol_2 = Label(root, text = f"{player_2_name} is 'X'")

        label_to_tell_symbol_1.grid(row = 0, column = 0)
        label_to_tell_symbol_2.grid(row = 0, column = 3)

        global label_to_tell_fisrt_chance
        global chance_before
        global chance

        if chance == 0:
            chance_before = 1
            if player_1_symbol == "X":
                 label_to_tell_fisrt_chance = Label(root, text = f"{player_1_name} to start first.")
            else:
                 label_to_tell_fisrt_chance = Label(root, text = f"{player_2_name} to start first.")
        else:
            chance_before = 0
            if player_1_symbol == "O":
                 label_to_tell_fisrt_chance = Label(root, text = f"{player_1_name} to start first.")
            else:
                 label_to_tell_fisrt_chance = Label(root, text = f"{player_2_name} to start first.")

        label_to_tell_fisrt_chance.grid(row = 1, column = 2)

        next_button = Button(root, text = "NEXT", background = "black", foreground = "white", borderwidth = 2, command = lambda:before_game())
        next_button.grid(row = 2, column = 3, padx = 2, pady = 2, sticky = E)

        exit_button = Button(root, text = "EXIT", background = "red", foreground = "black", borderwidth = 2, command = lambda : exit_window())
        exit_button.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = W)

def before_game():
    #destroying the buttons for the next widgets
    label_to_tell_symbol_1.destroy()
    label_to_tell_symbol_2.destroy()
    label_to_tell_fisrt_chance.destroy()
    next_button.destroy()
    exit_button.destroy()

    global label_whos_chance
    global chance

    #display whose chance is first
    if chance % 2 == 0:
        label_whos_chance = Label(root, text = "X CHANCE")
    else:
        label_whos_chance = Label(root, text = "O CHANCE")
    
    label_whos_chance.grid(row = 0, column = 2)

    game()

def game():
    #display which player won how many times in total
    global label_to_tell_how_many_won_1
    global player_1_won_count
    label_to_tell_how_many_won_1 = Label(root, text = f"{player_1_name} won {player_1_won_count} times.")
    label_to_tell_how_many_won_1.grid(row = 0, column = 0, columnspan = 2, sticky = W)
    
    global label_to_tell_how_many_won_2
    global player_2_won_count
    label_to_tell_how_many_won_2 = Label(root, text = f"{player_2_name} won {player_2_won_count} times.")
    label_to_tell_how_many_won_2.grid(row = 0, column = 3, columnspan = 2, sticky =E)

    #displaying buttons for all the 9 buttons (3 X 3). When a button is pressed it also send the value for rows and columns.
    global button_1_1
    button_1_1 = Button(root, height = 6, width = 10, borderwidth = 2, command = lambda: game_algorithm(1, 1, row_column_values))
    button_1_1.grid(row = 1, column = 1, padx = 1, pady = 1)

    global button_1_2
    button_1_2 = Button(root, height = 6, width = 10, borderwidth = 2, command = lambda: game_algorithm(1, 2, row_column_values))
    button_1_2.grid(row = 1, column = 2, padx = 1, pady = 1)

    global button_1_3
    button_1_3 = Button(root, height = 6, width = 10, borderwidth = 2, command = lambda: game_algorithm(1, 3, row_column_values))
    button_1_3.grid(row = 1, column = 3, padx = 1, pady = 1)

    global button_2_1
    button_2_1 = Button(root, height = 6, width = 10, borderwidth = 2, command = lambda: game_algorithm(2, 1, row_column_values))
    button_2_1.grid(row = 2, column = 1, padx = 1, pady = 1)

    global button_2_2
    button_2_2 = Button(root, height = 6, width = 10, borderwidth = 2, command = lambda: game_algorithm(2, 2, row_column_values))
    button_2_2.grid(row = 2, column = 2, padx = 1, pady = 1)

    global button_2_3
    button_2_3 = Button(root, height = 6, width = 10, borderwidth = 2, command = lambda: game_algorithm(2, 3, row_column_values))
    button_2_3.grid(row = 2, column = 3, padx = 1, pady = 1)

    global button_3_1
    button_3_1 = Button(root, height = 6, width = 10, borderwidth = 2, command = lambda: game_algorithm(3, 1, row_column_values))
    button_3_1.grid(row = 3, column = 1, padx = 1, pady = 1)

    global button_3_2
    button_3_2 = Button(root, height = 6, width = 10, borderwidth = 2, command = lambda: game_algorithm(3, 2, row_column_values))
    button_3_2.grid(row = 3, column = 2, padx = 1, pady = 1)

    global button_3_3
    button_3_3 = Button(root, height = 6, width = 10, borderwidth = 2, command = lambda: game_algorithm(3, 3, row_column_values))
    button_3_3.grid(row = 3, column = 3, padx = 1, pady = 1)

    global restart_button
    restart_button = Button(root, text = "RESTART", width = 7, background = "black", foreground = "white", borderwidth = 2, command = lambda: reset(), state = DISABLED)
    restart_button.grid(row = 4, column = 4, padx = 2, pady = 2, sticky = E)

    global exit_button
    exit_button = Button(root, text = "EXIT", width = 7, background = "red", foreground = "black", borderwidth = 2, command = lambda : exit_window())
    exit_button.grid(row = 4, column = 0, padx = 2, pady = 2, sticky = W)
    
    #list of all the 9 buttons for disabling them
    global button_game_list
    button_game_list = [button_1_1, button_1_2, button_1_3, button_2_1, button_2_2, button_2_3, button_3_1, button_3_2, button_3_3]

def game_algorithm(a, b, row_column_values):

    global chance
    global button_game_list
    global draw
    
    #from the positional data given by the button and by chance displaying the symbot of the player who clicked it.
    if a == 1 and b == 1:
        button_game_list.remove(button_1_1)
        button_1_1.destroy()
        if chance % 2 == 0:
            button_1_1_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = X_photo)
            row_column_values["row_1"][0] = "X"
        else:
            button_1_1_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = O_photo)
            row_column_values["row_1"][0] = "O"
        
        button_1_1_img.grid(row = 1, column = 1)

    elif a == 1 and b == 2:
        button_game_list.remove(button_1_2)
        button_1_2.destroy()
        if chance % 2 == 0:
            button_1_2_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = X_photo)
            row_column_values["row_1"][1] = "X"
        else:
            button_1_2_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = O_photo)
            row_column_values["row_1"][1] = "O"
        
        button_1_2_img.grid(row = 1, column = 2)

    elif a == 1 and b == 3:
        button_game_list.remove(button_1_3)
        button_1_3.destroy()
        if chance % 2 == 0:
            button_1_3_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = X_photo)
            row_column_values["row_1"][2] = "X"
        else:
            button_1_3_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = O_photo)
            row_column_values["row_1"][2] = "O"
        
        button_1_3_img.grid(row = 1, column = 3)
        
    elif a == 2 and b == 1:
        button_game_list.remove(button_2_1)
        button_2_1.destroy()
        if chance % 2 == 0:
            button_1_1_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = X_photo)
            row_column_values["row_2"][0] = "X"
        else:
            button_1_1_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = O_photo)
            row_column_values["row_2"][0] = "O"        
        
        button_1_1_img.grid(row = 2, column = 1)
    
    elif a == 2 and b == 2:
        button_game_list.remove(button_2_2)
        button_2_2.destroy()
        if chance % 2 == 0:
            button_1_2_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = X_photo)
            row_column_values["row_2"][1] = "X"
        else:
            button_1_2_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = O_photo)
            row_column_values["row_2"][1] = "O"        
        
        button_1_2_img.grid(row = 2, column = 2)
    
    elif a == 2 and b == 3:
        button_game_list.remove(button_2_3)
        button_2_3.destroy()
        if chance % 2 == 0:
            button_2_3_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = X_photo)
            row_column_values["row_2"][2] = "X"
        else:
            button_2_3_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = O_photo)
            row_column_values["row_2"][2] = "O"        
            
        button_2_3_img.grid(row = 2, column = 3)
    
    elif a == 3 and b == 1:
        button_game_list.remove(button_3_1)
        button_3_1.destroy()
        if chance % 2 == 0:
            button_3_1_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = X_photo)
            row_column_values["row_3"][0] = "X"
        else:
            button_3_1_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = O_photo)
            row_column_values["row_3"][0] = "O"
        
        button_3_1_img.grid(row = 3, column = 1)
        
    elif a == 3 and b == 2:
        button_game_list.remove(button_3_2)
        button_3_2.destroy()
        if chance % 2 == 0:
            button_3_2_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = X_photo)
            row_column_values["row_3"][1] = "X"
        else:
            button_3_2_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = O_photo)
            row_column_values["row_3"][1] = "O"
            
        button_3_2_img.grid(row = 3, column = 2)
        
    elif a == 3 and b == 3:
        button_game_list.remove(button_3_3)
        button_3_3.destroy()
        if chance % 2 == 0:
            button_3_3_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = X_photo)
            row_column_values["row_3"][2] = "X"
        else:
            button_3_3_img = Button(root, height = 112 , width = 112, borderwidth = 2, image = O_photo)
            row_column_values["row_3"][2] = "O"
            
        button_3_3_img.grid(row = 3, column = 3)

    global label_to_tell_won_match
    global player_2_won_count
    global player_1_won_count

    #finding whether any player has won the game bye forming straight lines
    if (row_column_values["row_1"][0] == row_column_values["row_1"][1] == row_column_values["row_1"][2] == "X" or
        row_column_values["row_2"][0] == row_column_values["row_2"][1] == row_column_values["row_2"][2] == "X" or
        row_column_values["row_3"][0] == row_column_values["row_3"][1] == row_column_values["row_3"][2] == "X" or
        row_column_values["row_1"][0] == row_column_values["row_2"][0] == row_column_values["row_3"][0] == "X" or
        row_column_values["row_1"][1] == row_column_values["row_2"][1] == row_column_values["row_3"][1] == "X" or
        row_column_values["row_1"][2] == row_column_values["row_2"][2] == row_column_values["row_3"][2] == "X" or
        row_column_values["row_1"][0] == row_column_values["row_2"][1] == row_column_values["row_3"][2] == "X" or
        row_column_values["row_1"][2] == row_column_values["row_2"][1] == row_column_values["row_3"][0] == "X"):
        
        if player_1_symbol == "X":
            label_to_tell_won_match = Label(root, text = f"{player_1_name} won!")
            player_1_won_count += 1
        else:    
            label_to_tell_won_match = Label(root, text = f"{player_2_name} won!")
            player_2_won_count += 1

        label_to_tell_won_match.grid(row = 4, column = 1, columnspan = 3, sticky = EW)

        for button in button_game_list:
            button["state"] = DISABLED

        restart_button["state"] = NORMAL

        draw -= 1

    if (row_column_values["row_1"][0] == row_column_values["row_1"][1] == row_column_values["row_1"][2] == "O" or
        row_column_values["row_2"][0] == row_column_values["row_2"][1] == row_column_values["row_2"][2] == "O" or
        row_column_values["row_3"][0] == row_column_values["row_3"][1] == row_column_values["row_3"][2] == "O" or
        row_column_values["row_1"][0] == row_column_values["row_2"][0] == row_column_values["row_3"][0] == "O" or
        row_column_values["row_1"][1] == row_column_values["row_2"][1] == row_column_values["row_3"][1] == "O" or
        row_column_values["row_1"][2] == row_column_values["row_2"][2] == row_column_values["row_3"][2] == "O" or
        row_column_values["row_1"][0] == row_column_values["row_2"][1] == row_column_values["row_3"][2] == "O" or
        row_column_values["row_1"][2] == row_column_values["row_2"][1] == row_column_values["row_3"][0] == "O"):
        
        if player_1_symbol == "O":
            label_to_tell_won_match = Label(root, text = f"{player_1_name} won!")
            player_1_won_count += 1
        else:    
            label_to_tell_won_match = Label(root, text = f"{player_2_name} won!")
            player_2_won_count += 1
            
        label_to_tell_won_match.grid(row = 4, column = 1, columnspan = 3, sticky = EW)
        
        for button in button_game_list:
            button["state"] = DISABLED
        
        restart_button["state"] = NORMAL

        draw -= 1

    global label_whos_chance
    label_whos_chance.destroy()

    chance += 1
    draw += 1

    if chance % 2 == 0:
        label_whos_chance = Label(root, text = "X CHANCE")
        label_whos_chance.grid(row = 0, column = 2)
    else:
        label_whos_chance = Label(root, text = "O CHANCE")
        label_whos_chance.grid(row = 0, column = 2)

    if draw == 9:
        label_to_tell_won_match = Label(root, text = "Match draw!!")
        label_to_tell_won_match.grid(row = 4, column = 1, columnspan = 3)
        
        restart_button["state"] = NORMAL

def reset():

    #resetting all the variables except the player won count
    global button_game_list
    button_game_list = [button_1_1, button_1_2, button_1_3, button_2_1, button_2_2, button_2_3, button_3_1, button_3_2, button_3_3]

    global label_to_tell_won_match
    label_to_tell_won_match.destroy()
    global row_column_values
    row_column_values = {"row_1" : ["column_1", "column_2", "column_3"], "row_2" : ["column_1", "column_2", "column_3"], "row_3" : ["column_1", "column_2", "column_3"]}

    global chance
    global chance_before

    if chance_before == 1:
        chance = 1
        chance_before = 0
    else:
        chance = 0
        chance_before = 1

    global draw
    draw = 0

    before_game()
   
start()
   
root.mainloop()