
# --- begin "pretty"
#
# pretty - A miniature library that provides a Python print and stdout
# wrapper that makes colored terminal text easier to use (eg. without
# having to mess around with ANSI escape sequences). This code is public
# domain - there is no license except that you must leave this header.
#
# Copyright (C) 2008 Brian Nez <thedude at bri1 dot com>
#
# http://nezzen.net/2008/06/23/colored-text-in-python-using-ansi-escape-sequences/

def display(text, color='normal'):
    codes = {
        'black':     '0;30', 'bright gray':    '0;37',
        'blue':      '0;34', 'white':          '1;37',
        'green':     '0;32', 'bright blue':    '1;34',
        'cyan':      '0;36', 'bright green':   '1;32',
        'red':       '0;31', 'bright cyan':    '1;36',
        'purple':    '0;35', 'bright red':     '1;31',
        'yellow':    '0;33', 'bright purple':  '1;35',
        'dark gray': '1;30', 'bright yellow':  '1;33',
        'normal':    '0'
    }
    print("\033[" + codes[color]+"m" + text + "\033[0m")