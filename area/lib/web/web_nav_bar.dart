import 'package:flutter/material.dart';

class WebNavBar extends StatelessWidget implements PreferredSizeWidget {
  const WebNavBar({super.key});

  @override
  Widget build(BuildContext context) {
    return AppBar(
      backgroundColor: const Color.fromARGB(255, 140, 211, 255),
      actions: <Widget>[
        _buildNavButton(context, 'Settings', '/settings'),
        _buildNavButton(context, 'About', '/about'),
      ],
    );
  }

  Widget _buildNavButton(BuildContext context, String label, String route) {
    return TextButton(
      onPressed: () => Navigator.pushNamed(context, route),
      child: Text(label, style: const TextStyle(color: Colors.white)),
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}