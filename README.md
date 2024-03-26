Abstract Chat Transport Connector

The goal is to enable the bot to connect to any channel by simply swapping the transport class between Discord and Telegram, without altering the business logic.

Tasks to Implement:
- ChatTransport class
  - def add_handler(event)
  - async def send_message(msg)
  - async def run

- ChatTransportDiscord service
- ChatTransportTelegram service

- SimpleBusinessLogic Bot
  - Initializes ChatTransport (configured to work with either Discord or Telegram through a single setting).
  - Listens for messages and responds with "Hi! Your message was received: {msg}".

The objective is to facilitate the bot's ability to receive and send messages from these two chat services. (You can request GPT-4 to write the code for this implementation).
