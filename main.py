from crew_config import crew

def evaluate_startup(idea: str):
    result = crew.kickoff(inputs={"idea": idea})
    return result

if __name__ == "__main__":
    idea = input("Enter your startup idea: ")
    print(evaluate_startup(idea))