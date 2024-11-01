import 'package:flutter/material.dart';
import '../shared/exit_button.dart';

class WebNavBar extends StatelessWidget implements PreferredSizeWidget {
  const WebNavBar({super.key});

  @override
  Widget build(BuildContext context) {
    // Example connection status for each service
    final services = [
      {'asset': 'assets/vectors/account.png', 'route': '/dashboard', 'isConnected': true},
      {'asset': 'assets/vectors/spotify.png', 'route': '/spotify', 'isConnected': false},
      {'asset': 'assets/vectors/twitch.png', 'route': '/twitch', 'isConnected': true},
      {'asset': 'assets/vectors/google.png', 'route': '/google', 'isConnected': false},
      {'asset': 'assets/vectors/youtube.png', 'route': '/youtube', 'isConnected': false},
      {'asset': 'assets/vectors/microsoft.png', 'route': '/microsoft', 'isConnected': true},
    ];

    final connectedServices = services.where((service) => service['isConnected'] as bool).toList();

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
        leading: buildExitButton(context),
        flexibleSpace: Row(
          children: <Widget>[
            Expanded(
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: connectedServices.map((service) {
                  return _buildNavButton(
                    context,
                    service['asset'] as String,
                    service['route'] as String,
                    service['isConnected'] as bool,
                  );
                }).toList(),
              ),
            ),
            _buildNavButton(context, 'assets/vectors/info.png', '/about', true),
          ],
        ),
      ),
    );
  }

  Widget _buildNavButton(BuildContext context, String assetPath, String route, bool isConnected) {
    return IconButton(
      onPressed: isConnected && ModalRoute.of(context)?.settings.name != route
          ? () => Navigator.pushNamed(context, route)
          : null,
      icon: Image.asset(
        assetPath,
        width: 32,
        height: 32,
        color: isConnected ? const Color.fromARGB(255, 140, 211, 255) : Colors.grey,
      ),
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}