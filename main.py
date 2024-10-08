import os
import sys
import getpass

import openai

import prompts

os.environ["OPENAI_API_KEY"] = getpass.getpass().rstrip()
client = openai.OpenAI()


if __name__ == "__main__":
    choice_prompt_mapping = {
        1: prompts.CONCEPT_PROMPT,
        2: prompts.SOLUTION_PROMPT,
    }

    while True:
        # 1) Listing available subjects
        print(prompts.GREETING)

        # 2) Choosing subject
        _ = input(prompts.GREETING_INPUT)

        # 3) Listing available types of prompts
        print(prompts.CHOOSE_PROMPT)

        # 4) Choosing prompt
        try:
            choice = int(input(prompts.CHOOSE_PROMPT_INPUT))
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

        print(answer)
        break
