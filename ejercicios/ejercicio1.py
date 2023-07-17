'''
Your function takes two arguments:
current father's age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.
'''
#solución 1
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - (son_years_old * 2))

#solución 2

twice_as_old = lambda dad_years_old, son_years_old: abs(dad_years_old - (son_years_old * 2))