def alert(args) -> str:
    warn = {
        "topic": 'Can you please move this topic elsewhere or stop discussing it?',
        "spam":  'Please stop spamming.',
        "rules": 'Please re-read the rules due to the nature of this discussion.'
    }
    if len(args) == 0:
        return "Unable to send warnings"
    
    if args[0] not in warn:
        return "warning not in warning list"
    
    return warn[args[0]]