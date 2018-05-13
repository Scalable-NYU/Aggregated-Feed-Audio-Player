# Functions for Client-Side Calls:

# When a user logs in and play, call this method to play the most recent un-played audio.
    app.route('/<string:user_id>')
    def get_latest_audio(user_id):
    	# code to query db
    	return string:audio_path

    # When a user click on 'Next' button, call this method to skip the current audio and run next audio.
    # Mark the current audio 'played'
    app.route('/<string:user_id>')
    def get_next_audio(user_id):
    	# code to query db
    	return string:audio_path

    //Probably JavaScript code:
    //When a user click on 'Pause' button, 
    //stop the audio playing directly from client side.