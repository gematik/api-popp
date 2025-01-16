<img align="right" width="250" height="47" src="images/Gematik_Logo_Flag_With_Background.png"/><br/>

# Release Notes api-popp

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#release-100">Release</a></li>
  </ol>
</details>

## Release 1.0.0
This project describes the following interfaces:

1. "I_PoPP_CheckIn_AuthorizationServer.yaml"  
   Interface from a PoPP-Module to PoPP-Service Authorization Server,
   this interface is used during a mobile Check-in to get an access token.
2. "I_PoPP_CheckIn_ResourceServer.yaml"  
   Interface from a PoPP-Module to PoPP-Service Resource Server,
   this interface is used to exchange an access token with a TAN-Set-Record.
3. "I_PoPP_Token_Generation.yaml"  
   Interface from a PoPP-Client to a PoPP-Service,
   this interface is used to create a PoPP-Token by the PoPP-Service and
   transfer the PoPP-Token to the PoPP-Client.
