# Einleitung

Dieses Dokument berücksichtigt folgende Artefakte:
1. gemSpec_PoPP_Service sichtbar auf [gemSpec_Pages][]
2. dieses git-project sichtbar gematik-intern [gematik_api-popp][]
3. dieses git-project gespiegelt auf github als [github_api-popp][]

Alle drei Artefakte haben ihren eigenen Release-Zyklus und ihre eigenen
Versionsnummern. Dieses Dokument beschreibt den Zusammenhang zwischen den
Artefakten.

# Übersicht

| [gematik_api-popp][] | [github_api-popp][] (main branch)    | gemSpec_PoPP_Service              |
|:---------------------|:-------------------------------------|:----------------------------------|
| tag "3.0.0_RC4"      | tag "gemSpec_PoPP_Service_1.0.0_CC2" | gemSpec_PoPP_Service_1.0.0_CC2    |
| tag "3.0.0_RC1"      | -                                    | [gemSpec_PoPP_Service_1.0.0_CC][] |
|

# Vorgehensweise

## [gematik_api-popp][] fortschreiben

Wenn das Projekt [gematik_api-popp][] weiterentwickelt und fortgeschrieben wird,
dann erhält es möglicherweise eigene, weitere Versionsnummern. Diese sind nach
außen nicht sichtbar, weder auf [github_api-popp][] noch [github_api-popp][].

Falls der Projektfortschritt von [gematik_api-popp][] nach [github_api-popp][]
transferiert wird, dann wird in [github_api-popp][] eine eigene Versionsnummer
als Tag vergeben.

Zusätzlich wird auf [github_api-popp][] ein Tag vergeben mit den Informationen
zur zugehörigen Spezifikation, beispielsweise "gemSpec_PoPP_Service_1.0.0_CC2".
Dieses Tag wird möglicherweise auf eine neuere Version in [github_api-popp][]
verschoben, wenn [github_api-popp][] aktualisiert wird, sich die zugehörige
Version der Spezifikation nicht änder.

## gemSpec_PoPP_Service fortschreiben

In gemSpec_PoPP_Service wird [github_api-popp][] referenziert und dann
(idealerweise / in Zukunft) auf ein Tag in [github_api-popp][] verwiesen,
welches die zugehörige Version der Dokumente in [github_api-popp][]
beinhaltet.

# Transfer

Die Übertragung von Daten von [gematik_api-popp][] nach [github_api-popp][]
wird wie folgt durch geführt:
1. ReleaseNotes auf gitlab und github überprüfen, ob das alles noch passt
2. Jenkins:
   1. JenkinsPipeline suchen nach "api-popp"
   2. auswählen: "Konnektor-api-popp-GitHub-PublishSources" 
2. 2. 
3. Build with parameters
    1. Gitlab Tag auswählen
    2. Commit message (Vorsicht, nur "unkritische" Zeichen verwenden): "Release Candidate 4"
    3. Automatic merge = "no" => pullRequest in github
    3. Remote_branch angeben
    4. "Build"-Button auf Jenkins
    5. PullRequest im github mergen
    6. Release im github anlegen


[github_api-popp]:https://github.com/gematik/api-popp
[gemSpec_Pages]:https://gemspec.gematik.de/
[gemSpec_PoPP_Service_1.0.0_CC]:https://gemspec.gematik.de/prereleases/Draft_Smartcards_24_3/gemSpec_PoPP_Service_V1.0.0_CC/
[gematik_api-popp]:https://gitlab.prod.ccs.gematik.solutions/git/spezifikation/api-popp
