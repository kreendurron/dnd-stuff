embed
<drac2>
out = []

g = load_json(get_gvar("575c8d91-53f2-4b44-a73c-ead0d9e8a1e5"))
if get("townID") in g.keys():
    grossRevenue = 1000
    netProfit = 0
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
Earnings
Gross Revenue: {{f'{grossRevenue:,}'}} GP/anum
Net Profit: {{f'{netProfit:,}'}} GP/anum
Daily Income: {{f'{dailyIncome:,}'}} GP/day
"

-f """You can set the tax rate for your town and other options coming soooon. (work in progress).
Feel free to help contribute @ https://github.com/kreendurron/dnd-stuff/blob/main/aliases/town.py"""
