outfile = open('dbinfoPokemon.txt', "w")
RarityID = 0
while RarityID != 69:
    
    RarityID = int(input("RarityID: "))
    if RarityID == 69:
        break
    RegionID = int(input("RegionID: " ))
    SpeciesID = int(input("SpeciesID: "))
    PokemonName = input("Pokemon Name: ")
    PokemonDescription = input("Poke Description: ")
    Attack = int(input("Attack: "))
    Defense = int(input("Defense: "))
    HP = int(input("HP: "))
    Speed = int(input("Speed: "))
    
    print(" ({},{},{},\'{}\',\'{}\',{},{},{},{}),".format(RarityID,RegionID,SpeciesID,PokemonName,PokemonDescription,Attack, Defense, HP, Speed ))
    print(" ({},{},{},\'{}\',\'{}\',{},{},{},{}),".format(RarityID,RegionID,SpeciesID,PokemonName,PokemonDescription,Attack, Defense, HP, Speed ),file=outfile)


outfile.close()