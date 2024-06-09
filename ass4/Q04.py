import tqdm
def primes_up_to(n):
    primes=[]
    with tqdm.trange(2,n) as t:
        for i in t:
            i_is_prime=not any(i%p==0 for p in primes)
            if i_is_prime:
                primes.append(i)
            t.set_description(f'{len(primes)} Primes')
    return primes
def main():
    primes=primes_up_to(1000)
    print(primes)

main()