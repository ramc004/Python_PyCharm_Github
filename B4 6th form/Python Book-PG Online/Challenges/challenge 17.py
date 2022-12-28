def umsScore(mark):
    percent = mark / 80 * 100
    if percent >= 80:
        grade = 'A'
    elif percent >= 70:
        grade = 'B'
    elif percent >= 60:
        grade = 'C'
    elif percent >= 50:
        grade = 'D'
    elif percent >= 40:
        grade = 'E'
    else:
        grade = 'U'
    return grade

mod1Mark = int(input("Enter module 1 mark: "))
mod2Mark = int(input("Enter module 2 mark: "))
mod3Mark = int(input("Enter module 3 mark: "))
meanMark = (mod1Mark + mod2Mark + mod3Mark) / 3
# prints final results
print(('\n'
       'Results\n'
       '----------\n'
       'Module 1: {}\n'
       'Module 2: {}\n'
       'Module 3: {}\n'
       'Overall : {}\n').format(umsScore(mod1Mark), umsScore(mod1Mark), umsScore(mod3Mark), umsScore(meanMark)))
