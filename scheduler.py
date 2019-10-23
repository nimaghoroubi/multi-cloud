import tasks


def somethingFunction(problem_id, parameters):
    if problem_id == "1":
        print('parameters: ', parameters)
        S = parameters["S"]
        K = parameters["K"]
        T = parameters["T"]
        r = parameters["r"]
        sig = parameters["sig"]
        print("S: ", S)
        return tasks.problem1(S, K, T, r, sig)
