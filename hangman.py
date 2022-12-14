"""
The hanged man art for each difficulty
"""
__E_LIVES__ = {
    5:  """
        *          o           .       +         .        *
     .                   ~+         *     +    |   '        .
        .   |       *      .    '      .     - o -       +
     +    - o -                   +       .    |      .
            |      .   '                     o             '
       +       ~+           *        .    *       +    *
     .               *           '      .       '         .
            '              +     *         .   ~~+     .    *
      *           o         .          *             o
     '    +    '       *       +   o       *     .      +
    __________________________________________________________
        """,
    4:  r"""
        *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .    *       +    *
     .               *         | '      .       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    3:  r"""
        *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '      .       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    2:  r"""
        *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /.\      '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    1:  r"""
        *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /|\      '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    0:  r"""
        *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /|\      '         .
            '              +   | *     / \ .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """
}


__M_LIVES__ = {
    7:  r"""
        *          o           .       +         .        *
     .                   ~+         *     +    |   '        .
        .   |       *      .    '      .     - o -       +
     +    - o -                   +       .    |      .
            |      .   '                     o             '
       +       ~+           *        .    *       +    *
     .               *           '      .       '         .
            '              +     *         .   ~~+     .    *
      *           o         .          *             o
     '    +    '       *       +   o       *     .      +
    __________________________________________________________
        """,
    6:  r"""
        *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .    *       +    *
     .               *         | '      .       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    5:  r"""
        *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '      .       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    4:  r"""
        *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /.       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    3:  r"""
        *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /.\      '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    2:  r"""
        *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /|\      '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    1:  r"""
        *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /|\      '         .
            '              +   | *     /   .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    0:  r"""
        *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /|\      '         .
            '              +   | *     / \ .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """
}

__H_LIVES__ = {
    10: r"""
       *          o           .       +         .        *
     .                   ~+         *     +    |   '        .
        .   |       *      .    '      .     - o -       +
     +    - o -                   +       .    |      .
            |      .   '                     o             '
       +       ~+           *        .    *       +    *
     .               *           '      .       '         .
            '              +     *         .   ~~+     .    *
      *           o         .          *             o
     '    +    '       *       +   o       *     .      +
    __________________________________________________________
        """,
    9: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .     - o -       +
     +    - o -                |  +       .    |      .
            |      .   '       |             o             '
       +       ~+           *  |     .    *       +    *
     .               *         | '      .       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    8: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +       .    |      .
            |      .   '       |             o             '
       +       ~+           *  |     .    *       +    *
     .               *         | '      .       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    7: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |             o             '
       +       ~+           *  |     .    *       +    *
     .               *         | '      .       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    6: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .    *       +    *
     .               *         | '      .       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    5: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '      .       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    4: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /.       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    3: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /.\      '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    2: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /|\      '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    1: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /|\      '         .
            '              +   | *     /   .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    0: r"""
        *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /|\      '         .
            '              +   | *     / \ .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """
}

__S_LIVES__ = {
    11: r"""
       *          o           .       +         .        *
     .                   ~+         *     +    |   '        .
        .   |       *      .    '      .     - o -       +
     +    - o -                   +       .    |      .
            |      .   '                     o             '
       +       ~+           *        .    *       +    *
     .               *           '      .       '         .
            '              +     *         .   ~~+     .    *
      *           o         .          *             o
     '    +    '       *       +   o       *     .      +
    __________________________________________________________
        """,
    10: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .     - o -       +
     +    - o -                |  +       .    |      .
            |      .   '       |             o             '
       +       ~+           *  |     .    *       +    *
     .               *         | '      .       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    9: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +       .    |      .
            |      .   '       |             o             '
       +       ~+           *  |     .    *       +    *
     .               *         | '      .       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    8: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |             o             '
       +       ~+           *  |     .    *       +    *
     .               *         | '      .       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    7: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .    *       +    *
     .               *         | '      .       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    6: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '      .       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    5: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /.       '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    4: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /.\      '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    3: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /|\      '         .
            '              +   | *         .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    2: r"""
       *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /|\      '         .
            '              +   | *     /   .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    1: r"""
        *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O *       +    *
     .               *         | '     /|\      '         .
            '              +   | *     / \ .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """,
    0: r"""
        *          o           .       +         .        *
     .                   ~+    __________ +    |   '        .
        .   |       *      .   |/      .|    - o -       +
     +    - o -                |  +     | .    |      .
            |      .   '       |        |    o             '
       +       ~+           *  |     .  O */      +    *
     .               *         | '     /|\/     '         .
            '              +   | *     / \ .   ~~+     .    *
      *           o         .  |       *             o
     '    +    '       *       |   o       *     .      +
    __________________________/|\_____________________________
        """
}
