import sys
import random
import md_flashcard_reader

# ----------------------------------------------------------------------------------------------------------------------
# gpt-2 installation is based on the guide in readme.md
MODEL_PATH = "C:/Users/Max/Desktop/Projects/048_PyAutoFlashCard/gpt-2"
sys.path.append(MODEL_PATH + "/src")
import interactive_conditional_samples_mod as gpt2

# ----------------------------------------------------------------------------------------------------------------------


def build_model_input(card_input, prime_by=1):

    # building the prompt from our card
    question = card_input.front_content[-1]
    answer = card_input.back_content[-1]
    context = card_input.hidden_content[-1]
    out_prompt = context + " Question: " + question + " Correct Answer: " + answer + " Wrong Answer: "

    # priming the prompt with a few of the first words of the answer
    primer = answer.split()[0:prime_by]
    primer = " ".join(primer)
    out_prompt += primer

    # formatting the prompt for gpt
    out_prompt = out_prompt.replace("\n", "")
    out_prompt = out_prompt.replace("   ", " ")

    return out_prompt, primer


def clean_model_output(generated):

    for i, ans in enumerate(generated):

        # cutting off model output after the first finished sentence to make it less predictable
        ans = ans.replace("!", ".")
        ans = ans.replace(";", ".")
        generated[i] = ans.split(".")[0] + "."

        # removing answers containing a questionmark
        if "?" in ans:
            del generated[i]

    return generated

# ----------------------------------------------------------------------------------------------------------------------


cards = md_flashcard_reader.read("contextcards_example.md")

for card in cards:

    prompt, primer = build_model_input(card, prime_by=1)

    # invoking model output with our mod
    output = gpt2.interact_model(
        model_name  = "1558M",
        models_dir  = MODEL_PATH + "/models",
        prompt      = prompt,
        length      = len(card.back_content[-1].split()*2),
        top_k       = 40,
        nsamples    = 4,
        temperature = 1,
        batch_size  = 1)

    output = clean_model_output(output)
    output = [primer + s for s in output]

    # ---------------
    # inserting the correct answer at a random index among the generated options
    random_index = random.randint(0, len(output))
    output.insert(random_index, card.back_content[-1])

    # ---------------
    # printing all the options
    print(card.front_content[-1] + "\n")
    for idx, out in enumerate(output):
        print("--- OPTION #" + str(idx) + " --------------\n" + out + "\n----------------------------\n")

    # ---------------
    # checking if the user chooses the correct answer
    choice = input("\nWhich of the answers above is the correct one? (0-" + str(len(output)) + ") >>>")
    if int(choice) == random_index:
        print("You are correct, it's answer #" + str(random_index) + "\n\n")
    else:
        print("You are wrong, it's answer #" + str(random_index) + "\n\n")
