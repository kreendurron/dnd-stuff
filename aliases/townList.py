embed
<drac2>
g = load_json(get_gvar("575c8d91-53f2-4b44-a73c-ead0d9e8a1e5"))
townlist = ' '.join([f"\n{k}" for k in g.keys()])

</drac2>
-f "{{townlist}}" #List of all the towns
