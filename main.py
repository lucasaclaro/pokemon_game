import requests


pokemon = 1

print('151 pokemons:\n ')

pokemon_water = []
pokemon_grass = []
pokemon_fire = []
pokemon_bug = []
pokemon_normal = []
pokemon_poison = []
pokemon_eletric = []
pokemon_ground = []
pokemon_fairy = []
pokemon_fighting = []
pokemon_psychic = []
pokemon_rock = []
pokemon_ghost = []
pokemon_ice = []
pokemon_dragon = []



while True:


    link = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    request = requests.get(link)
    request_json = request.json()
    pokemon_id = request_json['id']
    pokemon_name = request_json['forms'][0]['name']
    pokemon_type = request_json['types'][0]['type']['name']
    pokemon_move = request_json['moves'][0]['move']['name']
    print(f"{pokemon_id}: {pokemon_name} | Type: {pokemon_type} | Move: {pokemon_move}.")
    if pokemon_type == 'water':
        pokemon_water.append(pokemon_name)
    elif pokemon_type == 'grass':
        pokemon_grass.append(pokemon_name)
    elif pokemon_type == 'fire':
        pokemon_fire.append(pokemon_name)
    elif pokemon_type == 'bug':
        pokemon_bug.append(pokemon_name)
    elif pokemon_type == 'normal':
        pokemon_normal.append(pokemon_name)
    elif pokemon_type == 'poison':
        pokemon_poison.append(pokemon_name)
    elif pokemon_type == 'eletric':
        pokemon_eletric.append(pokemon_name)
    elif pokemon_type == 'ground':
        pokemon_ground.append(pokemon_name)
    elif pokemon_type == 'fairy':
        pokemon_fairy.append(pokemon_name)
    elif pokemon_type == 'fighting':
        pokemon_fighting.append(pokemon_name)
    elif pokemon_type == 'psychic':
        pokemon_psychic.append(pokemon_name)
    elif pokemon_type == 'rock':
        pokemon_rock.append(pokemon_name)
    elif pokemon_type == 'ghost':
        pokemon_ghost.append(pokemon_name)
    elif pokemon_type == 'ice':
        pokemon_ice.append(pokemon_name)
    elif pokemon_type == 'dragon':
        pokemon_dragon.append(pokemon_name)
    pokemon += 1


    if pokemon == 152:
        break


print(f"Total \n "
      f"Water: {len(pokemon_water)}.\n"
            f"Water: {len(pokemon_water)}.\n"
            f"Grass: {len(pokemon_grass)}.\n"
            f"Fire: {len(pokemon_fire)}.\n"
            f"Bug: {len(pokemon_bug)}.\n"
            f"Normal: {len(pokemon_normal)}.\n"
            f"Poison: {len(pokemon_poison)}.\n"
            f"Eletric: {len(pokemon_eletric)}.\n"
            f"Ground: {len(pokemon_ground)}.\n"
            f"Fairy: {len(pokemon_fairy)}.\n"
            f"Fighting: {len(pokemon_fighting)}.\n"
            f"Psychic: {len(pokemon_psychic)}.\n"
            f"Rock: {len(pokemon_rock)}.\n"
            f"Ghost: {len(pokemon_ghost)}.\n"
            f"Ice: {len(pokemon_ice)}.\n"
            f"Dragon: {len(pokemon_dragon)}.\n"
      
      f"")



