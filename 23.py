def song_decoder(song):
    song = str(song.split('WUB'))
    song = song.replace("'',", '')
    song = song.replace(' ', '')
    song = song.replace("',", '')
    song = song.replace("['", '')
    song = song.replace("']", '')
    song = song.replace("'", ' ')
    song.strip()
    return song


print(song_decoder('AWUBWUBWUBBWUBWUBWUBC'))
