
class FlashCard:
    def __init__(self, lines):
        self.lines = lines
        self.front_content = []
        self.back_content  = []
        self.hidden_content = []  # additional information that isn't shown on the card
        self.parse()

    def parse(self):
        pass

    def show(self):
        print("\n--- ", type(self).__name__, " ---")
        print("--- Vorderseite:")
        [print(c, end='') for c in self.front_content]
        print("--- Rückseite:")
        [print(c, end='') for c in self.back_content]

    def add_content(self, content, side="front"):
        side_dict = {"front": self.front_content, "back": self.back_content, "hidden": self.hidden_content}
        side = side_dict[side]
        if isinstance(content, list): side.extend(content)
        else: side.append(content)


class SimpleCard(FlashCard):

    def parse(self):
        self.add_content(self.lines[0], "front")
        self.add_content(self.lines[1:], "back")


class FrontBackCard(FlashCard):

    def parse(self):

        # a list of keywords to filter out
        forbidden_words = ["{FRONT}", "{BACK}", "{HIDDEN}", "{QUESTION}", "#", "##"]

        # start by adding content to the front
        add_to = "F"

        for line in self.lines[0:]:

            # check where to add the content to
            if   "{FRONT}" in line: add_to = "F"
            elif "{BACK}" in line: add_to = "B"
            elif "{HIDDEN}" in line: add_to = "H"

            # filter out keywords
            for word in forbidden_words:
                line = line.replace(word, "")

            # add the .md content to the right list
            if   add_to == "F": self.add_content(line, "front")
            elif add_to == "B": self.add_content(line, "back")
            elif add_to == "H": self.add_content(line, "hidden")


card_types = [SimpleCard, FrontBackCard]

# ----------------------------------------------------------------


def read(card_file: str):
    # read the file into a list of strings
    with open(card_file, encoding="utf-8") as f:
        lines = f.readlines()

    # split the lines into cards
    cards = []
    for line in lines:
        if line[0:2] == '# ': cards.append([])
        if line == "\n" or line == "": continue
        cards[-1].append(line)

    print(cards)

    # identify the type of card
    parsed_cards = []
    for card in cards:
        if "{QUESTION}" in card[0]: c = FrontBackCard(card)
        else:                       c = SimpleCard(card)
        c.show()
        parsed_cards.append(c)

    return parsed_cards


def mdToHtml(card_file: str, html_output: str):

    parsed_cards = read(card_file)

    # create the html output
    start_string = "<!DOCTYPE html>\n<html lang=\"de\">\n<body>"
    end_string = "</body>\n</html>"

    output = open(html_output, "w", encoding="utf-8")
    output.write(start_string)

    for idx, card in enumerate(parsed_cards):
        # headline
        output.write("<hr>")
        output.write("<h1 id=\"K%s\">Karte #%s</h1>" % (idx+1, idx+1))

        # front
        output.write("<h3 id=\"V%s\">Vorderseite:</h3>" % idx)
        [output.write(("<h5 id=\"c\">%s</h5>") % c) for c in card.front_content]

        # back
        output.write("<h3 id=\"V%s\">Rückseite:</h3>" % idx)
        [output.write(("<h5 id=\"c\">%s</h5>") % c) for c in card.back_content]

    output.write(end_string)
    output.close()

# ----------------------------------------------------------------


if __name__ == "__main__":
    mdToHtml("contextcards_example.md", "example.html")
