import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'area_page.dart';

class SpotifyPage extends StatelessWidget {
  const SpotifyPage({super.key});

  static const List<String> actions = [
    'A user follows a playlist',
    'A user likes a song',
    'A user shares a song',
    'A user starts listening to a song',
    'A song is added to a collaborative playlist',
    'A song is saved to the library',
    'A song is removed from a playlist',
    'A song is played on shuffle',
    'A new song is played',
    'A playlist is created',
    'A new artist is followed',
    'A playlist is shared',
    'A new follower is added to the user\'s playlist',
    'A playlist is followed by another user',
  ];

  static const List<Tuple2<String, String>> reactions = [
    Tuple2('YouTube', 'Like a YouTube video'),
    Tuple2('Microsoft', 'Send an email notification'),
    Tuple2('YouTube', 'Like a related YouTube video'),
    Tuple2('Google Drive', 'Sync shared song details with Google Drive'),
    Tuple2('YouTube', 'Start playing a related video'),
    Tuple2('Twitch', 'Send a notification in Twitch chat'),
    Tuple2('Google Drive', 'Save song details to Google Drive'),
    Tuple2('YouTube', 'Remove a related video from a playlist'),
    Tuple2('Twitch', 'Post a message in Twitch chat'),
    Tuple2('Twitch', 'Send a message in Twitch chat'),
    Tuple2('Google Calendar', 'Create a calendar event for playlist release'),
    Tuple2('YouTube', 'Subscribe to a YouTube channel'),
    Tuple2('Google Drive', 'Upload playlist details to Google Drive'),
    Tuple2('Google Calendar', 'Create an event to celebrate the new follower'),
    Tuple2('Microsoft', 'Send an email notification'),
  ];

  @override
  Widget build(BuildContext context) {
    return ActionReactionPage(
      title: 'Spotify',
      actions: actions,
      reactions: reactions,
    );
  }
}