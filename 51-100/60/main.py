def is_prime(n, check_list_for_primes): #checks if value is prime
    if check_list_for_primes.count(n) > 0: #checks if valu calculated before. if it were, it avoid loop.
        return True
    else:
        if n == 1:
            return False
        if n == 2 or n == 3:
            return True
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
                exit(0)
            i += 1
        check_list_for_primes.append(n) # if it never calculated, stores the value to avoid loop at the beginning of function.
    return True


def check_1(i, j): # checks the concanated values if they are primes.
    if is_prime(int(str(i)+str(j)), check_list_for_primes) == True and is_prime(int(str(j)+str(i)), check_list_for_primes) == True:
        return True
    else:
        return False
    
    
def check_2(temp_list): # checks the final list that obtain the minimum summation.
    for i in temp_list:
        for j in temp_list:
            if len(temp_list) == 1:
                return check_1(i, j)
            elif i == j:
                continue
            elif len(temp_list) == 1:
                return True
                break
            elif check_1(i, j) == False:
                return False
    return True


def func_(prime_list): # creates a dictionary summation of the five prime numbers in order to problem.
    prime_list.remove(5)    
    temp_list = []
    result_dic = {}
    # k = 0
    copy_primes = prime_list.copy()
    for i in prime_list:
        for z in prime_list:
            if z <= i:
                copy_primes.remove(z)
            else:
                break
        if i == max(prime_list):
            break
        elif i == 5:
            continue
        # for z in range(len(prime_list) - 1, 0, -1):
        #     if check_1(i,prime_list[z]) == True:
        #         max_prime_of_i = prime_list[z]
        #     break
        while len(temp_list) < 5:
            # if temp_list[1] == max_prime_of_i:
            #     break
            if len(temp_list) == 1:
                break
            if len(copy_primes) == 0 and len(temp_list) > 1:
                copy_primes = prime_list.copy()
                for z in prime_list:
                    if z <= temp_list[1]:
                        copy_primes.remove(z)
                    else:
                        break
                temp_list = []
                
            for j in prime_list:
                if len(copy_primes) > 0:
                    j = copy_primes[0]
                    copy_primes.remove(j)
                else:
                    break
                if temp_list.count(i) == 0:
                    temp_list.append(i)
                    continue
                temp_list.append(j)
                temp_list.sort()
                if check_2(temp_list) == True and len(temp_list) > 1:
                    continue
                elif check_2(temp_list) == False  and len(temp_list) > 1:
                    temp_list.remove(j)
            if len(temp_list) < 5 and len(copy_primes) == 0:
                continue
            elif len(temp_list) == 5:
                break
        copy_primes = prime_list.copy()
        if len(temp_list) == 5:
            result_dic[sum(temp_list)] = temp_list
            weight_ = 0
            check_weight = 0
            for p in temp_list:
                    weight_ = weight_ + len(str(p))
            if weight_ < check_weight or check_weight == 0:
                check_weight = weight_
            elif check_weight < weight_ and len(temp_list) == 5:
                return result_dic
        temp_list = []
    return result_dic


if __name__ == "__main__":
    dic_ = {}
    prime_list = []
    check_list_for_primes = []
    for i in range(3, 9000, 1): #creates prime list between given range
        if is_prime(i, check_list_for_primes) == True:
            prime_list.append(i)
    check_list_for_primes = prime_list.copy() #pseudo prime list to avoid calculating if the number is prime.
    dic_ = func_(prime_list) #final dictionary to obtain minimum summation of five prime numbers.
    x = min(list(dic_.keys()))
    print(str(x) + " : " + str(dic_[x]))