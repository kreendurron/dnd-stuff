!tembed
<drac2>

towns = load_json(get_gvar("fa6f4eb9-1ea4-4c76-b6b8-eeed4ee3a0ed"))
townnames = []

for town in towns:
  townnames.append(i.name)
</drac2>

taxablePopulation = float(town.population) - float(town.laborers)
townTaxRate = float(town.taxRate)*100
townTaxRevenue = round(townTaxRate*taxablePopulation)
income = float(town.laborOutput) * float(town.laborers) * float(town.workdays) + townTaxRevenue

miscExpenseRate = float(town.miscExpenses)*100 # %15
laborExpense = float(town.laborPayrate)*float(town.laborers) # 25,500
expenses = floor(miscExpenseRate * laborExpense/100 + laborExpense) #29,325


grossRevenue = floor(income + townTaxRevenue)
nationalTaxRate = float(town.nationalTaxRate)*100
nationalnationalTaxRate = floor(float(town.nationalTaxRate)*grossRevenue)
netProfit = floor(grossRevenue * float(town.nationalTaxRate) - expenses)
dailyIncome = floor(netProfit/365)


</drac2>

-title "Welcome to {{town.name}}"

-desc "Made possible by: {{town.mine}}"
-f "Town Names: {{townnames}}"
-f
"
**Town Statistics:**
Population: {{town.population}}
Laborers: {{town.laborers}}
Taxable Population: {{floor(taxablePopulation)}}
Town Tax Rate: {{round(townTaxRate)}}%
Town Tax Revenue: {{f'{townTaxRevenue:,}'}} GP/anum}
"

-f
"
**Expenses:**
National Tax Rate: {{round(nationalTaxRate)}}%
National Tax Expense: {{f'{nationalnationalTaxRate:,}'}} GP/anum}
Miscelaneous Expenses: {{round(miscExpenseRate)}}%
Labor Pay Rate: {{town.laborPayrate}} GP/anum
Labor Expense: {{floor(laborExpense)}} GP/anum
Expenses: {{expenses}}
"

-f "
**Earnings**
Gross Revenue: {{f'{grossRevenue:,}'}} GP/anum
Net Profit: {{f'{netProfit:,}'}} GP/anum
Daily Income: {{f'{dailyIncome:,}'}} GP/day
"

-footer "You can set the tax rate for your town. and other options coming soooon. (work in progress)"



!tembed
<drac2>
towns = load_json(get_gvar("fa6f4eb9-1ea4-4c76-b6b8-eeed4ee3a0ed"))
townnames = []
for i in towns:
  townnames.append(i.name)
</drac2>
-f "{{'\n'.join(townnames)}}"
