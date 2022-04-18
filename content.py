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
        'def': 'Two cells in the same house with exact the same two candidates.',
        'usage': 'Remove these two candidates in other cells in the same house.',
        'button_text': 'Next',
        'button_href': '/learn/2',
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
    {
        'title': 'Hidden pair',
        'def': 'A Hidden Pair is basically just a "buried" Naked Pair. It occurs when two candidates appear in exactly two cells within the same house.',
        'usage': 'Erase all the other candidates in the two cells.',
        'button_text': 'Next',
        'button_href': '/learn/3',
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
        'title': 'X-wing',
        'def': 'A row (column) that contains the same candidate in exactly two spots, as well as another parallel row (column) that mirrors it — containing the same candidate which forms a rectangle with the previous 2 spots.',
        'usage': 'Eliminate similar pencil marks in the columns (rows) passing through those spots',
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
