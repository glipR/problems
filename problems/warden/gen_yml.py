import yaml

obj = {
    "custom_judge": "grader.py",
    "test_cases": [
        {
            "in": f"tests/{x}.in",
            "out": f"tests/{x}.out",
            "points": 1,
        }
        for x in range(1, 16)
    ]
}


print(yaml.safe_dump(obj, indent=2))
