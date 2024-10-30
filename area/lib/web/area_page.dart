import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import '../web/web_nav_bar.dart';

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

class ActionReactionRectangle extends StatefulWidget {
  final Tuple2<String, String> actionReaction;
  final Color color;

  const ActionReactionRectangle({
    required this.actionReaction,
    required this.color,
    super.key,
  });

  @override
  ActionReactionRectangleState createState() => ActionReactionRectangleState();
}

class ActionReactionRectangleState extends State<ActionReactionRectangle> {
  bool _hovering = false;
  bool _isActive = false;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        if (kDebugMode) {
          print('Action: ${widget.actionReaction.item1}');
          print('Reaction: ${widget.actionReaction.item2}');
        }
      },
      child: MouseRegion(
        onEnter: (_) => setState(() => _hovering = true),
        onExit: (_) => setState(() => _hovering = false),
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 200),
          decoration: BoxDecoration(
            color: _hovering ? widget.color.withOpacity(0.7) : widget.color,
            borderRadius: BorderRadius.circular(10),
          ),
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 8.0),
                  child: Text(
                    widget.actionReaction.item1,
                    textAlign: TextAlign.center,
                    overflow: TextOverflow.ellipsis,
                    maxLines: 2,
                    style: const TextStyle(fontSize: 20, color: Colors.white),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 8.0),
                  child: Text(
                    widget.actionReaction.item2,
                    textAlign: TextAlign.center,
                    overflow: TextOverflow.ellipsis,
                    maxLines: 2,
                    style: const TextStyle(fontSize: 16, color: Colors.white70),
                  ),
                ),
                Switch(
                  value: _isActive,
                  onChanged: (value) => setState(() => _isActive = value),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
