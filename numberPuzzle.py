import random

class Puzzle:
    def __init__(self, initial_state):
        self.state = initial_state

    def display(self):
        for row in self.state:
            print(row)

    def move(self, direction):
        row, col = self.find_blank()
        if direction == 'up' and row > 0:
            self.state[row][col], self.state[row - 1][col] = self.state[row - 1][col], self.state[row][col]
        elif direction == 'down' and row < 2:
            self.state[row][col], self.state[row + 1][col] = self.state[row + 1][col], self.state[row][col]
        elif direction == 'left' and col > 0:
            self.state[row][col], self.state[row][col - 1] = self.state[row][col - 1], self.state[row][col]
        elif direction == 'right' and col < 2:
            self.state[row][col], self.state[row][col + 1] = self.state[row][col + 1], self.state[row][col]

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def shuffle(self, num_moves):
        directions = ['up', 'down', 'left', 'right']
        for i in range(num_moves):
            direction = random.choice(directions)
            self.move(direction)

    def is_solved(self):
        target_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.state == target_state

    def play(self):
        self.display()
        while not self.is_solved():
            move = input("Enter move (up/down/left/right): ")
            self.move(move)
            self.display()
        print("Congratulations! You solved the puzzle.")


# Example usage
initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
game = Puzzle(initial_state)
game.shuffle(50)  # Shuffle the puzzle
game.play()  # Play the game
