import time

import json
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
# Set redis storage with an empty json list
cache.set('primes',json.dumps([]))


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

# Output if the given number is a prime or not
@app.route('/isPrime/<int:number>')
def isPrime(number):
    if number <= 3:
        if number > 1:
            # 2 or 3, is a prime
            storePrime(number)
            return '%d is prime' % number
        else:
            return '%d is not prime' % number
    # Check for every possible factor using the 6k+i optimisation
    elif number % 2 == 0 or number % 3 == 0:
        return '%d is not prime' % number
    i = 5
    while i*i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return '%d is not prime' % number
        i += 6
    # No factors found, is a prime
    storePrime(number)
    return '%d is prime' % number

# Append given number to the json list stored in redis
def storePrime(number):
    # Retrieve list of prime numbers from redis
    primes = json.loads(cache.get('primes'))
    # Update redis storage with new list
    primes.append(number)
    primes.sort()
    cache.set('primes',json.dumps(primes))

# Output all prime numbers stored in redis
@app.route('/primesStored')
def primesStored():
    primes = json.loads(cache.get('primes'))
    # Check if list is empty
    if len(primes) == 0:
        return 'No primes are stored'
    # Return a string of all elements in the list
    output = ''
    for prime in primes:
        output += str(prime) + ', '
    return output
    