from paypalrestsdk.resource import Find, Create

class CreditCard(Find, Create):

  path = "v1/vault/credit-card"

CreditCard.convert_resources['credit_card'] = CreditCard