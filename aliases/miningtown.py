embed
<drac2>
pc = character().name
out = []

g = load_json(get_gvar("fa6f4eb9-1ea4-4c76-b6b8-eeed4ee3a0ed"))
if pc in g.keys():
    grossRevenue = 1000
    netProfit = 0
    dailyIncome = 0
    out.append(f"""-title "{name}'s town's Statistics" """)
    for k,v in g.get(pc).items():
        out.append(f''' -f "{k.title()}|{v}|inline" ''')

else:
    grossRevenue = 0
    netProfit = 0
    dailyIncome = 0
    out.append(f"""-title "It doesn't look like you've founded a town yet!" -desc "Que The Sad Trombone Sound." """)

return ' '.join(out)

</drac2>

-f "
**Earnings**
Gross Revenue: {{f'{grossRevenue:,}'}} GP/anum
Net Profit: {{f'{netProfit:,}'}} GP/anum
Daily Income: {{f'{dailyIncome:,}'}} GP/day
"

-footer "You can set the tax rate for your town and other options coming soooon. (work in progress)"
