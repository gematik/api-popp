<img align="right" width="250" height="47" src="images/Gematik_Logo_Flag_With_Background.png"/><br/>

# Changelog

This is the changelog for the project described in [README.md](./README.md).

The changelog follows [Keep a Changelog v1.0.0][], i.e., each release has the
following sections (if non-empty):

- Summary: Git-commit message
- Added
- Changed
- Deprecated
- Removed
- Fixed
- Security

The versioning policy of this project follows [Semantic Versioning v2.0.0][].

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#release-330">Release 3.3.0</a></li>
    <li><a href="#release-320">Release 3.2.0</a></li>
    <li><a href="#release-310">Release 3.1.0</a></li>
    <li><a href="#release-300">Release 3.0.0</a></li>
    <li><a href="#release-200">Release 2.0.0</a></li>
    <li><a href="#release-100">Release 1.0.0</a></li>
  </ol>
</details>

## Release 3.3.0

Summary of changes in 3.3.0 compared to 3.2.0:

1. added:
   1. additional interfaces for mobile check in, in particular:
      1. [I_AnbieterApp_mobile_CehckIn.yaml](src/openapi/I_AnbieterApp_mobile_CheckIn.yaml)
      2. [I_PoPP_Modul_mobile_CheckIn.yaml](src/openapi/I_PoPP_Modul_mobile_CheckIn.yaml)
      3. [I_PoPP_Service_mobile_CheckIn.yaml](src/openapi/I_PoPP_Service_mobile_CheckIn.yaml)
      4. [I_PoPP_Service_mobile_CheckIn_EHC.yaml](src/openapi/I_PoPP_Service_mobile_CheckIn_EHC.yaml)
      5. [I_PoPP_Service_mobile_Token_Generation.yaml](src/openapi/I_PoPP_Service_mobile_Token_Generation.yaml)

## Release 3.2.0

Summary of changes in 3.2.0 compared to 3.1.0:

1. changed:
   1. interface
      [I_PoPP_EHC_CertHash_Import.json](src/openapi/I_PoPP_EHC_CertHash_Import.json):  
      a new functionality is added to ask the PoPP-Service for know Job-IDs of
      the current "Lieferant"

## Release 3.1.0

Summary of changes in 3.1.0 compared to 3.0.0:

1. added
   1. interface
      [I_PoPP_EHC_CertHash_Import.json](src/openapi/I_PoPP_EHC_CertHash_Import.json)

## Release 3.0.0

Summary of changes in release 3.0.0 compared to 2.0.0:

1. changed:
   1. interface
      [I_PoPP_Token_Generation.yaml](src/openapi/I_PoPP_Token_Generation.yaml),
      list of major changes:
      1. add OSCP stapling to signed scenarios
      2. add claims of signed scenarios
      3. change names of enums in "TokenClaims"
      4. removed TAN handling
      5. removed property "pn" from "TokenMessage"
      6. removed property "x5c" from "TokenHeader"

## Release 2.0.0

Summary of changes in release 2.0.0 compared to 1.0.0:

1. added:
   1. interface
      [I_PoPP_Token_Generation.yaml](src/openapi/I_PoPP_Token_Generation.yaml)
2. removed:
   1. outdated interface specification "scenario/Specification.md"

## Release 1.0.0

First release with major version number greater than zero.

[Keep a Changelog v1.0.0]:http://keepachangelog.com/en/1.0.0/

[Semantic Versioning v2.0.0]:http://semver.org/spec/v2.0.0.html
