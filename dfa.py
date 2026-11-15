
TRANSITIONS = {
    ('q0', '0'): 'q0', ('q0', '1'): 'q1',
    ('q1', '0'): 'q0', ('q1', '1'): 'q2',
    ('q2', '0'): 'q3', ('q2', '1'): 'q2',
    ('q3', '0'): 'q3', ('q3', '1'): 'q3'
}

START_STATE = 'q0'
FINAL_STATES = {'q0', 'q1', 'q2'}

def verify_string(binary_string):
    state = START_STATE

    for symbol in binary_string:
        if symbol not in ('0', '1'):
            raise ValueError('Input must contain only 0 and 1')

        state = TRANSITIONS[(state, symbol)]

    return state in FINAL_STATES


test_strings = [
    '1010', '10101', '0110', '101110',
    '111010', '1011011', '01101010', '100100'
]

for value in test_strings:
    result = 'Accepted' if verify_string(value) else 'Rejected'
    print(f'{value:>8} : {result}')
