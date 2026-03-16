import time
import requests

class BlockchainMonitor:
    def __init__(self, blockchain_url):
        self.blockchain_url = blockchain_url

    def get_latest_block(self):
        response = requests.get(f'{self.blockchain_url}/latestblock')
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch data from blockchain.")

    def monitor(self):
        latest_block = self.get_latest_block()
        print(f'Latest block information: {latest_block}')

        while True:
            time.sleep(10)  # Check every 10 seconds
            new_block = self.get_latest_block()
            if new_block['height'] > latest_block['height']:
                print(f'New block detected! Height: {new_block['height']}')
                latest_block = new_block
            else:
                print('No new block detected.')

if __name__ == '__main__':
    blockchain_url = 'https://api.blockchain.info/'
    monitor = BlockchainMonitor(blockchain_url)
    monitor.monitor()