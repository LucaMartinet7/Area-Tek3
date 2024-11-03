import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'package:flutter/foundation.dart';
import '../web/area_page.dart';
import '../mobile/mobile_area.dart';

class GooglePage extends StatelessWidget {
  const GooglePage({super.key});

  static const List<Tuple3<String, String, String>> list = [
    Tuple3('Send an email', 'Post on Bluesky', 'http://127.0.0.1:8000/googlies/area-check-gmail-bluesky/'),
    Tuple3('Send an email', 'Play music on Spotify', 'http://127.0.0.1:8000/googlies/area-check-gmail-spotify/'),
    Tuple3('Send an email', 'Type in twitch channel', 'http://127.0.0.1:8000/googlies/area-check-gmail-twitch/')
  ];

  @override
  Widget build(BuildContext context) {
    if (kIsWeb) {
      return ActionReactionPage(
        title: 'Google',
        area: list,
      );
    } else {
      return MobileActionReactionPage(
        title: 'google',
        area: list,
      );
    }
  }
}