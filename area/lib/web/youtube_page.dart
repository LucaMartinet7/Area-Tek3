import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'area_page.dart';

class YoutubePage extends StatelessWidget {
  const YoutubePage({super.key});

  static const List<String> actions = [
    'A new video is uploaded',
    'A user subscribes to a channel',
    'A video reaches a milestone (e.g., 1M views)',
    'A new subscriber joins',
    'A user watches a video for the first time',
    'A user adds a video to a playlist',
    'A new playlist is created',
    'A new video is uploaded to a playlist',
    'A user shares a video',
    'A user comments on a video',
    'A live stream is scheduled',
    'A playlist is shared',
  ];

  static const List<Tuple2<String, String>> reactions = [
    Tuple2('Spotify', 'Play a playlist'),
    Tuple2('Twitch', 'Follow a random Twitch streamer'),
    Tuple2('Spotify', 'Play a celebratory song'),
    Tuple2('Microsoft Outlook', 'Send an email to the user'),
    Tuple2('Spotify', 'Play a soundtrack'),
    Tuple2('Spotify', 'Add the video\'s song to a Spotify playlist'),
    Tuple2('Google Drive', 'Sync the playlist details to Google Drive'),
    Tuple2('Microsoft Outlook', 'Send an email notification'),
    Tuple2('Google Calendar', 'Schedule a watch event'),
    Tuple2('Twitch', 'Share the comment in Twitch chat'),
    Tuple2('Microsoft Outlook', 'Send an email reminder'),
    Tuple2('Google Drive', 'Sync the playlist details to Google Drive'),
  ];

  @override
  Widget build(BuildContext context) {
    return ActionReactionPage(
      title: 'YouTube',
      actions: actions,
      reactions: reactions,
    );
  }
}