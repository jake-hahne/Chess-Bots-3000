from Bot.Logic.Base import AlgorithmBase
import random


class BestBot(AlgorithmBase):
    """BestBot chooses the most beneficial move from the set of all available moves then plays that move."""

    def getMove(self):
        """Method that serves the purpose of choosing the BestBot's next move"""
        board = self.getBoard()
        moves = board.generate_legal_moves()
        best_moves = []
        bot_color = self.color().lower()
        op_color = ''
        if bot_color == "white":
            op_color = "black"
        else:
            op_color = "white"

        for move in moves:
            board = self.getBoard()
            board.push_uci(move.uci())
            scores = self.getScores(board)

            if scores.get(bot_color) >= scores.get(op_color):
                best_moves.append(board.uci(move))

        c_index = random.randint(0, len(best_moves))
        move_choice = best_moves[c_index]
        return move_choice

    def getName(self):
        """Returns the name of the logic algorithm"""
        return self.__class__.__name__


# --------------Test Code for Move Choice----------------------- #
b = BestBot()
print(b.getMove())
print(b.getName())
