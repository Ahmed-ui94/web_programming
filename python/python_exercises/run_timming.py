def run_timing():
    run_time = 0
    number = 0
    while True:
        time1 = input("Enter 10km rum time: ")
        if not time1:

            break

        run_time += float(time1)
        number += 1
    s = run_time / number
    print(f"Average of {s} over {number} runs")


run_timing()
