import pytest
import upiter

@pytest.mark.parametrize(
    'vals, result', [
        ((1,), (1,)),
        ((1, 2, 3), (1, 2, 3)),
        (((1, 2),), ((1, 2),)),
        (((1, 2, 3), 4), ((1, 2, 3), 4)),
        ((1, 2, (3, 4)), (1, 2, (3, 4))),
        ((1, (2, 3), 4, 5), (1, (2, 3), 4, 5)),
        ((1, (2, (3, 4), 5), 6), (1, (2, 3, 5), (2, 4, 5), 6)),
        (
            (1, (2, (3, (4, 5), 6), (7, 8)), (9, 10, (11, 12))),
            (1, (2, 3, 7), (2, 3, 8), (2, (4, 5), 7), (2, (4, 5), 8), (2, 6, 7), (2, 6, 8), (9, 10, 11), (9, 10, 12))
        ),
        ([1, [2, [3, 4], 5], 6], (1, (2, 3, 5), (2, 4, 5), 6)),
        (
            {'hoge':'abc', 'foo':[2, 'fuga']},
            (
                {'hoge':'abc', 'foo':(2, 'fuga')},
            )
        ),
        (
            (
                {'hoge':'abc', 'foo':[[2, 'fuga']]},
                {'hoge':'xyz', 'bar':'piyo'},
            ), (
                {'hoge':'abc', 'foo':(2, 'fuga')},
                {'hoge':'xyz', 'bar':'piyo'},
            )
        ),
    ]
)
def test_union_product(vals, result):
    assert tuple(upiter.union_product(vals)) == result


@pytest.mark.parametrize(
    'vals, result', [
        ((1,), ((1,),)),
        ((1, 2, 3), ((1, 2, 3),)),
        (((1, 2),), ((1,), (2,))),
        (((1, 2, 3), 4), ((1, 4), (2, 4), (3, 4))),
        ((1, 2, (3, 4)), ((1, 2, 3), (1, 2, 4))),
        ((1, (2, 3), 4, 5), ((1, 2, 4, 5), (1, 3, 4, 5))),
        ((1, (2, (3, 4), 5), 6), ((1, 2, 6), (1, (3, 4), 6), (1, 5, 6))),
        (
            (1, (2, (3, (4, 5), 6), (7, 8)), (9, 10, (11, 12))),
            (
                (1, 2, 9), (1, 2, 10), (1, 2, (11, 12)),
                (1, (3, 4, 6), 9), (1, (3, 4, 6), 10), (1, (3, 4, 6), (11, 12)),
                (1, (3, 5, 6), 9), (1, (3, 5, 6), 10), (1, (3, 5, 6), (11, 12)),
                (1, (7, 8), 9), (1, (7, 8), 10), (1, (7, 8), (11, 12)),
            )
        ),
        ([1, [2, [3, 4], 5], 6], ((1, 2, 6), (1, (3, 4), 6), (1, 5, 6))),
        (
            ['abc', (1, [2, 'fuga'], (4, 5)), ['piyopiyo', 'puyo']],
            (
                ('abc', 1, 'piyopiyo'),
                ('abc', 1, 'puyo'),
                ('abc', (2, 'fuga'), 'piyopiyo'),
                ('abc', (2, 'fuga'), 'puyo'),
                ('abc', (4, 5), 'piyopiyo'),
                ('abc', (4, 5), 'puyo'),
            )
        ),
        (
            {'hoge':'abc', 'foo':[[1, [[2, 'fuga']], 4]], 'bar': 'puyo'},
            (
                {'hoge':'abc', 'foo':(1, (2, 'fuga'), 4), 'bar': 'puyo'},
            )
        ),
        (
            {'hoge':'abc', 'foo':(1, [2, 'fuga'], (4, 5)), 'bar': ['piyopiyo', 'puyo']},
            (
                {'hoge':'abc', 'foo':1, 'bar':'piyopiyo'},
                {'hoge':'abc', 'foo':1, 'bar':'puyo'},
                {'hoge':'abc', 'foo':(2, 'fuga'), 'bar':'piyopiyo'},
                {'hoge':'abc', 'foo':(2, 'fuga'), 'bar':'puyo'},
                {'hoge':'abc', 'foo':(4, 5), 'bar':'piyopiyo'},
                {'hoge':'abc', 'foo':(4, 5), 'bar':'puyo'},
            )
        ),
    ]
)
def test_product_union(vals, result):
    assert tuple(upiter.product_union(vals)) == result
