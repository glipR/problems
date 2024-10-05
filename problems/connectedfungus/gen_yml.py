import yaml

obj = {
    "archive": "archive.zip",
    "test_cases": [
        {
            "in": f"{x}.in",
            "out": f"{x}.out",
            "points": 1 if x != 1 else 0,
        }
        for x in range(1, 12)
    ]
}


print(yaml.safe_dump(obj, indent=2))