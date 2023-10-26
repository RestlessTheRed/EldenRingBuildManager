import json
import os

from twitchio.ext import commands

from build import Build

BUILDS_FILENAME = 'builds.json'
CURRENT_BUILD = 'current_build'


class Bot(commands.Bot):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.builds = self.load_builds()
        self.dc_count = 0

    @staticmethod
    def load_builds():
        builds = {}
        with open(BUILDS_FILENAME) as f:
            try:
                builds_json = json.load(f)
            except json.JSONDecodeError:
                builds_json = {}
        for build_name, build_info in builds_json.items():
            builds[build_name] = Build(**build_info)
        return builds

    def dump_builds(self):
        with open(BUILDS_FILENAME, 'w') as f:
            json.dump({
                build_name: build.to_json()
                for build_name, build in self.builds.items()
            },
                fp=f,
                ensure_ascii=False,
                indent=4,
            )

    async def event_ready(self):
        print(f'Logged in as {self.nick}. The bot is ready!')

    def add_build(self, build: Build):
        if build.name in self.builds:
            raise ValueError('A build with this name already exists!')
        self.builds[build.name] = build
        self.dump_builds()

    def remove_build(self, build_name: str):
        if build_name not in self.builds:
            raise ValueError('A build with this name is not found!')
        del self.builds[build_name]
        if CURRENT_BUILD in self.builds and self.builds[CURRENT_BUILD].name == build_name:
            del self.builds[CURRENT_BUILD]
        self.dump_builds()

    def set_build(self, build_name: str):
        if build_name not in self.builds:
            raise ValueError('A build with this name is not found!')
        self.builds[CURRENT_BUILD] = self.builds[build_name]
        self.dump_builds()

    def get_current_build(self):
        if CURRENT_BUILD in self.builds:
            return self.builds[CURRENT_BUILD].print()
        return 'No build set.'

    def get_rune_level(self):
        if CURRENT_BUILD in self.builds:
            current_build = self.builds[CURRENT_BUILD]
            return ('RL' + str(current_build.rune_level) +
                    f' +{current_build.regular_upgrade_level}/+{current_build.somber_upgrade_level}')
        return 'No build set.'

    def get_stats(self):
        if CURRENT_BUILD in self.builds:
            return self.builds[CURRENT_BUILD].print_stats()
        return 'No build set.'

    @commands.command()
    async def hi(self, ctx: commands.Context):
        await ctx.send(f'Ayo @{ctx.author.name}!')

    @commands.command()
    async def addbuild(self, ctx: commands.Context):
        if not ctx.author.is_mod:
            return
        try:
            build = Build.from_url(ctx.message.content)
            self.add_build(build)
            await ctx.send(f'Build {build.name} has been added.')
        except Exception as exception:
            await ctx.send(str(exception))

    @commands.command()
    async def addbuildfromtext(self, ctx: commands.Context):
        if not ctx.author.is_mod:
            return
        try:
            build = Build.from_text(ctx.message.content)
            self.add_build(build)
            await ctx.send(f'Build {build.name} has been added.')
        except Exception as exception:
            await ctx.send(str(exception))

    @commands.command()
    async def removebuild(self, ctx: commands.Context):
        if not ctx.author.is_mod:
            return
        build_name = ' '.join(ctx.message.content.split()[1:])
        try:
            self.remove_build(build_name)
            await ctx.send(f'Build {build_name} has been removed.')
        except Exception as exception:
            await ctx.send(str(exception))

    @commands.command()
    async def setbuild(self, ctx: commands.Context):
        if not ctx.author.is_mod:
            return
        build_name = ' '.join(ctx.message.content.split()[1:])
        try:
            self.set_build(build_name)
            await ctx.send(f'Current build has been set to {build_name}.')
        except Exception as exception:
            await ctx.send(str(exception))

    @commands.command()
    async def build(self, ctx: commands.Context):
        await ctx.send(self.get_current_build())

    @commands.command(aliases=['sl'])
    async def rl(self, ctx: commands.Context):
        await ctx.send(self.get_rune_level())

    @commands.command()
    async def stats(self, ctx: commands.Context):
        stats = self.get_stats()
        if stats:
            await ctx.send(stats)

    @commands.command()
    async def builds(self, ctx: commands.Context):
        if "ER_INVENTORY_USER_ID" in os.environ:
            await ctx.send(
                f'You can find my public builds here: '
                f'{"https://er-inventory.nyasu.business/browse/" + os.environ["ER_INVENTORY_USER_ID"]}'
            )

    @commands.command()
    async def setdccount(self, ctx: commands.Context):
        if not ctx.author.is_broadcaster:
            return
        starting_count: str = ctx.message.content.split()[1]
        if starting_count.isdigit():
            self.dc_count = int(starting_count)
            await ctx.send(f'DC count has been set to {starting_count}.')
        else:
            await ctx.send('It seems like the provided value is not a valid number.')

    @commands.command()
    async def dc(self, ctx: commands.Context):
        if ctx.author.is_broadcaster:
            self.dc_count += 1
        if self.dc_count % 10 == 1 and self.dc_count % 100 != 11:
            await ctx.send(f'A connection error occurred {self.dc_count} time this stream.')
            return
        await ctx.send(f'A connection error occurred {self.dc_count} times this stream.')
