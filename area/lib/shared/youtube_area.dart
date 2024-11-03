import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'package:flutter/foundation.dart';
import '../web/area_page.dart';
import '../mobile/mobile_area.dart';

class YoutubePage extends StatelessWidget {
  const YoutubePage({super.key});

  static const List<Tuple2<String, String>> list = [
    Tuple2('Upload\'s a Video', 'Creates a Spotify Playlist'),
    Tuple2('Watches a Video', 'Plays a Song (Crazy Frog) on Spotify'),
  ];

  @override
  Widget build(BuildContext context) {
    if (kIsWeb) {
      return ActionReactionPage(
        title: 'YouTube',
        area: list,
      );
    } else {
      return MobileActionReactionPage(
        title: 'youtube',
        area: list,
      );
    }
  }
}