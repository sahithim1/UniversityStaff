# Sahithi Mankala
import universitySalary

for name in (
        'James E. Ryan',
        'Groves, Allen',
        '181067633',
        'Hao Ran Laurenc Lin',
        '181016364'
        ):


    job, money, rank, year = universitySalary.report(name)
    punc = "is a"
    if job[0] == 'A':
        punc = "is an"
    print(name, punc, job, 'they make', money, "and has worked at UVA since",year,'(rank', str(rank)+')')

