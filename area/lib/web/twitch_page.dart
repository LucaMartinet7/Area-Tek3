import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'area_page.dart';

class TwitchPage extends StatelessWidget {
  const TwitchPage({super.key});

static const List<Tuple2<String, String>> list = [
    Tuple2('When Channel Goes live', 'Bluesky Post'),
    Tuple2('When Channel Goes live', 'Reddit Post')
];

  @override
  Widget build(BuildContext context) {
    return ActionReactionPage(
      title: 'Twitch',
      area: list
    );
  }
}