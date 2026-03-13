sessions = {}


def save_session(user, sector):

    if user not in sessions:
        sessions[user] = []

    sessions[user].append(sector)