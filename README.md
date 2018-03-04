Tool for extracting information from IDA Free signature files.

### Command-line options

Produce description in JSON format:

```
siginfo path-to-signature > output.json
```

Produce description in legacy text format:

```
siginfo path-to-signature --text > output.txt
```

### Dependencies

#### Linux

```
pacman -S python
```

#### OS X

```
brew install python
```

#### Windows

```
scoop install python
```

### Limitations

Test tool can report false positives because accidentally `siginfo` turned out to be a little better than legacy software.

### See also

* https://github.com/JohnDMcMaster/uvudec
* https://github.com/Nukem9/SwissArmyKnife
