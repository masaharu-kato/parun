import pytest #type:ignore
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
            ({'hoge':'abc', 'foo':(2, 'fuga')},)
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



# @pytest.mark.parametrize(
#     'vals, result', [
#         ((1, (2, (3, 4), 5), 6), (1, (2, 3, 5), (2, 4, 5), 6)),
#         (
#             {'hoge':'abc', 'foo':[2, 'fuga']},
#             {'hoge':'abc', 'foo':(2, 'fuga')}
#         ),
#         (
#             (
#                 {'hoge':'abc', 'foo':[[2, 'fuga']]},
#                 {'hoge':'xyz', 'bar':'piyo'},
#             ), {'hoge':'xyz', 'foo':(2, 'fuga'), 'bar':'piyo'}
#         ),
#     ]
# )
# def test_union_product_with_union_dicts(vals, result):
#     assert upiter.union_product(vals, union_dicts=True) == result



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



# @pytest.mark.parametrize(
#     'vals, result', [
#         ([1, [2, [3, 4], 5], 6], ((1, 2, 6), (1, (3, 4), 6), (1, 5, 6))),
#         (
#             {'hoge':'abc', 'foo':[[1, [[2, 'fuga']], 4]], 'bar': 'puyo'},
#             ({'hoge':'abc', 'foo':(1, (2, 'fuga'), 4), 'bar': 'puyo'}, )
#         ),
#         (
#             {'hoge':'abc', 'foo':(1, [2, 'fuga'], (4, 5)), 'bar': ['piyopiyo', 'puyo']},
#             (
#                 {'hoge':'abc', 'foo':1, 'bar':'piyopiyo'},
#                 {'hoge':'abc', 'foo':1, 'bar':'puyo'},
#                 {'hoge':'abc', 'foo':(2, 'fuga'), 'bar':'piyopiyo'},
#                 {'hoge':'abc', 'foo':(2, 'fuga'), 'bar':'puyo'},
#                 {'hoge':'abc', 'foo':(4, 5), 'bar':'piyopiyo'},
#                 {'hoge':'abc', 'foo':(4, 5), 'bar':'puyo'},
#             )
#         ),
#         (
#             [
#                 {"ca": 123, "cb": (4567, -890)}, [
#                     {"additional": "here"},
#                     {"number": [0, [10, 20], 30]},
#                     {}
#                 ]
#             ],
#             (
#                 {"ca": 123, "cb": 4567, "additional": "here"},
#                 {"ca": 123, "cb": 4567, "number": 0},
#                 {"ca": 123, "cb": 4567, "number": (10, 20)},
#                 {"ca": 123, "cb": 4567, "number": 30},
#                 {"ca": 123, "cb": 4567},
#                 {"ca": 123, "cb": -890, "additional": "here"},
#                 {"ca": 123, "cb": -890, "number": 0},
#                 {"ca": 123, "cb": -890, "number": (10, 20)},
#                 {"ca": 123, "cb": -890, "number": 30},
#                 {"ca": 123, "cb": -890},
#             )
#         )
#     ]
# )
# def test_product_union_with_union_dicts(vals, result):
#     assert upiter.product_union(vals, union_dicts=True) == result



@pytest.mark.parametrize(
    'args, result', [(
            ({'hoge':'abc', 'foo':1, 'bar':'puyo'}, {'hoge':'xyzz', 'foo':42, 'bar':'poyow'}),
            {'hoge':'xyzz', 'foo':42, 'bar':'poyow'}
        ), (
            ({'hoge':'abc', 'foo':1, 'bar':'puyo'}, {'foo':42, 'bar':'poyow'}),
            {'hoge':'abc', 'foo':42, 'bar':'poyow'}
        ), (
            ({'hoge':'abc', 'foo':1, 'bar':'puyo'}, {'foo':42, 'extra':'hahaha', 'bar':'poyow'}),
            {'hoge':'abc', 'foo':42, 'bar':'poyow', 'extra':'hahaha'}
        ), (
            ({'hoge':'abc', 'foo':1, 'bar':'puyo'}, {}),
            {'hoge':'abc', 'foo':1, 'bar':'puyo'}
        ), (
            ({'hoge':'abc', 'foo':1, 'bar':'puyo'}, {'hoge2':'abc2', 'foo2':12}),
            {'hoge':'abc', 'foo':1, 'bar':'puyo', 'hoge2':'abc2', 'foo2':12}
        )
    ]
)
def test_merge_dicts(args, result):
    assert upiter.merge_dicts(*args) == result



@pytest.mark.parametrize(
    'dicts, result', [
        (
            ({'hoge':'abc', 'foo':1, 'bar':'puyo'},),
            {'hoge':'abc', 'foo':1, 'bar':'puyo'}
        ), (
            ({'hoge':'abc', 'foo':1, 'bar':'puyo'}, {'hoge':'xyzz', 'foo':42, 'bar':'poyow'}),
            {'hoge':'xyzz', 'foo':42, 'bar':'poyow'}
        ), (
            ({'hoge':'abc', 'foo':1, 'bar':'puyo'}, {'foo':42, 'bar':'poyow'}),
            {'hoge':'abc', 'foo':42, 'bar':'poyow'}
        ), (
            ({'hoge':'abc', 'foo':1, 'bar':'puyo'}, {'foo':42, 'extra':'hahaha', 'bar':'poyow'}),
            {'hoge':'abc', 'foo':42, 'bar':'poyow', 'extra':'hahaha'}
        ), (
            ({'hoge':'abc', 'foo':1, 'bar':'puyo'}, {}),
            {'hoge':'abc', 'foo':1, 'bar':'puyo'}
        ), (
            ({'hoge':'abc', 'foo':1, 'bar':'puyo'}, {'hoge2':'abc2', 'foo2':12}),
            {'hoge':'abc', 'foo':1, 'bar':'puyo', 'hoge2':'abc2', 'foo2':12}
        ), (
            (
                {'hoge':'abc', 'foo':[1, 3, 4], 'bar':'puyo'},
                {'hoge2':'abc2', 'foo':[12, 17, 26, 32]},
                {'hoge1':['abc1', 'abc2'], 'hoge2':'ABC2', 'hoge3':'xyz3'},
                {'bar':142.5, 'bar_2':285.0}
            ),
            {'hoge':'abc', 'foo':[12, 17, 26, 32], 'bar':142.5, 'hoge2':'ABC2', 'hoge1':['abc1', 'abc2'], 'hoge3':'xyz3', 'bar_2':285.0}
        ),
        # (
        #     (
        #         {'hoge':('abc',), 'foo':(1,), 'bar':'puyo'},
        #         {'hoge':'wxyz', 'foo':15, 'baz':'puga'},
        #     ),
        #     {'hoge':('abc', 'wxyz'), 'foo':(1, 15), 'bar':'puyo', 'baz':'puga'}
        # ), (
        #     (
        #         {'hoge':['abc'], 'foo':[1], 'bar':'puyo'},
        #         {'hoge':'wxyz', 'foo':[15, 25], 'baz':'puga'},
        #         {'abc':3.1416, 'foo':(23, 13, 25), 'bar':111}
        #     ),
        #     {'hoge':('abc', 'wxyz'), 'foo':(1, 15, 25, 23, 13, 25), 'bar':'puyo', 'baz':('puga', 111), 'abc':3.1416}
        # ), (
        #     (
        #         {'hoge':'abc', 'foo':(1,), 'bar':['puyo']},
        #         {'hoge':['wxyz'], 'foo':15, 'baz':('puga',)},
        #         {'abc':[[3.1416]], 'foo':((23, 13, 25),), 'baz':111}
        #     ),
        #     {'hoge':['wxyz'], 'foo':(1, 15, (23, 13, 25)), 'bar':'puyo', 'baz':('puga', 111), 'abc':[3.1416]}
        # )
    ]
)
def test_union_dicts(dicts, result):
    assert upiter.union_dicts(dicts) == result



@pytest.mark.parametrize(
    'v, result', [
        (
            {'hoge':'abc', 'foo':1, 'bar':'puyo'},
            {'hoge':'abc', 'foo':1, 'bar':'puyo'}
        ),
        (
            ({'hoge':'abc', 'foo':1, 'bar':'puyo'},),
            {'hoge':'abc', 'foo':1, 'bar':'puyo'}
        ), (
            ({'hoge':'abc', 'foo':1, 'bar':'puyo'}, {'hoge':'xyzz', 'foo':42, 'bar':'poyow'}),
            {'hoge':'xyzz', 'foo':42, 'bar':'poyow'}
        )
    ]
)
def test_to_dict(v, result):
    assert upiter.to_dict(v) == result



@pytest.mark.parametrize(
    'arg, result', [
        (25, False),
        ([], True),
        ([25], True),
        ([25, -13], True),
        ("25", False),
        (tuple(), True),
        ((25, ), True),
        ((25, -13, 34, 0), True),
        (set(), True),
        ({13, 25, 12}, True),
        (None, False),
        (True, False),
        ({}, True),
        ({'hoge':25}, True),
        (('#'+str(i) for i in range(5)), True)
    ]
)
def test_is_iterable(arg, result):
    assert upiter.is_iterable(arg) == result



@pytest.mark.parametrize(
    'arg, result', [
        (25, (25,)),
        ([], []),
        ([25, -13], [25, -13]),
        ("25", ("25",)),
        (tuple(), tuple()),
        ((25, -13, 34, 0), (25, -13, 34, 0)),
        (set(), set()),
        ({13, 25, 12}, {13, 25, 12}),
        (None, tuple()),
        (True, (True,)),
        ({}, {}),
        ({'hoge':25}, {'hoge':25})
    ]
)
def test_as_iterable(arg, result):
    assert upiter.as_iterable(arg) == result



@pytest.mark.parametrize(
    'args, result', [(
        (str, [25, -34.56, {'hoge':'HOGE', 'fuga':[423, {'foo':('bar', 12, 345)}], 'pi':3.1416}, 'something']),
        ['25', '-34.56', {'hoge':'HOGE', 'fuga':['423', {'foo':('bar', '12', '345')}], 'pi':'3.1416'}, 'something']
    )]
)
def test_any_map(args, result):
    assert [*upiter.any_map(*args)] == result

