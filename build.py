import math
import os
import requests
from typing import Dict, Optional, Union


class Build:
    def __init__(
            self,
            name: str,
            rune_level: Union[int, str],
            weapon_upgrade_level: Union[int, str],
            link: Optional[str] = None,
            stats: Optional[Dict[str, int]] = None,
    ):
        self.name = name
        self.rune_level = int(rune_level)
        self.weapon_upgrade_level = int(weapon_upgrade_level)
        self.link = link or ''
        self.stats = stats

    @classmethod
    def from_text(cls, query):
        params = query.split()[1:]
        if params[0].startswith('"'):
            name = []
            for i, param in enumerate(params):
                name.append(param)
                if param.endswith('"'):
                    break
            name = ' '.join(name)[1:-1]
            params = [name] + params[i+1:]
        return cls(*params)

    @classmethod
    def from_url(cls, query):
        url = query.split()[1]
        api_url = os.environ['ER_INVENTORY_API_URL'].rstrip('/') + '/' + url.split('?b=')[1]
        res = requests.get(
            url=api_url,
            headers={
                'Authorization': f'{os.environ["ER_INVENTORY_TOKEN"]}',
                'Content-Type': 'application/json; charset=utf-8',
            },
        ).json()
        return cls(
            name=res['name'],
            rune_level=res['stats']['rl'],
            weapon_upgrade_level=int(res['weaponUpgrade']),
            link=url,
            stats=res['stats'],
        )

    def to_json(self):
        return {
            'name': self.name,
            'rune_level': self.rune_level,
            'weapon_upgrade_level': self.weapon_upgrade_level,
            'link': self.link,
            'stats': self.stats,
        }

    def print(self):
        rune_level = f'RL{str(self.rune_level)}'
        somber_upgrade_level = math.ceil(self.weapon_upgrade_level / 2.5)
        weapon_upgrade_level = f'+{self.weapon_upgrade_level}/+{somber_upgrade_level}'
        link = f'Link: {self.link}' if self.link else ''
        return ' '.join([
            self.name,
            rune_level,
            weapon_upgrade_level,
            link,
        ]).rstrip()

    def print_stats(self):
        if self.stats is not None:
            return 'VIG {} MND {} END {} STR {} DEX {} INT {} FTH {} ARC {}'.format(
                self.stats['vig'],
                self.stats['mnd'],
                self.stats['vit'],
                self.stats['str'],
                self.stats['dex'],
                self.stats['int'],
                self.stats['fth'],
                self.stats['arc'],
            )
