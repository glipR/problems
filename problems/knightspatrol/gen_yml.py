import yaml

obj = {
    "checker": "checker.py",
    "test_cases": [
        {
            "in": "tests/1.in",
            "out": "tests/1.in",
            "points": 1,
        }
    ]
}


print(yaml.safe_dump(obj, indent=2))
