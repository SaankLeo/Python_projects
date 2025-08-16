heroes = {
    "question": "Are they from Marvel?",
    "yes": {
        "question": "Were they born with powers?",
        "no": {
            "question": "Bit by a radioactive spider?",
            "yes": "Spider-Man",
            "no": {
                "question": "Associated with Jarvis?",
                "yes": "Iron Man",
                "no": "Captain America"
            }
        },
        "yes": "Thor"
    },
    "no": {
        "question": "Were they born with powers?",
        "yes": {
            "question": "Do they wear a cape?",
            "yes": "Superman",
            "no": {
                "question": "Are they an Amazonian fighter?",
                "yes": "Wonder Woman",
                "no": "Flash"
            }
        },
        "no": "Batman"
    }
}

def akinator(heroes):
    while isinstance(heroes,dict):
        question= heroes["question"]
        answer= input(question + "(yes,no): ").strip().lower()
        if answer not in ["yes","no"]:
            print("Please answer in yes or no")
            continue
        heroes=heroes[answer]
    print("I think it is:",heroes,". If not ,you need to stop watching movies and touch some grass.")

print("Think of a superhero:")
akinator(heroes)