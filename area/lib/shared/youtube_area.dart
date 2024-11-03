import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'package:flutter/foundation.dart';
import '../web/area_page.dart';
import '../mobile/mobile_area.dart';

class YoutubePage extends StatelessWidget {
  const YoutubePage({super.key});

  static const List<Tuple3<String, String, String>> list = [
    Tuple3('Test Action', 'Test Reaction', ' ' ),
    Tuple3('Test Action', 'Test Reaction', ' ')
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