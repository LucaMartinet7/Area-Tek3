import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'area_page.dart';

class MicrosoftPage extends StatelessWidget {
  const MicrosoftPage({super.key});

  static const List<Tuple2<String, String>> list = [
    Tuple2('An Email Outlook received', 'Sends a message in Google chat'),
    Tuple2('A new file is added to OneDrive', 'Copies it to Google Drive'),
    Tuple2('Receive a Team\'s message', 'Create a Google Calendar event'),
  ];

  @override
  Widget build(BuildContext context) {
    return ActionReactionPage(
      title: 'Microsoft',
      area : list
    );
  }
}