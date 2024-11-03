
import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'package:flutter/foundation.dart';
import '../web/area_page.dart';
import '../mobile/mobile_area.dart';

class TwitchPage extends StatelessWidget {
  const TwitchPage({super.key});

  static const List<Tuple3<String, String, String>> list = [
    Tuple3('User go live', 'Post to bluesky', 'http://127.0.0.1:8000/api/twitchs/area-twitchlive-bluesky/'),
    Tuple3('User go live', 'Play Spotify song', 'http://127.0.0.1:8000/api/twitchs/area-twitchlive-spotify/'),
  ];

  @override
  Widget build(BuildContext context) {
    if (kIsWeb) {
      return ActionReactionPage(
        title: 'Twitch',
        area: list,
      );
    } else {
      return MobileActionReactionPage(
        title: 'twitch',
        area: list,
      );
    }
  }
}