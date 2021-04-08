!tembed
<drac2>
out = []

g = load_json(get_gvar("575c8d91-53f2-4b44-a73c-ead0d9e8a1e5"))
income = float(g[townID]["Laborers"]) * float(g[townID]["Labor Payrate"])#laborers * laborPayrate (425*60=25500)
expenses = float(g[townID]["National Tax Rate"]) * float(income) #income * national taxrate + income
if get("townID") in g.keys():
    grossRevenue = 0 #laborers * laborOutput * workdays + taxrate on taxablePopulation
    netProfit = 0 #grossRevenue - expenses
    dailyIncome = 0
    out.append(f"""
-title "{name}'s Town: {townID}"
-f "**Statistics**"
""")
    for k,v in g[townID].items():
        out.append(f''' -f "{k.title()}|{v}|inline" ''')

else:
    grossRevenue = 0
    netProfit = 0
    dailyIncome = 0
    out.append(f"""-title "It doesn't look like you've founded a town yet!" -desc "Que The Sad Trombone Sound." """)

return ' '.join(out)

</drac2>

-f "
{{typeof(g[townID]["National Tax Rate"])}}
Earnings
Income: {{f'{income:,}'}} GP/anum
Expenses: {{f'{expenses:,}'}} GP/anum
Gross Revenue: {{f'{grossRevenue:,}'}} GP/anum (not calculated yet)
Net Profit: {{f'{netProfit:,}'}} GP/anum (not calculated yet)
Daily Income: {{f'{dailyIncome:,}'}} GP/day (not calculated yet)
"

-f """You can set the tax rate for your town and other options coming soooon.
Feel free to help contribute @ [mygithub](https://github.com/kreendurron/dnd-stuff 'https://github.com/kreendurron/dnd-stuff')"""
-footer "Work In Progress"






```py
!tembed
<drac2>
out = []

g = load_json(get_gvar("575c8d91-53f2-4b44-a73c-ead0d9e8a1e5"))
income = float(g[townID]["Laborers"]) * float(g[townID]["Labor Payrate"])#laborers(425) * laborPayrate(60) (425*60=25500)
expenses = float(float(g[townID]["National Tax Rate"])/100 * float(income)) #income(25000) * national taxrate(75%) + income

if get("townID") in g.keys():
    out.append(f"""
-title "{name}'s Town: {townID}"
-f "**Statistics**"
""")
    for k,v in g[townID].items():
        out.append(f''' -f "{k.title()}|{v}|inline" ''')

else:
    out.append(f"""-title "It doesn't look like you've founded a town yet!" -desc "Que The Sad Trombone Sound." """)

return ' '.join(out)

</drac2>

-f "
Earnings
Income: {{f'{income:,}'}} GP/anum
Expenses: {{f'{expenses:,}'}} GP/anum

"
```





!tembed
<drac2>
out = []

g = load_json(get_gvar("575c8d91-53f2-4b44-a73c-ead0d9e8a1e5"))

taxablePopulation = float(g[townID]["Population"])-float(g[townID]["Laborers"])
taxRevenue = float(g[townID]["Tax Rate"]) * taxablePopulation / 100 + taxablePopulation
income = float(g[townID]["Laborers"]) * float(g[townID]["Labor Payrate"])
grossRevenue = income + taxRevenue

netProfit = float(g[townID]["National Tax Rate"]) * grossRevenue / 100
dailyIncome = grossRevenue / float(g[townID]["Work Days"])

</drac2>

-f "
inspecting:

Income: {{f'{income:,}'}} GP/anum
netProfit or nationalTaxRate * income / 100 = {{netProfit}}
national tax rate = {{g[townID]["National Tax Rate"]}}
qty of laboreres = {{g[townID]["Laborers"]}}
labor Payrate = {{g[townID]["Labor Payrate"]}} GP/anum (wip)

taxablePopulation: {{f'{taxablePopulation:,}'}} People (wip)
Gross Revenue: {{f'{grossRevenue:,}'}} GP/anum (wip)

Daily Income: {{f'{dailyIncome:,}'}} GP/day (wip)

"
