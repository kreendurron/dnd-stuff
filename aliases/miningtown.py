!tembed
<drac2>

towns = load_json(get_gvar("fa6f4eb9-1ea4-4c76-b6b8-eeed4ee3a0ed"))
town = towns[0]

taxablePopulation = float(town.population) - float(town.laborers)
income = float(town.workdays) * float(town.laborProfitability) * float(town.laborers)
taxRevenue = float(town.taxIncome)*float(income)

miscExpenseRate = float(town.miscExpenses)*100
laborExpense = float(town.laborPayrate)*float(town.laborers)
expenses = miscExpenseRate + laborExpense


grossRevenue = floor(income + taxRevenue)
netProfit = floor(float(grossRevenue) * float(town.taxExpense) - float(expenses))
dailyIncome = floor(netProfit/365)


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
Labor Pay: {{town.laborPayrate}} GP/anum
"

-f "
Gross Revenue: {{f'{grossRevenue:,}'}} GP/anum
Net Profit: {{f'{netProfit:,}'}} GP/anum
Daily Income: {{f'{dailyIncome:,}'}} GP/day
"

-footer "You can set the tax rate for your town. and other options coming soooon. (work in progress)"
