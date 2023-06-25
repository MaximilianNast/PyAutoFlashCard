import sys
import random

# ----------------------------------------------------------------------------------------------------------------------
# gpt-2 installation is based on this guide and left as an exercise to the reader:
# https://timhanewich.medium.com/running-openais-gpt-2-language-model-on-your-pc-5d5e1b9fbb8b
MODEL_PATH = "C:/Users/Max/Desktop/Projects/048_PyAutoFlashCard/gpt-2"
sys.path.append(MODEL_PATH + "/src")
import interactive_conditional_samples_mod as gpt2

# ----------------------------------------------------------------------------------------------------------------------
# definining the text input for the prompt to be completed by gpt-2
context = "Requirements engineering is about the elicitation, analysis, specification, and validation of"           \
          " requirements for software. Software requirements can be of three different types. There are functional" \
          " requirements, non-functional requirements, and domain requirements. The operation of the software"      \
          " should be performed and the proper output should be expected for the user to use. Non-functional"       \
          " requirements deal with issues like portability, security, maintainability, reliability, scalability,"   \
          " performance, reusability, and flexibility. They are classified into the following types: interface"     \
          " constraints, performance constraints (such as response time, security, storage space, etc.), operating" \
          " constraints, life cycle constraints (maintainability, portability, ...), and economic constraints."     \
          " Knowledge of how the system or software works is needed when it comes to specifying non-functional"     \
          " requirements. Domain requirements have to do with the characteristic of a certain category or domain"   \
          " of projects. "

question   = "What is Requirements Engineering about? "
answer     = "Requirements engineering is about the elicitation, analysis, specification, and validation of"   \
             " requirements for software. "

prompt = context + "Question: " + question + "Answer:"
print(prompt)

# ----------------------------------------------------------------------------------------------------------------------
# invoking model output with our mod
output = gpt2.interact_model(model_name="774M", models_dir=MODEL_PATH + "/models", prompt=prompt,
                            length=32, top_k=100, nsamples=3)

# ----------------------------------------------------------------------------------------------------------------------
# inserting the correct answer at a random index among the generated options
random_index = random.randint(0, len(output))
output.insert(random_index, answer)

# ----------------------------------------------------------------------------------------------------------------------
# printing all the options
[print("--- OPTION #" + str(idx) + " --------------\n" + out) for idx, out in enumerate(output)]

# ----------------------------------------------------------------------------------------------------------------------
# checking if the user chooses the correct answer
choice = input("\nWhich of the answers above is the correct one? (0-3) >>>")
if choice == random_index:
    print("You are correct, it's answer #" + str(random_index))
else:
    print("You are wrong, it's answer #" + str(random_index))
