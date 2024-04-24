<img align="right" width="250" height="47" src="images/Gematik_Logo_Flag_With_Background.png"/><br/>

# API Specification for Scenarios

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#release-notes">Release Notes</a></li>
    <li><a href="#changelog">Changelog</a></li>
    <li><a href="#folder-structure">Folder Structure</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## About the Project

This project is part of a PoPP (Proof of Patient Presence) Variant 2b (i.e.,
the electronic Health Card (eHC) is connected via an eHealth-Cardterminal
(eHCT)).
The component PoPP-Service needs information from the eHC, but has no direct
connection to the eHC.
Thus, the PoPP-Service sends a "Scenario" via the PoPP-Client to the Konnektor.
The Konnektor sends the ISO/IEC 7816-4 command APDu from the "Scenario" to the
eHC (via the eHCT) and collects the corresponding responses APDU.
The collected response APDU are returned to the PoPP-Service (also via the
PoPP-Client).

In particular this project describes the interface to and from the Konnektor
regarding the handling of "Scenarios". For further details, consult the
[Specification](./scenario/Specification.md).

```plantuml
'https://plantuml.com/en/
skinparam componentStyle rectangle

component [Konnektor]   as "Konnektor"    #white
component [eHKT]        as "eHCT"         #white
component [PoppService] as "PoPP-Service" #white
component [PoppClient]  as "PoPP-Client"  #white
component [eGK]         as "eHC"          #white
note "Card-to-Card with\nTrusted Channel via\nPopp-Client" as n1

eGK         -- eHKT
eHKT        -- Konnektor
Konnektor   -- PoppClient
Konnektor   -  n1          #white
PoppClient  -  PoppService
eGK         -  n1          #red
n1          -  PoppService #red
```

## Release Notes
See [ReleaseNotes.md](./ReleaseNotes.md) for all information regarding the
(latest) releases.

## Changelog
See [CHANGELOG.md](./CHANGELOG.md) for information about changes.

## Folder Structure

| Folder   | Subfolder | Content                                                |
|:---------|-----------|--------------------------------------------------------|
| images   |           | static image material for rendering Markdown documents |
| scenario |           | specification of "scenario" and corresponding response | 

## Contributing
If you want to contribute, please check our [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

Copyright 2024 gematik GmbH

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License.

See the [LICENSE](./LICENSE) for the specific language governing permissions and
limitations under the License.

Unless required by applicable law, the software is provided "as is" without
warranty of any kind, either express or implied, including, but not limited to,
the warranties of fitness for a particular purpose, merchantability, and/or 
non-infringement.
The authors or copyright holders shall not be liable in any manner whatsoever
for any damages or other claims arising from, out of or in connection with the
software or the use or other dealings with the software, whether in an action
of contract, tort, or otherwise.

The software is the result of research and development activities, therefore not
necessarily quality assured and without the character of a liable product.
For this reason, gematik does not provide any support or other user assistance
(unless otherwise stated in individual cases and without justification of a
legal obligation). Furthermore, there is no claim to further development and 
adaptation of the results to a more current state of the art.

Gematik may remove published results temporarily or permanently from the place
of publication at any time without prior notice or justification.
