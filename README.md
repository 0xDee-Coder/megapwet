# megapwet



Updated Tool: megaETH Faucet using Python (with proxy and non-proxy support)

ℹ️ This tool has a rather complex setup, so please read the instructions carefully.

🌐 Dapps Link: MegaETH (https://testnet.megaeth.com/#5)

✔️ Crusty Swap
✔️ Cap App
✔️ Bebop
✔️ Gte Swaps
✔️ Teko Finance
✔️ Onchain Gm
✔️ Xl Meme
✔️ Omnihub
✔️ Mintair
✔️ Easynode
✔️ Hopnetwork
✔️ Rainmakr

✔️ Multi-threaded, multi-account support, etc.

===========
🖥 Instructions: After downloading and extracting the tool, open your terminal
## Installation

1. Clone this repository

```bash
git clone https://github.com/0xDee-Coder/megapwet.git
cd megapwet
```
- set the ref_code in the .env file
```bash
nano .env
```
2. Install dependencies
```bash
pip install -r requirements.txt or pip3 install -r requirements.txt
```
3. Fill Data and Proxy (Optional)

```bash
nano data/proxies.txt
```
5. Add Private Key
```bash
nano data/private_keys.txt
```
6. Method: Using CapSolver
- Go to CapSolver and register
- Copy the API key and update config.yaml with:
```
USE_CAPSOLVER: true
CAPSOLVER_API_KEY: CAP-xxxxxxxxxxxxxxxx
```

7. Steps to run:
- Run the bot and choose option [3] Database actions
- If it’s your first time running: Select [1] to create the database
- If you have new wallets, use [5] to update the DB
- Use [4] to update tasks in the bot whenever tasks.py is changed

- This is important! Always re-run this after updating tasks.py.

- After task updates are complete:
- Return to the main menu and select [1] to start the bot
- After running, you can check completed tasks via [3] Database actions → [3]
- Completed tasks won’t run again unless reinitialized.
- To reinitialize: [3] Database actions → [2] or [4]

8. Run the tool with the following commands:
- For Windows or Termux: Faucet:
```
python3 faucet.py or python faucet.py
```
Check balance: 
```
python main.py
```
- For MacOS or Linux: Faucet
```
python3 faucet.py or python faucet.py
```
Check balance: 
```
python main.py
```

=========
## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This bot is for educational purposes only. Use it at your own risk. The developer is not responsible for any account-related issues or potential losses.
