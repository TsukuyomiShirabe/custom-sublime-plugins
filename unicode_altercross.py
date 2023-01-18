import sublime
import sublime_plugin

'''
Unicode Altercross
A plugin that works similar to Alt+X hotkey in MS Word.

Add the following JSON dicts to [Preferences > Key Bindings]
    { "keys": ["alt+z"], "command": "unicode_to_char" },
    { "keys": ["alt+x"], "command": "char_to_unicode" }
'''

def tryResolveUnicode(hex_str):
    try:
        char_str = bytes.fromhex(hex_str).decode('utf-16be')
        return True, char_str
    except:
        ...
    try:
        char_str = bytes.fromhex(hex_str).decode('utf-8')
        return True, char_str
    except:
        ...
    return False, ''


def tryResolveChar(char_str):
    try:
        hex_str = char_str.encode('utf-16be').hex().upper()
        return True, hex_str
    except:
        ...
    return False, ''


class CharToUnicodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        raw_selection_offset = self.view.sel()[0]
        start_offset, stop_offset = sorted(list(raw_selection_offset))

        if start_offset == stop_offset:
            look_behind = 4
            candidate_start_offset = max(0, stop_offset - look_behind)
            candidate_selection_offset = sublime.Region(candidate_start_offset, stop_offset)
            candidate_selection_contents = self.view.substr(candidate_selection_offset)

            is_unicode, _ = tryResolveUnicode(candidate_selection_contents)
            if not is_unicode:
                start_offset = max(0, stop_offset - 1)


        selection_offset = sublime.Region(start_offset, stop_offset)
        selection_contents = self.view.substr(selection_offset)
        is_legal, resolved_str = tryResolveChar(selection_contents)
        if is_legal:
            self.view.replace(edit, selection_offset, resolved_str)


class UnicodeToCharCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        raw_selection_offset = self.view.sel()[0]
        start_offset, stop_offset = sorted(list(raw_selection_offset))

        if start_offset == stop_offset:
            for look_behind in [4, 2]:
                candidate_start_offset = max(0, stop_offset - look_behind)
                candidate_selection_offset = sublime.Region(candidate_start_offset, stop_offset)
                candidate_selection_contents = self.view.substr(candidate_selection_offset)

                is_legal, _ = tryResolveUnicode(candidate_selection_contents)
                if is_legal:
                    start_offset = candidate_start_offset
                    break

        selection_offset = sublime.Region(start_offset, stop_offset)
        selection_contents = self.view.substr(selection_offset)
        is_legal, resolved_str = tryResolveUnicode(selection_contents)
        
        if is_legal:
            self.view.replace(edit, selection_offset, resolved_str)
