from dataclasses import dataclass
from environs import Env


@dataclass
class TgBotCongig:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBotCongig


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBotCongig(token=env('BOT_TOKEN')))
