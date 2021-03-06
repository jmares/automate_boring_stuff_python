import pyinputplus as pyip
import random, time

number_of_questions = 10
correct_answers = 0

for question in range(number_of_questions):
    # Pick 2 random numbers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s x %s = ' % (question, num1, num2)

    try:
        # Right answers are handled by allowRegexes
        # Wrong answers are handled by blockRegexes, with a custom message
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
            blockRegexes=[('.*', 'Incorrect!')],
            timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correct_answers += 1
    time.sleep(1)
print('Score: %s / %s' % (correct_answers, number_of_questions))