# Author: Isaiah Martin
HANDOFF_WORDS = [
    "medicine",
    "bleeding",
    "blood",
    "unconscious",
    "seizure",
    "hurt",
    "fell",
    "fall",
    "medication",
    "fever",
    "injury",
    "emergency",
    "vomit",
]


class BabysitterHelper:
    """A babysitter assistant using simple rulesand AI."""

    def __init__(self, name, instructions, baby_info_book, model):
        """Set up the helper with its name, instructions, tool, model, and history."""
        self.name = name
        self.instructions = instructions
        self.baby_info_book = baby_info_book
        self.model = model
        self.history = []

    def respond(self, user_message):
        """Record the user's message, choose a reply, and record it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply using keyword rules."""
        text = user_message.lower()
        if self.needs_human(text):
            return "Please contact his parents about that by calling 813-719-0284. If he is in immediate danger, call emergency services."
        if self.baby_info_book.find_topic(text) is not None:
            return self.info_reply(user_message)
        if "hello" in text:
            return f"Hello! I'm {self.name}. Ask me about his daily routine."
        return self.model_reply()

    def needs_human(self, text):
        """Return True if the question requires parental involvement."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def info_reply(self, user_message):
        """Use the information book to answer a question."""
        topic = self.baby_info_book.find_topic(user_message)
        if topic is None:
            return "What would you like to know about his routine?"
        info = self.baby_info_book.info_for(topic)
        return f"{info}"

    def model_reply(self):
        """Ask the model for an answer, or return a safe reply."""
        reply = self.model.reply(self.instructions, self.history)
        if not reply or not reply.strip():
            return "I'm not sure about that. Please ask his parents."
        return reply
