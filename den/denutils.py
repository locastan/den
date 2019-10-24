from collections import Sequence
import discord


class DenUtils:
    """Basic utils."""

    def time_converter(units):
        return sum(int(x) * 60 ** i for i, x in enumerate(reversed(units.split(":"))))


    def color_lookup(color="grey"):
        colors = {"blue": 0x3366FF, "red": 0xFF0000, "green": 0x00CC33, "orange": 0xFF6600,
                  "purple": 0xA220BD, "yellow": 0xFFFF00, "teal": 0x009999, "magenta": 0xBA2586,
                  "turquoise": 0x00FFFF, "grey": 0x666666, "pink": 0xFE01D1, "white": 0xFFFFFF}
        color = colors[color]
        return color


    def fmt_join(words: Sequence, ending: str = 'or'):
        if not words:
            return ""
        elif len(words) == 1:
            return words[0]
        else:
            return '{} {} {}'.format(', '.join(map(str, words[:-1])), ending, words[-1])


    def cooldown_formatter(seconds, custom_msg="0"):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)

        if h > 0:
            msg = "{0}h"
            if m > 0 and s > 0:
                msg += ", {1}m, and {2}s"
            elif s > 0 and m == 0:
                msg += " and {2}s"
            elif s == 0 and m == 0:
                pass
            else:
                msg += " and {1}m"
        elif h == 0 and m > 0:
            msg = "{1}m" if s == 0 else "{1}m and {2}s"
        elif m == 0 and h == 0 and s > 0:
            msg = "{2}s"
        else:
            msg = custom_msg
        return msg.format(h, m, s)


    def time_formatter(seconds):
        # Calculate the time and input into a dict to plural the strings later.
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        data = PluralDict({'hour': h, 'minute': m, 'second': s})

        # Determine the remaining time.
        if h > 0:
            fmt = "{hour} hour{hour(s)}"
            if data["minute"] > 0 and data["second"] > 0:
                fmt += ", {minute} minute{minute(s)}, and {second} second{second(s)}"
            if data["second"] > 0 == data["minute"]:
                fmt += ", and {second} second{second(s)}"
            msg = fmt.format_map(data)
        elif h == 0 and m > 0:
            if data["second"] == 0:
                fmt = "{minute} minute{minute(s)}"
            else:
                fmt = "{minute} minute{minute(s)}, and {second} second{second(s)}"
            msg = fmt.format_map(data)
        elif m == 0 and h == 0 and s > 0:
            fmt = "{second} second{second(s)}"
            msg = fmt.format_map(data)
        else:
            msg = "None"
        return msg


    def build_embed(msg):
        embed = discord.Embed(colour=0xFF0000, description=msg)
        return embed