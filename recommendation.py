def getRecommendation(weatherType, moodType):
    recommendations = {
        ('rain', 'negative'): "Listen to a relaxing playlist and do indoor yoga.",
        ('rain', 'neutral'): "Watch a movie and enjoy a cup of tea.",
        ('rain', 'positive'): "Dance in the rain or read a favorite book!",

        ('clear', 'positive'): "Go for a run or have a picnic in the park!",
        ('clear', 'neutral'): "Go for a walk or visit a museum.",
        ('clear', 'negative'): "Soak up some sun and let nature uplift your spirit.",

        ('clouds', 'positive'): "Take aesthetic cloudy day pictures or enjoy coffee.",
        ('clouds', 'neutral'): "Read a novel or do a small creative project.",
        ('clouds', 'negative'): "Meditate or write your thoughts in a journal."
    }

    return recommendations.get((weatherType, moodType), "Try to relax and take care of yourself today.")
