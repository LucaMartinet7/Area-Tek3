import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'area_page.dart';

class GooglePage extends StatelessWidget {
  const GooglePage({super.key});

  static const List<String> actions = [
    'A new email is received',
    'A file is uploaded to Google Drive',
    'A calendar event is created',
    'A new contact is added to Google Contacts',
    'A calendar event is canceled',
    'A new email is received with an attachment',
    'A calendar event starts',
    'A file is shared',
    'A new email from a specific contact',
    'A calendar reminder is triggered',
    'A new file is added to Google Drive',
    'A folder is created in Google Drive',
    'A document is shared with the user',
    'A new sheet is added to Google Sheets',
    'A form response is received in Google Forms',
  ];

  static const List<Tuple2<String, String>> reactions = [
    Tuple2('Spotify', 'Play a specific song'),
    Tuple2('Microsoft OneDrive', 'Sync the file to OneDrive'),
    Tuple2('Twitch', 'Post a message in Twitch chat'),
    Tuple2('YouTube', 'Subscribe to a channel'),
    Tuple2('Microsoft Outlook', 'Cancel the event in Outlook'),
    Tuple2('Google Drive', 'Save the attachment to Drive'),
    Tuple2('Spotify', 'Play a specific song or playlist'),
    Tuple2('Microsoft OneDrive', 'Sync the shared file'),
    Tuple2('Spotify', 'Play a personalized song'),
    Tuple2('Twitch', 'Send a message in Twitch chat'),
    Tuple2('Microsoft Outlook', 'Send an email notification'),
    Tuple2('YouTube', 'Upload a video to match the folder'),
    Tuple2('Twitch', 'Post a message in Twitch chat'),
    Tuple2('Microsoft OneDrive', 'Sync the sheet to OneDrive'),
    Tuple2('Spotify', 'Play a song'),
  ];

  @override
  Widget build(BuildContext context) {
    return ActionReactionPage(
      title: 'Google',
      actions: actions,
      reactions: reactions,
    );
  }
}