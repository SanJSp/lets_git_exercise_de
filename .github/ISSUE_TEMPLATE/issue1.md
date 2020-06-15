---
name: Aufgabe 1 Template
about: Das erste Issue, welches Aufgabe 1 abbildet.
title: Titel der Webseite hinzufügen
labels: good first issue
assignees: ''

---

#### Beschreibung
Wenn Besucher auf deine Website kommen, dann wissen sie im Moment nicht, worum es geht, da auf der Website keine Informationen über deinen Charackter zu sehen sind. Du solltest einen Titel hinzufügen, sodass die Besucher verstehen, um welchen Charakter es sich auf dieser Webseite handelt.

#### Dateien
Wenn du nicht weißt, wie man einen Titel erstellt, schau mal auf dieses Cheatsheet unter Header. Du sollst einen H1 Header verwenden. Bedenke, dass Markdown Symbole häufig von einem Leerzeichen gefolgt werden, um korrekt zu rendern.
https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf

#### Aufgaben
Führe folgende Schritte aus:
- [ ] Navigiere in der Git Bash/im Terminal zu deinem Repository. Das sollte durch den Befehl ```cd \<dein github name\>.github.io``` klappen.
- [ ] Da wir hier den Github Flow verwenden wollen, sollst du einen neuen Branch mit dem Namen ```feature1_new_title``` erstellen. Dafür verwendest du den Befehl ```git branch feature1_new_title```. Achte darauf, dass der Branch wirklich so heißt, sonst können wir deine Änderungen nicht korrigieren.
- [ ] Wechsle auf den erstellten Branch mit dem Befehl ```git checkout feature1_new_title```
- [ ] Nun wollen wir das Repository im Explorer (oder einem anderen Programm, welches Ordner anzeigen kann) öffnen. Navigiere dafür einfach zum Ordner, worin dein Repository geclont wurde. Als Hilfe kannst du auch unsere Shortcuts probieren: Dafür gibtst du in der Git Bash unter Windows den Befehl ```explorer.exe .``` ein. Unter Linux gibst du den Befehl ```nautilus .``` ein. Als Mac User kannst du den Befehl ```open .```verwenden
- [ ] Nun sollst du den Titel zu der Webseite hinzufügen. Öffne dafür die index.md Datei mit einem Editor. Lösche alles, was bereits in der Datei steht und nutze Github flavoured Markdown, um einen Titel zu der Website hinzuzufügen. Falls du nicht weißt wie, schau in das Cheatsheet.
- [ ] Nachdem du den Titel hinzugefügt hast, musst du die index.md Datei speichern. Füge dann in der Git Bash/deinem Termianl die Datei ```index.md``` der Staging Area hinzu. Das machst du mit dem Befehl ```git add index.md```. Anschließend musst du die Veränderungen commiten. Führe einen Commit mit dem Befehl ```git commit -m „Added Title“``` aus. Pushe dann die Veränderungen mit dem Befehl ```git push```. Dabei kann ein Fehler auftreten, weshalb du eine Fehlermeldung siehst. Kopiere dann einfach den Befehl aus der Fehlermeldung und führe diesen aus.
- [ ] Erstelle auf Github einen Pull Request von deinem feature Branch in den Master Branch. dafür musst du in den Tab Pull Requests wechseln und dann auf den grünen Button "Compare & Pull Request" klicken. Wähle dann einen Titel, um in ein paar Worten auszusagen, was in diesem Pull Request geschehen ist. Im Textkörper des Pull Request beschreibst du das gelöste Problem. Was war das Problem? Wie hast du es gelöst? Welche betroffenen Dateien gibt es?
- [ ] Nun werden von uns geschriebene Tests deine Veränderungen prüfen. Sollten alle Tests (2 Stück) bestanden worden sein, dann kannst du deine Änderungen in den Master Branch mergen. Falls die Tests fehlschlagen, schaue in die Kommentare des Pull Requests, um herauszufinden woran es lag. Behebe die Fehler, sodass die Tests durchlaufen. Eine gute Idee ist es, die Schritte des Issues erneut zu durchlaufen und zu schauen, ob alles richtig geschrieben ist. Außerdem kannst du dir die Index.md Datei auf Github anschauen und die richtige Formattierung überprüfen. Wenn du es für 15 Minuten ohne Erfolg nicht hingekriegt hast, kannst du in das Kursforum schauen.
- [ ] Gib das vom Bot im Pull Request kommentierte Passwort im Quiz auf openHPI ein.
- [ ] Lösche deinen Feature Branch. Dafür musst du den Branch im remote Repository hier auf Github und bei dir lokal löschen. Für den Branch hier auf Github betrachtest du deinen Pull Request und kannst unten den Branch löschen. Deinen Branch im lokalen Repository löschst du, nachdem du in deiner Bash/Terminal auf den master Branch gewechselt bist mit `git branch -d feature1_new_title`. Führe dann auf dem master ```git pull``` aus, um dein Repository auf den neuesten Stand zu bringen.
- [ ] Schließe dieses Issue.
- [ ] Betrachte deine Webseite und schau, ob sich etwas verändert hat. Gegebenenfalls musst du ein paar Mal die Seite aktualisieren.

Solltest du Fragen haben, kannst du einen Blick ins Kurs Forum werfen.
