# Cryptanalysis Module
This program is intended to take in a file containing text as input, process the contents, and provide useful information to aid in cryptanalysis. The following are features that have been or are intended to be added.

## Intended Features Overview
### Information features
- **Print Output** - Upon completion the program will provide the option to create a text file of the results which can be saved.
- **Plaintext Checker** - The program is equipped with an english dictionary which it will use to check the initial input as well as the result of any bruteforce or decryption attempts.
- **Alphabet Identification** - The program will identify characters in the text and provide information on which alphabets these fall into.
- **Unique Character Identification** - The program will identify unique characters in the text and provide both a total number and list of these characters.
- **Letter Frequency Analysis** - Will provide information on the frequency of characters in the text which can be used to identify/rule out monoalphabetic substitution cyphers.
- **Frequency Comparison** - Will compare frequency of characters to frequncy in plain english.
- **Kasiski Examination** - Will identify repeated patterns in the text to attempt key length calculation in polyalphabetic substitution cyphers.
### Decryption features
- **Frequency Based Decryption** - The program will attempt to use the results of the frequency analysis to perform a monoalphabetic substitution on a small portion of the text (Or the whole text if the input is small).
- **Ceaser Cypher Bruteforce** - The program will attempt a bruteforce operation using the ceaser cypher with all 26 variations (or until plain english is found).

## Stretch Features
These features are not guaranteed to be added but may be worked on at some point.
- **Alternative Output Types**
    - md file outputs
    - Pdf outputs
- **Alternative Input Methods**
    - Other file types (such as word)
    - Image recognition
- **Additional Language Support**
    - Adding additional dictionaries
    - Adding additional language letter frequencies
    - Language Identification feature