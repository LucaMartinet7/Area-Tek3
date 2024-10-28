import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'area_page.dart';

class MicrosoftPage extends StatelessWidget {
  const MicrosoftPage({super.key});

  static const List<String> actions = [
    'A new email is received',
    'A file is uploaded to OneDrive',
    'A calendar event is created',
    'A new email is received with an attachment',
    'A file is deleted from OneDrive',
    'A new file is shared in OneDrive',
    'A calendar event is canceled',
    'A new folder is created in OneDrive',
    'A new email from a specific contact',
    'A calendar event starts',
    'A file is updated in OneDrive',
    'A new meeting is scheduled in Outlook',
    'A contact is added to Outlook',
    'A new document is uploaded to OneDrive',
    'A user accepts a meeting invite',
  ];

  static const List<Tuple2<String, String>> reactions = [
    Tuple2('Google Drive', 'Save the attachment to Drive'),
    Tuple2('YouTube', 'Upload a related video'),
    Tuple2('Spotify', 'Play a related song'),
    Tuple2('Google Calendar', 'Create an event based on the email'),
    Tuple2('Google Drive', 'Delete corresponding file in Google Drive'),
    Tuple2('YouTube', 'Upload a video related to the file'),
    Tuple2('Google Calendar', 'Cancel the event in Google Calendar'),
    Tuple2('Spotify', 'Add a related playlist to Spotify'),
    Tuple2('Twitch', 'Post a message in Twitch chat'),
    Tuple2('Spotify', 'Play a playlist related to the event'),
    Tuple2('Google Drive', 'Sync the updated file to Drive'),
    Tuple2('YouTube', 'Upload a video related to the meeting'),
    Tuple2('Spotify', 'Add a related song to a playlist'),
    Tuple2('Twitch', 'Post a message in Twitch chat'),
    Tuple2('Google Drive', 'Save meeting details to Drive'),
  ];

  @override
  Widget build(BuildContext context) {
    return ActionReactionPage(
      title: 'Microsoft',
      actions: actions,
      reactions: reactions,
    );
  }
}