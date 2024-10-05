import yaml

obj = {
    "archive": "archive.zip",
    "custom_judge": "grader.py",
    "unbuffered": True,
    "test_cases": [
        {
            "in": f"{x}.in",
            "out": f"{x}.out",
            "points": 0 if x == 1 else 1,
        }
        for x in range(1, 26)
    ]
}


print(yaml.safe_dump(obj, indent=2))