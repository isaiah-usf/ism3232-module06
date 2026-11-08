# Author: Isaiah Martin
from my_assistant import BabysitterHelper
from my_tool import BabyInfoBook

BABY_INFO = {
    "sleep": {
        "keywords": ["nap", "sleep", "bedtime"],
        "answer": "[His typical nap intervals are 2 hours awake, then 3 hours awake, then 4 hours awake. He does not have a fixed nap or bedtime, as the intervals depend on the time he wakes up each morning as well as how long he naps for during each nap. His first nap will typicall last 1.5 to 2 hours, and his second will typically last for 1 to 1.5 hours.]",
    },
    "feeding": {
        "keywords": ["bottle", "feed", "eat", "food", "snack"],
        "answer": "[He no longer requires a bottle. I have prepared meals in the refrigerator, and he is to be offered that along with one of his straw cups filled with whole milk at every feeding, and he should be fed before every nap, and given a snack after he wakes up from every nap. For snacks offer him a vegetable or fruit pouch from the closet, along with either some cut up fruit or sticks/puffs.]",
    },
    "diapers": {
        "keywords": ["diaper", "wipes"],
        "answer": "[His changing table is in his room. If he attempts to roll while being changed, calmly say no rolling and put a hand on his shoulder to prevent him from rolling. There is no need to raise your voice, just hold him in place and offer him something to hold. Spare diapers, size 5, are located in the closet behind the rocking chair. Wipes can be found in the same location. After cleaning him, apply some of the vaseline to his butt cheeks to prevent diaper rash, he has very sensitive skin. Aside from cleaning anything that may have gotten onto it, his penis and foreskin do not require any special attention, and do not attempt to retract the foreskin for any reason, that is not necessary at his current age.]",
    },
    "allergies": {
        "keywords": ["allergy", "allergies", "allergic"],
        "answer": "[Jack does not have any known allergies, but please refrain from feeding him shellfish as I have an allergy and I am unsure if he has inherited it.]",
    },
    "comfort": {
        "keywords": ["cry", "crying", "upset", "soothe"],
        "answer": "[If Jack is upset, pick him up and speak gently to him. Sometimes a change of scenery will help, so walking to a different room or outside briefly is often helpful. He also loves music and knows the word for it, so offering to play music and then slowly swaying with him while it plays will often calm him down. Stay calm, if you are doing something necessary that is upsetting him, it is okay that he cries so long as you do not become frustrated with him and soothe him after the task is done. Remember that he is only a year old, he is quite limited in terms of emotional regulation and it falls on you to keep control of yourself and the situation. Never allow the behavior of the child to influence your emotional state negatively.]",
    },
}


INSTRUCTIONS = """
You are Cierra's Oracle, an assistant helping Cierra care for Jack.

Jack is one year old.
Jack drinks whole milk from a straw cup instead of using a bottle.
Jack should always have access to water from a straw cup.
Jack enjoys listening to music, which often helps calm him down.

Answer questions clearly and briefly.
Never invent facts about Jack or his routine.
Never guess the answer to question you are unsure about.
If you do not know an answer, say that you do not know and suggest asking his parents.
"""

if __name__ == "__main__":
    from ollama_model import OllamaModel

    baby_info_book = BabyInfoBook(BABY_INFO)
    model = OllamaModel("granite4.1:3b")

    helper = BabysitterHelper(
        "Cierra's Oracle",
        INSTRUCTIONS,
        baby_info_book,
        model,
    )

    print("Type a message, or type quit to stop.")
    user_message = input("You: ")
    while user_message != "quit":
        print(f"{helper.name}: {helper.respond(user_message)}")
        user_message = input("You: ")

    print(f"Messages in this conversation: {len(helper.history)}")
