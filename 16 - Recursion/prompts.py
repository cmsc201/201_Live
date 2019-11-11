def get_input_until(prompt, sentinel):
    result = input(prompt)
    if result == sentinel:
        return []
    else:
        results = [result]
        results.extend(get_input_until(prompt, sentinel))
        return results


def get_number_inputs(prompt, number):
    if number == 0:
        return []
    else:
        result = input(prompt)
        results = [result]
        results.extend(get_number_inputs(prompt, number - 1))
        return results


if __name__ == '__main__':
    inputs = get_input_until("Give a thing or STOP", "STOP")
    print(inputs)
    second_inputs = get_number_inputs("Give a thing", len(inputs))
    print(second_inputs)
