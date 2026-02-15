def calculate_greatest_common_divisor(numbers: list[int]) -> None:

    smallest_number = min(numbers)
    gcd_list = []
    while True:
        divisor_count = 0
        for number in numbers:
            if smallest_number == 0:
                print('This numeric sequence has no GCD.')
                break

            if number % smallest_number == 0:
                divisor_count += 1
                gcd_list.append(smallest_number)

        if divisor_count == len(numbers):
            for divisor in range(len(gcd_list)):
                if gcd_list[divisor]:
                    smallest_divisor = gcd_list[divisor]
                elif divisor > smallest_divisor and divisor > 1:
                    smallest_divisor = gcd_list[divisor]
                else:
                    smallest_divisor = 1

            print(f'The GCD of the numbers {numbers} is {smallest_divisor}')
            break

        smallest_number -= 1

calculate_greatest_common_divisor([9, 3, 5])
calculate_greatest_common_divisor([123, 100, 5])
calculate_greatest_common_divisor([25, 5, 15])
calculate_greatest_common_divisor([18,60])
calculate_greatest_common_divisor([55, 22])
calculate_greatest_common_divisor([15, 150])
calculate_greatest_common_divisor([81, 9])
