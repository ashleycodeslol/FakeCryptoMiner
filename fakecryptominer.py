import random, string, os, time, colorama

def mine(coin='BITCOIN'):
    while True:
        print(f'{colorama.Fore.GREEN}>{({"BITCOIN": "BTC", "DOGECOIN": "DOGE", "ETHERUM": "ETH"}.get(coin))}  | {colorama.Fore.LIGHTBLUE_EX}', f"".join(random.choice(string.ascii_letters + string.digits) for i in range(0, 64+1)), f"{colorama.Fore.GREEN}| 0.00")
        time.sleep(0.085)

if __name__ == "__main__":
    os.system('cls')
    print(f"""          
{colorama.Fore.LIGHTBLUE_EX}░█████╗░██████╗░████████╗███████╗███╗░░░███╗██╗░██████╗  ███╗░░░███╗██╗███╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗╚══██╔══╝██╔════╝████╗░████║██║██╔════╝  ████╗░████║██║████╗░██║██╔════╝██╔══██╗
███████║██████╔╝░░░██║░░░█████╗░░██╔████╔██║██║╚█████╗░  ██╔████╔██║██║██╔██╗██║█████╗░░██████╔╝
██╔══██║██╔══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║██║░╚═══██╗  ██║╚██╔╝██║██║██║╚████║██╔══╝░░██╔══██╗
██║░░██║██║░░██║░░░██║░░░███████╗██║░╚═╝░██║██║██████╔╝  ██║░╚═╝░██║██║██║░╚███║███████╗██║░░██║
{colorama.Fore.CYAN}╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚═╝╚═════╝░  ╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝\n\n""")   
    coin = input(f"{colorama.Fore.CYAN}Welcome to Artemis Miner!\nWhat would you like to mine {colorama.Fore.BLUE}\nBitcoin \nEtherum \nDogeCoin\n\n").upper().rstrip()
    
    if coin in (valid_coins := ('BITCOIN', 'ETHERUM', 'DOGECOIN')):
        mine(coin) 
         
    else:
        print(f"{colorama.Fore.LIGHTRED_EX}Invalid coin selected... mining {(coin := random.choice(valid_coins).capitalize())}")
        time.sleep(1)
        mine(coin.upper())