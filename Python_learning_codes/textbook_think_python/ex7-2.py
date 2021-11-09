def eval_loop():
    while True:
        user_input = input('>>>')
        if eval(user_input) == 'done':
            break
        print(eval(user_input))
    return eval(user_input)

eval_loop()