import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'package:flutter/foundation.dart';
import '../web/area_page.dart';
import '../mobile/mobile_area.dart';

class GooglePage extends StatelessWidget {
  const GooglePage({super.key});

  static const List<Tuple2<String, String>> list = [
    Tuple2('Test Action', 'Test Reaction'),
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
        title: 'Google',
        area: list,
      );
    }
  }
}