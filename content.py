home_data = {
    'title': 'Learn Sudoku techniques!',
    'objective': 'In classic Sudoku, the objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 subgrids that compose the grid contain all of the digits from 1 to 9.',
    'terms': [
        ('Cell', 'single box in the grid'),
        ('House', '3 × 3 subgrid or a row or a column'),
        ('Candidate', 'possible digits to fill this cell, if there is only one candidate for a cell, then this candidate is the correct answer')
    ],
    'img_url': 'https://www.learn-sudoku.com/images/sample_puzzle_half.gif',
    'patterns': ['Naked pair', 'Hidden pair', 'X-wing']
}
learns_data = [
    {
        'title': 'Naked pair',
        'def': 'Two cells in the same house <b>with and only with</b> the same 2 candidates.',
        'usage': 'Remove these 2 candidates in <b>other cells in the same house</b>.',
        'why': """Two cells in the same house only have the same 2 candidates &rarr;<br>
                  These 2 candidates have to be in these 2 cells &rarr;<br>
                  Other cells cannot have these 2 candidates, so remove them.""",
        'button_text': 'Next',
        'button_href': '/learn/2/1',
        'slides': [
            {
                'img_url': 'https://www.learn-sudoku.com/images/naked_pair1.gif',
                'title': 'The initial state',
                'description': ''
            },
            {
                'img_url': 'https://pic.imgdb.cn/item/625c9b16239250f7c500bc3d.png',
                'title': 'Find Naked Pair',
                'description': 'The two green cells have exactly two candidates: 2 & 3. So, remove all 2 and 3 in other cells (pink ones).'
            },
            {
                'img_url': 'https://pic.imgdb.cn/item/625c9b16239250f7c500bc38.png',
                'title': 'After removing',
                'description': ''
            }
        ]
    },

    [
        {
            'title': 'Hidden pair',
            'def': 'A Hidden Pair is basically just a "buried" Naked Pair. It occurs when two candidates <b>appear and only appear</b> in two cells within the same house.',
            'usage': 'Erase all the other candidates in the two cells.',
            'why': """
                The two candidates only appear in two cells in the same house &rarr;<br>
                These 2 candidates have to be in these 2 cells &rarr;<br>
                Other candidates in these two cells can be removed.<br><br>
                """,
            'button_text': 'Continue',
            'button_href': '/learn/2/2',
            'slides': [
                {
                    'img_url': 'https://pic.imgdb.cn/item/625ca084239250f7c505c7ab.png',
                    'title': 'The initial state',
                    'description': ''
                },
                {
                    'img_url': 'https://pic.imgdb.cn/item/625ca084239250f7c505c7af.png',
                    'title': 'Find Hidden Pair',
                    'description': 'The two green cells are the only two that contain 6 & 9. So, erase all the other pencil marks (pink ones) in the green cells'
                },
                {
                    'img_url': 'https://pic.imgdb.cn/item/625ca084239250f7c505c7b4.png',
                    'title': 'After erasing',
                    'description': ''
                }
            ]
        },
        {
            'title': 'Hidden pair',
            'text': """
                If we put Naked pair and Hidden pair together, we can conclude that:<br>
                Within the same house, <br>if <b>2 cells only have the same 2 candidates (naked pair)</b> or <b>the 2 candidates only appear in 2 cells (hidden pair)</b>, <br>then these 2 candidates have to be in these 2 cells, <br>so we can remove <b>these 2 candidates in other cells</b> or <b>other candidates in these two cells</b><br>
                <b>Actually, when the number 2 extend to 3 or more, the strategy still holds!</b>
            """,
            'button_text': 'Next',
            'button_href': '/learn/3',
            'imgs': [
                {
                    'img_url': 'https://pic.imgdb.cn/item/625c9b16239250f7c500bc3d.png',
                    'description': 'Naked Pair'
                },
                {
                    'img_url': 'https://pic.imgdb.cn/item/625ca084239250f7c505c7af.png',
                    'description': 'Hidden Pair'
                },
            ]
        }
    ],

    {
        'title': 'X-wing',
        'def': 'A row (column) that contains the same candidate in and only in two spots, as well as another parallel row (column) that mirrors it — containing the same candidate which <b>forms a rectangle with the previous 2 spots</b>.',
        'usage': 'Eliminate the candidates in the columns (rows) passing through the 4 vertices of the rectangle',
        'why': """
            The candidate only appears at the 4 vertices of the rectangle in the two rows (columns). &rarr;<br>
            This number must be at a diagonal of the rectangle (or it will violate the rule). &rarr;<br>
            The candidate in other cells of these two columns (rows) can be removed.
        """,
        'button_text': 'Take quiz',
        'button_href': '/quiz',
        'slides': [
            {
                'img_url': 'https://pic.imgdb.cn/item/625cbd82239250f7c5299c54.png',
                'title': 'Find X-wing',
                'description': 'There are two parallel rows both containing exactly two 4s which together form a rectangle.'
            },
            {
                'img_url': 'https://pic.imgdb.cn/item/625cbd82239250f7c5299c59.png',
                'title': 'Remove candidates',
                'description': 'All other 4s in the columns are can be erased (pink ones).'
            },
            {
                'img_url': 'https://pic.imgdb.cn/item/625cbd82239250f7c5299c5d.png',
                'title': 'After removal',
                'description': ''
            }
        ]
    }
]
