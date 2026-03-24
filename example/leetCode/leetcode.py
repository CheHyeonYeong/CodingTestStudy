from copy import deepcopy


class Solution:
    def solve(self, value: int) -> int:
        return value


if __name__ == "__main__":
    # 제출 전에는 아래 블록을 제거하세요.
    method_name = "solve"
    test_cases = [
        {"args": (1,), "expected": 1},
        {"args": (7,), "expected": 7},
    ]

    solver = Solution()
    method = getattr(solver, method_name)

    for index, case in enumerate(test_cases, start=1):
        args = deepcopy(case.get("args", ()))
        kwargs = deepcopy(case.get("kwargs", {}))
        expected = case["expected"]
        result = method(*args, **kwargs)
        passed = result == expected

        print(f"[case {index}] {'PASS' if passed else 'FAIL'}")
        print(f"args     = {args}")
        print(f"kwargs   = {kwargs}")
        print(f"expected = {expected}")
        print(f"result   = {result}")
        print()
