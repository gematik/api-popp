<img align="right" width="250" height="47" src="images/Gematik_Logo_Flag_With_Background.png"/><br/>

# Release Notes api-popp

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#release-200">Release 2.0.0</a></li>
    <li><a href="#release-100">Release 1.0.0</a></li>
  </ol>
</details>

## Release 2.0.0
This release describes the following interface which substitutes the interface
from release 1.0.0:

- "I_PoPP_Token_Generation.yaml"  
   Interface from a PoPP-Client to a PoPP-Service,
   this interface is used to create a PoPP-Token by the PoPP-Service and
   transfer the PoPP-Token to the PoPP-Client.

## Release 1.0.0
- Description of the interface between component "PoPP26-Service" on one hand
  and a Konnektor on the other hand for the purpose of sending arbitrary
  ISO/IEC 7816-4 command APDU to a smartcard available in an eHealth-Cardterminal
  connected to the Konnektor.
