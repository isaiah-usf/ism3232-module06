# two_bots.py
# Author: Isaiah Martin

from chatbot import SupportChatbot
from mock_model import MockModel
from order_tool import OrderLookup
from stock_tool import StockLookup

order_tool = OrderLookup({"A100": "shipped", "A101": "processing"})
stock_tool = StockLookup({"rain jacket": 12, "day pack": 0})

model = MockModel()


goobus = SupportChatbot(
    "Goobus", "You are cheerful and brief.", order_tool, stock_tool, model
)
river = SupportChatbot(
    "River", "You are formal and detailed.", order_tool, stock_tool, model
)

goobus.respond("hello")
goobus.respond("Where is order A100?")
river.respond("hello")

print(goobus.name, len(goobus.history))
print(river.name, len(river.history))
print(goobus.history[1]["content"])
print(river.history[1]["content"])
print(goobus.instructions)
print(river.instructions)
