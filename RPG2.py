import random
import time
def game_over(): 
    over = 1
    if over == (1):
        print("\033[31m" + """
                  game over       
        ███████████████████████████
        ███████▀▀▀░░░░░░░▀▀▀███████
        ████▀░░░░░░░░░░░░░░░░░▀████
        ███│░░░░░░░░░░░░░░░░░░░│███
        ██▌│░░░░░░░░░░░░░░░░░░░│▐██
        ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
        ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
        ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
        ██▌░│██████▌░░░▐██████│░▐██
        ███░│▐███▀▀░░▄░░▀▀███▌│░███
        ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
        ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
        ████▄─┘██▌░░░░░░░▐██└─▄████
        █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
        ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
        █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
        ███████▄░░░░░░░░░░░▄███████
        ██████████▄▄▄▄▄▄▄██████████
        ███████████████████████████
                  game over    """ + "\033[0m") 
    time.sleep(5)   
    jogo() 

dano_2x_tempo = 0
ataque_cava = 0
pontos_vampiro = 0
defesa_cava = 0

def jogo():
    itens = []
    herois = []
    lista_monstro = []
    monstro_morto = [] 
    lixo = []
       
    class poçãos:
        def __init__(self, nome_item, quantidade, efeito):
            self.nome_item = nome_item
            self.quantidade = quantidade
            self.efeito = efeito
       
    def curar_vida(poçãos, heroi):
        if poçãos.quantidade > 0:
            poçãos.quantidade -= 1
            heroi.vida += 20
            if poçãos.quantidade < 1:
                lixo.append(poçãos)
                itens.remove(poçãos)
        else:
            print(f"{poçãos.nome_item} indisponível")        
    def pocao_ataque(poçãos, heroi):
        if poçãos.quantidade > 0:
            poçãos.quantidade -= 1
            heroi.ataque_e += 10
            if poçãos.quantidade < 1:
                lixo.append(poçãos)
                itens.remove(poçãos)
 
    def pocao_defesa(poçãos, heroi):
        if poçãos.quantidade > 0:
            poçãos.quantidade -= 1
            heroi.defesa_e += 5
            if poçãos.quantidade < 1:
                lixo.append(poçãos) 
                itens.remove(poçãos)
   
    def pocao_negar_ataque(poçãos, heroi):
        if poçãos.quantidade > 0:
            poçãos.quantidade -= 1
            heroi.negar_ataque = 999
            heroi.negar_tempo += 2
            if poçãos.quantidade <= 0:
                lixo.append(poçãos)
                itens.remove(poçãos)
        
    def pocao_espinhos(poçãos, heroi):
        if poçãos.quantidade > 0:
            heroi.espinhos += 5
            poçãos.quantidade-= 1
            if poçãos.quantidade <= 0:
                lixo.append(poçãos)
                itens.remove(poçãos)
       
    def dano_2x(poçãos, heroi):
        global dano_2x_tempo
        if poçãos.quantidade > 0:
            poçãos.quantidade -= 1  
            dano_2x_tempo += 2
            if poçãos.quantidade <= 0:
                lixo.append(poçãos)
                itens.remove(poçãos)
   
    def barra_de_vida(vida_atual, vida_maxima, tamanho=25):
        porcentagem_vida = vida_atual / vida_maxima
        blocos_preenchidos = int(porcentagem_vida * tamanho)
        barra = "█" * blocos_preenchidos + "-" * (tamanho - blocos_preenchidos)
        return f"|{barra}|"
    
    def habilidade_vampiro(heroi, monstro):
        global pontos_vampiro, ataque_cava
        defesa_cava = herois[0].defesa + herois[0].defesa_e
        lista_monstro[monstro].vida += lista_monstro[monstro].ataque * 0.2
        print(f"       O {lista_monstro[monstro].nome} ganhou {lista_monstro[monstro].ataque * 0.2:.1f} de vida")
        print(f"       e tem {pontos_vampiro} de pontos de habilidade")
        input()
        if pontos_vampiro >= 5:
            pontos_vampiro = 0
            lista_monstro[monstro].vida += lista_monstro[monstro].ataque * 1.5
            herois[0].vida -= (lista_monstro[monstro].ataque * 1.5) - defesa_cava 
            print("\033[31m" + f"{lista_monstro[monstro].nome} utilizou a " + "\033[1m" + "GARRA SANGRENTA" + "\033[0m")
            time.sleep(1.5)
            print(f"{herois[0].nome} sofreu {(lista_monstro[monstro].ataque * 1.5) - defesa_cava} de Dano")
            time.sleep(1.5)
            print(f"Vampiro recuperou {lista_monstro[monstro].ataque * 1.5} de vida")
            time.sleep(1.5)
        else:
            pontos_vampiro += 1  
    
    def habilidade_troll(heroi, troll):
        pass       
   
    def efeito_cavaleiro(cavaleiro):
        print("\033c" , end = "")
        print("\033[35m"+"1 ———> fortificação"+"\033[0m", "        2 pontos")
        print("\033[31m"+"2 ———> afiação"+"\033[0m", "             2 pontos")
        print("\033[34m\033[1m"+"3 ———> fortalecimento"+"\033[0m", "    4 pontos")
        escolha_cava = input("                ")
        if escolha_cava == "1":
            if cavaleiro.contador_efeito >= 2:
                if cavaleiro.quantidade_efeito > 0:
                    cavaleiro.defesa_e += 5
                    cavaleiro.quantidade_efeito -= 1
                    cavaleiro.contador_efeito -= 2
                    efeca = "\033[35m"+"5"+"\033[0m"
                    print("seu herói ganhou %s de %s extra" % (efeca, de2))
                    print()
                    input()
                else:
                    print("você gastou toda sua habilidade")   
                    input()
            else:
                print("sua habilidade ainda não está carregada")
                input()
        elif escolha_cava == "2":  
            if cavaleiro.contador_efeito >= 2:
                if cavaleiro.quantidade_efeito > 0:
                    cavaleiro.ataque_e += 10
                    cavaleiro.quantidade_efeito -= 1
                    cavaleiro.contador_efeito -= 2
                    print("seu herói ganhou","\033[31m"+"10"+"\033[0m", "de", "\033[31m"+"ataque"+"\033[0m" ,"extra")
                    print()
                    input()
                else:
                    print("você gastou toda sua habilidade")   
                    input()
            else:
                print("sua habilidade ainda não está carregada")
                input()    
        elif escolha_cava == "3":
            if cavaleiro.contador_efeito >= 4:
                if cavaleiro.quantidade_efeito > 0:
                    cavaleiro.ataque_e += 10
                    cavaleiro.defesa_e += 5 
                    cavaleiro.quantidade_efeito -= 1
                    cavaleiro.contador_efeito -= 4
                    print("seu herói ganhou","\033[31m"+"10"+"\033[0m", "de", "\033[31m\033[1m"+"ataque"+"\033[0m" ,"extra " + f"e\n", "\033[34m"+"5"+"\033[0m", "de", "\033[35m\033[1m"+"defesa"+"\033[0m", "extra")
                    print()
                    input()
                else:
                    print("você gastou toda sua habilidade")   
                    input()
            else:
                print("sua habilidade ainda não está carregada")
                input()    
        
        else:
            print("opção inválida") 
            input()   
    def dado():
        dada = random.randint(1, 20)
        return dada    
                 
    def lutar(monstro, ataque_dado):
                global dano_2x_tempo, ataque_cava,defesa_cava 
                ataque_troll = lista_monstro[monstro].ataque
                ataque_cava = herois[0].ataque + herois[0].ataque_e + ataque_dado 
                defesa_troll = lista_monstro[monstro].defesa
                defesa_cava = herois[0].defesa + herois[0].defesa_e

                for cavaleiro in herois:
                    if cavaleiro.negar_ataque > 0:
                        ataque_troll -= cavaleiro.negar_ataque 
                        if ataque_troll < 0:
                            ataque_troll = 0                    
                    
                    if dano_2x_tempo > 0:
                        ataque_cava *= 2
                    
                    if ataque_troll > defesa_cava:
                        cavaleiro.vida -= (ataque_troll - defesa_cava)
                        lista_monstro[monstro].vida -= cavaleiro.espinhos                
                    if ataque_cava > defesa_troll:
                        lista_monstro[monstro].vida -= (ataque_cava - defesa_troll)
                    
                    
                    if cavaleiro.negar_ataque > 0:
                        cavaleiro.negar_tempo -= 1 
                        if cavaleiro.negar_tempo < 0:
                            cavaleiro.negar_ataque = 0
                    cavaleiro.contador_efeito += 1   
                    if herois[0].defesa_e > 0:
                        herois[0].defesa_e -= 1
                    if herois[0].ataque_e > 0:
                        herois[0].ataque_e -= 1
                    if dano_2x_tempo > 0:
                        dano_2x_tempo -= 1
                            
                        
    def ataque_monstro(heroi, monstro, ataque_cava):  
                ataque_troll = lista_monstro[monstro].ataque
                ataque_cava = herois[0].ataque + herois[0].ataque_e 
                defesa_troll = lista_monstro[monstro].defesa
                defesa_cava = herois[0].defesa + herois[0].defesa_e

                for cavaleiro in herois:
                    if cavaleiro.negar_ataque > 0:
                        ataque_troll -= cavaleiro.negar_ataque 
                        if ataque_troll < 0:
                            ataque_troll = 0                    
                    
                    if ataque_troll > defesa_cava:
                        cavaleiro.vida -= (ataque_troll - defesa_cava)
                    
                    
                    if cavaleiro.negar_ataque > 0:
                        cavaleiro.negar_tempo -= 1 
                        if cavaleiro.negar_tempo < 0:
                            cavaleiro.negar_ataque = 0
                           
    
    def defender(monstro, defesa_dado):
                global dano_2x_tempo, ataque_cava, defesa_cava 
                ataque_troll = lista_monstro[monstro].ataque
                ataque_cava = herois[0].ataque + herois[0].ataque_e 
                defesa_troll = lista_monstro[monstro].defesa
                defesa_cava = herois[0].defesa + herois[0].defesa_e + defesa_dado

                for cavaleiro in herois:
                    if cavaleiro.negar_ataque > 0:
                        ataque_troll -= cavaleiro.negar_ataque 
                        if ataque_troll < 0:
                            ataque_troll = 0   
                    if dano_2x_tempo > 0:
                        ataque_cava *= 2                  
                    
                    if ataque_troll > defesa_cava:
                        cavaleiro.vida -= (ataque_troll - defesa_cava)
                    if ataque_cava > defesa_troll:
                        lista_monstro[monstro].vida -= (ataque_cava - defesa_troll)
                    
                    
                    if cavaleiro.negar_ataque > 0:
                        cavaleiro.negar_tempo -= 1
                        if cavaleiro.negar_tempo <= 0:
                            cavaleiro.negar_ataque = 0
                    if herois[0].nome_class == "cavaleiro":
                        cavaleiro.contador_efeito += 1     
                    if herois[0].defesa_e > 0:
                        herois[0].defesa_e -= 1
                    if herois[0].ataque_e > 0:
                        herois[0].ataque_e -= 1
                    if dano_2x_tempo > 0:
                        dano_2x_tempo -= 1   
    
    limpar_tela = 21
    
    seuca = "\033[33m" + "cavaleiro" + "\033[0m"
    suahaca = "\033[34m" + "fortalecimento" + "\033[0m"
    
    vid2 = "\033[32m" + " Vida" + "\033[0m"
    ata2 = "\033[31m" + " Ataque" + "\033[0m"
    de2 = "\033[35m" + " Defesa" + "\033[0m"
    
    vid1 = "\033[32m" + "1 - Vida:" + "\033[0m"
    ata1 = "\033[31m" + "2 - Ataque:" + "\033[0m"
    de1 = "\033[35m" + "3 - Defesa:" + "\033[0m"
    
    ni = "\033[34m" + "Nível:" + "\033[0m"
    vid = "\033[32m" + "Vida:" + "\033[0m"
    ata = "\033[31m" + "Ataque:" + "\033[0m"
    de = "\033[35m" + "Defesa:" + "\033[0m"
    ou = "\033[33m" + "Ouro:" + "\033[0m"
    x = "\033[32m" + "XP:" + "\033[0m"
    
    pontos_v = 0
    pontos_a = 0
    pontos_d = 0
    
    class Cavaleiro:
        def __init__(self, nome_class, nome_habilidade, level, vida, vida_meda, ataque, defesa, nome, xp, meta, pontos, ouro, ataque_e, defesa_e, negar_ataque, negar_tempo, efeito, quantidade_efeito, contador_efeito, espinhos):
            self.nome_class = nome_class
            self.nome_habilidade = nome_habilidade
            self.level = level
            self.vida = vida
            self.vida_meda = vida_meda 
            self.ataque = ataque
            self.defesa = defesa
            self.nome = nome
            self.xp = xp
            self.meta = meta
            self.pontos = pontos
            self.ouro = ouro
            self.ataque_e = ataque_e
            self.defesa_e = defesa_e
            self.negar_ataque = negar_ataque 
            self.negar_tempo = negar_tempo
            self.efeito = efeito
            self.quantidade_efeito = quantidade_efeito
            self.contador_efeito = contador_efeito
            self.espinhos = espinhos 
        def level_up(self):
            self.level += 1
            self.vida = self.vida_meda  # Pode ajustar a fórmula de vida ao upar
            self.pontos += 3
            self.meta = 20 + self.level * 5
            helist ="\033[34m" + f"{self.nome} subiu para o nível {self.level}!" + "\033[0m"
            print(f"{helist}")
     
    # Criação do herói
    while limpar_tela > 1:
        print("\033c")
        limpar_tela -= 1

    def definir_personagem():    
        nomedp = input("Qual o nome do seu personagem: ")
        
        print(
        ("\033c") + 
        ("\033[47m\033[30m\033[3m" + f"{'':^43} {'CLASSES':^44} {'':^43}" + "\033[0m\n") +
        ("\033[30m\033[3m\033[47m" + f"{'':^43} {'CAVALEIRO':^44} {'':^43}" + "\n" + f"{'':^45}  {'Habilidade':<20}" + f"{'fortalecimento':^24} {'':^40}" + "\n") +
        (f"{'':^43} {'_':^44} {'':^43}" + "\n") +
        ("\033[32m\033[1m\033[47m" +f"{'':^9} {'Vida':<7}" + f"{'  100':^37}" + "\033[0m") +
        ("\033[31m\033[3m\033[47m" +f"{'Ataque':<7}" + f"{' 10':^37}" + "\033[0m") +
        ("\033[35m\033[3m\033[47m" +f"{'Defesa':<7}" + f"{'5':>18} {'':^8}" + "\033[0m" + "\033[0m" + "\n") + 
        ("\033[30m\033[47m" +f"{'':^41} {'        Objetivos    ':^44} {'':^45}") + '\n' +
        (f"{'':^27} {'  —————————————————————————':<44}") + (f"{'  —————————————————————————':<44} {'':^15}") + '\n' +
        (f"{'':^27} {' |perder o mínimo possível |':<44}") + (f"{' |   derrotar o inimigo o  |':<44} {'':^14} \n ") +
        (f"{'':^27} {'|de vida antes de ativar  |':<44}") + (f"{'|   mais rápido possível  |':<44} {'':^13} \n ") +
        (f"{'':^27} {'|     A Habilidade        |   ':<44}") + (f"{'|                         |':<44} {'':^13} \n ") +
        (f"{'':^27} {' —————————————————————————':<44}") + (f"{' —————————————————————————':<44} {'':^14}" + "\033[0m")

       
       
        
        )

        while True:
            classe_escolhida = input("qual classe você escolhe: ")
            classe_escolhida = classe_escolhida.lower()
            if classe_escolhida == "cavaleiro":
                p_cavaleiro = Cavaleiro("cavaleiro", "fortalecimento", 0, 100 + 5 * pontos_v, 100 + 5 * pontos_v, 10 + 2 * pontos_a, 5 + 2 * pontos_d, nomedp, 0, 20, 0, 10, 0, 0, 0, 0, efeito_cavaleiro, 2, 0, 0)   
                herois.append(p_cavaleiro)
                break 
            if classe_escolhida == "exit":
                exit()
            else:
                print("escolha inválida")   

        return nomedp

    nomee = definir_personagem()

    def jogo_em_si():
     while True:
        herois[0].ouro += 0
        
        for cavaleiro in herois:
            if cavaleiro.xp >= cavaleiro.meta:
                while cavaleiro.xp >= cavaleiro.meta:
                    cavaleiro.xp -= cavaleiro.meta
                    cavaleiro.level_up()
                    
        print("\033c")
        print()
        print('1 - Jogar dado')
        print('2 - Gerar monstros')
        print('3 - Mostrar stats')
        print()
        print("4  " + "\033[44m"+f"{'————————— Upar stats —————————':^40}"+"\033[0m")
        print()
        print("5  " + "\033[41m"+f"{'———————————— Lutar ———————————':^40}"+"\033[0m")
        print()
        print("6  " + "\033[43m"+f"{'———————————— Loja ————————————':^40}"+"\033[0m")
        print()
        escolha = input('Escolha: ')
        
        if escolha == '1':
             
            print(f'                 ⚁{dado()}')   
        
        elif escolha == '2':
            
            class monstro:
                def __init__(self, nome, level, vida, vida_meta, ataque, defesa, xp, ouro, habilidade):
                    self.nome = nome
                    self.level = level
                    self.vida = vida
                    self.vida_meta = vida_meta
                    self.ataque = ataque 
                    self.defesa = defesa
                    self.xp = xp
                    self.ouro = ouro
                    self.habilidade = habilidade 
                    
            
            for _ in range(5):
                level = random.randint(herois[0].level - 5, herois[0].level + 10)
                if level < 0:
                    level = 0
                monstro_raca = random.randint(1, 3)
                if monstro_raca == 1 or monstro_raca == 2:
                    troll = monstro("\033[32m"+"Troll"+"\033[0m", level, 100 + 10 * level, 100 + 10 * level, 10 + 3 * level + random.randint(0, 7), 5 + 3 + 3 * level, 10 + 2 * level + (100 + 10 * level) / 10, 10 + ((100 + 10 * level) * 0.1) + ((10 + 3 * level + random.randint(0, 7)) * 0.2) + level, habilidade_troll)
                    lista_monstro.append(troll)
                if monstro_raca == 3:
                    vampiro = monstro("\033[31m"+"Vampiro"+"\033[0m", level, 75 + 5 * level, 75 + 5 * level, 10 + 5 * level + random.randint(0, 5), 3 + 3 + 3 * level, 15 + 4 * level + (100 + 10 * level) / 9, 10 + ((100 + 10 * level) * 0.1) + ((10 + 3 * level + random.randint(0, 7)) * 0.5) + level, habilidade_vampiro)  
                    lista_monstro.append(vampiro)                
            for monstro in lista_monstro:
                if monstro.level <= 0:
                    monstro.level = 0
            
            for troll in lista_monstro:
                print(f'{troll.nome} - Nível: {troll.level}, Vida: {troll.vida}, Ataque: {troll.ataque}, Defesa: {troll.defesa}, XP: {troll.xp:.2f}')
                print()
            input()
            print("\033c" , end = "")  
        
        elif escolha == '4':
            for cavaleiro in herois:
                
                print(f'\n{vid1} {cavaleiro.vida}')
                print(f'{ata1} {cavaleiro.ataque}')
                print(f'{de1} {cavaleiro.defesa}')
                print()
                print(f'Você tem {cavaleiro.pontos} pontos para gastar.')
                print()
                escolha_stat = int(input('Qual stat você quer melhorar: '))
                pontos = int(input('Quantos pontos você quer gastar: '))
                
                if pontos > cavaleiro.pontos:
                    print('Você colocou mais pontos do que tem!')
                    continue

                if escolha_stat == 1:
                    cavaleiro.vida += 5 * pontos
                    cavaleiro.vida_meda += 5 * pontos
                    cavaleiro.pontos -= pontos
                    print(f'Sua vida agora é {cavaleiro.vida}.')
                elif escolha_stat == 2:
                    cavaleiro.ataque += 3 * pontos
                    cavaleiro.pontos -= pontos
                    print(f'Seu ataque agora é {cavaleiro.ataque}.')
                elif escolha_stat == 3:
                    cavaleiro.defesa += 1.5 * pontos
                    cavaleiro.pontos -= pontos
                    print(f'Sua defesa agora é {cavaleiro.defesa}.')
                else:
                    print('Opção inválida.')
                input()    
      
        elif escolha == '3':
            for cavaleiro in herois:
                print()
                print(f'Nome: {cavaleiro.nome}')
                print(f'{ni} {cavaleiro.level}')
                print(f'{vid} {cavaleiro.vida}')
                print(f'{ata} {cavaleiro.ataque}')
                print(f'{de} {cavaleiro.defesa}')
                print(f'{x} {cavaleiro.xp:.2f}')
                print(f"{ou} {cavaleiro.ouro:.2f}")
                print(f"Pontos de evolução: {cavaleiro.pontos}")
                print()
                print("\033[41m"+"          monstros derrotados           "+"\033[0m")
                if monstro_morto:
                    for i, monstro in enumerate(monstro_morto):
                        nome_monstro = monstro_morto[i].nome
                        nível_monstro = monstro_morto[i].level
                        print("\033[2m\033[9m\033[34m" + f"{nome_monstro}" + ":" + "\033[0m","\033[34m\033[2m" + "Nível " + f"{nível_monstro}" + "\033[0m")
                    input()
                else:
                    print("você não tem monstros derrotados")
                input()    
                        
        elif escolha == "5":
            i = 0
            lista_monstro.sort(key = lambda monstro: monstro.level)
            for troll in lista_monstro:
                print(f'{i} --> {troll.nome} - Nível: {troll.level} \n Vida: {troll.vida}\n Ataque: {troll.ataque} \n Defesa: {troll.defesa}\n XP: {troll.xp:.2f} \n')
                i += 1
            
            print("Escolha um monstro para lutar")
            monstro = int(input("              "))
            print("\033c")
            limpeza = 0
            if lista_monstro[monstro]:
             while lista_monstro[monstro].vida > 0 and herois[0].vida > 0:
                if limpeza != 0:
                    lista_monstro[monstro].habilidade(herois[0], monstro)
                print()
                defes = "\033[35m"+"1 - Defender"+"\033[0m"
                bata = "\033[31m" + "2 - Atacar" + "\033[0m"
                vi = "\033[33m" + "3 - Ver inventário" + "\033[0m"
                habi = "\033[34m\033[1m" + "4 - usar habilidade" + "\033[0m"
                print("\033c", end = "")
                print(
"\033[33m"+f"{herois[0].nome:<35}"+"\033[0m" + f"   {lista_monstro[monstro].nome}\n" 
"\033[34m"+f"{'Nível:':<7}" , f"{herois[0].level:<30}" + f"{'Nível:':<7}"+ f"{lista_monstro[monstro].level}\n"+"\033[0m" +
"\033[32m"+f"{'Vida:':<7}" , f"{herois[0].vida:<30}" + f"{'Vida:':<7}" + f"{lista_monstro[monstro].vida:.2f}  \n"+"\033[0m" +   
"\033[32m"+f"{barra_de_vida(herois[0].vida, herois[0].vida_meda):<37}" + f"{barra_de_vida(lista_monstro[monstro].vida ,lista_monstro[monstro].vida_meta)}\n"+"\033[0m" +
("\033[31m"+f"{'Ataque: ':<7}" + f"{(herois[0].ataque + herois[0].ataque_e) * 2:<30}" + f"{'Ataque':<7}"+ f"{lista_monstro[monstro].ataque}\n"+"\033[0m" if dano_2x_tempo > 0 
else "\033[31m"+f"{'Ataque: ':<7}" + f"{herois[0].ataque + herois[0].ataque_e:<30}" + f"{'Ataque':<7}"+ f"{lista_monstro[monstro].ataque}\n"+"\033[0m") +            
"\033[35m"+f"{'Defesa:':<7}" , f"{herois[0].defesa + herois[0].defesa_e:<30}" + f"{'Defesa:':<7}" + f"{lista_monstro[monstro].defesa}\n"+"\033[0m" +
("\033[34m"+"pontos de habilidade:"+ f"{herois[0].contador_efeito}\n" + "\033[0m" if herois[0].contador_efeito > 0 else "") +
("\033[31m\033[1m\033[2m"+"2X Dano:"+f"{dano_2x_tempo:<10}\n"+"\033[0m" if dano_2x_tempo > 0 else "") +
("\033[31m\033[2m"+"Ataque extra:"+ f"{herois[0].ataque_e:<10}\n"+"\033[0m" if herois[0].ataque_e > 0 else"") +
("\033[35m\033[2m"+"Defesa extra:"+ f"{herois[0].defesa_e:<10}\n"+"\033[0m" if herois[0].defesa_e > 0 else"") +
("\033[31m\033[3m\033[9m\033[2m"+"negar ataque:" + f"{herois[0].negar_tempo:<10}\n" + "\033[0m" if herois[0].negar_ataque > 0 else"") +
("\033[34m\033[2m\033[9m"+"Espinhos:"+ f"{herois[0].espinhos:<10}\n"+"\033[0m" if herois[0].espinhos > 0 else"") 
)
                print()
                opção = input("{} \n{} \n{} \n{} \n        ".format(defes, bata, vi, habi))
                opção = opção.lower()
                print("\033c")
                if opção == "2":
                    limpeza = 1
                    ataque_dado = dado()
                    print("\033c", end = "")
                    print(
    (
        "\033[31m\033[1m" + f"{ataque_dado:>23}⚁" + "\033[0m" 
        if ataque_dado >= 15 
        else "\033[31m" + f"{ataque_dado:>23}⚁" + "\033[0m" 
        if ataque_dado >= 9 
        else "\033[31m\033[2m" + f"{ataque_dado:>23}⚁" + "\033[0m" 
        if ataque_dado >= 1 
        else ""
    )
                    )
                    print("\0337", end = "")
                    time.sleep(1)
                    print(
"\033[33m"+f"{herois[0].nome:35}"+"\033[0m" + f"   {lista_monstro[monstro].nome}\n" 
"\033[34m"+f"{'Nível:':<7}" , f"{herois[0].level:30}" + f"{'Nível:':<7}"+ f"{lista_monstro[monstro].level}\n"+"\033[0m" +
"\033[32m"+f"{'Vida:':<7}" , f"{herois[0].vida:<30}" + f"{'Vida:':<7}" + f"{lista_monstro[monstro].vida:.2f}  \n"+"\033[0m" +   
"\033[32m"+f"{barra_de_vida(herois[0].vida, herois[0].vida_meda):37}" + f"{barra_de_vida(lista_monstro[monstro].vida ,lista_monstro[monstro].vida_meta)}\n"+"\033[0m" +
("\033[31m"+f"{'Ataque: ':<7}" + f"{(herois[0].ataque + herois[0].ataque_e) * 2:<30}" + f"{'Ataque':<7}"+ f"{lista_monstro[monstro].ataque}\n"+"\033[0m" if dano_2x_tempo > 0 
else "\033[31m"+f"{'Ataque: ':<7}" + f"{herois[0].ataque + herois[0].ataque_e:<30}" + f"{'Ataque':<7}"+ f"{lista_monstro[monstro].ataque}\n"+"\033[0m") +            
"\033[35m"+f"{'Defesa:':<7}" , f"{herois[0].defesa + herois[0].defesa_e:<30}" + f"{'Defesa:':<7}" + f"{lista_monstro[monstro].defesa}\n"+"\033[0m" +
("\033[34m"+"pontos de habilidade:"+ f"{herois[0].contador_efeito}\n" + "\033[0m" if herois[0].contador_efeito > 0 else "") +
("\033[31m\033[1m\033[2m"+"2X Dano:"+f"{dano_2x_tempo}\n"+"\033[0m" if dano_2x_tempo > 0 else "") +
("\033[31m\033[2m"+"Ataque extra:"+ f"{herois[0].ataque_e}\n"+"\033[0m" if herois[0].ataque_e > 0 else"") +
("\033[35m\033[2m"+"Defesa extra:"+ f"{herois[0].defesa_e}\n"+"\033[0m" if herois[0].defesa_e > 0 else"") +
("\033[31m\033[3m\033[9m\033[2m"+"negar ataque:" + f"{herois[0].negar_tempo}" + "\033[0m" if herois[0].negar_ataque > 0 else"") +
("\033[34m\033[2m\033[9m"+"Espinhos:"+ f"{herois[0].espinhos}\n"+"\033[0m" if herois[0].espinhos > 0 else"") 
)
                    lutar(monstro, ataque_dado)
                    time.sleep(0.75)                   
                    print("\0338", end = "")
                    print(
"\033[33m"+f"{herois[0].nome:<35}"+"\033[0m" + f"   {lista_monstro[monstro].nome}\n" 
"\033[34m"+f"{'Nível:':<7}" , f"{herois[0].level:<30}" + f"{'Nível:':<7}"+ f"{lista_monstro[monstro].level}\n"+"\033[0m" +
"\033[32m"+f"{'Vida:':<7}" , f"{herois[0].vida:<30}" + f"{'Vida:':<7}" + f"{lista_monstro[monstro].vida:.2f}  \n"+"\033[0m" +   
"\033[32m"+f"{barra_de_vida(herois[0].vida, herois[0].vida_meda):<37}" + f"{barra_de_vida(lista_monstro[monstro].vida ,lista_monstro[monstro].vida_meta)}\n"+"\033[0m" +
"\033[31m"+f"{'Ataque: ':<7}" + f"{ataque_cava:<30}" + f"{'Ataque':<7}"+ f"{lista_monstro[monstro].ataque}\n"+"\033[0m" +
"\033[35m"+f"{'Defesa:':<7}" , f"{herois[0].defesa + herois[0].defesa_e:<30}" + f"{'Defesa:':<7}" + f"{lista_monstro[monstro].defesa}\n"+"\033[0m" +
("\033[34m"+"pontos de habilidade:"+ f"{herois[0].contador_efeito}\n" + "\033[0m" if herois[0].contador_efeito > 0 else "") +
("\033[31m\033[1m\033[2m"+"2X Dano:"+f"{dano_2x_tempo}\n"+"\033[0m" if dano_2x_tempo > 0 else "") +
("\033[31m\033[2m"+"Ataque extra:"+ f"{herois[0].ataque_e}\n"+"\033[0m" if herois[0].ataque_e > 0 else"") +
("\033[35m\033[2m"+"Defesa extra:"+ f"{herois[0].defesa_e}\n"+"\033[0m" if herois[0].defesa_e > 0 else"") +
("\033[31m\033[3m\033[9m\033[2m"+"negar ataque:" + f"{herois[0].negar_tempo}" + "\033[0m" if herois[0].negar_ataque > 0 else"") +
("\033[34m\033[2m\033[9m"+"Espinhos:"+ f"{herois[0].espinhos}\n"+"\033[0m" if herois[0].espinhos > 0 else"") 
)
                    time.sleep(1)
                    
                          
                    
                elif opção == "3":
                    while True:
                        print("\033c",end = "")
                        print(f"{ou} {herois[0].ouro:.2f}")
                    
                        for i, item in enumerate(itens):
                            print(f" {i} --->  {item.nome_item} quantidade {item.quantidade}\n")
                    
                        inventário_uso = input("o que você vai usar: ")
                        try:
                            inventário_uso = int(inventário_uso)
                        except:
                            print("você não falou um número")
                            time.sleep(1)
                            continue
                        if inventário_uso < len(itens):
                         if itens[inventário_uso].nome_item == "poção de vida":
                            print(f"sua {vid2} era: {herois[0].vida}")
                            itens[inventário_uso].efeito(itens[inventário_uso], herois[0])
                            print(f"sua {vid2} agora é: {herois[0].vida}")
                            input()
                            break
                         elif itens[inventário_uso].nome_item == "poção de ataque":
                            print(f"seu {ata2} era: {herois[0].ataque}")
                            itens[inventário_uso].efeito(itens[inventário_uso], herois[0])
                            print(f"seu {ata2} agora é: {herois[0].ataque + herois[0].ataque_e}")
                            input()
                            break
                         elif itens[inventário_uso].nome_item == "poção de defesa":
                            print(f"sua {de2} era: {herois[0].defesa}")
                            itens[inventário_uso].efeito(itens[inventário_uso], herois[0])
                            print(f"sua {de2} agora é: {herois[0].defesa + herois[0].defesa_e}")
                            input()
                            break
                         elif itens[inventário_uso].nome_item == "Batata de negar ataque":
                            itens[inventário_uso].efeito(itens[inventário_uso], herois[0])
                            print(f"você agora vai defender {herois[0].negar_tempo} ataques")
                            input()
                            break
                         elif itens[inventário_uso].nome_item == "poção de espinhos":
                            itens[inventário_uso].efeito(itens[inventário_uso], herois[0])
                            print(f"você agora tem","\033[34m"+f"{herois[0].espinhos}"+"\033[0m","de","\033[34m\033[2m\033[9m"+"espinhos"+"\033[0m")
                            input()
                            break
                         elif itens[inventário_uso].nome_item == "2X dano":
                            itens[inventário_uso].efeito(itens[inventário_uso], herois[0])
                            print(f"seus ataques agora vão ter "+"\033[31m\033[1m"+"2X Dano "+f"{dano_2x_tempo}" + "vezes"+"\033[0m")
                            input()
                            break
                         else:
                            pass  
                        else:
                            print ("esse item não está em sua bolsa")    
                            time.sleep(1.5)
               
               
                elif opção == ("1"):
                    limpeza = 1
                    defesa_dado = dado()
                    print("\033c" , end = "")
                    print(
     (
      "\033[35m\033[1m" + f"{defesa_dado:>20}⚁" + "\033[0m" 
      if defesa_dado >= 15
      else
      "\033[35m" + f"{defesa_dado:>20}⚁" + "\033[0m" 
      if defesa_dado >= 10
      else
      "\033[35m\033[2m" + f"{defesa_dado:>20}⚁" + "\033[0m" 
      if defesa_dado >= 1
      else "")
)
                    print("\0337" ,end = "")
                    time.sleep(1)
                    print(
"\033[33m"+f"{herois[0].nome:<35}"+"\033[0m" + f"   {lista_monstro[monstro].nome}\n" 
"\033[34m"+f"{'Nível:':<7}" , f"{herois[0].level:<30}" + f"{'Nível:':<7}"+ f"{lista_monstro[monstro].level}\n"+"\033[0m" +
"\033[32m"+f"{'Vida:':<7}" , f"{herois[0].vida:<30}" + f"{'Vida:':<7}" + f"{lista_monstro[monstro].vida:.2f}  \n"+"\033[0m" +   
"\033[32m"+f"{barra_de_vida(herois[0].vida, herois[0].vida_meda):<37}" + f"{barra_de_vida(lista_monstro[monstro].vida ,lista_monstro[monstro].vida_meta)}\n"+"\033[0m" +
("\033[31m"+f"{'Ataque: ':<7}" + f"{(herois[0].ataque + herois[0].ataque_e) * 2:<30}" + f"{'Ataque:':<7}"+ f"{lista_monstro[monstro].ataque}\n"+"\033[0m" if dano_2x_tempo > 0 
else "\033[31m"+f"{'Ataque: ':<7}" + f"{herois[0].ataque + herois[0].ataque_e:<30}" + f"{'Ataque:':<7}"+ f"{lista_monstro[monstro].ataque}\n"+"\033[0m") +            
"\033[35m"+f"{'Defesa:':<7}" , f"{herois[0].defesa + herois[0].defesa_e:<30}" + f"{'Defesa:':<7}" + f"{lista_monstro[monstro].defesa}\n"+"\033[0m" +
("\033[34m"+"pontos de habilidade:"+ f"{herois[0].contador_efeito}\n" + "\033[0m" if herois[0].contador_efeito > 0 else "") +
("\033[31m\033[1m\033[2m"+"2X Dano:"+f"{dano_2x_tempo}\n"+"\033[0m" if dano_2x_tempo > 0 else "") +
("\033[31m\033[2m"+"Ataque extra:"+ f"{herois[0].ataque_e}\n"+"\033[0m" if herois[0].ataque_e > 0 else"") +
("\033[35m\033[2m"+"Defesa extra:"+ f"{herois[0].defesa_e}\n"+"\033[0m" if herois[0].defesa_e > 0 else"") +
("\033[31m\033[3m\033[9m\033[2m"+"negar ataque:" + f"{herois[0].negar_tempo}" + "\033[0m" if herois[0].negar_ataque > 0 else"") +
("\033[34m\033[2m\033[9m"+"Espinhos:"+ f"{herois[0].espinhos}\n"+"\033[0m" if herois[0].espinhos > 0 else"") 
)
                    defender(monstro, defesa_dado)
                    time.sleep(0.75)
                    print("\0338", end = "")
                    print(
"\033[33m"+f"{herois[0].nome:<35}"+"\033[0m" + f"   {lista_monstro[monstro].nome}\n" 
"\033[34m"+f"{'Nível:':<7}" , f"{herois[0].level:<30}" + f"{'Nível:':<7}"+ f"{lista_monstro[monstro].level}\n"+"\033[0m" +
"\033[32m"+f"{'Vida:':<7}" , f"{herois[0].vida:<30}" + f"{'Vida:':<7}" + f"{lista_monstro[monstro].vida:.2f}  \n"+"\033[0m" +   
"\033[32m"+f"{barra_de_vida(herois[0].vida, herois[0].vida_meda):<37}" + f"{barra_de_vida(lista_monstro[monstro].vida ,lista_monstro[monstro].vida_meta)}\n"+"\033[0m" +
"\033[31m"+f"{'Ataque: ':<7}" + f"{ataque_cava:<30}" + f"{'Ataque':<7}"+ f"{lista_monstro[monstro].ataque}\n"+"\033[0m" +
"\033[35m"+f"{'Defesa:':<7}" , f"{herois[0].defesa + defesa_dado + herois[0].defesa_e:<30}" + f"{'Defesa:':<7}" + f"{lista_monstro[monstro].defesa}\n"+"\033[0m" +
("\033[34m"+"pontos de habilidade:"+ f"{herois[0].contador_efeito}\n" + "\033[0m" if herois[0].contador_efeito > 0 else "") +
("\033[31m\033[1m\033[2m"+"2X Dano:"+f"{dano_2x_tempo}\n"+"\033[0m" if dano_2x_tempo > 0 else "") +
("\033[31m\033[2m"+"Ataque extra:"+ f"{herois[0].ataque_e}\n"+"\033[0m" if herois[0].ataque_e > 0 else"") +
("\033[35m\033[2m"+"Defesa extra:"+ f"{herois[0].defesa_e}\n"+"\033[0m" if herois[0].defesa_e > 0 else"") +
("\033[31m\033[3m\033[9m\033[2m"+"negar ataque:" + f"{herois[0].negar_tempo}" + "\033[0m" if herois[0].negar_ataque > 0 else"") +
("\033[34m\033[2m\033[9m"+"Espinhos:"+ f"{herois[0].espinhos}\n"+"\033[0m" if herois[0].espinhos > 0 else"") 
)
                    time.sleep(0.75)  
                elif opção == ("4"):
                    print("O herói da classe {} vai usar a \nhabilidade \"{}\"".format(seuca, suahaca))
                    input()
                    herois[0].efeito(herois[0])
                    ataque_monstro(herois[0], monstro, ataque_cava)         

                elif opção == ("exit"):
                    exit()    

                else:
                    print("Opção inválida.")
                if herois[0].vida <= 0:
                        print(f"{herois[0].nome} foi derrotado!")
                        time.sleep(1)
                        game_over()   
                elif lista_monstro[monstro].vida <= 0:
                        litrom ="\033[31m" + f"{lista_monstro[monstro].nome} foi derrotado!" + "\033[0m"
                        print(f"{litrom}")
                        herois[0].xp += lista_monstro[monstro].xp
                        herois[0].ouro += lista_monstro[monstro].ouro
                        herois[0].ataque_e = 0
                        herois[0].defesa_e = 0
                        herois[0].contador_efeito = 0
                        herois[0].espinhos = 0
                        print(f"você ganhou "+"\033[32m"+f"{lista_monstro[monstro].xp} de "+"\033[0m"+"\033[32m"+"EXP"+"\033[0m"+".")
                        print("você ganhou "+"\033[33m"+f"R$ {lista_monstro[monstro].ouro}"+"\033[0m"+".")
                        input()
                        monstro_morto.append(lista_monstro.pop(monstro))
                        herois[0].quantidade_efeito = 2
                        break
        elif escolha == ("6"):  
            while True:
                print("\033c", end= "")
                print("\033[43m" + f'{"":^42}' + "                                            " + f'{"":^42}' + "\033[0m")
                print("\033[37m\033[43m\033[1m" + f'{"":^42}' + "                    Loja                    " + f'{"":^42}' + "\033[0m")
                print("\033[43m" + f'{"":^42}' + "                                            " + f'{"":^42}' + "\033[0m")
                print()
                print(f" você tem R$ {herois[0].ouro}")
                print()        
                print(f'{"":^42}' + "1 --->","\033[31m"+"poção de cura"+"\033[0m","                R$ 50")
                print(f'{"":^42}' + "2 --->","\033[31m\033[1m"+"poção de ataque"+"\033[0m","              R$ 50")
                print(f'{"":^42}' + "3 --->","\033[35m"+"poção de defesa"+"\033[0m","              R$ 50")
                print(f'{"":^42}' + "4 --->","\033[33m\033[3m"+"batata de negar ataque"+"\033[0m","       R$ 75")
                print(f'{"":^42}' + "5 --->","\033[34m\033[2m\033[9m"+"poção de espinhos"+"\033[0m","            R$ 40")
                print(f'{"":^42}' + "6 --->","\033[31m\033[1m"+"poção de dobro de dano"+"\033[0m","       R$ 75")
                print()
                print("\033[31m" + f'{"":^42}' + "0 ——————————>   SAIR DA LOJA               "+"\033[0m")            
                
                
                it = input(f'{"":^42}' + "                    ")
                if it == "1":
                    if herois[0].ouro >= 50:
                        poção1 = ("\033[32m"+"poção de vida"+"\033[0m")
                        print("você comprou uma {}".format(poção1))
                        herois[0].ouro -= 50
                        nova_p_vida = poçãos("poção de vida", 1, curar_vida)
                        itens.append(nova_p_vida)
                        time.sleep(1)
                    else:
                        print("você não tem dinheiro suficiente") 
                        print("Falta " + "\033[33m" + "R$" + f"{ 50 - herois[0].ouro}" + "\033[0m")    
                        time.sleep(1.5)       
                elif it == "2":
                    if herois[0].ouro >= 50:
                        if herois[0].ouro >= 50:
                            poção2 = ("\033[31m"+"poção de ataque"+"\033[0m")
                            print("você comprou uma {}".format(poção2))
                            time.sleep(1)
                            herois[0].ouro -= 50
                            nova_p_ataque = poçãos("poção de ataque", 1, pocao_ataque)  
                            itens.append(nova_p_ataque)  
                            time.sleep(1)         
                        else:
                            print("você não tem dinheiro suficiente") 
                            print("Falta " + "\033[33m" + "R$" + f"{ 50 - herois[0].ouro}" + "\033[0m")    
                            time.sleep(1.5)       
                    else:
                        print("você não tem dinheiro suficiente") 
                        print("Falta " + "\033[33m" + "R$" + f"{ 50 - herois[0].ouro}" + "\033[0m")    
                        time.sleep(1.5)       
                elif it == ("3"):
                    if herois[0].ouro >= 50:
                        poção3 = "\033[35m" + "poção de defesa" + "\033[0m"
                        print("você comprou uma {}".format(poção3))
                        herois[0].ouro -= 50
                        nova_p_defesa = poçãos("poção de defesa", 1, pocao_defesa)
                        itens.append(nova_p_defesa)
                        time.sleep(1)
                    else:
                         print("você não tem dinheiro suficiente") 
                         print("Falta " + "\033[33m" + "R$" + f"{ 50 - herois[0].ouro}" + "\033[0m")    
                         time.sleep(1.5)       
                elif it == ("4"):
                    if herois[0].ouro >= 75:
                        herois[0].ouro -= 75
                        poção4 = "\033[34m"+"batata de negar ataque"+"\033[0m"
                        print("você comprou uma {}".format(poção4))
                        nova_batata = poçãos("Batata de negar ataque", 1, pocao_negar_ataque)
                        itens.append(nova_batata)
                        time.sleep(1)   
                    else:
                         print("você não tem dinheiro suficiente") 
                         print("Falta " + "\033[33m" + "R$" + f"{ 75 - herois[0].ouro}" + "\033[0m")    
                         time.sleep(1.5)          
                elif it == "5":
                    if herois[0].ouro >= 40:
                        print("você comprou uma","\033[9m\033[2m\033[34m" + "poção de espinhos" + "\033[0m")
                        nova_p_espinhos = poçãos("poção de espinhos", 1 , pocao_espinhos)
                        itens.append(nova_p_espinhos)
                        time.sleep(1)
                    else:
                        print("você não tem dinheiro suficiente")
                        print("Falta " + "\033[33m" + "R$" + f"{ 40 - herois[0].ouro}" + "\033[0m")    
                        time.sleep(1.5)       
                elif it == "6":
                    if herois[0].ouro >= 75:
                        print("você comprou uma poção de "+"\033[31m\033[1m"+"dobro de dano"+"\033[0m")
                        nova_p_dobro_de_dano = poçãos("2X dano", 1, dano_2x)
                        itens.append(nova_p_dobro_de_dano)
                        time.sleep(1)
                    else:
                        print("você não tem dinheiro suficiente") 
                        print("Falta " + "\033[33m" + "R$" + f"{ 75 - herois[0].ouro}" + "\033[0m")    
                        time.sleep(1.5)       
                elif it == ("0"):
                    print("boa aventura")
                    time.sleep(1)
                 
                    break                 
                else:
                    print("você não escolheu nenhum item disponível")
                    time.sleep(1)

        elif escolha == ("exit"): # isso é para encerar logo
            print("\033c")
            exit()

        elif escolha == ("df1reset"): # isso é para testar layout das classes
            definir_personagem()

        else:
            print("Opção inválida.")
    jogo_em_si()       
        
            

# Inicia o jogo
jogo()