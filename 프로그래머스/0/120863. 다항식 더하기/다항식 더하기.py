def solution(polynomial):
    terms = polynomial.split(" + ")
    intResult = 0
    xResult = 0

    for t in terms:
        if "x" in t:
            xResult += 1 if t == "x" else int(t[:-1])
        else:
            intResult += int(t)

    # 둘 다 0이면 "0"
    if xResult == 0 and intResult == 0:
        return "0"

    result = []
    if xResult:
        result.append("x" if xResult == 1 else str(xResult) + "x")
    if intResult:
        result.append(str(intResult))

    return " + ".join(result)
