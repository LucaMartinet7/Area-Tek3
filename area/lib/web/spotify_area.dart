import 'package:area/web/web_nav_bar.dart';
import 'package:flutter/material.dart';

class SpotifyPage extends StatelessWidget {
  const SpotifyPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const WebNavBar(),
      body: Column(
        children: [
          Container(
            padding: const EdgeInsets.all(20.0),
            child: Image.asset(
              'assets/images/spotify.png',
              height: 50,
            ),
          ),
          Expanded(
            child: GridView.builder(
              padding: const EdgeInsets.all(50.0),
              gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 5,
                crossAxisSpacing: 15.0,
                mainAxisSpacing: 15.0,
                childAspectRatio: 3 / 4, // Maintain the aspect ratio
              ),
              itemCount: 10, // 2 rows of 5 rectangles
              itemBuilder: (context, index) {
                return ActionReactionRectangle(
                  onPressed: () {
                    print('Button $index pressed');
                  },
                  defaultText: 'Rectangle $index',
                  hoverText: 'Hovered $index',
                  buttonText: 'Action $index',
                  color: Colors.primaries[index % Colors.primaries.length], // Different colors
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}

class ActionReactionRectangle extends StatefulWidget {
  final VoidCallback onPressed;
  final String defaultText;
  final String hoverText;
  final String buttonText;
  final Color color;

  const ActionReactionRectangle({
    required this.onPressed,
    required this.defaultText,
    required this.hoverText,
    required this.buttonText,
    required this.color,
    super.key,
  });

  @override
  _ActionReactionRectangleState createState() => _ActionReactionRectangleState();
}

class _ActionReactionRectangleState extends State<ActionReactionRectangle> {
  bool _hovering = false;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: widget.onPressed,
      child: MouseRegion(
        onEnter: (_) => setState(() => _hovering = true),
        onExit: (_) => setState(() => _hovering = false),
        child: AnimatedContainer(
          duration: Duration(milliseconds: 200),
          decoration: BoxDecoration(
            color: _hovering ? widget.color.withOpacity(0.7) : widget.color,
            borderRadius: BorderRadius.circular(10),
          ),
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  _hovering ? widget.hoverText : widget.defaultText,
                  style: TextStyle(color: Colors.white),
                ),
                if (_hovering)
                  ElevatedButton(
                    onPressed: widget.onPressed,
                    child: Text(widget.buttonText),
                  ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}