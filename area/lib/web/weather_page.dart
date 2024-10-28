import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'area_page.dart';

class WeatherPage extends StatelessWidget {
  const WeatherPage({super.key});

  static const List<String> actions = [
    'it rains'
  ];

  static const List<Tuple2<String, String>> reactions = [
    Tuple2('YouTube', 'it pours'),
  ];

  @override
  Widget build(BuildContext context) {
    return ActionReactionPage(
      title: 'weather',
      actions: actions,
      reactions: reactions,
    );
  }
}