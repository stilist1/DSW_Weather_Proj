import pytest
from mood_analyzer import MoodAnalyzer

@pytest.fixture
def analyzer():
    return MoodAnalyzer()

def test_positive_sentiment(analyzer):
    assert analyzer.analyzeMood("I'm very happy today!") == 'positive'

def test_negative_sentiment(analyzer):
    assert analyzer.analyzeMood("I feel terrible and sad.") == 'negative'

def test_neutral_sentiment(analyzer):
    assert analyzer.analyzeMood("Today is a day.") == 'neutral'
