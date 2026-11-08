# Author: Isaiah Martin


class BabyInfoBook:
    """A tool that knows basic information about a child."""

    def __init__(self, baby_info):
        """Store the information this tool can look up."""
        self.baby_info = baby_info

    def find_topic(self, text):
        """Return the first known topic mentioned in text, or None."""
        for topic, details in self.baby_info.items():
            for keyword in details["keywords"]:
                if keyword in text.lower():
                    return topic
        return None

    def info_for(self, topic):
        """Return information for one topic, or None if unknown."""
        if topic in self.baby_info:
            return self.baby_info[topic]["answer"]
        return None
