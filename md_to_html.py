
class FlashCard:
    def __init__(self, lines):
        self.lines = lines
        self.front_content = []
        self.back_content  = []
        self.parse()

    def parse(self):
        pass

    def show(self):
        print("\n--- ", type(self).__name__, " ---")
        print("--- Vorderseite:")
        [print(c, end='') for c in self.front_content]
        print("--- Rückseite:")
        [print(c, end='') for c in self.back_content]

    def add_front_content(self, content):
        if isinstance(content, list): self.front_content.extend(content)
        else: self.front_content.append(content)

    def add_back_content(self, content):
        if isinstance(content, list): self.back_content.extend(content)
        else: self.back_content.append(content)


class SimpleCard(FlashCard):

    def parse(self):
        self.add_front_content(self.lines[0])
        self.add_back_content(self.lines[1:])


class FrontBackCard(FlashCard):

    def parse(self):
        self.add_front_content(self.lines[0])
        add_to = "F"
        for line in self.lines[1:]:
            if   "{FRONT}" in line: add_to = "F"
            elif "{BACK}" in line: add_to = "B"
            if   add_to == "F":
                self.add_front_content(line)
            elif add_to == "B":
                self.add_back_content(line)


card_types = [SimpleCard, FrontBackCard]

# ----------------------------------------------------------------


def mdToHtml(card_file: str, html_output: str):
    pass

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

    # create the html output
    start_string = "<!DOCTYPE html>\n<html lang=\"de\">\n<body>"
    end_string = "</body>\n</html>"

    output = open(html_output, "w", encoding="utf-8")
    output.write(start_string)

    for idx, card in enumerate(parsed_cards):
        # headline
        output.write("<hr>")
        output.write("<h1 id=\"K%s\">Karte #%s</h1>" % (idx, idx))

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
    mdToHtml("../../045_Software_Engineering_SS23/Blatt_5/Markdown to HTML - Basic (PYTHON Alternative)/cards.md", "example.html")
