async def remind_users(chan, role: str, work: str, date: str, time: str) -> str:
    await chan.send(f"<@&{role}> Don't forget the {work} due {date} at {time}.")
    return 'Reminder sent.'