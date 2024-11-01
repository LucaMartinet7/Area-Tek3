import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import '../web/web_nav_bar.dart';
import '../shared/area_rectangle.dart';

import 'dart:math';

class ActionReactionPage extends StatelessWidget {
  final String title;
  final List<Tuple2<String, String>> area;

  const ActionReactionPage({
    required this.title,
    required this.area,
    super.key,
  });

  Color _getRandomColor() {
    final Random random = Random();
    Color color;
    do {
      color = Color.fromARGB(
        255,
        random.nextInt(256),
        random.nextInt(256),
        random.nextInt(256),
      );
    } while (_isColorTooLight(color));
    return color;
  }

  bool _isColorTooLight(Color color) {
    // Calculate the luminance of the color
    double luminance = (0.299 * color.red + 0.587 * color.green + 0.114 * color.blue) / 255;
    // Return true if the color is too light
    return luminance > 0.7;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const WebNavBar(),
      body: Center(
        child: Wrap(
          spacing: 20.0,
          runSpacing: 20.0,
          children: area.map((actionReaction) {
            return SizedBox(
              width: 350,
              height: 350,
              child: ActionReactionRectangle(
                actionReaction: actionReaction,
                color: _getRandomColor(),
              ),
            );
          }).toList(),
        ),
      ),
    );
  }
}
