max_step = 10
for step in range(max_step, 120):
    year = int(step / 12) + 1
    month = step % 12
    my_step = (year - 1) * 12 + month
    print(f"step={step},year={year},month={month},my_step={my_step}")
