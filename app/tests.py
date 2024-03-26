import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from app.services.telegram.chat_transport import ChatTransportTelegram
from app.config import ChannelMode
from listener import SimpleBusinessLogic
from services.discord.chat_transport import ChatTransportDiscord


@pytest.mark.asyncio
async def test_init_with_telegram_mode():
    business_logic = SimpleBusinessLogic(ChannelMode.TELEGRAM)
    assert isinstance(business_logic._transporter, ChatTransportTelegram)


@pytest.mark.asyncio
async def test_message_reception_and_response_telegram():
    with patch('app.services.telegram.chat_transport.ChatTransportTelegram.send_message', new_callable=AsyncMock) as mock_send:
        business_logic = SimpleBusinessLogic(ChannelMode.TELEGRAM)
        mock_message = AsyncMock(text='Hello')
        await business_logic.listen(mock_message)
        mock_send.assert_awaited_once_with(
            mock_message, text='Hi! Your message was received: Hello'
        )


def test_extract_text_telegram():
    mock_message = MagicMock(text='Test message')
    extracted_text = ChatTransportTelegram.extract_text(mock_message)
    assert extracted_text == 'Test message'


@pytest.mark.asyncio
async def test_send_message_telegram():
    telegram_transport = ChatTransportTelegram()
    mock_message = MagicMock()
    mock_message.answer = AsyncMock()
    await telegram_transport.send_message(mock_message, text='Hello')
    mock_message.answer.assert_awaited_once_with('Hello')


@pytest.mark.asyncio
async def test_send_message_discord():
    discord_transport = ChatTransportDiscord()
    mock_message = MagicMock()
    mock_message.channel.send = AsyncMock()
    await discord_transport.send_message(mock_message, text='Hello')
    mock_message.channel.send.assert_awaited_once_with('Hello')


def test_extract_text_discord():
    mock_message = MagicMock(content='Test message')
    extracted_text = ChatTransportDiscord.extract_text(mock_message)
    assert extracted_text == 'Test message'
