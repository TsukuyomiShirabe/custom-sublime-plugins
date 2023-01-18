# custom-sublime-plugins
Custom plugins for **Sublime Text**



### Installation

(For Windows Users)

Without further explanation, just put corresponding `*.py` script to `C:\Users\<UserName>\AppData\Roaming\Sublime Text\Packages\User`, then setup user preferences for key bindings.



## Unicode Altercross
A plugin that works similar to `Alt+X` hotkey in MS Word. Convert between characters and their Unicode hex values. 

### Installation

Add the following JSON dicts to [Preferences > Key Bindings] in **Sublime Text**:

```
    { "keys": ["alt+z"], "command": "unicode_to_char" },
    { "keys": ["alt+x"], "command": "char_to_unicode" }
```
