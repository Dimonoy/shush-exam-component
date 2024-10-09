import os

import openai
from dotenv import load_dotenv

import prompts

load_dotenv()
client = openai.OpenAI()


if __name__ == "__main__":
    choice_prompt_mapping = {
        1: prompts.CONCEPT_PROMPT,
        2: prompts.SOLUTION_PROMPT,
        3: prompts.PROBLEM_GENERATION_PROMPT,
        4: prompts.VERIFY_SOLUTION_PROMPT,
        5: prompts.REAL_WORLD_APPLICATION_PROMPT,
        6: prompts.SOLUTIONS_NEXT_STEP_PROMPT,
    }
    # 1) Listing available subjects
    print(prompts.GREETING)

    # 2) Choosing subject
    _ = input(prompts.GREETING_INPUT)

    while True:
        try:
            # 3) Listing available types of prompts
            print(prompts.CHOOSE_OPTION)

            # 4) Choosing prompt
            try:
                choice = int(input(prompts.CHOOSE_OPTION_INPUT))
            except ValueError:
                print("Input number from 1 to 6 next time (=")
                continue

            prompt = choice_prompt_mapping.get(choice)

            # 5) Getting user question
            user_input = input("Question: ")

            # 6) Getting answer
            answer = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": prompt,
                    },
                    {
                        "role": "user",
                        "content": user_input,
                    },
                ],
            )

            with open("message_history.log", "a") as log_file:
                chat_completion_message = answer.choices[0].message

                log_file.write(chat_completion_message.__str__() + "\n")
                print(chat_completion_message)
        except KeyboardInterrupt:
            print(prompts.FAREWELL)
            break
    client.close()
