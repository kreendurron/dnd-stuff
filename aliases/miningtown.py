!tembed
<drac2>

towns = load_json(get_gvar("fa6f4eb9-1ea4-4c76-b6b8-eeed4ee3a0ed"))
town = towns[0]

townTaxRate = float(town.taxIncome)*100
taxablePopulation = float(town.population) - float(town.laborers)
income = float(town.workdays) * float(town.laborProfitability) * float(town.laborers)
townTaxRevenue = floor(float(town.taxIncome)*income)


miscExpenseRate = float(town.miscExpenses)*100
laborExpense = float(town.laborPayrate)*float(town.laborers)
expenses = miscExpenseRate + laborExpense


grossRevenue = floor(income + townTaxRevenue)
nationalTaxRate = float(town.taxExpense)*100
nationalTaxExpense = floor(float(town.taxExpense)*grossRevenue)
netProfit = floor(grossRevenue * float(town.taxExpense) - expenses)
dailyIncome = floor(netProfit/365)


</drac2>

-title "Welcome to {{town.name}}"

-desc "{{town.mine}}"

-f
"
**Town Statistics:**
Population: {{town.population}}
Laborers: {{town.laborers}}
Town Tax Rate: {{round(float(townTaxRate))}}%
Town Tax Revenue: {{f'{townTaxRevenue:,}'}} GP/anum}
"

-f
"
**Expenses:**
National Tax Rate: {{round(nationalTaxRate)}}%
National Tax Expense: {{f'{nationalTaxExpense:,}'}} GP/anum}
Miscelaneous Expenses: {{round(miscExpenseRate)}}%
Labor Pay: {{town.laborPayrate}} GP/anum
"

-f "
**Earnings**
Gross Revenue: {{f'{grossRevenue:,}'}} GP/anum
Net Profit: {{f'{netProfit:,}'}} GP/anum
Daily Income: {{f'{dailyIncome:,}'}} GP/day
"

-footer "You can set the tax rate for your town. and other options coming soooon. (work in progress)"
