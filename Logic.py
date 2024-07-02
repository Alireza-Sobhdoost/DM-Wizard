import re


def expression(s):
    # Step 1: Find the outermost parentheses

    def replace_not_operator(match):
        return f'(not {match.group(1)})'

    def replace_single_quote(match):
        return f'{match.group(1)}'
        # print(f'not {match.group(1)}')

    def single_quote_handeler(a):
        def myfind(arr, arg):
            out = []
            for i in range(len(arr)):
                if arr[i] == arg:
                    out.append(i)
            return out

        opens = myfind(a, "(")
        endes = myfind(a, ")")
        sq = myfind(a, "'")
        c = a

        for i in range(len(sq)):
            for j in range(len(endes)):
                # print(sq[i] - endes[j])
                if sq[i] - endes[j] == 1 and sq[i] != len(a) - 1:
                    c = c[:opens[-(j + 1)]] + "(not(" + c[opens[-(j + 1)] + 1:sq[i]] + ")" + c[sq[i] + 1:]
                elif sq[i] - endes[j] == 1 and sq[i] == len(a) - 1:
                    b = c.replace("'", "")
                    b = f'not({b})'
        return b

    if "nand" in s:
        x = s.split("nand")
        s = f"{x[0]}and{x[1]}'"
    if "nor" in s:
        x = s.split("nor")
        s = f"{x[0]}or{x[1]}'"
    if "nxor" in s:
        x = s.split("nxor")
        s = f"{x[0]}xor{x[1]}'"
    if "not" in s:
        pattern = re.compile(r'not\s+([a-zA-Z])')
        s = re.sub(pattern, replace_not_operator, s)

    if "'" in s:
        s = single_quote_handeler(s)

    # print(s)

    # print(s)
    expression = "(" + s + ")"
    start_index = expression.find('(')
    end_index = expression.rfind(')')
    if start_index != -1 and end_index != -1:
        outer_expression = expression[start_index + 1:end_index]
    else:
        outer_expression = expression

    # Step 2: Handle 'not' operation after closing parentheses

    # Step 3: Replace alphabets with dictionary values
    # for k, v in d.items():
    #     outer_expression = outer_expression.replace(k, str(v))

    # Step 4: Count the unique alphabets

    # Step 5: Replace operators with Python logical operators

    outer_expression = outer_expression.replace('T', '@')
    outer_expression = outer_expression.replace('F', '#')
    outer_expression = outer_expression.replace('and', '&')
    outer_expression = outer_expression.replace('xor', '^')
    outer_expression = outer_expression.replace('or', '|')
    outer_expression = outer_expression.replace('not', '!')

    processed_expression = outer_expression
    unique_alphabets = set(re.findall(r'[a-zA-Z]', processed_expression))
    d = {alpha: idx for idx, alpha in enumerate(unique_alphabets)}

    # print(d)
    alphabet_count = len(unique_alphabets)

    # if end_index < len(expression) - 1 and expression[end_index + 1] == "'":
    #     outer_expression = f'not({outer_expression})'
    # outer_expression = outer_expression.replace("'", f'not({outer_expression})')
    outer_expression = outer_expression.replace('!', 'not')
    outer_expression = outer_expression.replace('@', 'True')
    outer_expression = outer_expression.replace('#', 'False')

    processed_expression = outer_expression

    count_true = 0
    binary_numbers = [[int(x) for x in format(i, '0' + str(alphabet_count) + 'b')] for i in range(2 ** alphabet_count)]
    result = [[bool(x) for x in binary_number] for binary_number in binary_numbers]
    previous_result = None
    for i in result:
        # Assigning values from binary numbers to corresponding variables
        values = i
        # print(values)
        variables = dict(zip(d.keys(), values))
        # Evaluating the processed expression
        current_result = eval(processed_expression, {}, variables)
        if eval(processed_expression, {}, variables):
            count_true += 1
        if previous_result is not None and current_result != previous_result:
            return "Probability"

        previous_result = current_result



    if count_true == (2 ** alphabet_count):
        return "Tautology"
    elif count_true == 0:
        return "Contradiction"

# Example usage

# expression_str = "(p or q or (not p and r and not q))"
# resultExp, count , d = expression(expression_str)
# print("Processed Expression:", resultExp)
# print("Number of Unique Alphabets:", count)
#
# count_true = 0
# binary_numbers = [[int(x) for x in format(i, '0' + str(count) + 'b')] for i in range(2 ** count)]
# result = [[bool(x) for x in binary_number] for binary_number in binary_numbers]
# print(result)
#
# for i in result:
#     # Assigning values from binary numbers to corresponding variables
#     values = i
#     print(values)
#     variables = dict(zip(d.keys(), values))
#
#     # Evaluating the processed expression
#     if eval(resultExp, {}, variables):
#         count_true += 1
#         print("Values that evaluate to True:", values)
#
# print("Total Count of True Values:", count_true)
#
# print(expression(expression_str))