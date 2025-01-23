def load_data(path):
    activities = []
    with open(path) as fs:
        for line in fs:
            if line:
                a = line.strip().split(",")
                activities.append((float(a[0]),float(a[1])))
    return activities


def asp(a):
    """Computes the optimal solution to the Activity Selection Problem
    (ASP) with activities a as input.
    
    The input is a list of activities each defined as a tuple (s,f)
    containing starting and finish times as floats.
    """
    sorted(a, key=lambda a: a[1])
    return []

def main():
    path = "asp_data.txt"
    activities = load_data(path)
    solution = asp(activities)
    print(solution)

if __name__ == "__main__":
    main()