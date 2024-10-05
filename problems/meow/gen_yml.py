import yaml

obj = {
    "archive": "archive.zip",
    "test_cases": [
        {
            "in": f"{x}.in",
            "out": f"{x}.out",
            "points": 0 if x == 1 else 1,
        }
        for x in range(1, 7)
    ]
}


print(yaml.safe_dump(obj, indent=2))