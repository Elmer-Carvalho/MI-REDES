from screens.homeScreen import homeScreen
from screens.loginScreen import loginScreen
from screens.menuScreen import menuScreen
from screens.registerScreen import registerScreen
from screens.searchTicketsScreen import searchTicketsScreen
from screens.ticketsPurchaseScreen import ticketsPurchaseScreen
from screens.ticketsQueryScreen import ticketsQueryScreen

def filterScreens(state: dict) -> dict:
    if state["screen"] == "home":
        return homeScreen()
    
    if state["screen"] == "login":
        return loginScreen()

    if state["screen"] == "register":
        return registerScreen()

    if state["screen"] == "menu":
        return menuScreen(state["user_data"])

    if state["screen"] == "search":
        return searchTicketsScreen()

    if state["screen"] == "consult":
        return ticketsQueryScreen(state["server_data"])

    if state["screen"] == "displayTicketsForPurchase":
        return ticketsPurchaseScreen(state["server_data"], state["user_data"])

    
