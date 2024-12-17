def fizzbuzz(nums, fizz, buzz):
    game_nums = nums
    
    for i in range(1, game_nums+1):
        if i % (fizz*buzz) == 0:
            print("FizzBuzz")
        
        elif i % fizz == 0: print("Fizz")
        elif i % buzz == 0: print("Buzz")
        else: print(i)

fizzbuzz(100, 3, 5)
