import random

random.seed(0)


class Die:
    """A haunted die"""

    def roll(self):

        return random.randint(1, 6)


class Player:


    def __init__(self, name):
        self.name = name
        self.score = 0
        self.soul_intact = True

    def add_points(self, points):
        # Each point is a fragment of your soul
        self.score += points
        if points > 15:
            print(f"{self.name} feels a slight chill as {points} soul fragments are collected.")
        else:
            print(f"{self.name} adds {points} points. Total: {self.score}")


class HumanPlayer(Player):
    """You poor, lost soul"""

    def take_turn(self, die):
        turn_score = 0
        print(f"\n{self.name}'s turn begins...s.")

        while True:
            # Cast the die into the void
            roll = die.roll()
            print(f"{self.name} rolled a {roll}" + (" - THE DIE BETRAYS YOU!" if roll == 1 else ""))

            # The cruel '1' that ends all hopes and dreams
            if roll == 1:
                print(f"The shadows laugh as {self.name} loses all points this turn.")
                return 0

            # Another step deeper into temptation
            turn_score += roll
            print(f"Turn score: {turn_score} (Total would be: {self.score + turn_score})")

            # The eternal question: greed or safety?
            choice = input("Tempt fate again (r) or cling to your meager winnings (h)? ")
            if choice.lower() == 'h':
                self.add_points(turn_score)
                return turn_score


class DemonicOpponent(Player):
    """It's not cheating if you're supernatural"""

    def __init__(self, name, greed=15):
        super().__init__(name)
        self.greed = greed
        self.victims = 0

    def take_turn(self, die):
        turn_score = 0
        print(f"\n{self.name}'s eyes gleam with otherworldly power.")

        while True:
            # Even demons must abide by the rules of the die
            roll = die.roll()
            print(f"{self.name} rolled a {roll}")

            if roll == 1:
                print(f"{self.name} hisses in frustration as their turn yields nothing.")
                return 0

            turn_score += roll
            print(f"{self.name} has accumulated {turn_score} points this turn.")

            # Demons have simple strategies
            if turn_score >= self.greed:
                self.add_points(turn_score)
                if turn_score > 12:
                    self.victims += 1
                    print(f"{self.name} has claimed {self.victims} souls in this game.")
                return turn_score

            print(f"{self.name} hungers for more points...")


class AccursedGame:
    """This isn't just a game - it's a binding contract"""

    def __init__(self, mortal, demon):
        self.mortal = mortal
        self.demon = demon
        self.current_player = self.mortal  # Mortals always go first (disadvantage)
        self.die = Die()
        self.winning_score = 100

    def switch_player(self):
        # The cosmic pendulum swings
        self.current_player = self.demon if self.current_player == self.mortal else self.mortal

    def check_winner(self):
        # Has someone collected enough soul fragments?
        if self.mortal.score >= self.winning_score:
            return self.mortal
        elif self.demon.score >= self.winning_score:
            return self.demon
        return None

    def play_game(self):
        print("╔════════════════════════════════════╗")
        print("║  THE ACCURSED GAME OF SKULL DICE!  ║")
        print("╚════════════════════════════════════╝")
        print(f"First to {self.winning_score} soul fragments will claim the other's essence!")


        while True:
            self.current_player.take_turn(self.die)


            winner = self.check_winner()
            if winner:
                print(f"\n☠️  {winner.name} HAS WON WITH {winner.score} POINTS! ☠️")
                if winner == self.demon:
                    print(f"Poor {self.mortal.name}... another soul claimed by {self.demon.name}.")
                else:
                    print(f"Impressive, {self.mortal.name}! You've bested a creature of the void!")
                break


            self.switch_player()



if __name__ == "__main__":
    print("Welcome, mortal, to a game where dice are more than just plastic cubes.")

    # Who dares to play?
    mortal_name = input("By what name shall the cosmos know you? ")
    mortal = HumanPlayer(mortal_name)

    # Your demonic opponent emerges
    demon_names = ["BLese", "Asmodan", "Lilith", "Mephiston", "Abadon", "Grandpa"]
    demon_name = random.choice(demon_names)
    print(f"\nFrom the shadows emerges {demon_name}, your otherworldly opponent.")

    # How strategic is your opponent?
    try:
        difficulty = int(input("How cunning is your opponent? (1-5, higher = more devious): "))
        greed_level = 10 + (difficulty * 2)  # Higher difficulty = higher greed threshold
    except:
        print("Your indecision has been noted.")
        greed_level = random.randint(10, 20)

    demon = DemonicOpponent(demon_name, greed_level)

    # Let the cosmic game begin!
    game = AccursedGame(mortal, demon)
    game.play_game()

    print("\nThe game is over, but remember your choices...")
