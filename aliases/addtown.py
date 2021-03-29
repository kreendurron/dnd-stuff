embed
<drac2>
if townID: # check if character has cvar "townID"
    character().delete_cvar("townID") #delete cvar if it exists
    character().set_cvar_nx("townID","%*%") #create a new townID cvar with userinput
else:
    character().set_cvar_nx("townID","%*%") #create a new townID cvar with userinput
</drac2>

-f "Your the proud new owner of {{townID}}!"
-t 300
