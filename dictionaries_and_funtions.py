# questionaire dictionary
question_template = {
    "title": "default title",
    "question": "default question",
    "answer": "default answer",
    "hints": []
}
  
# a function to help us populate new questions:
def make_new_question(title, question, answer, hints=None):
    new_q = question_template.copy()

    # always require title, question, answer
    new_q["title"] = title
    new_q["question"] = question
    new_q["answer"] = answer

    # sometimes there aren't hints, that's fine. Otherwise, add them:
    if hints is not None:
        new_q["hints"].extend(hints)

    return new_q

#Then we added a few questions (abbreviated for simplicity):
question_1 = make_new_question("title1", "question1", "answer1", ["q1 hint1", "q1 hint2"])
question_2 = make_new_question("title2", "question2", "answer2")
question_3 = make_new_question("title3", "question3", "answer3", ["q3 hint1"])

#Something doesn't add up! Trick to be posted tomorrow
