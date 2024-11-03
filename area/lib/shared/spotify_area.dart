import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'package:flutter/foundation.dart';
import '../web/area_page.dart';
import '../mobile/mobile_area.dart';

class SpotifyPage extends StatelessWidget {
  const SpotifyPage({super.key});

  static const List<Tuple3<String, String, String>> list = [
    Tuple3('When play Spotify song', 'Send message in twitch chat', 'http://127.0.0.1:8000/api/googlies/area-check-spotify-twitch/'),
    Tuple3('When you play Spotify song', 'Post on Bluesky', 'http://127.0.0.1:8000/api/googlies/area-check-spotify-bluesky/')
  ];

  @override
  Widget build(BuildContext context) {
    if (kIsWeb) {
      return ActionReactionPage(
        title: 'Spotify',
        area: list,
      );
    } else {
     return MobileActionReactionPage(
      title: 'spotify',
        area: list,
      );
    }
  }
}
