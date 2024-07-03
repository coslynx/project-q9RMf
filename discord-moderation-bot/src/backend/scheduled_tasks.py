import discord
import asyncio

class ScheduledTasks:
    def __init__(self, client):
        self.client = client

    async def scheduled_task1(self):
        # Implement scheduled task 1 logic here
        pass

    async def scheduled_task2(self):
        # Implement scheduled task 2 logic here
        pass

    async def scheduled_task3(self):
        # Implement scheduled task 3 logic here
        pass

    async def start_scheduled_tasks(self):
        await self.scheduled_task1()
        await self.scheduled_task2()
        await self.scheduled_task3()

# Initialize the ScheduledTasks class with the Discord client
scheduled_tasks = ScheduledTasks(client)