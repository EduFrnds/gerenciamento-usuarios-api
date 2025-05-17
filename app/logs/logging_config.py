import logging
import os

def configure_logging():
    # Define o caminho dos arquivos de log
    log_directory = "logs"

    # Cria o diretório, se não existir
    os.makedirs(log_directory, exist_ok=True)

    # Configura o logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(os.path.join(log_directory, "app.log")),  # Salva o log no diretório
            logging.StreamHandler()  # Também exibe o log no console
        ]
    )

    return logging.getLogger(__name__)
