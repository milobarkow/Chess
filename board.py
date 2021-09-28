import keyboard
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Piece:

    def __init__(self, x, y):
        self.x_position = x
        self.x_position = y


class Board:

    def __init__(self):
        self.board_key = []
        self.board = []
        self.path = 'C:/Users/12158/Documents/chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.move_number = 1
        self.play()

    # Create two 2d-arrays
    # Returns an 8x8 array of Piece objects in starting positions
    # Also creates an 8x8 array where each string is the notation of that square
    def init(self):
        key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        out = []
        filler = []
        temp = []
        for i in range(7, 0, -1):
            filler.clear()
            out.append(filler)
            temp.clear()
            self.board_key.append(temp)
            for j in range(7):
                x = key[j]
                y = i + 1
                new = Piece(x, y)
                filler.append(new)
                temp.append(x + str(y))
        return out

    def start_game(self):
        self.driver.get('https://chess.com')

    def get_move(self):
        move_element = WebDriverWait(self.driver, sys.maxsize) \
            .until(EC.presence_of_element_located((By.XPATH, "//div[@data-ply=" + str(self.move_number) + "]")))
        print(" move #" + str(self.move_number) + ": " + move_element.text)
        return move_element.text

    def play(self):
        self.start_game()
        while not keyboard.is_pressed('q'):
            last_move = self.get_move()
            self.move_number += 1
        self.driver.quit()
        keyboard.wait('esc')

    def get_enemy_move(self, input):
        lets = ['K', 'Q', 'R', 'B', 'N']
        xpos = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
