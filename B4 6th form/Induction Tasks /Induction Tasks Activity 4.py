class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "What is 6 multiplied by 8?\n(a) 48\n(b)14",
    "What is the sum of 19 and 92?\n(a) 111\n(b)120",
    "What is 9 divided by 3?\n(a) 3\n(b) 6",
    "What is 8 multiplied by 9?\n(a) 72\n(b) 17",
    "What is 59 subtract 92?\n(a) -33\n(b) 33",
    "What is 9 multiplied by 7?\n(a) 63\n(b)16",
    "What is the sum of 208 and 92?\n(a) 300\n(b)120",
    "What is 8 divided by 2?\n(a) 4\n(b) 6",
    "What is 8 multiplied by 7?\n(a) 56\n(b) 17",
    "What is 78 subtract 345?\n(a) -247\n(b) 403",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompt[2], "a"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "a"),
    Question(question_prompt[5], "a"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "a"),
    Question(question_prompt[8], "a"),
    Question(question_prompt[9], "a"),
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got", score, "out of", len(questions))


run_quiz(questions)










