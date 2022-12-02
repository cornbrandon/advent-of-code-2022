import argparse
import os

parser = argparse.ArgumentParser(description='Process elves file')
parser.add_argument('inputFile')

args = parser.parse_args()

def main():
    with open(os.path.join(os.path.dirname(__file__), args.inputFile)) as file:
        games = []
        for line in file:
            game = line.strip().split(' ')
            # part2 plays
            games.append(game)
        
        nonStratScores = list(map(scorePlay, games.copy()))
        
        strategic = list(map(findStrat, games))
        strategicScores = list(map(scorePlay, strategic))
        
        print('Part 1 scores:')
        print(f'opponent: {sum(i[0] for i in nonStratScores)}')
        print(f'me: {sum(j[1] for j in nonStratScores)}')
        
        print('Part 2 scores:')
        print(f'opponent: {sum(i[0] for i in strategicScores)}')
        print(f'me: {sum(j[1] for j in strategicScores)}')
                    
# return the values for the play
def scorePlay(play):
    play = list(map(playConvert, play))
    scoreList = [0,0]
    if play[0] == play[1]:
        scoreList[0] = scoreList[1] = 3 + shapeScore(play[0])
        return tuple(scoreList)
    elif play[0] == 'rock':
        match play[1]:
            case 'paper':
                # win
                scoreList[0] += shapeScore(play[0])
                scoreList[1] += shapeScore(play[1]) + 6
                return tuple(scoreList)
            case 'scissors':
                #lose
                scoreList[0] += shapeScore(play[0]) + 6
                scoreList[1] += shapeScore(play[1])
                return tuple(scoreList)
    elif play[0] == 'paper':
        match play[1]:
            case 'scissors':
                scoreList[0] += shapeScore(play[0])
                scoreList[1] += shapeScore(play[1]) + 6
                return tuple(scoreList)
            case 'rock':
                scoreList[0] += shapeScore(play[0]) + 6
                scoreList[1] += shapeScore(play[1])
                return tuple(scoreList)
    elif play[0] == 'scissors':
        match play[1]:
            case 'rock':
                scoreList[0] += shapeScore(play[0])
                scoreList[1] += shapeScore(play[1]) + 6
                return tuple(scoreList)
            case 'paper':
                scoreList[0] += shapeScore(play[0]) + 6
                scoreList[1] += shapeScore(play[1])
                return tuple(scoreList)

def shapeScore(shape):
    match shape:
        case 'rock':
            return 1
        case 'paper':
            return 2
        case 'scissors':
            return 3

def playConvert(shape):
    match shape:
        case 'A'|'X':
            return 'rock'
        case 'B'|'Y':
            return 'paper'
        case 'C'|'Z':
            return 'scissors'

def findStrat(game):
    match game[1]:
        case 'Y':
            game[1] = game[0]
        case 'Z':
            match game[0]:
                case 'A':
                    game[1] = 'B'
                case 'B':
                    game[1] = 'C'
                case 'C':
                    game[1] = 'A'
        case 'X':
            match game[0]:
                case 'A':
                    game[1] = 'C'
                case 'B':
                    game[1] = 'A'
                case 'C':
                    game[1] = 'B'
    return game
    
if __name__ == "__main__":
    main()