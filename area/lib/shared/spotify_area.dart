import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'package:flutter/foundation.dart';
import '../web/area_page.dart';
import '../mobile/mobile_area.dart';

class SpotifyPage extends StatelessWidget {
  const SpotifyPage({super.key});

  static const List<Tuple2<String, String>> list = [
    Tuple2('A new song is played', 'Send a message in users Twitch chat'),
    Tuple2('If the Beatles are playing', 'Send Microsoft Outlook email'),
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
      title: 'Spotify',
        area: list,
      );
    }
  }
}
