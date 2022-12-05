"""
    the hanged man for difficulty hard
"""
e_lives = {
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


m_lives = {
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
     .               *         | '     / \      '         .
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

h_lives = {
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
