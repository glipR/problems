import yaml

obj = {
    "checker": "checker.py",
    "test_cases": [
        {
            "in": "tests/1.in",
            "out": "tests/1.out",
            "points": 0,
        }
    ] + [
        {
            "in": f"tests/{x}.in",
            "out": f"tests/{x}.out",
            "points": 1,
        }
        for x in range(2, 11)
    ]
}


print(yaml.safe_dump(obj, indent=2))
