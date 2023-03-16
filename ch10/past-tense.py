words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

def past_tense(list):
    past_tense = []
    for word in list:
        if (word[-1] == "e"):
            past_tense.append(word + "d")
        else:
            past_tense.append(word + "ed")
    return past_tense
        
print(past_tense(words))
