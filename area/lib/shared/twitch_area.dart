import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'package:flutter/foundation.dart';
import '../web/area_page.dart';
import '../mobile/mobile_area.dart';

class TwitchPage extends StatelessWidget {
  const TwitchPage({super.key});

  static const List<Tuple2<String, String>> list = [
    Tuple2('When Channel Goes live', 'Bluesky Post'),
    Tuple2('When Channel Goes live', 'Reddit Post')
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