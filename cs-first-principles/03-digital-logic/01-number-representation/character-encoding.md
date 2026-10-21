# Character Encoding

> **Layer:** [03 Digital Logic](../README.md) › [Number Representation](README.md)
> **Builds on:** [Binary and Positional Notation](binary-and-positional-notation.md), [Functions and Cardinality](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md)
> **Enables:** [Lexing and Parsing](../../06-programming-languages/03-compilers/lexing-and-parsing.md), [String Matching](../../05-algorithms-and-data-structures/06-string-algorithms/string-matching.md), [HTTP and the Web](../../08-networking/05-application-layer/http-and-the-web.md), [Web Security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md)

## Essence

Text is stored by mapping characters to numbers and numbers to bytes. That takes two separate decisions: a *character set* that assigns each abstract character a number (a code point), and an *encoding* that turns code points into byte sequences. For decades each language region had its own incompatible sets, so text moved between systems turned into garbage. Unicode replaced them with one code space for all of the world's writing systems, and Unicode Transformation Format 8-bit (UTF-8) became the dominant encoding because it is backward compatible with the American Standard Code for Information Interchange (ASCII), compact for Latin text and safe to process byte by byte. What remains hard is that a "character" as users see it may be several code points, so length, comparison and slicing of text are subtler than they look.

## Core tenets

1. **Characters, code points and bytes are three different things.** A character is an abstract unit of writing (the letter "é"). A code point is the number assigned to it (U+00E9). An encoding defines the bytes that store it (`C3 A9` in UTF-8, `E9 00` in UTF-16 little-endian). Bugs arise when code confuses these layers, for example by treating a byte count as a character count.

2. **ASCII fixed the first 128 code points, and everyone kept them.** ASCII (standardised in 1963) uses 7 bits for English letters, digits, punctuation and control codes such as newline. Its layout encodes structure: upper and lower case letters differ by one bit (`0x20`). Its 128 values are the common subset of nearly every later encoding, which is why plain English text usually survives encoding mix-ups.

3. **Unicode is one code space for all scripts.** Unicode assigns code points from U+0000 to U+10FFFF, about 1.1 million slots, of which about 155,000 were assigned to characters as of Unicode 16.0 (2024), with more added each year. It separates *what* a character is from *how it looks* (glyphs are the font's job). The first 65,536 code points form the Basic Multilingual Plane; emoji and many historic scripts lie above it.

4. **UTF-8 encodes each code point in 1 to 4 bytes with a self-describing pattern.** Code points below 128 use one byte identical to ASCII. Others use a lead byte (`110xxxxx`, `1110xxxx` or `11110xxx`) announcing the length, followed by continuation bytes (`10xxxxxx`). Consequences: any ASCII file is valid UTF-8; a byte below 128 never appears inside a multi-byte character, so searching for `/` or a zero (NUL) byte is safe; a decoder dropped into the middle of a stream can resynchronise at the next lead byte; and byte order never matters. Ken Thompson and Rob Pike designed it in 1992.

5. **UTF-16 is not fixed-width either.** UTF-16 uses 2 bytes for code points in the Basic Multilingual Plane and a 4-byte surrogate pair for the rest. Systems designed when Unicode was expected to fit in 16 bits (Java, JavaScript, Windows) adopted it, and they expose "characters" that are really 16-bit code units, so an emoji can have length 2. Only UTF-32 is fixed-width per code point, at four bytes each.

6. **What a user sees as one character can be many code points.** "é" can be one code point (U+00E9) or two ("e" plus combining acute accent U+0301). A family emoji can be seven code points joined by zero-width joiners. The user-perceived unit is a grapheme cluster. Correct cursor movement, truncation and length limits must operate on grapheme clusters, not bytes or code points.

7. **Equal-looking strings need normalisation before comparison.** Because the same text has several code point sequences, Unicode defines normalisation forms (such as Normalization Form C (NFC), which composes, and Normalization Form D (NFD), which decomposes) that map equivalent sequences to a canonical one. Comparing, hashing or indexing without normalising treats visually identical strings as different.

8. **Encoding errors are a security surface.** Decoders that accept overlong UTF-8 forms (encoding `/` in two bytes) once let attackers slip forbidden characters past filters that checked bytes before decoding. Look-alike characters from different scripts (homoglyphs) enable spoofed domain names. Interpret text in one well-defined encoding, validate it at the boundary, and normalise before making security decisions.

## Key concepts

| Term | Meaning |
|---|---|
| Character set | A mapping from characters to code points. |
| Code point | The number assigned to a character, written U+XXXX. |
| Encoding | A mapping from code points to byte sequences. |
| Code unit | The fixed-size chunk an encoding uses: 8 bits in UTF-8, 16 in UTF-16. |
| Surrogate pair | Two UTF-16 code units encoding one code point above U+FFFF. |
| Grapheme cluster | A user-perceived character, possibly several code points. |
| Normalisation | Converting equivalent code point sequences to a canonical form. |
| Byte Order Mark (BOM) | Optional leading code point U+FEFF signalling encoding and byte order. |
| Mojibake | Garbled text from decoding bytes with the wrong encoding. |

## How it fits

- **Below:** Code points are unsigned integers in [binary notation](binary-and-positional-notation.md); an encoding is an injective [function](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md) from code points to byte strings, which is what makes decoding unambiguous.
- **Above:** Source code is text, so [lexing and parsing](../../06-programming-languages/03-compilers/lexing-and-parsing.md) starts by decoding it. [String matching](../../05-algorithms-and-data-structures/06-string-algorithms/string-matching.md) and [tries and suffix structures](../../05-algorithms-and-data-structures/06-string-algorithms/tries-and-suffix-structures.md) operate on bytes or code points. Protocols declare encodings, as in [the Hypertext Transfer Protocol (HTTP) and the web](../../08-networking/05-application-layer/http-and-the-web.md), and [naming and the Domain Name System (DNS)](../../08-networking/05-application-layer/naming-and-dns.md) has to map international names onto ASCII. Encoding confusion underlies injection and spoofing in [web security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md).
- **Siblings:** Like [integers](integers-and-twos-complement.md) and [floating point](floating-point.md), it is an interpretation of bit patterns; unlike them, its unit of meaning has variable length, which makes random access costly.

## Common misconceptions

- **"Unicode is a 16-bit encoding."** Unicode is a code space up to U+10FFFF, not an encoding; UTF-8, UTF-16 and UTF-32 are its encodings.
- **"A string's length is the number of characters."** Depending on the language it may be bytes, UTF-16 code units or code points; none equals user-perceived characters in general.
- **"Plain text has no encoding."** Every byte sequence needs an encoding to be read as text; "plain text" just means the encoding was left implicit.

## Go deeper

- The Unicode Consortium, *The Unicode Standard* (version 1.0, 1991; regularly revised): the authoritative definitions, including normalisation and grapheme rules.
- Rob Pike and Ken Thompson, "Hello World or Καλημέρα κόσμε or こんにちは 世界" (1993): the design of UTF-8 as adopted in Plan 9.
- Joel Spolsky, "The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets" (2003): a short practical primer.
