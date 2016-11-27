import inspect

class AsyncMetaclass(type):
    async def __call__(cls, *args, **kwargs):
        if inspect.iscoroutinefunction(cls.__new__):
            obj = await cls.__new__(cls, *args, **kwargs)
        else:
            obj = cls.__new__(cls, *args, **kwargs)
        if inspect.iscoroutinefunction(cls.__init__):
            await obj.__init__(*args, **kwargs)
        else:
            obj.__init__(*args, **kwargs)
        return obj


class Animal(object):
    def __init__(self, legs):
        self._legs = legs

    @property
    def legs(self):
        return self._legs


class AsyncAnimal(metaclass=AsyncMetaclass):
    async def __init__(self, legs):
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
    import asyncio
    asyncio.get_event_loop().run_until_complete(main())
