import yaml

obj = {
    "custom_judge": "grader.py",
    "test_cases": [
        {
            "in": "tests/1.in",
            "out": "tests/1.in",
            "points": 1,
        }
    ]
}


print(yaml.safe_dump(obj, indent=2))
