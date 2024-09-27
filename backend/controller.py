from validations.validate_cancellation import validateCancellation
from validations.validate_login import validateLogin
from validations.validate_purchase import validatePurchase
from validations.validate_registration import validateRegistration
from validations.validate_shoppingCart import validateShoppingCart
from validations.validate_ticketDisplay import validateTicketDisplay
from validations.validate_ticketQuery import validateTicketQuery

"""Filtra as requisições enviadas pelo cliente"""
def filterRequests(request: dict) -> dict:
    if request["type"] == "register":
        return validateRegistration(request["data_request"])
    
    if request["type"] == "login":
        return validateLogin(request["data_request"])
    
    if request["type"] == "consult":
        return validateTicketQuery(request["data_request"])

    if request["type"] == "search":
        return validateTicketDisplay(request["data_request"])
    
    if request["type"] == "shoppingCart":
        return validateShoppingCart(request["data_request"])

    if request["type"] == "purchaseConfirmed":
        return validatePurchase(request["data_request"])
    
    if request["type"] == "cancellationConfirmed":
        return validateCancellation(request["data_request"])
    
