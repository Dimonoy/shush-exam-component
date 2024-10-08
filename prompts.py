from colorama import Fore, Back


def _wrap_ai_message(message):
    line = len(message.split("\n")[0]) * "="

    return (
        Fore.GREEN
        + Back.BLACK
        + "\n"
        + line
        + "\n"
        + message
        + line
        + Fore.RESET
        + Back.RESET
    )


def _wrap_user_message(message):
    return Fore.WHITE + "\t" + message + Fore.RESET


GREETING = _wrap_ai_message(
    "Welcome! I am Stacy, wanna go to the prom together ;)\n"
    "If not, then I could offer you some help with any\n"
    "school subject of your choice.\n"
    "Here is the rich list:\n"
    "...\n"
    "...\n"
    "...\n"
    "...\n"
    "...\n"
    f"{Fore.RED}666) Math\n{Fore.GREEN}"
    "...\n"
    "...\n"
    "...\n"
    "...\n"
    "Choose whatever you would like ;)\n"
)

GREETING_INPUT = _wrap_user_message("Hmm... I think I am interested in ")

CHOOSE_PROMPT = _wrap_ai_message(
    "I see. What a great choice))))\n"
    "So what specifically do you\n"
    "need?\n"
    "\n"
    "1) Concept\n"
    "2) Solution\n"
    "3) \n"
    "4) \n"
    "5) \n"
    "6) \n"
)

CHOOSE_PROMPT_INPUT = _wrap_user_message("Umm... Specifially I want ")

# Math system prompts
CONCEPT_PROMPT = (
    "The user is going to send a term or a phrase related to math. "
    "I want you to give him an exmplanation of the given term or phrase. "
    "I want you to write a one/two/three sentences, where in the first "
    "sentence you put his input, space char, hyphen char, space char "
    "and than the explanation itself."
)
SOLUTION_PROMPT = (
    "The user is going to give you a problem. Analyze the assigment "
    "thoroughly and give him an explanation on how to solve it. "
    "If no assigment given, than deduct the solution on your own. "
    "I want you to give an answer in the following format: "
    "Given variables; Variables to find; Solution; Answer. "
    'In "Given variables" section explain each variable; '
    'In "Variables to find" section explain each variable; '
    'In "Solution" section explain each step; '
    'In "Answer" section write just a short answer/answer itself.'
)
