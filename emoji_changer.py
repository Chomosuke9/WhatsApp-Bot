import emoji

emoji_to_symbol = {
    "😀": " :D ",
    "😁": " :D ",
    "😂": " ^_^ ",
    "😃": " :) ",
    "😄": " :) ",
    "😅": " ^-^ ",
    "😆": " XD ",
    "😉": " ;) ",
    "😊": " ^^ ",
    "😋": " :P ",
    "😍": " ^_^ ",
    "😘": " :* ",
    "😗": " :* ",
    "😙": " :* ",
    "😚": " :* ",
    "🙂": " :-) ",
    "🤗": " (>_<) ",
    "🤩": " ^-^ ",
    "🥰": " ^_^ ",
    "😏": " :-] ",
    "😐": " :-| ",
    "😑": " -_- ",
    "😒": " :-/ ",
    "🙄": " (._.) ",
    "😬": " D: ",
    "🤔": " (._.?) ",
    "😴": " (-.-)Zzz ",
    "😌": " (^_^) ",
    "😛": " :P ",
    "😜": " ;P ",
    "😝": " XP ",
    "🤤": " *_* ",
    "😪": " (>_<) ",
    "😢": " ;_; ",
    "😭": " T_T ",
    "🥺": " (T_T) ",
    "😨": " (O_O) ",
    "😰": " :-O ",
    "😥": " ;_; ",
    "😱": " (O_O) ",
    "😲": " O_O ",
    "🥵": " (>_<) ",
    "🥶": " (>_<) ",
    "😇": " O:) "
}


def remove_emoji(text):
    try:
        return emoji.replace_emoji(text, "")
    except:
        return "error"
def replace_emoji_with_symbol(text):
    try:
        for emoji, symbol in emoji_to_symbol.items():
            text = text.replace(emoji, symbol)
        return remove_emoji(text)
    except:
        return "error"

