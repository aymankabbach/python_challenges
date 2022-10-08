## City A has one million citizens and is growing at a rate of 50 thousand annually
## City B has 500,000 citizens and is growing 8% annually
## Write a program that calculates in how many years there will be more citizens in city B than in city A
city_A_citizens=1000000
city_B_citizens=500000
def increzse_city_A_citizens():
    global city_A_citizens
    city_A_citizens+=50000
    return city_A_citizens
def increzse_city_B_citizens():
    global city_B_citizens
    city_B_citizens*=1.08
    return city_B_citizens
def start():
    global city_A_citizens,city_B_citizens
    year=0
    while city_B_citizens<city_A_citizens:
        city_A_citizens=increzse_city_A_citizens()
        city_B_citizens=increzse_city_B_citizens()
        print(f"city A , {city_A_citizens}")
        print(f"city B , {city_B_citizens}")
        year+=1
    print(f"after {year} years city B would have more citizens")
start()
