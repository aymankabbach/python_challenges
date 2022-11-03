## City A has one million citizens and is growing at a rate of 50 thousand annually
## City B has 500,000 citizens and is growing 8% annually
## Write a program that calculates in how many years there will be more citizens in city B than in city A
def increase_citizens(city_citizens,number):
    city_citizens+=number
    return city_citizens
def start():
    city_A_citizens=1000000
    city_B_citizens=500000
    year=0
    while city_B_citizens<city_A_citizens:
        city_A_citizens=increase_citizens(city_A_citizens,50000)
        city_B_citizens=increase_citizens(city_B_citizens,city_B_citizens*8/100)
        year+=1
    print(f"after {year} years city B would have more citizens")
start()
