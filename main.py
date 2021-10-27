def texas_method_main():
    print("Hello friend.")
    print("This little app makes it possible to create a full week of Texas Method training.")
    print("Please give us some information about your current maxes for your intensity day\n")

    week_focus = input("Do you have a bench or press week? (b/p) ")
    print("")

    squat_reps = int(input("How many squat reps do you plan for this week? (1-5) "))
    if squat_reps == 4:
        squat_reps = 3
    squat_sets = set_counter(squat_reps)
    squat_max = float(input("What is your squat weight for this week in kg? "))
    print("")

    if week_focus == "b":
        bench_reps = int(input("How many benchpress reps do you plan for this week? (1-5) "))
        if bench_reps == 4:
            bench_reps = 3
        bench_sets = set_counter(bench_reps)
        bench_max = float(input("What is your benchpress weight for this week in kg? "))
        print("")
    else:
        press_reps = int(input("How many press reps do you plan for this week? (1-5) "))
        if press_reps == 4:
            press_reps = 3
        press_sets = set_counter(press_reps)
        press_max = float(input("What is your press weight for this week in kg? "))
        print("")

    deadlift_reps = int(input("How many deadlift reps do you plan for this week? (1-5) "))
    if deadlift_reps == 4:
        deadlift_reps = 3
    deadlift_max = float(input("What is your deadlift weight for this week in kg? "))
    print("")

    if week_focus == "b":
        press_reps = int(input("How many press reps did you do last week? (1-5) "))
        if press_reps == 4:
            press_reps = 3
        press_sets = set_counter(press_reps)
        press_max = float(input("What was your press weight last week in kg? "))
        print("")
    else:
        bench_reps = int(input("How many benchpress reps did you do last week? (1-5) "))
        if bench_reps == 4:
            bench_reps = 3
        bench_sets = set_counter(bench_reps)
        bench_max = float(input("What was your benchpress weight last week in kg? "))
        print("")

    if week_focus == "b":
        print(f"Day 1\n"
              f"Squat: 5x 5x {weight_calculations(squat_reps, squat_max)}kg\n"
              f"Benchpress: 5x 5x {weight_calculations(bench_reps, bench_max)}kg\n"
              f"Deadlift: 3x 5x {deadlift_weight_calculations(deadlift_reps, deadlift_max)}kg\n"
              f"\n"
              f"Day 2\n"
              f"Squat: 2x 5x {low_intensity_lower_body(weight_calculations(squat_reps, squat_max))}kg\n"
              f"Chinup: 3x AMRAP\n"
              f"Press: 3x 5x {low_intensity_upper_body(weight_calculations(press_reps, press_max))}kg\n"
              f"\n"
              f"Day 3\n"
              f"Squat: {squat_sets}x {squat_reps}x {squat_max}kg\n"
              f"Benchpress: {bench_sets}x {bench_reps}x {bench_max}kg\n"
              f"Deadlift: 1x {deadlift_reps}x {deadlift_max}kg\n")
    else:
        print(f"Day 1\n"
              f"Squat: 5x 5x {weight_calculations(squat_reps, squat_max)}kg\n"
              f"Press: 5x 5x {weight_calculations(press_reps, press_max)}kg\n"
              f"Deadlift: 3x 5x {deadlift_weight_calculations(deadlift_reps, deadlift_max)}kg\n"
              f"\n"
              f"Day 2\n"
              f"Squat: 2x 5x {low_intensity_lower_body(weight_calculations(squat_reps, squat_max))}kg\n"
              f"Chin-up: 3x AMRAP\n"
              f"Benchpress: 3x 5x {low_intensity_upper_body(weight_calculations(bench_reps, bench_max))}kg\n"
              f"\n"
              f"Day 3\n"
              f"Squat: {squat_sets}x {squat_reps}x {squat_max}kg\n"
              f"Press: {press_sets}x {press_reps}x {press_max}kg\n"
              f"Deadlift: 1x {deadlift_reps}x {deadlift_max}kg\n")


def weight_calculations(reps, weight):
    if reps == 5:
        volume_weight = weight * 0.9
    elif reps == 4 or reps == 3:
        volume_weight = weight * 0.85
    elif reps == 2:
        volume_weight = weight * 0.8
    else:
        volume_weight = weight * 0.775
    return my_round(volume_weight)


def deadlift_weight_calculations(reps, weight):
    if reps == 5:
        volume_weight = weight * 0.8
    elif reps == 4 or reps == 3:
        volume_weight = weight * 0.75
    elif reps == 2:
        volume_weight = weight * 0.7
    else:
        volume_weight = weight * 0.675
    return my_round(volume_weight)


def low_intensity_upper_body(volume_weight):
    low_volume_weight = volume_weight * 0.9
    return my_round(volume_weight)


def low_intensity_lower_body(volume_weight):
    low_volume_weight = volume_weight * 0.8
    return my_round(volume_weight)


def my_round(x, base=0.5):
    return base * round(x/base)


def set_counter(reps):
    if reps == 5:
        sets = 1
    elif reps == 3:
        sets = 2
    elif reps == 2:
        sets = 3
    else:
        sets = 5
    return sets


if __name__ == '__main__':
    texas_method_main()
