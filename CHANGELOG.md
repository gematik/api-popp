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
    <li><a href="#release-300">Release 3.0.0</a></li>
    <li><a href="#release-200">Release 2.0.0</a></li>
    <li><a href="#release-100">Release 1.0.0</a></li>
  </ol>
</details>

## Release 3.0.0
Summary of changes in release 3.0.0 compared to 2.0.0:
1. added:
   1. interface "I_PoPP_CheckIn_AuthorizationServer.yaml"
   2. interface "I_PoPP_CheckIn_ResourceServer.yaml"
2. changed:
   1. interface "I_PoPP_Token_Generation.yaml"
3. removed
   1. removed property "x5c" for object "TokenHeaders"
      in interface "I_PoPP_Token_Generation.yaml"
   2. removed property "pn" for object "TokenMessage"
      in interface "I_PoPP_Token_Generation.yaml"

## Release 2.0.0
Summary of changes in release 2.0.0 compared to 1.0.0:
1. added:  
   1. interface "I_PoPP_Token_Generation.yaml"
2. removed:
   1. outdated interface specification "scenario/Specification.md"

## Release 1.0.0
First release with major version number greater than zero.

[Keep a Changelog v1.0.0]:http://keepachangelog.com/en/1.0.0/
[Semantic Versioning v2.0.0]:http://semver.org/spec/v2.0.0.html
