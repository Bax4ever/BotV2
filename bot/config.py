import os
from dotenv import load_dotenv

load_dotenv()

Trackademybot=os.getenv("Trackademybot")
infura_url = os.getenv("INFURA_URL")
etherscan_api_key = os.getenv("ETHERSCAN_API_KEY")
graph_API_KEY = os.getenv("graph_API_KEY")
botbundler_token = os.getenv("botbundler_token")
GRAPHQL_URL = os.getenv("GRAPHQL_URL")
MORALIS_API_KEY=os.getenv("MORALIS_API_KEY")
ankr_url= os.getenv("ankr_url")
ankr_api=os.getenv("ankr_api")
RAILWAY_PUBLIC_URL=os.getenv("RAILWAY_PUBLIC_URL")
DATABASE_URL=os.getenv("DATABASE_URL")