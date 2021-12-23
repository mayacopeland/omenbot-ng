async def remind_users(chan, role, work, date, time):
    await chan.send(f"<@&{role}> Don't forget the {work} due {date} at {time}.")
    return 'Reminder sent.'