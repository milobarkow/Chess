import keyboard
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Piece:

    def __init__(self, x, y, n):
        self.x_position = x
        self.x_position = y
        self.notation = n


class Board:

    def __init__(self):
        self.board = []
        self.path = 'C:/Users/12158/Documents/chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.move_number = 1
        self.init()
        self.play()

    # Create two 2d-arrays
    # Returns an 8x8 array of Piece objects in starting positions
    def init(self):
        key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        out = []
        filler = []
        for i in range(7, 0, -1):
            filler.clear()
            out.append(filler)
            for j in range(7):
                n = key[j]
                x = j
                y = i + 1
                new = Piece(x, y, n)
                filler.append(new)
        return out

    def start_game(self):
        self.driver.get('https://chess.com')

    def get_move(self):
        move_element = WebDriverWait(self.driver, sys.maxsize) \
            .until(EC.presence_of_element_located((By.XPATH, "//div[@data-ply=" + str(self.move_number) + "]")))
        last = self.get_last_sqaure()
        print(" move #" + str(self.move_number) + ": " + last + ' to ' +move_element.text)
        return move_element.text

    def play(self):
        self.start_game()
        while not keyboard.is_pressed('q'):
            last_move = self.get_move()
            self.move_number += 1
        self.driver.quit()
        keyboard.wait('esc')

    def get_last_sqaure(self):
        lets = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        divs = self.driver.find_elements_by_css_selector("#board-vs-personalities div")
        options =''
        for element in divs:
            if element.get_attribute('class')[:4] == 'high':
                options = options + element.get_attribute('class') + ' '
        options = options.split()
        note = options[1][-2:]
        note = lets[int(note[0]) - 1] + note[1]
        return note

