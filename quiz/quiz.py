from question import question

prompts = [
    "Is sadvinegar hot?\n(a) yes\n(b) no\n\n",
    "Which is the highest caliber Skyblock Discord server?\n(a) Skyblock Simplified\n(b) SkyblockZ\n(c) They all suck, please touch grass\n\n",
    "Wyvest\n(a) Wyvest\n(b) Wyvest\n(c) Wyvest\n\n"
]

questions = [
    question(prompts[0], "a"),
    question(prompts[1], "c"),
    question(prompts[2], "b"),
]


def quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " questions correct!")

quiz(questions)