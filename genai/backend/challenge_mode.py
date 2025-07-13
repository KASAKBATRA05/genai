
import random
from fuzzywuzzy import fuzz

def generate_questions(text, num=2):
    sents = [s for s in text.split('.') if len(s)>30]
    random.shuffle(sents)
    qs = []
    for sent in sents[:num]:
        ws = sent.split()
        key = ws[len(ws)//2]
        qs.append((f"Fill the blank: {sent.replace(key,'_____')}", key, sent))
    return qs

def evaluate_answer(uans, correct):
    from fuzzywuzzy import fuzz
    score = fuzz.partial_ratio(uans.lower(), correct.lower())
    if score>80:
        return "Correct ✅", f"Correct answer was '{correct}'"
    else:
        return "Incorrect ❌", f"Expected '{correct}'"
