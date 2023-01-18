# custom-sublime-plugins
Custom plugins for **Sublime Text**

## Unicode Altercross
A plugin that works similar to Alt+X hotkey in MS Word.
Add the following JSON dicts to [Preferences > Key Bindings] in **Sublime Text**:
```
    { "keys": ["alt+z"], "command": "unicode_to_char" },
    { "keys": ["alt+x"], "command": "char_to_unicode" }
```
