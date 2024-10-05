import yaml

obj = {
    "archive": "archive.zip",
    "checker": "checker.py",
    "test_cases": [
        {
            "in": f"{x}.in",
            "out": f"{x}.out",
            "points": 0 if x == 1 else 1,
        }
        for x in range(1, 21)
    ]
}


print(yaml.safe_dump(obj, indent=2))