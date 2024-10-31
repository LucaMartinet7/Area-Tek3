import 'package:flutter/material.dart';
import '../shared/api_service.dart';

class WebNavBar extends StatelessWidget implements PreferredSizeWidget {
  const WebNavBar({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        border: Border.all(
          color: const Color.fromARGB(255, 140, 211, 255),
          width: 5,
        ),
      ),
      child: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: _buildExitButton(context),
        flexibleSpace: Row(
          children: <Widget>[
            Expanded(
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  _buildNavButton(context, 'assets/vectors/account.png', '/dashboard'),
                  _buildNavButton(context, 'assets/vectors/spotify.png', '/spotify'),
                  _buildNavButton(context, 'assets/vectors/twitch.png', '/twitch'),
                  _buildNavButton(context, 'assets/vectors/google.png', '/google'),
                  _buildNavButton(context, 'assets/vectors/youtube.png', '/youtube'),
                  _buildNavButton(context, 'assets/vectors/microsoft.png', '/microsoft'),
                ],
              ),
            ),
            _buildNavButton(context, 'assets/vectors/info.png', '/about'),
          ],
        ),
      ),
    );
  }

  Widget _buildNavButton(BuildContext context, String assetPath, String route) {
    return IconButton(
      onPressed: ModalRoute.of(context)?.settings.name == route
          ? null
          : () => Navigator.pushNamed(context, route),
      icon: Image.asset(
        assetPath,
        width: 32,
        height: 32,
        color: const Color.fromARGB(255, 140, 211, 255),
      ),
    );
  }

  Widget _buildExitButton(BuildContext context) {
    return IconButton(
      onPressed: () async {
        await logout(context);
      },
      icon: Image.asset(
        'assets/vectors/exit.png',
        width: 32,
        height: 32,
        color: const Color.fromARGB(255, 140, 211, 255),
      ),
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}