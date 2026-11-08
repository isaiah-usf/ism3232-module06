# Week 11 answers

## Exercise 1
1. The message the customer never saw:
The one labeled 'system'

2. How many times the customer has spoken:
The customer spoke twice and it's labeled 'user'

3. Can the model tell that the last reply came from the order tool? Why does that matter?
No, in history they are all labeled assistant regardless of which component of the assistant composed it.

4. The customer now types "thanks". How many messages are sent on the next call?
6, all the ones from before plus the new one


(.venv) SSgtStupid% python3 main.py
Type a message, or type quit to stop.
You: how long does shipping take
Goobus: Shipping takes 3 to 5 business days.
You: can i return a sale item
Goobus: No, sale items cannot be returned.
You: do you offer gift wrapping
Goobus: sowwy i dunno, i can pass you to a human agent for that info.
You: do you have a store in orlando
Goobus: sowwy i dunno, i can pass you to a human agent for that info.
You: quit
Messages in this conversation: 8
(.venv) SSgtStupid%
