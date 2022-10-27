import asyncio
from prisma import Prisma
import os.path
from os import path


async def main() -> None:

    print("Database exists: "+str(path.exists('database.db')))

    prisma = Prisma()
    await prisma.connect()

    if not path.exists('database.db'):
        # write your queries here
        user = await prisma.user.create(
            data={
                'name': 'Robert',
                'email': 'robert@craigie.dev'
            },
        )

    # find all users
    users = await prisma.user.find_many()
    print(users)

    # find all users includes posts
    users = await prisma.user.find_many(
        include={
            'posts': True
        },
    )
    print(users)

    # find all posts where title and content equal to prisma
    posts = await prisma.post.find_many(
        where={
            'OR': [
                {'title': {'contains': 'prisma'}},
                {'content': {'contains': 'prisma'}},
            ]
        }
    )

    print(posts)

    user = await prisma.user.create(
        data={
            'name': 'Jhon',
            'email': 'jhon@acme.com',
            'posts': {
                'create': {
                    'title': 'My first posts from Prisma!'
                },
            },
        },
    )

    print(user)
    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
