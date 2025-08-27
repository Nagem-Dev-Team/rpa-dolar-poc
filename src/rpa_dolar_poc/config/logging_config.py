import logging
import logging.config
from .settings import settings

def setup_logging(default_level=logging.INFO):
    log_level = settings.log_level
    third_party_level = settings.third_party_log_level
    
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "file_rotating": {
                 "class": "logging.handlers.TimedRotatingFileHandler",
                "formatter": "default",
                "filename": "logs/app.log",
                "when": "midnight",
                "interval": 1,
                "backupCount": 15,          # manter 15 dias
                "encoding": "utf8"
            }
        },
        "root": {
            "handlers": ["console", "file_rotating"],
            "level": log_level,
        },
        "loggers": {
            # Configuração específica para bibliotecas de terceiros
            "requests": {
                "level": third_party_level,
                "handlers": ["console", "file_rotating"],
                "propagate": False
            },
            "typer": {
                "level": third_party_level,
                "handlers": ["console", "file_rotating"],
                "propagate": False
            }
        }
    }




    logging.config.dictConfig(logging_config)
