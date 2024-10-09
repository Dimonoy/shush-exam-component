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

CHOOSE_OPTION = _wrap_ai_message(
    "I see. What a great choice))))\n"
    "So what specifically do you\n"
    "need?\n"
    "\n"
    "1) Concept\n"
    "2) Solution\n"
    "3) Problem generation\n"
    "4) Verfy solution\n"
    "5) Real world application\n"
    "6) Solution's next step\n"
)

CHOOSE_OPTION_INPUT = _wrap_user_message("Umm... Specifially I want ")

FAREWELL = _wrap_ai_message("Bye bye! Have a nice day)\n")

# Math system prompts
CONCEPT_PROMPT = (
    "The user is going to send a term or a phrase related to math. "
    "I want you to give him an exmplanation of the given term or phrase. "
    "I want you to write at most 3 sentences, where in the first "
    "sentence you write his inputed term or phrase, space char, "
    "hyphen char, space char and than the explanation itself."
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
PROBLEM_GENERATION_PROMPT = (
    "The user is going to send you a math exercise. I want you "
    "to generate exactly the same exercise preferably preserving "
    "the same terms and sentences, but changing only variables and "
    "conditions of the exercise. Preferably make the exercise to be "
    "solved in the way that it doesn't require user to utilize "
    "calculator."
)
VERIFY_SOLUTION_PROMPT = (
    "The user is going to send you two blocks of text: math exercise "
    "and his/her solution. I want you to verify his solution against "
    "the given exercise, providing short tips on what he had to do "
    "in the particular parts of his/her solution. Preferably, don't "
    "provide the answer to the exercise. If the answer is wrong, you just "
    "point it out and show him where he/she might have made a mistake."
)
REAL_WORLD_APPLICATION_PROMPT = (
    "The user is going to send a term or a phrase related to math. "
    "I want you to give him at most 5 real world applicaitons of "
    "the concept he provided."
)
SOLUTIONS_NEXT_STEP_PROMPT = (
    "The user is going to send you two blocks of text: math exercise "
    "and his/her solution. I want you to provide the next step on how "
    "to proceed to solve his exercise. If it happens that the next step "
    "is the last step, hence the answer itself, don't show him the answer. "
    "Instead, explicitly state this fact and give me a tip on how to "
    "complete his solution."
)
