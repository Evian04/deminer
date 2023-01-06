from src.deminer import Deminer


game = Deminer((10, 10), 20)
game.display_grid()

while True:
    action = input("Do you wanna explore, report or unreport a place : ")

    match action:
        case "explore":
            game.explore(int(input("i : ")), int(input("j : ")))
        
        case "report":
            game.report_mine(int(input("i : ")), int(input("j : ")))
        
        case "unreport":
            game.cancel_report(int(input("i : ")), int(input("j : ")))
        
        case other:
            print(f"{action} doesn't march with any keyword")
        
    game.display_grid()