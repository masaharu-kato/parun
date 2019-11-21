def Args(pargs:list=[], kwargs:dict={}): pass
def Union(*args): pass
def Product(*args): pass
def Format(text:str): pass

data_list = {
    "pargs01": Args([
        "hoge",
        "fuga"
    ]),
    "pargs02": Union(
        Args([
            "hoge",
            "fuga01"
        ]),
        Args([
            "hoge",
            "fuga02"
        ])
    ),
    "pargs03": Args([
        "hoge",
        Union("fuga01", "fuga02")
    ]),
    "pargs04": Args([
        "hoge",
        Union(Product("fuga01", "fuga02"), "fuga03")
    ]),
    "pargs05": Args([
        Union("hogeA", "hogeB"),
        Union(Product("fuga01", "fuga02"))
    ]),
    "kwargs01": Args([], {
        "-pa": 45,
        "-pb": -2.67
    }),
    "kwargs02a": Union(
        Args([], {"-pa": 45, "-pb": -2.67}),
        Args([], {"-pa": 45, "-pb": 4.33})
    ),
    "kwargs02b": Args([], {
        "-pa": 45,
        "-pb": Union(-2.67, 4.33)
    }),
    "kwargs03": Args([], {
        "-pa": 45,
        "-pb": Union(-2.67, 4.33),
        "-pc": Union("hoge", "fugga", "piyopiyo")
    }),
    "kwargs04": Union(Product(
        Args([], {
            "-pa": 143,
            "-pb": -64.245
        }), Union(
            Args([], {"-color": "orange", "-order": "second"}),
            Args([], {"-color": "blue", "-order": "thrid", "-n": 180}),
            Args([], {"-n": 250}),
            Args([], {"-pb": 0, "-order": "first"}),
            Args([], {})
        )
    )),
    "kwargs05": Union(Product(
        Args([], { "-pa": 120, "-pb": -20}),
        Union(Args([], {"-pc1": 41}), Args([], {"-pc2": 42})),
        Union(Args([], {"-pd1": "foo1", "-pd2": "foo2", "-pd3": "foo3"}))
    )),
    "kwargs06": Args([], {
        "-cval": 25,
        "-pa": 156,
        "-pb": 424.18,
        "--color": Union("orange", "red", "blue", "green"),
        "-n": Union(100, 120),
        ">": Format("out/n{-n}_{-color}.json")
    }),
    "kwargs07a": Args([], {
        "-pa": 90,
        "-cols": Union(Product("orange", "red", "blue", "green")),
        "-n": Union(100, 200)
    }),
    "kwargs07b": Args([], {
        "-pa": 90,
        "-cols": "orange red",
        "-n": Union(100, 200)
    }),
    "kwargs08": Args([], {
        "-pa": 90,
        "-cols": Union(Product("orange", "red"), Product("ocean blue", "natural green 2", "yellow")),
        "--indexes": Union(0, Product(2, 5, 4), Product(-4, 0, Union(1, 2), 13))
    }),
    "pkwargs01": Args([
        Union("hoge", "fuga"),
        "foobar"
    ], {
        "-pa": 156,
        "-n": Union(100, 120),
        ">": Format("out/n{-n}_{$1}_{$2}.json")
    }),
    "allargs01": Args([
        Format("input_n{-n:>03}.bin")
    ], {
        "-cval": 35,
        "-opt1": None,
        "-opt2": None,
        "-pa": 156,
        "-pb": 424.18,
        "-color": Union("red", "blue"),
        "-order": Union("first", "second", "third"),
        "-n": Union(50, 100),
        ">": Format("out/n{-n:>03}_{-color}_{-order}.json")
    })
}