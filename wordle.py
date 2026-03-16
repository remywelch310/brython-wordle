from browser_graphics import *
import random
import urllib.request

WORD_URL = "https://codehs.com/uploads/f488da9718f333275a7f34bf277fa45c"

response = urllib.request.urlopen(WORD_URL)
data = response.read()

words = data.strip().split()


#Modern UI Colors
COLOR_BG = "#121213"
COLOR_EMPTY = "#3a3a3c"
COLOR_GREEN = "#6aaa64"
COLOR_YELLOW = "#c9b558"
COLOR_ABSENT = "#3a3a3c"
COLOR_TEXT = "#ffffff"
COLOR_SUBTITLE = "#818384"

#Global State
word_to_guess = random.choice(words)
current_guess = ""
guess_count = 0
game_over = False
grid_squares = [] 
grid_labels = []

#UI Setup
bg = Rectangle(400, 500)
bg.set_color(COLOR_BG)
add(bg)

title = Text("WORDLE")
title.set_font("bold 26pt Arial")
title.set_color(COLOR_TEXT)
title.set_position(125, 45)
add(title)

line = Line(0, 55, 400, 55)
line.set_color(COLOR_EMPTY)
add(line)

message_label = Text("TYPE YOUR GUESS")
message_label.set_font("10pt Arial")
message_label.set_color(COLOR_SUBTITLE)
message_label.set_position(110, 420)
add(message_label)

def draw_board():
    start_x = 85  
    start_y = 80
    size = 42     
    margin = 6
    
    for row in range(6):
        row_sq = []
        row_lbl = []
        for col in range(5):
            x = start_x + (col * (size + margin))
            y = start_y + (row * (size + margin))
            
            sq = Rectangle(size, size)
            sq.set_position(x, y)
            sq.set_color(COLOR_BG) 
            
            try:
                sq.set_border_color(COLOR_EMPTY)
                sq.set_border_width(2)
            except:
                sq.set_color(COLOR_EMPTY)
            
            add(sq)
            
            lbl = Text("")
            lbl.set_font("bold 22pt Arial")
            lbl.set_position(x + 10, y + 33)
            lbl.set_color(COLOR_TEXT)
            add(lbl)
            
            row_sq.append(sq)
            row_lbl.append(lbl)
        grid_squares.append(row_sq)
        grid_labels.append(row_lbl)

def check_guess():
    global current_guess, guess_count, game_over
    
    guess = current_guess.lower()
    target = list(word_to_guess)
    result_colors = ["#787c7e"] * 5 
    
    # Pass 1: Greens
    for i in range(5):
        if guess[i] == word_to_guess[i]:
            result_colors[i] = COLOR_GREEN
            target[i] = None
            
    # Pass 2: Yellows
    for i in range(5):
        if result_colors[i] == COLOR_GREEN: continue
        if guess[i] in target and guess[i] is not None:
            result_colors[i] = COLOR_YELLOW
            target.remove(guess[i])
            
    for i in range(5):
        grid_squares[guess_count][i].set_color(result_colors[i])
        try:
            grid_squares[guess_count][i].set_border_width(0)
        except:
            pass
        
    guess_count += 1
    
    if guess == word_to_guess:
        game_over = True
        message_label.set_text("GENIUS!")
        message_label.set_color(COLOR_GREEN)
    elif guess_count >= 6:
        game_over = True
        message_label.set_text("THE WORD WAS: " + word_to_guess.upper())
        message_label.set_color(COLOR_SUBTITLE)
    
    current_guess = ""

def on_key_down(event):
    global current_guess
    if game_over: return
    
    key = event.key
    
    if key == "Enter":
        if len(current_guess) == 5:
            if current_guess in words:
                check_guess()
            else:
                message_label.set_text("NOT IN WORD LIST")
        else:
            message_label.set_text("TOO SHORT")
            
    elif key == "Backspace" or key == "BackSpace":
        if len(current_guess) > 0:
            current_guess = current_guess[:-1]
            grid_labels[guess_count][len(current_guess)].set_text("")
            
    elif len(key) == 1 and key.isalpha():
        if len(current_guess) < 5:
            grid_labels[guess_count][len(current_guess)].set_text(key.upper())
            current_guess += key.lower()
            message_label.set_text("") # Clear errors while typing

draw_board()
add_key_down_handler(on_key_down)
