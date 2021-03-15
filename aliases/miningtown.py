embed
<drac2>

towns = load_json(get_gvar("fa6f4eb9-1ea4-4c76-b6b8-eeed4ee3a0ed"))
town = towns[0]

taxablePopulation = float(town.population) - float(town.laborers)
income = float(town.workdays) * float(town.laborProfitability) * float(town.laborers)
taxRevenue = float(town.taxIncome)*float(income)
expenses = float(town.miscExpenses) + float(town.laborPayrate)
nationalTax = float(town.taxExpense)*100


grossRevenue = float(income) + float(taxRevenue)
netProfit = float(grossRevenue) - float(expenses) * float(nationalTax)

</drac2>

-title "Welcome to {{town.name}}"

-desc "{{town.mine}}"

-f
"
Town Statistics:
Population: {{town.population}}
Laborers: {{town.laborers}}
Tax Rate: {{round(float(town.taxIncome)*100)}}%
taxRevenue: {{taxRevenue}}
"

-f
"
Expenses:
National Tax: {{round(float(town.taxExpense)*100)}}%
Miscelaneous Expenses: {{round(float(town.miscExpenses)*100)}}%
Labor Pay: {{town.laborPayrate}} gp/anum (2sp per laborer per day *300 days)
"

-f "
Gross Revenue: {{f'{grossRevenue:,}'}} per anum
Net Profit: {{f'{netProfit:,}'}} per anum (still working on calc)

"

-footer "You can set the tax rate for your town. and other options coming soooon. (work in progress)"
