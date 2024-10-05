import yaml

obj = {
    "test_cases": [
        {
            "in": f"tests/{x}.in",
            "out": f"tests/{x}.out",
            "points": 0 if x == 1 else 1,
        }
        for x in range(1, 11)
    ]
}


print(yaml.safe_dump(obj, indent=2))
