Semesterprojekt - Woche X + 1
***

- ### Skizziere deine Idee und definiere Anforderungen, die Du noch erreichen willst!

    - Für ein Quiz-Spiel mit Lernkarten werden oft falsche Antwortmöglichkeiten benötigt. So ähnlich wie bei "Wer wird 
    Millionär" gibt es bei solchen Spielen oftmals 4 Antwortmöglichkeiten, die syntaktisch alle 4 richtig klingen, von denen
    semantisch allerdings nur eine einzige korrekt ist.

    - Um diese falschen Antwortmöglichkeiten automatisch zu generieren, kann man eine Schwachstelle aktueller Sprachmodelle
    ausnutzen. Man sagt auch, dass Modelle wie GPT-2 "halluzinieren". Sie sind sehr gut darin, Texte so zu vervollständigen,
    dass diese Syntaktisch einwandfrei aussehen, aber ansonsten völlig sinnfrei sind.

    - Daraus ergeben sich die gewünschten falschen Antwortmöglichkeiten für das Quizspiel.

    - Zu erreichende ziele:

        - integration des geschriebenen LearningCard-parsers mit einem speziell hierfür gedachten Kartentyp
        - Erweitertes Lernspiel (z.B. mehrere Fragen hintereinander)

    - Die technischen Details von Sprachmodellen sollen hier NICHT weiter angepasst sondern nur genutzt werden

- ### Wie kannst Du den Erfolg der Umsetzung messen?

  - Vorerst sollten die generierten Antworten nicht "auf den ersten Blick" falsch aussehen. (Bspw.: Text endet mitten im
  Satz / ausgedachte Wörter).

- ### Überlege Dir eine Möglichkeit mir Einblick in Deine Entwicklung zu geben! Hier bietet sich z.B. ein git-Repo an.

  - Der Code und eine Erklärung ist unter

    ```
    https://github.com/MaximilianNast/PyAutoFlashCard
    ```

    zu finden.

- ### Hast Du bis zur Abgabe dieser Aufgabe schon etwas umgesetzt? Wenn ja was?

  - minimal working example
  - Installationsanleitung
  - Nutzungsanleitung