# todo 1: value input, durasi, dan gaji pokok
OT = {
    "Gloria": [3, 7, 1.5],
    "Winda": [2, 3, 11.5, 2, 2, 2],
    "Fajar": [2, 1.5, 2, 1.5, 2.5, 8.5, 1.5],
    "Lira": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1],
    "Iman": [10, 2, 2, 1],
    "Simbah": [2, 3, 7.5, 1, 0.5, 1],
    "Dede": [3, 8.5, 1.5, 3, 2]
}
name = input("What is your name? ").title()
gross = int(input("How much your basic salary?\n"))


def total(name):
    duration = sum(OT[name])
    return duration


# todo 2: cek income dari perhitungan wiki
hourly = round((gross / 173))
wiki = round(hourly * total(name))

# todo 4: cek durasi lembur dan kalkulasinya
"""
0 - 8 jam: 2x upah sejam
9 jam : 3x upah sejam
10 - 12: 4x upah sejam
"""


def uu(name):
    incentive = []
    for x in OT[name]:
        if x <= 8:
            tot = (x * 2) * hourly
            incentive.append(tot)
        elif 8 < x <= 9:
            tot = ((8 * 2) * hourly) + (((x - 8) * 3) * hourly)
            incentive.append(tot)
        elif x > 9:
            tot = ((8 * 2) * hourly) + ((1 * 3) * hourly) + ((x - 9) * 4) * hourly
            incentive.append(tot)
    print(f'''\nUU incentive detail: 
hours: {OT[name]}
nominal: {incentive}''')
    return round(sum(incentive))


# todo 5: Compiling the result
print(f'''
    1. Your over time total duration is: {total(name)} hours
    2. Your hourly income is Rp {hourly}
    3. Incentive based on wiki.sirogu adalah: Rp. {wiki}
    ({total(name)} x Rp. {hourly})
    4. Incentive based UU adalah: Rp {uu(name)}
''')
