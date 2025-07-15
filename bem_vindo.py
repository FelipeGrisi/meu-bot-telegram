import os
from telegram.ext import Application, MessageHandler, filters
import logging

# Configure o log para ver o que está acontecendo
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Substitua 'SEU_TOKEN_AQUI' pelo token do seu bot
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") # Lembre-se de colocar seu token aqui!

async def welcome_new_members(update, context):
    """
    Envia uma mensagem de boas-vindas quando novos membros entram no grupo.
    A função agora é 'async' para ser compatível com a nova estrutura da biblioteca.
    """
    chat_id = update.effective_chat.id
    new_members = update.message.new_chat_members

    for member in new_members:
        # Verifica se o membro não é o próprio bot
        if not member.is_bot:
            welcome_message = (
                f"Bem vindo, guerreiro SaiyaJin!"
            )
            # await é necessário para funções assíncronas
            await context.bot.send_message(chat_id=chat_id, text=welcome_message)
            logger.info(f"Mensagem de boas-vindas enviada para {member.first_name} no chat {chat_id}")

def main():
    """Inicia o bot usando a nova estrutura da Application."""
    # 1. Construir a Application
    application = Application.builder().token(TOKEN).build()

    # 2. Adicionar o handler
    # Note que welcome_new_members não precisa mais ser passada diretamente para MessageHandler
    # Em vez disso, é adicionada com um filtro
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_members))

    # 3. Iniciar o bot
    logger.info("Bot de Boas-Vindas Iniciado!")
    application.run_polling() # 'run_polling' substitui 'start_polling' e 'idle'

if __name__ == '__main__':
    main()