import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'package:flutter/foundation.dart';
import '../web/area_page.dart';
import '../mobile/mobile_area.dart';

class GmailPage extends StatelessWidget {
  const GmailPage({super.key});

  static const List<Tuple2<String, String>> list = [
    Tuple2('An Email Outlook received', 'Sends a message in Google chat'),
    Tuple2('A new file is added to OneDrive', 'Copies it to Google Drive'),
    Tuple2('Receive a Team\'s message', 'Create a Google Calendar event'),
  ];

  @override
  Widget build(BuildContext context) {
    if (kIsWeb) {
      return ActionReactionPage(
        title: 'Gmail',
        area: list,
      );
    } else {
      return MobileActionReactionPage(
        title: 'Gmail',
        area: list,
      );
    }
  }
}