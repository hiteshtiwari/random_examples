    # class Solution:
    def myAtoi(s: str) -> int:
        min_range = (2 ** 31) * -1
        max_range = (2 ** 31) - 1

        input_str = s.strip()
        if input_str[0] == '-':
            mul = -1
            input_str = input_str[1:]
        elif input_str[0] == '+':
            mul = 1
            input_str = input_str[1:]
        print(f"input_str is {input_str}" )
        final_str = ''
        for i in range(len(input_str)):
            print(f"i is {input_str[i]}")
            if input_str[i] not in list(map(str, list(range(10)))):
                print("under if condition")
                final_str = input_str[:i]
                break
            else: 
                print("under else condition")
                final_str = input_str[:]
        print(f"final_str is {final_str}" )
        if len(final_str) == 0:
            return 
        else:
            print(int(final_str))
            return int(final_str) * mul
        
    print(myAtoi('-45 jiofewj fewjo'))