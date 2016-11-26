import asyncio

class AsyncMetaclass(type):
    async def __call__(cls, *args, **kwargs):
        obj = super(AsyncMetaclass, cls).__call__()
        await obj.__asyncinit__(*args, **kwargs)
        return obj


class Animal(object):
    def __init__(self, legs):
        self._legs = legs

    @property
    def legs(self):
        return self._legs


class AsyncAnimal(metaclass=AsyncMetaclass):
    async def __asyncinit__(self, legs):
        self._legs = legs

    @property
    async def legs(self):
        return self._legs


async def main():
    animal = Animal(4)
    print(animal.legs)

    async_animal = await AsyncAnimal(4)
    print(await async_animal.legs)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
