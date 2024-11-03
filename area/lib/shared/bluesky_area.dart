import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'package:flutter/foundation.dart';
import '../web/area_page.dart';
import '../mobile/mobile_area.dart';

class BlueSkyPage extends StatelessWidget {
  const BlueSkyPage({super.key});

  static const List<Tuple3<String, String, String>> list = [
    Tuple3('When You Post', 'play a song on spotify', 'http://127.0.0.1:8000/api/googlies/area-check-bluesky-spotify/'),
    Tuple3('When You Post', 'Send Message in your Twitch Chat', 'http://127.0.0.1:8000/api/googlies/area-check-bluesky-twitch/'),
  ];

  @override
  Widget build(BuildContext context) {
    if (kIsWeb) {
      return ActionReactionPage(
        title: 'BlueSky',
        area: list,
      );
    } else {
      return MobileActionReactionPage(
        title: 'BlueSky',
        area: list,
      );
    }
  }
}