import os, platform
sistema = platform.system()

### rode o script em um prompt/terminal como administrador/root
def main():
    print('+++++++++++++++++++++++++++++++++++++++++++++')
    print('+ ==> ELE APENAS TIRA OS ADs                +')
    print('+ [1] CRACKEAR                              +')
    print('+ [2] REMOVE CRACK                          +')
    print('+ [3] VERIFICAR SE JA ESTA CRACKEADO        +')
    print('+ [4] EXIT                                  +')
    print('+++++++++++++++++++++++++++++++++++++++++++++')
print('\n')

crack = """
0.0.0.0 adclick.g.doublecklick.net
0.0.0.0 googleads.g.doubleclick.net
0.0.0.0 http://www.googleadservices.com
0.0.0.0 pubads.g.doubleclick.net
0.0.0.0 securepubads.g.doubleclick.net
0.0.0.0 pagead2.googlesyndication.com
0.0.0.0 spclient.wg.spotify.com
0.0.0.0 audio2.spotify.com
"""
if sistema == 'Windows':
    main()
    try:
        escolha = int(input('>>'))
        while escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
            escolha = int(input('>>'))
        if escolha == 1:
            diretorio = os.chdir('C:\Windows\System32\drivers\etc')
            with open('hosts','a') as crack:
                crack.write("""
    0.0.0.0 adclick.g.doublecklick.net
    0.0.0.0 googleads.g.doubleclick.net
    0.0.0.0 http://www.googleadservices.com
    0.0.0.0 pubads.g.doubleclick.net
    0.0.0.0 securepubads.g.doubleclick.net
    0.0.0.0 pagead2.googlesyndication.com
    0.0.0.0 spclient.wg.spotify.com
    0.0.0.0 audio2.spotify.com
    """)
                print('[+]Crackeado com sucesso !!! ')
        elif escolha == 2:
            diretorio = os.chdir('C:\Windows\System32\drivers\etc')
            with open('hosts','w') as remove:
                remove.write("""
    # Copyright (c) 1993-2009 Microsoft Corp.
    #
    # This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
    #
    # This file contains the mappings of IP addresses to host names. Each
    # entry should be kept on an individual line. The IP address should
    # be placed in the first column followed by the corresponding host name.
    # The IP address and the host name should be separated by at least one
    # space.
    #
    # Additionally, comments (such as these) may be inserted on individual
    # lines or following the machine name denoted by a '#' symbol.
    #
    # For example:
    #
    #      102.54.94.97     rhino.acme.com          # source server
    #       38.25.63.10     x.acme.com              # x client host

    # localhost name resolution is handled within DNS itself.
    #	127.0.0.1       localhost
    #	::1             localhost
    """)
                print('[+]Remoçao de ADs concluida.Voltando ao original!!')
                exit()
        elif escolha == 3:
            os.chdir('C:\Windows\System32\drivers\etc')
            abrir = open('hosts','r')
            if crack in abrir.read():
                print("[+]Seu Spotify ja está crackeado.")
                exit()
            else:
                print("[-]Seu spotify nao esta crackeado.")
                exit()
        elif escolha == 4:
            exit()

    except ValueError:
        print('[-]Verifique sua escolha novamente.')
    except KeyboardInterrupt:
        print('[-]Voce cancelou, saindo..')
        exit()
    except PermissionError:
        print('[!]RODE O SCRIPT NO PROMPT/TERMINAL COMO ADMIN/ROOT')
    except FileNotFoundError:
        print('[-]Ha algum arquivo faltando para completar o crack : hosts')
else:
    print('[ :( ]  SpotifyCrack roda apenas no Windows .')