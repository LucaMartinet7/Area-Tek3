import 'package:flutter/material.dart';

class WebNavBar extends StatelessWidget implements PreferredSizeWidget {
  const WebNavBar({super.key});

  @override
  Widget build(BuildContext context) {
    return AppBar(
      backgroundColor: const Color.fromARGB(255, 140, 211, 255),
      leading: _buildNavButton(context, 'assets/vectors/exit.png', '/logout'),
      flexibleSpace: Row(
        children: <Widget>[
          Expanded(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                _buildNavButton(context, 'assets/vectors/account.png', '/account'),
                _buildNavButton(context, 'assets/vectors/spotify.png', '/spotify'),
                _buildNavButton(context, 'assets/vectors/twitch.png', '/twitch'),
                _buildNavButton(context, 'assets/vectors/google.png', '/google'),
                _buildNavButton(context, 'assets/vectors/deezer.png', '/deezer'),
                _buildNavButton(context, 'assets/vectors/microsoft.png', '/microsoft'),
              ],
            ),
          ),
          _buildNavButton(context, 'assets/vectors/info.png', '/about'),
        ],
      ),
    );
  }

  Widget _buildNavButton(BuildContext context, String assetPath, String route) {
    return IconButton(
      onPressed: () => Navigator.pushNamed(context, route),
      icon: Image.asset(
        assetPath,
        width: 32,
        height: 32,
      ),
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}