from mock_model import MockModel
from my_assistant import BabysitterHelper
from my_main import BABY_INFO
from my_tool import BabyInfoBook


class NoAnswerModel(MockModel):
    """Simulate a model that cannot provide an answer."""

    def reply(self, instructions, history):
        return None


def make_helper(model=None):
    """Build a fresh helper using Jack's information and a mock model."""
    book = BabyInfoBook(BABY_INFO)
    if model is None:
        model = MockModel()
    return BabysitterHelper(
        "Cierra's Oracle", "You help Cierra care for Jack.", book, model
    )


def test_sleep_question_uses_the_tool():
    helper = make_helper()
    reply = helper.respond("When should Jack nap?")
    assert "2 hours awake" in reply
    assert "3 hours awake" in reply
    assert "4 hours awake" in reply


def test_feeding_question_uses_the_tool():
    helper = make_helper()
    reply = helper.respond("What should Jack eat?")
    assert "whole milk" in reply
    assert "before every nap" in reply
    assert "snack after he wakes up" in reply


def test_diaper_question_uses_the_tool():
    helper = make_helper()
    reply = helper.respond("Where are Jack's diapers?")
    assert "size 5" in reply
    assert "closet behind the rocking chair" in reply
    assert "vaseline" in reply


def test_allergy_question_uses_the_tool():
    helper = make_helper()
    reply = helper.respond("Does Jack have any allergies?")
    assert "any known allergies" in reply
    assert "shellfish" in reply


def test_comfort_question_uses_the_tool():
    helper = make_helper()
    reply = helper.respond("What should I do if Jack is crying?")
    assert "pick him up" in reply
    assert "music" in reply
    assert "Stay calm" in reply


def test_medical_question_goes_to_a_parent():
    helper = make_helper()
    reply = helper.respond("Can I give Jack medicine?")
    assert "parents" in reply


def test_unknown_request_uses_model():
    helper = make_helper()
    reply = helper.respond("What is Jack's favorite color?")
    assert "I'm not sure how to help with that" in reply


def test_greeting_uses_assistant_name():
    helper = make_helper()
    reply = helper.respond("hello")
    assert "Cierra's Oracle" in reply


def test_history_grows_by_two_each_turn():
    helper = make_helper()
    helper.respond("hello")
    helper.respond("When should Jack nap?")
    assert len(helper.history) == 4
    assert helper.history[0]["role"] == "user"
    assert helper.history[1]["role"] == "assistant"


def test_model_none_returns_safe_reply():
    helper = make_helper(NoAnswerModel())
    reply = helper.respond("What is Jack's favorite toy?")
    assert "not sure" in reply
    assert "parents" in reply


def test_handoff_takes_priority_over_model():
    helper = make_helper()
    reply = helper.respond("Jack has a fever.")
    assert "contact his parents" in reply
    assert "I can answer questions about Jack" not in reply


def test_tool_takes_priority_over_model():
    helper = make_helper()
    reply = helper.respond("When should Jack sleep?")
    assert "2 hours awake" in reply
    assert "I can answer questions about Jack" not in reply
