#lISTA TEMPORÁRIa
pet_shop = []
while True:
    opcao = input('Deseja cadastrar u  pet? (s ou n): ').lower()
    if opcao == 'n':
        print('Saindo do sistema, tchau')
        break
    if opcao == 's':
            nome = input('nome do pet: ')
            raça = input('raça: ')
            dono = input('nome do dono: ')
novo_pet = {
    'nome': nome,
    'raça': raça,
    'dono': dono,
    'status': 'aguardando'
}
#Lista principal
pet_shop.append(novo_pet)
print(f'\n✅ {nome} adicionado á lista')
print(f'\nTotal de pets cadastrados hoje: {len(pet_shop)}')

