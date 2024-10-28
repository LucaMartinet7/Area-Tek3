import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'area_page.dart';

class TwitchPage extends StatelessWidget {
  const TwitchPage({super.key});

static const List<String> actions = [
    'A streamer goes live',
    'A user follows a channel',
    'A new video is uploaded',
    'A channel gains a follower',
    'A streamer starts streaming a specific game',
    'A user gifts a subscription',
    'A streamer hosts another channel',
    'A stream reaches a milestone (e.g., 100 viewers)',
    'A user clips a moment from a stream',
    'A user subscribes to a streamer',
    'A streamer starts streaming in a new category',
    'A user follows a streamer',
    'A streamer goes live for a charity event',
    'A new emote is added',
    'A streamer reaches a new follower milestone',
];

static const List<Tuple2<String, String>> reactions = [
    Tuple2('Google Calendar', 'Create a calendar event for the live stream'),
    Tuple2('YouTube', 'Subscribe to a YouTube channel'),
    Tuple2('Google Drive', 'Save video metadata to Google Drive'),
    Tuple2('YouTube', 'Like a related video on YouTube'),
    Tuple2('Spotify', 'Play the game soundtrack'),
    Tuple2('Google Calendar', 'Create a calendar event for the gift'),
    Tuple2('YouTube', 'Upload a video promoting the hosted streamer'),
    Tuple2('Microsoft Outlook', 'Send an email notification'),
    Tuple2('Google Drive', 'Save the clip to Google Drive'),
    Tuple2('YouTube', 'Like a related video on YouTube'),
    Tuple2('Microsoft OneDrive', 'Save the stream details to OneDrive'),
    Tuple2('Spotify', 'Play a related song to celebrate'),
    Tuple2('Google Calendar', 'Create an event for the charity stream'),
    Tuple2('Spotify', 'Play a celebratory song'),
    Tuple2('Microsoft Outlook', 'Send an email notification'),
];

  @override
  Widget build(BuildContext context) {
    return ActionReactionPage(
      title: 'Twitch',
      actions: actions,
      reactions: reactions,
    );
  }
}