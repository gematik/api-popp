<img align="right" width="250" height="47" src="../images/Gematik_Logo_Flag_With_Background.png"/><br/>

# Introduction

This file specifies a request and the corresponding response. The request
contains a <a href="#Scenario">Scenario</a> and is sent to a Konnektor. The
Konnektor generates the corresponding response.

## Scenario

Basically a "Scenario" contains a list of ISO/IEC 7816-4 command APDU which are
intended to be sent to a smartcard. Such a "Scenario" is useful in case the
roundtrip time of a "producer" (here PoPP-Service) and a "consumer" (here the
smartcard) is rather large. Thus, instead of sending one command APDU at a time
the "producer" compiles and sends a "scenario" to a "proxy" (here the
Konnektor) which is closer to the "consumer".

Typical use cases involve more than one "scenario". Furthermore, it makes no
sense to continue a "scenario" in case the "consumer" behaves unexpectedly.

It follows, that a "scenario" contains the following information:

1. **Version:** An integer defining how to decode information.
2. **TimeSpan:** Time span between sending the result of a scenario till the
   (expected) arrival time of the next "scenario". Here the Konnektor uses this
   information to detect a timeout. The special value zero in a "scenario"
   indicates that this is the last "scenario" in a sequence.
3. **List:** A list with zero, one or more elements of the following types:
   1. **ExpectedStatusWords (ESW)**: a list of expected status words, in case a
      smartcard returns a response APDU where the status word of that response
      APDU is not in the list of the expected status words it makes no sense to
      continue the "scenario".
   2. **CommandAPDU:** an octet string with an ISO/IEC 7816-4 command APDU.
   3. **LoggingInformation:** an object with the following attributes:
      1. **LogLevel:** an integer representation of a [log level][].
      2. **LogMessage:** an [UTF-8][] string.

For security reasons a "scenario" is signed by a "producer" (here the 
PoPP-Service). Thus, before signing a "scenario" has to be serialized.

<details>
  <summary>Version specific serialization</summary>
  <ol>
    <li><a href="#version-0">Version 0</a></li>
  </ol>
</details>

A "scenario" together with its signature and the X.509 certificate with the
public signature verification key is encoded into an [RFC 5652][] structure,
where the serialized "scenario" is the signed content.

## Version 0

### Serialization of a scenario

For version 0 a "scenario" is an [ASN.1][] structure and uses [DER][] for
encoding and decoding. Hereafter the serialized form is specified:

1. A "scenario" **SHALL** be a DER SEQUENCE data object with tag 0x30 = '30'
   where the sequence consists of three elements.
   1. The first element **SHALL** be a DER INTEGER data object with tag 0x02 =
      '02' encoding the version number.
   2. The second element **SHALL** be a DER INTEGER data object with tag 0x02 =
      '02' encoding the time span in milliseconds.
   3. The third element **SHALL** be a DER SEQUENCE data object with tag 0x30 =
      '30' where the sequence contains zero, one or more elements of a _list_.
   4. That _list_ **SHALL NOT** contain elements with tags not element of
      {'04', '30', '31'}.
   5. The first element in _list_ (if present) **SHALL** be a data object with
      tag 0x30 = '30' (expected status words).
   6. The elements in _list_ **SHALL** be encoded and interpreted as follows:
      1. DER SEQUENCE data object with tag 0x30 = '30' where the sequence
         consists of one or more elements of DER INTEGER data objects with tag
         0x02 = '02' encoding an expected status word.
      2. DER OCTETSTRING data object with tag 0x04 = '04' where the value-field
         contains an ISO/IEC 7816-4 command APDU.
      3. DER SET data object with tag 0x31 = '31' with the following children:
         - DER INTEGER data object with tag 0x02 = '02' with a [log level][]
         - DER UTF8String data object with tag 0x0c = '0c' with a log message
2. The "consumer" of a "scenario" **MAY** use the information from a SET data
   object with tag 0x31 = '31' within _list_ for logging information.
3. The "consumer" of a "scenario" **MAY** completely ignore SET data objects
   with tag 0x31 = '30' from the _list_ in a "scenario".

**Example 1**: Some commands, positive time span indicating this is not the last
"scenario" in a sequence.

```
Version  = 0  
TimeSpan = 1000 ms  
list = {
  expectedStatusWords: {'9000' = NoError, '6a81' = CorruptDataWarning}
  loggingInformation:  {INFO, "Select MF"}
  commandApdu: '00 a4 040c' = SELECT MF, see gemSpec_COS (N040.800)
  loggingInformation:  {DEBUG, "read EF.GDO"}
  commandApdu. '00 b0 8200 00' = READ BINARY, shortFileIdentifier=2, offset=0, Ne<=256
  loggingInformation:  {DEBUG, "read EF.ATR"}
  commandApdu. '00 b0 9d00 00' = READ BINARY, shortFileIdentifier=2, offset=0, Ne<=256
}
```

_**Note:** Non-hexadecimal characters in the following output and line feeds are
shown only for better reading. Everything after a #-character explains the line._

```
30 5c                                 # SEQUENCE with 3 elements
|  02 01 00                           #     INTEGER := 0
|  02 02 03e8                         #     INTEGER := 1000
|  30 53                              #     SEQUENCE with 7 elements
|  |  30 09                           #         SEQUENCE with 2 elements
|  |  |  02 03 009000                 #             INTEGER := 36864
|  |  |  02 02 6281                   #             INTEGER := 25217
|  |  31 0e                           #         SET with 2 elements
|  |  |  02 01 14                     #             INTEGER := 20
|  |  |  0c 09 53656c656374204d46     #             UTF8String := "Select MF"
|  |  04 04 00a4040c                  #         OCTETSTRING with 1st command APDU
|  |  31 10                           #         SET with 2 elements
|  |  |  02 01 0a                     #             INTEGER := 10
|  |  |  0c 0b 726561642045462e47444f #             UTF8String := "read EF.GDO"
|  |  04 05 00b0820000                #         OCTETSTRING with 2nd command APDU
|  |  31 10                           #         SET with 2 elements
|  |  |  02 01 0a                     #             INTEGER := 10
|  |  |  0c 0b 726561642045462e415452 #             UTF8String := "read EF.ATR"
|  |  04 05 00b09d0000                #         OCTETSTRING with 3rd command APDU
```

**Example 2:** Empty "scenario" with a zero time span indicating, that this is
the last "scenario" of a sequence:

```
Version  = 0  
TimeSpan = 0 ms  
list = {}
```

_**Note:** Non-hexadecimal characters in the following output and line feeds are
shown only for better reading. Everything after a #-character explains the line._

```
30 08       # SEQUENCE with 3 elements
|  02 01 00 #     INTEGER := 0
|  02 01 00 #     INTEGER := 0
|  30 00    #     SEQUENCE with 0 elements
```

### Serialization of the corresponding response

For each command APDU of a "scenario" which is sent to a smartcard the smartcard
returns a corresponding response APDU. Hereafter the serialized form is
specified:

1. A collection of response APDU corresponding to a "scenario" **SHALL** be a
   DER SEQUENCE data object with tag 0x30 = '30' where the sequence consists of
   zero, one or more elements.
2. Each element in the sequence **SHALL** be a DER OCTETSTRING data object with
   tag 0x04 = '04' where the value-field contains an ISO/IEC 7816-4 response
   APDU.
3. The i-th element in the sequence **SHALL** be the response APDU corresponding
   to the i-th command APDU in the "scenario".

**Example 1:** Assuming the "scenario" from example 1 above is sent to a
smartcard and the smartcard responded with '6a82' = FileNotFound to the second
command APDU (read EF.GDO), then the corresponding response would be:

_**Note:** Because the status word of the second response APDU is not in the 
list of expected status words no further command APDU is sent to the smartcard.
Consequently, no further response APDU is present._

```
list = {
  '9000' = NoError      (select MF)
  '6a82' = FileNotFound (read EF.GDO)
}
```

_**Note:** Non-hexadecimal characters in the following output and line feeds are
shown only for better reading. Everything after a #-character explains the line._

```
30 08         # SEQUENCE with 2 elements
   04 02 9000 #     OCTETSTRING with response APDU to 1st command APDU
   04 02 6a82 #     OCTETSTRING with response APDU to 2nd command APDU
```


[ASN.1]:https://en.wikipedia.org/wiki/ASN.1
[DER]:https://en.wikipedia.org/wiki/X.690#DER_encoding
[RFC 5652]:https://datatracker.ietf.org/doc/html/rfc5652
[UTF-8]:https://en.wikipedia.org/wiki/UTF-8
[log level]:https://www.slf4j.org/api/org/apache/log4j/Level.html
