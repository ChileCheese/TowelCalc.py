while 1 == 1:
    p_of_towel = .75 
    vinyel_p = .08
    packaging_p = .16
    expense = .99
    towel_sold_p = 10.99

    a_1 = input('Does a discount need applied?')
    if a_1 == 'no':
        discount = 0
        pass
    if a_1 == 'yes':
        a_2 = input('How much of a discount should be applied?')
        discount = towel_sold_p * float(a_2)

    Amount_towels = int(input('how many towels did you sell:'))
    Price_all_towels = (float(p_of_towel) * int(Amount_towels))
    expenses = (float(expense) * int(Amount_towels))
    total_dis = (int(Amount_towels) * float(discount))
    total_rev = (int(Amount_towels) * float(towel_sold_p) - float(total_dis))
    profit = (total_rev) - (expenses) 

    print('revune: $', total_rev)
    print('expenses: $', expenses)
    print('discount: $', total_dis)
    print('profit: $', profit)
