import os
import sys

print ("""

BEM VINDO A TOOL DESENVOLVIDA PELO MRX.
USE COM SABEDORIA.
APOIADOR(A): CYBER STELF
""")

print ("""
[A] - Atualizador de repositórios
[B] - Aulas
[C] - O que é a Cyber Stelf?
""")

aux = input(":_>")

if aux == 'b' or aux == "B":
    print ("""
    Seja bem-vindo a central de aulas via linha de terminal
    Criador : MRX
    Apoiadores : Cyber Stelf
    Modo de uso: Digite o número de sua dúvida corretamente como aparece e terá a resposta em seu terminal
    """)

    print ("")
    print ("")

    print (' [01] - O que é um trojan?  ')
    print (' [02] - O que é um Pentest? ')
    print (' [03] - Quais as fases de um ataque? ')
    print (' [04] - O que é um backdoor? ')
    print (' [05] - O que é um White Hat? ')
    print (' [06] - O que é um Black Hat? ')
    print (' [07] - O que é um Gray Hat? ')
    print (' [08] - O que é um Lammer? ')
    print (' [09] - O que é um Script Kiddie? ')
    print (' [10] - O que é um Vírus? ')
    print (' [11] - O que é um worm? ')
    print (' [12] - Quais os tipo de pentest? ')
    print (' [13] - O que é o NetCat?')
    print (' [14] - O que é um Keylogger? ')
    print (' [15] - O que é um BruteForce? ')
    print (' [16] - Rainbow Crack ')
    print (' [17] - Entendendo Aplicações Web ')
    print (' [18] - O que é Negativação de Serviços? ')
    print (' [19] - Ataque Dos = Entenda ')
    print (' [20] - Ataque DDoS = Entenda ')
    print (' [21] - O que é Ping Flood? ')
    print (' [22] - O que é SYN Flood? ')
    print (' [23] - O que é um Smurf Attack? ')
    print (' [24] - O que é Sequestro de Sessão? ')
    print (' [25] - O que é um Sniffer? ')
    print (' [26] - Como surgiu o Sniffer? ')
    print (' [27] - O que é um DNS Pharming? ')
    print (' [28] - O que é um Exploit? ')
    print (' [29] - O que é um Buffer Overflow? ')
    print (' [30] - O que é Metasploit Framework? ')
    print (' [31] - O que é Google Hacking? ')
    print (' [32] - O que são portas HTTPS? ')
    print (' [33] - O que são portas FTP? ')
    print (' [34] - O que são portas SSH? ')
    print (" [35] - O que é um Host? ")

if aux == "C" or aux == "c":
    print ("""
    =================
       CYBER STELF 
    =================
    A Cyber Stelf é um grupo dedicado a ajudar pessoas que querem aprender hacking e que querem
    ter conhecimento sobre o assunto, procuramos ajudar a sociedade, sem burocracia, atendemos a 
    denúncias e corremos atras para resolver-las, nosso foco maior são as pessoas! A Cyber Stelf
    está com você até o fim!

    LINK: https://chat.whatsapp.com/DIwPHjV1Ftf6g6mrlYVHNU

    [Exit] - Sair 
    """)

if aux == "a" or aux == "A":
    print ("""

    [1] - Atualizar Repositórios
    [2] - Instalar python
    [3] - Instalar python2
    [4] - Instalar PHP
    [5] - Instalar Openssh
    [6] - Instalar Ruby
    [7] - Instalar Perl
    [8] - Instalar Curl
    [9] - Instalar Dart
    [-A] - Instalar Python 2 - Termux
    [-B] - Instalar Openssh - Termux
""")

aux = input(":_>")

if aux == '01' or aux == '1':
    print ("Atualizando repositórios aguarde...")
    os.system("clear")
    os.system("apt upgrade -y && apt update -y")
    os.system("clear")

elif aux == '02' or aux == '2':
    print ("Instalando Python aguarde...")
    os.system("clear")
    os.system("apt-get install python -y")
    os.system("clear")

elif aux == '03' or aux == '3':
    print ("Instalando Python2 aguarde...")
    os.system("clear")
    os.system("apt-get install python2 -y")
    os.system("clear")

elif aux == '04' or aux == '4':
    print ("Instalando PHP aguarde...")
    os.system("clear")
    os.system("apt-get install php -y")
    os.system("clear")

elif aux == '05' or aux == '5':
    print ("Instalando Openssh aguarde...")
    os.system("clear")
    os.system("apt-get install openssh -y")
    os.system("clear")

elif aux == '06' or aux == '6':
    print ("Instalando Ruby aguarde...")
    os.system("clear")
    os.system("apt-get install ruby -y")
    os.system("clear")

elif aux == '07' or aux == '7':
    print ("Instalando Perl aguarde...")
    os.system("clear")
    os.system("apt-get install perl -y")
    os.system("clear")

elif aux == '08' or aux == '8':
    print ("Instalando Curl aguarde...")
    os.system("clear")
    os.system("apt-get install Curl -y")
    os.system("clear")

elif aux == '09' or aux == "9":
    print ("Instalando Dart aguarde...")
    os.system("clear")
    os.system("apt-get install dart -y")
    os.system("clear")

elif aux == "-a" or aux == "-A":
    print("Instalando Python2 no seu terminal Termux aguarde...")
    os.system("clear")
    os.system("apt update -y & apt upgrade -y")
    os.system("apt install python2 -y")
    os.system("clear")

elif aux == "-B" or aux == "-b":
    print("Instalando Openssh no seu terminal Termux aguarde...")
    os.system("clear")
    os.system("apt update -y & apt upgrade -y")
    os.system("apt install openssh -y")
    os.system("clear")

if aux == '01' or aux == '01':
    print ('+----------------------------------------------------------------------------------+')
    print ('|        ---> VOCÊ ESCOLHEU A OPÇÃO 1 <--- // --> Oque é um trojan <--             |')
    print ('+----------------------------------------------------------------------------------+')
    print ('|--> Os cavalos de troias ¨Trojans¨ são programas que funcionam aparentemente nor- |')
    print ('|   -mais, mas na verdade acaba realizando outras tarefas sem que o usuário tome   |')
    print ('|   conhecimento. Quando rodamos um jogo, conseguimos jogar normalmente, mas na    |')
    print ('|   verdade , além do jogo, podem estar sendo executado outros programas em con-   |')
    print ('|   -juntos para dar acesso ao seu computador a um possivel atacante quando voce   |')
    print ('|   se conectar a internet ou então, voce pode ter informações roubadas e enviadas |')
    print ('|   por e-mail para o atacante, ou onde for a imaginação do hacker! <--            |')
    print ('+----------------------------------------------------------------------------------+')
     

elif aux == '02' or aux == '02':
    print ('+------------------------------------------------------------------------------+')
    print ('|      ---> VOCÊ ESCOLHEU A OPÇÃO 2 <--- // --> Oque é um Pentest? <--         |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> O Teste de Intrusão é um processo de análise detalhada do nível de segu-  |')
    print ('|    rança de um sistema ou rede usando perspectiva de um infrator. Trata-se   |')
    print ('|    de um teste realista de auto nível de segurança das infra-estruturas e    |')
    print ('|    da informação que estas detêm. No Teste de Intrusão são testadas as vul-  |')
    print ('|   -nerabilidades técnicas e conceituais das infra-estruturas alvo! <--       |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '03' or aux == '03':
    print ('+------------------------------------------------------------------------------+')
    print ('|   ---> VOCÊ ESCOLHEU A OPÇÃO 3 <--- // --> Quais as fases de um ataque? <--  |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Levantamento de informações:  É a fase mais importante de um ataque e de  |')
    print ('|    um teste de invasão. Baseado no que é descoberto nessa fase, todo o pla-  |')
    print ('|   -nejamento é realizado e os vetores de um ataque definidos!                |')
    print ('|    Varredura: Nessa fase o atacante busca informações mais detalhadas do     |')
    print ('|    alvo, que possam permitir definir seus vetores de ataque e enxergar as    |')
    print ('|    possibilidades que podem permitir ganhar acesso ao sistema, atravéz da    |')
    print ('|    exploração de alguma falha encontrada!                                    |')
    print ('|    Ganhando Acesso: Aqui o atacante coloca em prática tudo aquilo que plane- |')
    print ('|   -jou a partir das informações obtidas préviamente!                         |')
    print ('|    Mantendo Acesso: Após conseguir o acesso, o atacante busca, de alguma     |')
    print ('|    forma, manter o acesso conseguindo atravéz de seus ataques. Isso normal-  |')
    print ('|   -mente não é utilizado por um pen tester, a não ser que seja extremamente  |')
    print ('|    necessário!                                                               |')
    print ('|    Limpando Rastros: Nessa fase final do ataque, o atacante apaga todos os   |')
    print ('|    resgistros de operações realizadas dentro do sistema comprometido! <--    |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '04' or aux == '04':
    print ('+------------------------------------------------------------------------------+')
    print ('|       ---> VOCÊ ESCOLHEU A OPÇÃO 4 <--- // --> Oque é um Backdoor <--        |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Os Backdoor são programas destinados a fornecer um meio de acesso remoto  |')
    print ('|    ao hacker a uma máquina que provavelmente teve sua segurança comprometida |')
    print ('|    por ele anteriormente. Normalmente, esses programas abrem uma porta no    |')
    print ('|    computador atacado, e nessa porta tem o servidor do hacker escutando,     |')
    print ('|    apenas esperando o hacker se conectar nela para dar total acesso ao com-  |')
    print ('|                           -putador  <--                                      |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '05' or aux == '05':
    print ('+------------------------------------------------------------------------------+')
    print ('|      ---> VOCÊ ESCOLHEU A OPÇÃO 5 <--- // --> Oque é um White Hat? <--       |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> White Hat é o Hacker que age a favor da sociedade ¨um Hacker ético¨ con-  |')
    print ('|    siderado por todos ¨o bonzinho da história¨! <--                          |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '06' or aux == '06':
    print ('+------------------------------------------------------------------------------+')
    print ('|      ---> VOCÊ ESCOLHEU A OPÇÃO 6 <--- // --> Oque é um Black Hat? <--       |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> White Hat é o Hacker odiado por uns e temidos por outros, ele age a seu   |')
    print ('|    favor, causando caos e medo na sociedade, ele age sem ética e ataca       |')
    print ('|    tudo e todos sem dó, é considerado ¨o vilão da história¨ <--              |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '07' or aux == '07':
    print ('+------------------------------------------------------------------------------+')
    print ('|      ---> VOCÊ ESCOLHEU A OPÇÃO 7 <--- // --> Oque é um Gray Hat? <--        |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Um Gray Hat é um Hacker que age com e sem ética ao mesmo tempo, ele é a   |')
    print ('|    favor e contra a sociedade, ataca por diversão e calcula oque vai fazer<--|')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '08' or aux == '08':
    print ("""
    +------------------------------------------------------------------------------+
    |        ---> VOCÊ ESCOLHEU A OPÇÃO 8 <--- // --> Oque é um Lammer? <--        |
    +------------------------------------------------------------------------------+
    |--> Lammer ou Lamer é um termo utilizado para as pessoas que não possuem      |
    |    nenhum conhecimento sobre hack e utilizam ferramentas desenvolvidas por   |
    |                   outros para realizarem seus ataques                     <--|
    +------------------------------------------------------------------------------+
    """)
    

elif aux == '09' or aux == '09':
    print ("""
    +------------------------------------------------------------------------------+
    |   ---> VOCÊ ESCOLHEU A OPÇÃO 09 <--- // --> O que é um Script Kiddie? <--    |
    +------------------------------------------------------------------------------+
    |--> Um Script Kiddie (garoto dos scripts, em uma tradução literal) é um termo |
    |    dado aos garotos inexperientes (geralmente na faixa etária inferior a 17  |
    |    anos) que praticam atividades semelhantes a hackers, como invasões e ex-  |
    |   -plorações de vulnerabilidades (ou pelo menos tentam praticar) utilizando- |
    |    se de métodos, ferramentas, e scripts desenvolvidos por hackers        <--|
    +------------------------------------------------------------------------------+
    """)    

elif aux == '10' or aux == '10':
    print ('+------------------------------------------------------------------------------+')
    print ('|       ---> VOCÊ ESCOLHEU A OPÇÃO 10 <--- // --> Oque é um Vírus? <--         |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Os vírus, para começar a trabalhar, precisam ser ativados, ou seja,       |')
    print ('|    você precisa executar o programa infectado. Somente após isso, ele        |')
    print ('|    começará a infectar outros arquivos. Se algum arquivo infectado for       |')
    print ('|    levado e executado em outro computador, então o vírus começará a          |')
    print ('|    atacar os arquivos dos outros computadores também! <--                    |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '11':
    print ('+------------------------------------------------------------------------------+')
    print ('|       ---> VOCÊ ESCOLHEU A OPÇÃO 11 <--- // --> Oque é um Worm? <--          |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Um Worm ou verme é um programa que pode infectar tanto uma máquina local  |')
    print ('|    quanto uma máquina externa. Normalmente, os Worms exploram falhas de      |')
    print ('|    segurança em outros programas para se propagarem, como é o caso do        |')
    print ('|    Worm BLASTER, que ficou mundialmente conhecido após infectar milhares     |')
    print ('|    de computadores em poucas horas. Esse Worm explorava um problema de pro-  |')
    print ('|   -gramação em um serviço conhecido por rpc-dcom, que vem ativado por        |')
    print ('|    padrão nos sistemas operacionais Windows 2000 e Windows XP <--            |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '12':
    print ('+------------------------------------------------------------------------------+')
    print ('|   ---> VOCÊ ESCOLHEU A OPÇÃO 12 <--- // --> Quais os tipos de pentest? <--   |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Blind: Nessa modalidade o auditor não conhece nada sobre o alvo que irá   |')
    print ('|    atacar, porém o alvo sabe que será atacado e o que será feito durante o   |')
    print ('|                                     teste. <-                                |')
    print ('|--> Double Blind: Nessa modalidade o auditor não conhece nada sobre o alvo,   |')
    print ('|    e o alvo não sabe que será atacado e tão pouco sabe quais testes o audi-  |')
    print ('|   -tor irá realizar. <-                                                      |')
    print ('|--> Gray Box: Nessa modalidade o auditor tem conhecimento parcial do alvo,    |')
    print ('|    e o alvo sabe que será atacado e também sabe quais testes serão           |')
    print ('|                                   realizados. <-                             |')
    print ('|--> Double Gray Box: Nesta modalidade o auditor tem conhecimento parcial do   |')
    print ('|    alvo, e o alvo sabe que será atacado, porém, não sabe quais testes serão  |')
    print ('|                                   realizados. <-                             |')
    print ('|--> Tandem: Nessa modalidade o auditor tem total conhecimento sobre o alvo,   |')
    print ('|    o alvo sabe que será atacado e oque será feito durante o ataque. Também   |')
    print ('|    conhecido como ¨Caixa de cristal¨. <-                                     |')
    print ('|--> Reversal: Nessa modalidade o auditor tem conhecimento total do alvo,      |')
    print ('|    porém o alvo não sabe que será atacado, e tão pouco sabe quais testes     |')
    print ('|                                  serão executados. <-                        |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '13':
    print ('+------------------------------------------------------------------------------+')
    print ('|         ---> VOCÊ ESCOLHEU A OPÇÃO 13 <--- // --> Oque é NetCat? <--         |')
    print ('+------------------------------------------------------------------------------+')
    print ('|-->NetCat é uma ferramenta usada para ler e escrever dados em conexões de     |')
    print ('|   rede usando o protocolo TCP/IP. Dada sua grande versibilidade, o NetCat é  |')
    print ('|   considerado pelos hackers o canivete suiço do TCP/IP, podendo ser usado    |')
    print ('|   para fazer desde portscans até brute force ataques! <--                    |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '14':
    print ('+------------------------------------------------------------------------------+')
    print ('|     ---> VOCÊ ESCOLHEU A OPÇÃO 14 <--- // --> Oque é um Keilogger? <--       |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Keylloger são programas utilizados para gravar tudo aquilo que o usuário  |')
    print ('|    digita no teclado. Alguns, mais avançados, armazenam screenshots da tela  |')
    print ('|    ou até mesmo a área ao redor do ponteiro do mouse onde ocorre um click<-- |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '15':
    print ('+------------------------------------------------------------------------------+')
    print ('|         ---> VOCÊ ESCOLHEU A OPÇÃO 15 <--- // --> Brute Force <--            |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Umas das mais conhecidas técnicas de invasão de sistemas é, sem dúvida,   |')
    print ('|    o bruteforce. O método de funcionamento de um ataque desse tipo é muito   |')
    print ('|    simples: são geradas várias tentativas de conexão a partir do nome de um  |')
    print ('|    provável usuário da máquina alvo. A técnica consiste em gerar combinações |')
    print ('|    de senhas para esse usuário, na tentativa de ¨adivinhas¨ a senha dele. <- |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '16':
    print ('+------------------------------------------------------------------------------+')
    print ('|         ---> VOCÊ ESCOLHEU A OPÇÃO 16 <--- // --> RainbownCrack <--          |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> RainbownCrack é um programa que gera rainbow tables para serem usadas na  |')
    print ('|    quebra de senhas. O RainbowCrack difere dos programas de força bruta      |')
    print ('|    convencionais, pois utiliza tabelas previamente criadas, chamadas rainbow |')
    print ('|    tables, para reduzir drasticamente o tempo necessário para quebrar senhas!|')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '17':
    print ('+------------------------------------------------------------------------------+')
    print ('|   ---> VOCÊ ESCOLHEU A OPÇÃO 17 <--- // --> Entendendo Aplicações Web <--    |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Aplicações web são programas que ficam em um servidor web e executam      |')
    print ('|    tarefas para dar uma resposta ao usuário. Webmails, web fóruns e blogs    |')
    print ('|    são exemplos de aplicações web. Uma aplicação web usa uma arquitetura     |')
    print ('|    cliente/servidor, normalmente com um navegador web como cliente e o web   |')
    print ('|    server como o servidor da aplicação! <--                                  |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '18':
    print ('+------------------------------------------------------------------------------+')
    print ('|---> VOCÊ ESCOLHEU A OPÇÃO 18 <--- // --> O que é negativação de serviços? <--|')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Um ataque de negativação de serviço, é quando o atacante deixa o sistema  |')
    print ('|    impossível de ser usado ou significativamente lento, a ponto de conseguir |')
    print ('|    realizar poucas tarefas. Esses ataques podem ser realizados contra um     |')
    print ('|    sistema individual ou contra uma rede inteira e normalmente são rea-      |')
    print ('|                             -lizados com sucesso <--                         |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '19':
    print ('+------------------------------------------------------------------------------+')
    print ('|      ---> VOCÊ ESCOLHEU A OPÇÃO 19 <--- // --> Ataque DoS = Entenda <--      |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> De acordo com a definição do CERT (Computer Emergency Response Team), os  |')
    print ('|    ataques DoS (Denial of Service), também conhecido denominados Ataques de  |')
    print ('|    Negativação de Serviços, consistem em tentativas de impedir usuários      |')
    print ('|    legítimos de utilizarem um deteterminado serviço de um computador. Para   |')
    print ('|    isso, são usadas técnicas que podem: sobrecarregar uma rede a tal ponto   |')
    print ('|    em que os verdadeiros usuários dela não consigam usá-la; derrubar uma     |')
    print ('|    conexão entre dois ou mais computadores; fazer tantas requisições a um    |')
    print ('|    site até que este não consiga mais ser acessado; nega acesso a um sistema |')
    print ('|    ou a determinados usuários! <--                                           |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '20':
    print ('+------------------------------------------------------------------------------+')
    print ('|     --->VOCÊ ESCOLHEU A OPÇÃO 20 <--- // --> Ataque DDoS = Entenda <--       |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> O DDoS, sigla para Distributed Denial of Service, é um ataque DoS         |')
    print ('|    ampliado, ou seja , que utiliza até milhares de computadores para atacar  |')
    print ('|    um determinado alvo. Esse é um dos tipos mais eficazes de ataques e já    |')
    print ('|    prejudicou sites conhecidos, tais como os da CNN, Amazon, Yahoo,          |')
    print ('|    Microsoft e eBay. Para que os ataques do tipo DDoS sejam bem sucedidos,   |')
    print ('|    é necessário que se tenha um número grande de computadores para fazerem   |')
    print ('|    parte do ataque. Uma das melhores formas encontradas para se ter tantas   |')
    print ('|    máquinas, foi inserir programas de ataque DDoS em vírus ou softwares      |')
    print ('|                                    maliciosos! <--                           |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '21':
    print ('+------------------------------------------------------------------------------+')
    print ('|      ---> VOCÊ ESCOLHEU A OPÇÃO 21 <--- // --> Oque é Ping Flood? <--        |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Ping Flood é um ataque de negativação de serviço simples no qual o        |')
    print ('|    atacante sobrecarrega o sistema vítima com pacotes ICMP Echo Request      |')
    print ('|                            (pacotes ping)! <--                               |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '22':
    print ('+-------------------------------------------------------------------------------+')
    print ('|        ---> VOCÊ ESCOLHEU A OPÇÃO 22 <--- // --> Oque é SYN Flood? <--        |')
    print ('+-------------------------------------------------------------------------------+')
    print ('|--> SYN Flood ou ataque SYN é uma forma de (DoS) em sistemas computadorizados, |')
    print ('|    na qual o atacante envia uma sequência de requisições SYN para um sistema- |')
    print ('|                                         alvo! <--                             |')
    print ('+-------------------------------------------------------------------------------+')
    

elif aux == '23':
    print ('+------------------------------------------------------------------------------+')
    print ('|     ---> VOCÊ ESCOLHEU A OPÇÃO 23 <--- // --> Oque é um Smurf Attack? <--    |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> O Smurf é outro tipo de ataque de negativação de serviço. O agressor      |')
    print ('|    envia uma rápida sequência de solicitações de Ping (um teste para         |')
    print ('|    verificar se um servidor da internet está acessível) para um endereço de  |')
    print ('|                                      broadcast! <--                          |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '24':
    print ('+------------------------------------------------------------------------------+')
    print ('|  ---> VOCÊ ESCOLHEU A OPÇÃO 24 <--- // --> Oque é Sequestro de Sessão? <--   |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> A idéia por detrás do ataque de sequestro de sessão, ou session hijacking |')
    print ('|    é justamente utilizar credêniais válidas para acessar recursos que não    |')
    print ('|                       estão disponíveis publicamente! <--                    |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '25':
    print ('+------------------------------------------------------------------------------+')
    print ('|       ---> VOCÊ ESCOLHEU A OPÇÃO 25 <--- // --> Oque é um Sniffer? <--       |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Sniffer é uma ferramenta capaz de capturar todo o tráfego de uma rede.    |')
    print ('|    Assim sendo é possivel capturar todo o tráfego malicioso de trojans e     |')
    print ('|    também capturar as senhas que trafegam sem criptografia pela rede! <--    |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '26':
    print ('+------------------------------------------------------------------------------+')
    print ('|     ---> VOCÊ ESCOLHEU A OPÇÃO 26 <--- // --> Como surgiu o sniffer? <--     |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> A captura de tais dados era muito trivial em redes que possuiam HUBs      |')
    print ('|    onde a informação trafegada é replicada por toda a rede. Como evolução    |')
    print ('|    surgiram os switchs, onde a rede passou a trabalhar de forma mais         |')
    print ('|    segmentada, encaminhando os pacotes apenas para a porta onde estava       |')
    print ('|    conectado a máquina de destino, com isso dificultou o uso de ferramentas  |')
    print ('|                                de sniffer! <--                               |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '27':
    print ('+------------------------------------------------------------------------------+')
    print ('|     ---> VOCÊ ESCOLHEU A OPÇÃO 27 <--- // --> O que é DNS Pharming? <--      |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Em informática Pharming é o termo atribuído ao ataque baseado na técnica  |')
    print ('|    DNS cache poisoning, que consiste em corromper o DNS em uma rede de       |')
    print ('|    computadores, fazendo com que a URL de um site passe a apontar para um    |')
    print ('|                servidor diferente do original! <--                           |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '28':
    print ('+------------------------------------------------------------------------------+')
    print ('|      ---> VOCÊ ESCOLHEU A OPÇÃO 28 <--- // --> O que é um Exploit? <--       |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Um Exploi, em segurança da informação, é um programa de computador, uma   |')
    print ('|    porção de dados ou uma sequência de comandos que se aproveita das         |')
    print ('|    vulnerabilidades de um sistema computacional- como próprio sistema        |')
    print ('|    operativo ou serviços de interação de protocolos(ex: Servidores Web)! <-- |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '29':
    print ('+------------------------------------------------------------------------------+')
    print ('|   ---> VOCÊ ESCOLHEU A OPÇÃO 29 <--- // --> O que é um Buffer Overflow? <--  |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Um buffer overflow acontece quando um programa vulnerável a esse tipo     |')
    print ('|    de falha tenta copiar mais informações para dentro de um bufer do que     |')
    print ('|    esse buffer consegue suportar. Para visualizar isso, é a mesma coisa      |')
    print ('|    que pegar uma garrafa de refrigerante de 2 litros e virar ela toda num    |')
    print ('|    copo de 500ml. Com certeza ocorrerá uma sujeira na mesa em que isso foi   |')
    print ('|    feito, e é a mesma coisa que ocorre na memória, um esparramado de         |')
    print ('|    caracteres sobre a memória que irá subrescrever informações importantes   |')
    print ('|    assim como o refrigerante sujou toda a toalha da mesa. <--                |')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '30':
    print ('+------------------------------------------------------------------------------+')
    print ('| ---> VOCÊ ESCOLHEU A OPÇÃO 30 <--- // --> O que é Metasploit Framework? <--  |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Como mencionado em seu Website, Metasploit Framework é uma forma avançada |')
    print ('|    plataforma Open Source, concebida especificamente com o objetivo de       |')
    print ('|    reforçar e acelerar o desenvolvimento, ensaio e utilização de exploits!<--|')
    print ('+------------------------------------------------------------------------------+')
    

elif aux == '31':
    print ('+------------------------------------------------------------------------------+')
    print ('|     ---> VOCÊ ESCOLHEU A OPÇÃO 31 <--- // --> O que é Google Hacking? <--    |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Google Hacking é a atividade de usar recursos de busca do site, visando   |')
    print ('|    atacar ou proteger melhor as informações de uma empresa. As informações   |')
    print ('|    disponíveis nos servidores web da empresa provavelmente estarão nas bases |')
    print ('|    de dados do Google. Um servidor mal configurado pode expor diversas       |')
    print ('|    informações da empresa no Google. Não é difícil conseguir acesso a        |')
    print ('|    arquivos de base de dados de sites atravéz do Google! <--                 |')
    print ('+------------------------------------------------------------------------------+')

elif aux == '32':
    print ('+------------------------------------------------------------------------------+')
    print ('|    ---> VOCÊ ESCOLHEU A OPÇÃO 32 <--- // --> O que são portas HTTPS? <--     |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Sua função é estabelecer uma comunicação entre diferentes sistemas de     |')
    print ('|    informações, geralmente está presente na porta 8080 e na porta 80      <--|')
    print ('+------------------------------------------------------------------------------+')

elif aux == '33':
    print ('+------------------------------------------------------------------------------+')
    print ('|       ---> VOCÊ ESCOLHEU A OPÇÃO 33 <--- // --> O que é um FTP? <--          |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> FTP é um protocolo de internet que permite que computadores dentro de uma |')
    print ('|    rede promovam trocas de arquivos em massa. Para funcionar corretamente,   |')
    print ('|    o FTP deve usar duas portas - Porta 21 para comando e controle, e a porta |')
    print ('|                      20 para transporte de dados <--                         |')
    print ('+------------------------------------------------------------------------------+')

elif aux == '34':
    print ('+------------------------------------------------------------------------------+')
    print ('|        ---> VOCÊ ESCOLHEU A OPÇÃO 34 <--- // --> O que é um SSH? <--         |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> SSH ou Cápsula de Segurança é um protocolo de administração remota que    |')
    print ('|permite aos usuários controlar e modificar seus servidores pela internet <--  |')
    print ('+------------------------------------------------------------------------------+')

elif aux == '35':
    print ('+------------------------------------------------------------------------------+')
    print ('|        ---> VOCÊ ESCOLHEU A OPÇÃO 35 <--- // --> O que é um Host? <--        |')
    print ('+------------------------------------------------------------------------------+')
    print ('|--> Por definição, host é qualquer computador ou máquina conectado a uma      |')
    print ('|    rede, que conta com número de IP e nome definidos. Essas máquinas são     |')
    print ('|    responsáveis por oferecer recursos, informações e serviços aos usuários   |')
    print ('|                               ou clientes! <--                               |')
    print ('+------------------------------------------------------------------------------+')
