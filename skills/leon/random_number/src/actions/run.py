from bridges.python.src.sdk.leon import leon
from bridges.python.src.sdk.types import ActionParams
import secrets


def run(params: ActionParams) -> None:
    """Leon gives a random number"""
    leon.answer({
        'key': 'answer',
        'data': {
            'answer': secrets.SystemRandom().randint(0, 100)
        }
    })
